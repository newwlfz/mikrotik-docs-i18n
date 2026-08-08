import hashlib
import json
import os
import requests

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
CACHE_FILE = "doc_cache.json"

# 需要自动翻译的目标语言清单（对应 Docusaurus i18n 标识）
TARGET_LOCALES = {
    "zh-Hans": "简体中文",
    "zh-Hant": "繁體中文（请使用台湾/香港网络技术常用词汇）",
}


def get_file_hash(content: str) -> str:
  return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_cache() -> dict:
  if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
      return json.load(f)
  return {}


def save_cache(cache: dict):
  with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)


def translate_doc(text: str, target_lang_name: str) -> str:
  """调用 DeepSeek 翻译整篇文档为指定语言，同时保留双语气泡节点"""
  if not DEEPSEEK_API_KEY:
    print("⚠️ 未配置 DEEPSEEK_API_KEY，保留原文")
    return text

  prompt = (
      f"你是一个精通网络工程和 RouterOS 的专业翻译专家。"
      f"请将输入的英文技术文档翻译为【{target_lang_name}】。\n"
      f'对于正文段落，请转换为带双语属性的标签：<span class="bilingual-text" data-original="英文原文">译文</span>。\n'
      f"注意：Markdown 标题（#）、代码块（```）、表格结构和 Front Matter 元数据不要包含在 span 标签内，仅翻译标题文字。"
  )

  headers = {
      "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
      "Content-Type": "application/json",
  }

  payload = {
      "model": "deepseek-chat",
      "messages": [
          {"role": "system", "content": prompt},
          {"role": "user", "content": text},
      ],
      "temperature": 0.3,
  }

  try:
    response = requests.post(
        DEEPSEEK_API_URL, headers=headers, json=payload, timeout=90
    )
    if response.status_code == 200:
      return response.json()["choices"][0]["message"]["content"]
    else:
      print(f"❌ API 调用失败 [{response.status_code}]: {response.text}")
      return text
  except Exception as e:
    print(f"❌ 请求异常: {e}")
    return text


def process_i18n_docs():
  docs_dir = "docs"
  cache = load_cache()

  if not os.path.exists(docs_dir):
    return

  for root, _, files in os.walk(docs_dir):
    for file in files:
      if file.endswith(".md") or file.endswith(".mdx"):
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, docs_dir)

        with open(file_path, "r", encoding="utf-8") as f:
          raw_content = f.read()

        file_hash = get_file_hash(raw_content)

        # 遍历所有配置的目标语种
        for locale, lang_name in TARGET_LOCALES.items():
          target_dir = os.path.join(
              "i18n", locale, "docusaurus-plugin-content-docs", "current"
          )
          target_file_path = os.path.join(target_dir, rel_path)
          cache_key = f"{locale}:{rel_path}"

          # 检查缓存：如果该语言的文件 Hash 没变，直接 Skip！
          if cache.get(cache_key) == file_hash and os.path.exists(
              target_file_path
          ):
            print(f"⚡ [{locale}] 跳过 {rel_path} (未变更)")
            continue

          print(
              f"🚀 [{locale} - {lang_name}] 正在翻译/更新文件: {rel_path}..."
          )
          translated_content = translate_doc(raw_content, lang_name)

          os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
          with open(target_file_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

          cache[cache_key] = file_hash

  save_cache(cache)


if __name__ == "__main__":
  process_i18n_docs()
