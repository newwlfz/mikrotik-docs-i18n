#!/usr/bin/env python3
"""
fetch_docs.py - 增量拉取官方 Markdown，利用现有文件建立缓存
"""

import os
import re
import time
import json
import requests
from urllib.parse import urlparse
from datetime import datetime
import email.utils

BASE_URL = "https://manual.mikrotik.com"
LLMS_TXT_URL = "https://manual.mikrotik.com/llms.txt"
OUTPUT_DIR = "docs"
CACHE_FILE = "etag_cache.json"
USER_AGENT = "MikroTik-Doc-Mirror/1.0 (+https://github.com/your-repo)"
REQUEST_DELAY = 1
RETRY_COUNT = 3
RETRY_DELAY = 2


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


def load_etag_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_etag_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)


def get_local_file_info(filepath):
    """返回本地文件的修改时间（RFC 1123 格式）和大小（字节）"""
    if os.path.exists(filepath):
        mtime = os.path.getmtime(filepath)
        # 转换为 GMT 时间字符串
        dt = datetime.utcfromtimestamp(mtime)
        last_modified = email.utils.format_datetime(dt, usegmt=True)
        size = os.path.getsize(filepath)
        return last_modified, size
    return None, None


def head_request(url):
    """发送 HEAD 请求获取响应头，返回 (etag, last_modified, content_length)"""
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.head(url, headers=headers, timeout=15)
        resp.raise_for_status()
        etag = resp.headers.get("ETag")
        last_modified = resp.headers.get("Last-Modified")
        content_length = resp.headers.get("Content-Length")
        return etag, last_modified, content_length
    except Exception as e:
        print(f"   HEAD 请求失败: {e}")
        return None, None, None


def fetch_page_with_conditional(url, cache, local_filepath):
    """
    根据缓存和本地文件，决定是否需要下载。
    返回 (content, updated)，其中 updated 表示是否下载了新内容。
    """
    headers = {"User-Agent": USER_AGENT}
    cached = cache.get(url, {})

    # 1. 如果缓存中有 ETag，使用 If-None-Match
    if cached.get("etag"):
        headers["If-None-Match"] = cached["etag"]
    elif cached.get("last_modified"):
        headers["If-Modified-Since"] = cached["last_modified"]
    else:
        # 2. 没有缓存，但本地文件存在 → 先 HEAD 获取信息，与本地文件比较
        if os.path.exists(local_filepath):
            local_mtime, local_size = get_local_file_info(local_filepath)
            if local_mtime:
                etag, last_modified, content_length = head_request(url)
                if etag and last_modified:
                    # 如果服务器 Last-Modified 与本地 mtime 一致，且大小相同，认为未变
                    # 将两个时间字符串统一为 RFC 1123 格式比较
                    if last_modified == local_mtime and content_length and int(content_length) == local_size:
                        # 文件未变，缓存并跳过下载
                        cache[url] = {"etag": etag, "last_modified": last_modified}
                        print("   (利用本地文件，未修改)")
                        return None, False
                # 如果不一致，则继续执行 GET 下载
        # 若无缓存且本地不存在或不匹配，则直接 GET
        pass

    # 执行 GET（带条件头或不带）
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 304:
                # 未修改（缓存命中）
                return None, False
            elif resp.status_code == 200:
                # 获取新内容
                new_etag = resp.headers.get("ETag")
                new_last_modified = resp.headers.get("Last-Modified")
                cache[url] = {}
                if new_etag:
                    cache[url]["etag"] = new_etag
                if new_last_modified:
                    cache[url]["last_modified"] = new_last_modified
                return resp.text, True
            else:
                print(f"  尝试 {attempt}/{RETRY_COUNT} 状态码 {resp.status_code}")
                if attempt < RETRY_COUNT:
                    time.sleep(RETRY_DELAY * attempt)
                    headers = {"User-Agent": USER_AGENT}  # 重置条件头
        except Exception as e:
            print(f"  尝试 {attempt}/{RETRY_COUNT} 异常: {e}")
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_DELAY * attempt)
                headers = {"User-Agent": USER_AGENT}
    print(f"⚠️ 所有重试失败: {url}")
    return None, False


def save_markdown(content, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def cleanup_orphan_files(expected_paths):
    print("\n🧹 清理本地多余的英文文档...")
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
        print("   ✅ 本地文件与官方列表一致。")
    else:
        print(f"   ✅ 清理完成，删除 {removed_count} 个孤立文件。")


def main():
    print("🔍 获取官方文档页面列表...")
    urls = get_llms_urls()
    print(f"✅ 共发现 {len(urls)} 个页面")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    cache = load_etag_cache()
    expected_paths = set()
    downloaded_count = 0
    skipped_count = 0

    for idx, url in enumerate(urls, 1):
        rel_path = get_path_from_url(url)
        if not rel_path:
            print(f"⏭️ 跳过无效 URL: {url}")
            continue
        expected_paths.add(rel_path)
        local_path = os.path.join(OUTPUT_DIR, rel_path)

        print(f"[{idx}/{len(urls)}] 检查: {url}")
        content, updated = fetch_page_with_conditional(url, cache, local_path)

        if content is None and not updated:
            skipped_count += 1
        elif content is not None and updated:
            save_markdown(content, local_path)
            downloaded_count += 1
            print(f"   ✅ 已更新: {rel_path}")
        else:
            print(f"   ❌ 获取失败，跳过")
        time.sleep(REQUEST_DELAY)

    save_etag_cache(cache)
    cleanup_orphan_files(expected_paths)

    print(f"\n🎉 拉取完成：更新 {downloaded_count} 个文件，跳过 {skipped_count} 个未变化文件。")


if __name__ == "__main__":
    main()
