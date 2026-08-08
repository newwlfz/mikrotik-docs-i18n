#!/usr/bin/env python3
"""
fetch_docs.py - 从 MikroTik 官方文档拉取所有英文 Markdown 源码（带重试 + 清理孤儿文件）
"""

import os
import re
import time
import requests
from urllib.parse import urlparse

BASE_URL = "https://manual.mikrotik.com"
LLMS_TXT_URL = "https://manual.mikrotik.com/llms.txt"
OUTPUT_DIR = "docs"
USER_AGENT = "MikroTik-Doc-Mirror/1.0 (+https://github.com/your-repo)"
REQUEST_DELAY = 1          # 每次请求间隔（秒）
RETRY_COUNT = 3            # 重试次数
RETRY_DELAY = 2            # 重试基础等待（秒）

def get_llms_urls():
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(LLMS_TXT_URL, headers=headers, timeout=30)
    resp.raise_for_status()
    content = resp.text
    urls = re.findall(r'https?://manual\.mikrotik\.com/docs/[^\s\)"]+', content)
    urls = list(dict.fromkeys(urls))
    return urls

def get_path_from_url(url):
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

def fetch_page_with_retry(url):
    headers = {"User-Agent": USER_AGENT}
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.text
            else:
                print(f"  尝试 {attempt}/{RETRY_COUNT} 返回状态码 {resp.status_code}")
                if attempt < RETRY_COUNT:
                    time.sleep(RETRY_DELAY * attempt)
        except Exception as e:
            print(f"  尝试 {attempt}/{RETRY_COUNT} 请求异常: {e}")
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_DELAY * attempt)
    print(f"⚠️ 所有重试失败: {url}")
    return None

def save_markdown(content, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def cleanup_orphan_files(expected_paths):
    """删除 docs/ 目录下不在预期列表中的文件"""
    print("\n🧹 开始清理本地多余的英文文档...")
    removed_count = 0
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, OUTPUT_DIR)
            if rel_path not in expected_paths:
                os.remove(local_path)
                print(f"   🗑️ 已删除: {rel_path}")
                removed_count += 1
    if removed_count == 0:
        print("   ✅ 本地文件与官方列表完全一致，无需清理。")
    else:
        print(f"   ✅ 清理完成，共删除 {removed_count} 个孤立的旧文档。")

def main():
    print("🔍 获取官方文档页面列表...")
    urls = get_llms_urls()
    print(f"✅ 共发现 {len(urls)} 个页面")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    expected_paths = set()

    for idx, url in enumerate(urls, 1):
        rel_path = get_path_from_url(url)
        if not rel_path:
            print(f"⏭️ 跳过无效 URL: {url}")
            continue
        expected_paths.add(rel_path)
        local_path = os.path.join(OUTPUT_DIR, rel_path)

        print(f"[{idx}/{len(urls)}] 下载: {url} -> {local_path}")
        content = fetch_page_with_retry(url)
        if content is not None:
            save_markdown(content, local_path)
            print(f"   ✅ 保存成功")
        else:
            print(f"   ❌ 下载失败，跳过")
        time.sleep(REQUEST_DELAY)

    # 清理孤儿文件
    cleanup_orphan_files(expected_paths)
    print("🎉 所有文档拉取完成。")

if __name__ == "__main__":
    main()
