import os
import json
import shutil
import subprocess
import re
import requests

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
CACHE_FILE = "doc_cache.json"


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


def cleanup_disabled_locales():
    """清理已禁用的语种目录"""
    i18n_dir = "i18n"
    if not os.path.exists(i18n_dir):
        return

    for item in os.listdir(i18n_dir):
        item_path = os.path.join(i18n_dir, item)
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
        # 正则后处理链接，确保全自动转换为相对路径
        return fix_mikrotik_links(translated_text)
    except Exception as e:
        print(f"❌ DeepSeek API 请求失败: {e}")
        return text_content


# 1. 执行残留目录清理
cleanup_disabled_locales()

# 2. 打印当前工作的语种与提示词状态
print(f"🚀 激活语种列表: {active_locales}")
for lang in active_locales:
    print(f"📌 [{lang}] 使用 System Prompt:\n{target_prompts.get(lang, '')}\n{'-'*50}")
