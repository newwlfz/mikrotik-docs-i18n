#!/usr/bin/env python3
"""
fetch_docs.py - 增量拉取官方 Markdown 文档，基于 ETag/Last-Modified 判断更新
职责：
1. 从 /llms.txt 获取官方完整列表
2. 清理孤儿文件（英文文档和翻译文档）
3. 自动删除非激活语种的翻译目录
4. 基于 ETag/Last-Modified 增量下载
5. 下载后自动修正：
   - 官方绝对链接 -> 相对路径 (/docs/xxx)
   - 相对图片链接 -> 官方 CDN 绝对路径
6. 维护 sync_state.json
"""

import os
import re
import time
import json
import requests
import shutil
from urllib.parse import urlparse
from datetime import datetime
import email.utils

# ========== 配置 ==========
BASE_URL = "https://manual.mikrotik.com"
LLMS_TXT_URL = "https://manual.mikrotik.com/llms.txt"
OUTPUT_DIR = "docs"
I18N_DIR = "i18n"
STATE_FILE = "sync_state.json"
USER_AGENT = "MikroTik-Doc-Mirror/1.0 (+https://github.com/your-repo)"
REQUEST_DELAY = 1
RETRY_COUNT = 3
RETRY_DELAY = 2


# ========== 工具函数 ==========
def load_state():
    """加载状态文件"""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_state_atomic(state):
    """原子性地保存状态文件（先写临时文件，再重命名覆盖）"""
    tmp_file = STATE_FILE + ".tmp"
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    os.replace(tmp_file, STATE_FILE)  # 原子重命名


def get_official_urls():
    """从 /llms.txt 提取所有文档 URL"""
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(LLMS_TXT_URL, headers=headers, timeout=30)
    resp.raise_for_status()
    content = resp.text
    urls = re.findall(r'https?://manual\.mikrotik\.com/docs/[^\s\)"]+', content)
    urls = list(dict.fromkeys(urls))
    return urls


def url_to_relative_path(url):
    """从 URL 提取本地相对路径"""
    parsed = urlparse(url)
    path = parsed.path
    if not path.startswith("/docs/"):
        if path in ("/docs", "/docs/"):
            return "index.md"
        return None
    rel = path[len("/docs/"):]
    if not rel:
        return "index.md"
    if rel.endswith("/"):
        rel += "index.md"
    if not re.search(r"\.[a-zA-Z0-9]+$", rel):
        rel += ".md"
    return rel


def compute_md5(filepath):
    """计算文件 MD5"""
    import hashlib
    if not os.path.exists(filepath):
        return None
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def fix_document_content(content, rel_path):
    """
    修正下载后的文档内容：
    1. 将官方绝对链接替换为相对路径（如 /docs/xxx）
    2. 将相对图片链接替换为官方 CDN 绝对路径
    """
    # 1. 官方绝对链接 -> 相对路径
    content = re.sub(r'https?://manual\.mikrotik\.com/docs/([a-zA-Z0-9_\-/\#]+)', r'/docs/\1', content)

    # 2. 相对图片链接 -> 官方 CDN 绝对路径
    dir_name = os.path.dirname(rel_path)
    if dir_name:
        base_url = f"https://manual.mikrotik.com/docs/{dir_name}/"
        content = re.sub(r'\(\.?/img/', f'({base_url}img/', content)
    else:
        content = re.sub(r'\(\.?/img/', '(https://manual.mikrotik.com/docs/img/', content)

    return content


def head_request_with_retry(url):
    """发送 HEAD 请求获取响应头，支持重试"""
    headers = {"User-Agent": USER_AGENT}
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            resp = requests.head(url, headers=headers, timeout=15)
            if resp.status_code == 200:
                return resp.headers
            else:
                print(f"   HEAD 尝试 {attempt}/{RETRY_COUNT} 状态码 {resp.status_code}")
                if attempt < RETRY_COUNT:
                    time.sleep(RETRY_DELAY * attempt)
        except Exception as e:
            print(f"   HEAD 尝试 {attempt}/{RETRY_COUNT} 异常: {e}")
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_DELAY * attempt)
    return None


def fetch_page_with_retry(url, headers=None):
    """GET 请求下载页面内容，支持重试"""
    if headers is None:
        headers = {"User-Agent": USER_AGENT}
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp
            elif resp.status_code == 304:
                return None  # 未修改
            else:
                print(f"   GET 尝试 {attempt}/{RETRY_COUNT} 状态码 {resp.status_code}")
                if attempt < RETRY_COUNT:
                    time.sleep(RETRY_DELAY * attempt)
                    headers = {"User-Agent": USER_AGENT}  # 重置条件头
        except Exception as e:
            print(f"   GET 尝试 {attempt}/{RETRY_COUNT} 异常: {e}")
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_DELAY * attempt)
                headers = {"User-Agent": USER_AGENT}
    return None


def get_active_locales():
    """从 i18n.config.js 读取启用的语种列表"""
    import subprocess
    import json as json_module
    js_code = """
    const { activeLocales } = require('./i18n.config');
    console.log(JSON.stringify(activeLocales));
    """
    try:
        res = subprocess.check_output(["node", "-e", js_code], text=True)
        return json_module.loads(res.strip())
    except Exception as e:
        print(f"⚠️ 读取 i18n.config.js 失败: {e}")
        return ["zh-Hans"]


