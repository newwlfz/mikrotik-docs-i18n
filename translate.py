#!/usr/bin/env python3
import os
import json
import shutil
import subprocess
import re
import hashlib
import requests

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
CACHE_FILE = "doc_cache.json"
DOCS_DIR = "docs"
I18N_DIR = "i18n"


def get_locales_config():
    """从 i18n.config.js 读取配置及动态生成的 Prompt"""
    js_code = """
    const { SUPPORTED_LOCALES, activeLocales, getSystemPrompt } = require('./i18n.config');
    const prompts = {};
    activeLocales.forEach(lang => {
        prompts[lang] = getSystemPrompt(lang);
    });
    console.log(JSON.stringify({
        supported: SUPPORTED_LOCALES,
        active: activeLocales,
        prompts: prompts
    }));
    """
    try:
        res = subprocess.check_output(["node", "-e", js_code], text=True)
        return json.loads(res.strip())
    except Exception as e:
        print(f"⚠️ 读取 i18n.config.js 失败: {e}")
        return {"supported": {}, "active": ["zh-Hans"], "prompts": {}}


config_data = get_locales_config()
supported_locales = config_data.get("supported", {})
active_locales = config_data.get("active", ["zh-Hans"])
target_prompts = config_data.get("prompts", {})


def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def compute_md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def cleanup_disabled_locales():
    if not os.path.exists(I18N_DIR):
        return
    for item in os.listdir(I18N_DIR):
        item_path = os.path.join(I18N_DIR, item)
        if os.path.isdir(item_path) and item not in active_locales:
            print(f"🧹 检测到语种 [{item}] 已被禁用，正在清理残留文件夹: {item_path}...")
            shutil.rmtree(item_path)


def fix_mikrotik_links(content):
    pattern = r'https?://manual\.mikrotik\.com/docs/([a-zA-Z0-9_\-/\#]+)'
    return re.sub(pattern, r'/docs/\1', content)


def call_deepseek_api(system_prompt, text_content):
    if not DEEPSEEK_API_KEY:
        print("⚠️ 未检测到 DEEPSEEK_API_KEY，跳过翻译！")
        return text_content
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_content}
        ],
        "temperature": 0.2
    }
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        res_json = response.json()
        translated_text = res_json['choices'][0]['message']['content']
        return fix_mikrotik_links(translated_text)
    except Exception as e:
        print(f"❌ DeepSeek API 请求失败: {e}")
        return None


def cleanup_translations():
    """清理 i18n 目录下孤立的翻译文件（对应英文源文件已不存在的）"""
    if not os.path.exists(DOCS_DIR):
        return
    print("\n🧹 开始清理孤立的翻译文件...")
    # 收集所有现有的英文文件相对路径
    existing_en = set()
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md") or file.endswith(".mdx"):
                rel = os.path.relpath(os.path.join(root, file), DOCS_DIR)
                existing_en.add(rel)

    removed_count = 0
    for lang in active_locales:
        lang_root = os.path.join(I18N_DIR, lang, "docusaurus-plugin-content-docs", "current")
        if not os.path.exists(lang_root):
            continue
        for root, _, files in os.walk(lang_root):
            for file in files:
                if file.endswith(".md") or file.endswith(".mdx"):
                    trans_path = os.path.join(root, file)
                    rel_path = os.path.relpath(trans_path, lang_root)
                    if rel_path not in existing_en:
                        os.remove(trans_path)
                        print(f"   🗑️ 删除孤立翻译 [{lang}]: {rel_path}")
                        removed_count += 1
        # 尝试删除空目录（非强制）
        try:
            os.removedirs(lang_root)
        except OSError:
            pass

    if removed_count == 0:
        print("   ✅ 没有孤立的翻译文件。")
    else:
        print(f"   ✅ 清理完成，共删除 {removed_count} 个孤立翻译文件。")


def process_translation():
    if not os.path.exists(DOCS_DIR):
        print(f"⚠️ 未找到 {DOCS_DIR} 目录，结束执行。")
        return

    cache = load_cache()
    translated_count = 0
    skipped_count = 0

    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if not (file.endswith(".md") or file.endswith(".mdx")):
                continue
            src_file_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_file_path, DOCS_DIR)

            with open(src_file_path, "r", encoding="utf-8") as f:
                source_content = f.read()

            content_md5 = compute_md5(source_content)

            for lang in active_locales:
                system_prompt = target_prompts.get(lang)
                if not system_prompt:
                    continue

                target_dir = os.path.join(
                    I18N_DIR, lang, "docusaurus-plugin-content-docs", "current", os.path.dirname(rel_path)
                )
                target_file_path = os.path.join(target_dir, os.path.basename(rel_path))
                cache_key = f"{lang}:{rel_path}"

                if cache.get(cache_key) == content_md5 and os.path.exists(target_file_path):
                    skipped_count += 1
                    continue

                print(f"🌐 正在翻译 [{lang}]: {rel_path} ...")
                translated_content = call_deepseek_api(system_prompt, source_content)

                if translated_content:
                    os.makedirs(target_dir, exist_ok=True)
                    with open(target_file_path, "w", encoding="utf-8") as f:
                        f.write(translated_content)
                    cache[cache_key] = content_md5
                    translated_count += 1
                    print(f"✅ 完成 [{lang}]: {target_file_path}")
                else:
                    print(f"❌ 跳过写入 [{lang}]: {rel_path} (API 未成功返回)")

    save_cache(cache)
    print(f"\n🎉 翻译处理结束：完成 {translated_count} 个文件，跳过未修改文件 {skipped_count} 个。")

    # 最后清理孤儿翻译
    cleanup_translations()


if __name__ == "__main__":
    cleanup_disabled_locales()
    print(f"🚀 激活语种列表: {active_locales}")
    process_translation()
