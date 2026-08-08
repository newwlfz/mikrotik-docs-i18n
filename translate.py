import hashlib
import json
import os
import re
import requests

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
CACHE_FILE = "doc_cache.json"


def get_file_hash(content: str) -> str:
  """计算字符串的 SHA-256 哈希值"""
  return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_cache() -> dict:
  if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
      return json.load(f)
  return {}


def save_cache(cache: dict):
  with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)


def translate_text_with_deepseek(text: str) -> str:
  """调用 DeepSeek V3 将正文翻译为双语对照标签格式"""
  if not DEEPSEEK_API_KEY:
    print("⚠️ 未配置 DEEPSEEK_API_KEY，跳过翻译调用（保留原文）")
    return text

  prompt = (
      "你是一个精通网络工程和 RouterOS 的专业翻译专家。"
      "请将输入的英文技术文档转换为中文，并保持技术术语准确。"
      "对正文段落，请包装为带有双语属性的 HTML 标签，格式如："
      '<span class="bilingual-text" data-original="英文原文">中文译文</span>。\n'
      "注意：Markdown 标题（#）、代码块（```）、表格语法和Front"
      " Matter元数据不要包装标签，仅翻译标题文本或保持代码原样。"
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
        DEEPSEEK_API_URL, headers=headers, json=payload, timeout=60
    )
    if response.status_code == 200:
      return response.json()["choices"][0]["message"]["content"]
    else:
      print(f"❌ API 调用失败 [{response.status_code}]: {response.text}")
      return text
  except Exception as e:
    print(f"❌ 请求异常: {e}")
    return text


def process_docs():
  docs_dir = "docs"
  cache = load_cache()
  updated_count = 0

  if not os.path.exists(docs_dir):
    os.makedirs(docs_dir)

  for root, _, files in os.walk(docs_dir):
    for file in files:
      if file.endswith(".md") or file.endswith(".mdx"):
        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8") as f:
          raw_content = f.read()

        current_hash = get_file_hash(raw_content)

        # 比对 Hash 决定是否发起翻译
        if cache.get(file_path) == current_hash:
          print(f"⚡ [跳过] {file_path} 内容未变动（耗费 0 Token）")
          continue

        print(f"🚀 [更新] 检测到 {file_path} 变更/新建，进行整篇翻译...")
        translated_content = translate_text_with_deepseek(raw_content)

        # 覆写文件并更新哈希缓存
        with open(file_path, "w", encoding="utf-8") as f:
          f.write(translated_content)

        cache[file_path] = get_file_hash(translated_content)
        updated_count += 1

  save_cache(cache)
  print(f"✅ 处理完成，本次共更新/翻译了 {updated_count} 个文档。")


if __name__ == "__main__":
  process_docs()