# ========== 核心逻辑 ==========
def cleanup_orphan_files(official_paths, state, active_locales):
    """
    清理孤儿文件：
    - 删除 docs/ 下不在 official_paths 中的英文文件
    - 删除 i18n/ 下不在 official_paths 中的翻译文件
    - 删除非激活语种的整个目录
    - 从 state 中删除不在 official_paths 中的条目
    """
    print("\n🧹 清理孤儿文件...")
    removed_english = 0
    removed_translation = 0
    removed_state = 0

    # 1. 清理英文文档
    for root, _, files in os.walk(OUTPUT_DIR):
        for file in files:
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, OUTPUT_DIR)
            if rel_path not in official_paths:
                os.remove(local_path)
                print(f"   🗑️ 删除英文: {rel_path}")
                removed_english += 1

    # 2. 清理翻译文档
    # 首先删除非激活语种的整个目录
    if os.path.exists(I18N_DIR):
        for lang_dir in os.listdir(I18N_DIR):
            if lang_dir not in active_locales:
                full_path = os.path.join(I18N_DIR, lang_dir)
                if os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                    print(f"   🗑️ 删除非激活语种目录: {lang_dir}")
                    # 从状态中清除该语种的所有翻译记录
                    for rel_path, file_state in state.items():
                        if "translations" in file_state and lang_dir in file_state["translations"]:
                            del file_state["translations"][lang_dir]
                    removed_state += 1  # 简化计数

        # 然后对激活语种进行文件级清理
        for lang in active_locales:
            lang_root = os.path.join(I18N_DIR, lang, "docusaurus-plugin-content-docs", "current")
            if not os.path.exists(lang_root):
                continue
            for root, _, files in os.walk(lang_root):
                for file in files:
                    if file.endswith(".md") or file.endswith(".mdx"):
                        trans_path = os.path.join(root, file)
                        rel_path = os.path.relpath(trans_path, lang_root)
                        if rel_path not in official_paths:
                            os.remove(trans_path)
                            print(f"   🗑️ 删除翻译 [{lang}]: {rel_path}")
                            removed_translation += 1
                            # 从状态中清除该文件的该语种记录
                            if rel_path in state and "translations" in state[rel_path]:
                                if lang in state[rel_path]["translations"]:
                                    del state[rel_path]["translations"][lang]
            # 尝试删除空目录
            try:
                os.removedirs(lang_root)
            except OSError:
                pass

    # 3. 清理状态文件（移除不再存在的文档条目）
    for key in list(state.keys()):
        if key not in official_paths:
            del state[key]
            removed_state += 1
            print(f"   🗑️ 清除状态: {key}")

    if removed_english == 0 and removed_translation == 0 and removed_state == 0:
        print("   ✅ 没有孤儿文件需要清理。")
    else:
        print(f"   ✅ 清理完成：删除 {removed_english} 个英文，{removed_translation} 个翻译，{removed_state} 个状态条目。")

    return state


def process_downloads(official_paths, state):
    """下载或更新每个文件，并修正内容"""
    print("\n📥 处理文件下载...")
    updated_count = 0
    skipped_count = 0

    for idx, rel_path in enumerate(official_paths, 1):
        url = f"https://manual.mikrotik.com/docs/{rel_path}"
        local_path = os.path.join(OUTPUT_DIR, rel_path)

        print(f"[{idx}/{len(official_paths)}] 检查: {rel_path}")

        # 获取当前缓存信息
        cached = state.get(rel_path, {})
        etag = cached.get("etag")
        last_modified = cached.get("last_modified")

        # 构建请求头
        headers = {"User-Agent": USER_AGENT}
        if etag:
            headers["If-None-Match"] = etag
        elif last_modified:
            headers["If-Modified-Since"] = last_modified

        # 发送请求
        resp = fetch_page_with_retry(url, headers)

        if resp is None:
            # 304 Not Modified，跳过
            skipped_count += 1
            print(f"   ⏭️ 未修改，跳过")
            continue
        elif resp.status_code == 200:
            # 下载成功
            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            # 1. 修正内容（链接 + 图片）
            fixed_content = fix_document_content(resp.text, rel_path)

            # 2. 写入文件
            with open(local_path, "w", encoding="utf-8") as f:
                f.write(fixed_content)

            # 3. 更新状态
            new_etag = resp.headers.get("ETag")
            new_last_modified = resp.headers.get("Last-Modified")
            new_md5 = compute_md5(local_path)

            # 清除旧翻译状态（因为文件内容变了）
            state[rel_path] = {
                "etag": new_etag,
                "last_modified": new_last_modified,
                "md5": new_md5,
                "translations": {}  # 清空，等待翻译阶段重建
            }
            print(f"   ✅ 已更新")
            updated_count += 1
        else:
            print(f"   ❌ 下载失败，状态码 {resp.status_code if resp else 'None'}")
            continue

        time.sleep(REQUEST_DELAY)

    print(f"\n📊 下载统计：更新 {updated_count} 个，跳过 {skipped_count} 个。")
    return state


def main():
    print("=" * 60)
    print("MikroTik 文档同步工具 - 下载阶段")
    print("=" * 60)

    # 1. 获取官方列表
    print("\n🔍 获取官方文档列表...")
    urls = get_official_urls()
    official_paths = set()
    for url in urls:
        rel_path = url_to_relative_path(url)
        if rel_path:
            official_paths.add(rel_path)
    print(f"✅ 共发现 {len(official_paths)} 个文档")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 2. 获取启用的语种
    active_locales = get_active_locales()
    print(f"📝 启用语种: {active_locales}")

    # 3. 加载状态文件
    state = load_state()
    print(f"📋 状态文件包含 {len(state)} 个条目")

    # 4. 清理孤儿文件
    state = cleanup_orphan_files(official_paths, state, active_locales)

    # 5. 处理下载
    state = process_downloads(official_paths, state)

    # 6. 保存状态
    save_state_atomic(state)
    print(f"\n💾 状态文件已保存 ({len(state)} 个条目)")

    print("\n" + "=" * 60)
    print("✅ 下载阶段完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
