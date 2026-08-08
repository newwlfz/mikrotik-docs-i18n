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
    """加载 MD5 增量缓存，避免重复翻译未修改的文件"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_cache(cache):
    """保存缓存"""
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def compute_md5(text):
    """计算文本 MD5"""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def cleanup_disabled_locales():
    """清理已禁用的语种目录"""
    if not os.path.exists(I18N_DIR):
        return

    for item in os.listdir(I18N_DIR):
        item_path = os.path.join(I18N_DIR, item)
        if os.path.isdir(item_path) and item not in active_locales:
            print(f"🧹 检测到语种 [{item}] 已被禁用，正在清理残留文件夹: {item_path}...")
            shutil.rmtree(item_path)


def fix_mikrotik_links(content):
    """后处理：将官方绝对链接自动替换为相对路径"""
    pattern = r'https?://manual\.mikrotik\.com/docs/([a-zA-Z0-9_\-/\#]+)'
    return re.sub(pattern, r'/docs/\1', content)


def call_deepseek_api(system_prompt, text_content):
    """调用 DeepSeek API 进行翻译"""
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


def process_translation():
    """遍历 docs/ 目录，将文件翻译并写入对应 i18n 语种目录"""
    if not os.path.exists(DOCS_DIR):
        print(f"⚠️ 未找到 {DOCS_DIR} 目录，结束执行。")
        return

    cache = load_cache()
    translated_count = 0
    skipped_count = 0

    # 遍历 docs 目录下的所有 Markdown 文件
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if not (file.endswith(".md") or file.endswith(".mdx")):
                continue

            src_file_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_file_path, DOCS_DIR)

            with open(src_file_path, "r", encoding="utf-8") as f:
                source_content = f.read()

            content_md5 = compute_md5(source_content)

            # 对每个启用的语种进行翻译处理
            for lang in active_locales:
                system_prompt = target_prompts.get(lang)
                if not system_prompt:
                    continue

                # Docusaurus 规定的 i18n 目标路径结构
                target_dir = os.path.join(
                    I18N_DIR, lang, "docusaurus-plugin-content-docs", "current", os.path.dirname(rel_path)
                )
                target_file_path = os.path.join(target_dir, os.path.basename(rel_path))

                cache_key = f"{lang}:{rel_path}"

                # 检查缓存与文件是否存在，若未变动则跳过
                if cache.get(cache_key) == content_md5 and os.path.exists(target_file_path):
                    skipped_count += 1
                    continue

                print(f"🌐 正在翻译 [{lang}]: {rel_path} ...")
                translated_content = call_deepseek_api(system_prompt, source_content)

                if translated_content:
                    os.makedirs(target_dir, exist_ok=True)
                    with open(target_file_path, "w", encoding="utf-8") as f:
                        f.write(translated_content)

                    # 更新缓存
                    cache[cache_key] = content_md5
                    translated_count += 1
                    print(f"✅ 完成 [{lang}]: {target_file_path}")
                else:
                    print(f"❌ 跳过写入 [{lang}]: {rel_path} (API 未成功返回)")

    save_cache(cache)
    print(f"\n🎉 翻译处理结束：完成 {translated_count} 个文件，跳过未修改文件 {skipped_count} 个。")


if __name__ == "__main__":
    cleanup_disabled_locales()
    print(f"🚀 激活语种列表: {active_locales}")
    process_translation()
