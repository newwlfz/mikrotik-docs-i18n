import hashlib
import json
import os
import shutil
import subprocess
import requests

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
CACHE_FILE = "doc_cache.json"


def get_locales_config():
  """从 i18n.config.js 读取激活与禁用语种配置"""
  js_code = """
    const { SUPPORTED_LOCALES, activeLocales } = require('./i18n.config');
    console.log(JSON.stringify({
        supported: SUPPORTED_LOCALES,
        active: activeLocales
    }));
    """
  try:
    res = subprocess.check_output(["node", "-e", js_code], text=True)
    return json.loads(res.strip())
  except Exception as e:
    print(f"⚠️ 读取 i18n.config.js 失败: {e}")
    return {"supported": {}, "active": ["zh-Hans", "zh-Hant"]}


config_data = get_locales_config()
supported_locales = config_data["supported"]
active_locales = config_data["active"]

# 提取真正需要 AI 翻译的目标语种及专属 Prompt
TARGET_LOCALES = {
    key: supported_locales[key]["promptName"]
    for key in active_locales
    if key in supported_locales
}


def cleanup_disabled_locales():
  """自动应对禁用语种：删除 i18n/ 目录下已被 enabled: false 的语种文件夹"""
  i18n_dir = "i18n"
  if not os.path.exists(i18n_dir):
    return

  for item in os.listdir(i18n_dir):
    item_path = os.path.join(i18n_dir, item)
    if os.path.isdir(item_path) and item not in active_locales:
      print(
          f"🧹 检测到语种 [{item}] 已被禁用，正在清理残留文件夹:"
          f" {item_path}..."
      )
      shutil.rmtree(item_path)


# 执行禁用语种自动清理
cleanup_disabled_locales()

# ... (后续 translate.py 核心增量翻译与 API 请求代码保持不变) ...
