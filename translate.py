#!/usr/bin/env python3
"""
translate.py - 增量翻译 MikroTik 文档
职责：
1. 基于 MD5 判断文件是否需要重新翻译
2. 对启用语种逐一翻译
3. 处理 API 错误（重试、分类）
4. 维护 sync_state.json 翻译状态
"""

import os
import sys
import re
import time
import json
import hashlib
import requests
from datetime import datetime

# ========== 配置 ==========
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DOCS_DIR = "docs"
I18N_DIR = "i18n"
STATE_FILE = "sync_state.json"
RETRY_COUNT = 3
RETRY_DELAY = 2


# ========== 工具函数 ==========
def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_state_atomic(state):
    tmp_file = STATE_FILE + ".tmp"
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    os.replace(tmp_file, STATE_FILE)


def compute_md5(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def get_locales_config():
    """从 i18n.config.js 读取配置及动态生成的 Prompt"""
    import subprocess
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


def fix_content_links(content, rel_path):
    """
    后处理：
    1. 将官方绝对链接替换为相对路径（镜像站内部）
    2. 将本地相对图片链接替换为官方 CDN 绝对 URL（避免下载图片）
    """
    # 1. 替换文档内部绝对链接为相对路径
    content = re.sub(r'https?://manual\.mikrotik\.com/docs/([a-zA-Z0-9_\-/\#]+)', r'/docs/\1', content)

    # 2. 替换图片链接：./img/  ->  官方对应目录的 img/
    dir_name = os.path.dirname(rel_path)
    if dir_name:
        base_url = f"https://manual.mikrotik.com/docs/{dir_name}/"
        content = re.sub(r'\(\./img/', f'({base_url}img/', content)
    else:
        # 根目录文档（如 introduction.md）
        content = re.sub(r'\(\./img/', '(https://manual.mikrotik.com/docs/img/', content)

    return content


def is_fatal_error(status_code):
    """判断是否为致命错误（401/402）"""
    return status_code in (401, 402)


def is_client_error(status_code):
    """判断是否为客户端错误（400/422）"""
    return status_code in (400, 422)


def is_retryable_error(status_code):
    """判断是否为可重试错误（429/500/503）"""
    return status_code in (429, 500, 503)


def call_deepseek_api(system_prompt, text_content, lang, rel_path):
    """
    调用 DeepSeek API 进行翻译
    返回: (translated_text, error_code, error_message)
    """
    if not DEEPSEEK_API_KEY:
        return None, "401", "未设置 DEEPSEEK_API_KEY"

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

    # 重试循环
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            response = requests.post(DEEPSEEK_API_URL, headers=headers,
                                   json=payload, timeout=120)

            if response.status_code == 200:
                res_json = response.json()
                translated = res_json['choices'][0]['message']['content']
                # 🆕 应用后处理（链接和图片）
                translated = fix_content_links(translated, rel_path)
                return translated, None, None

            # 处理错误码
            status_code = response.status_code
            error_data = response.json().get('error', {})
            error_msg = error_data.get('message', f'HTTP {status_code}')

            if is_fatal_error(status_code):
                # 401/402 - 立即停止
                return None, str(status_code), f"{status_code}: {error_msg}"

            elif is_client_error(status_code):
                # 400/422 - 不重试，标记失败
                return None, str(status_code), f"{status_code}: {error_msg}"

            elif is_retryable_error(status_code):
                # 429/500/503 - 重试
                print(f"   ⚠️ [{lang}] 尝试 {attempt}/{RETRY_COUNT}: {status_code} {error_msg}")
                if attempt < RETRY_COUNT:
                    wait_time = RETRY_DELAY * (2 ** (attempt - 1))
                    time.sleep(wait_time)
                    continue
                else:
                    return None, str(status_code), f"{status_code}: {error_msg} (重试 {RETRY_COUNT} 次后仍失败)"

            else:
                # 其他未预期错误
                return None, str(status_code), f"{status_code}: {error_msg}"

        except requests.exceptions.Timeout:
            print(f"   ⚠️ [{lang}] 尝试 {attempt}/{RETRY_COUNT}: 超时")
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_DELAY * attempt)
                continue
            else:
                return None, "408", "请求超时 (重试 3 次后仍失败)"

        except requests.exceptions.ConnectionError:
            print(f"   ⚠️ [{lang}] 尝试 {attempt}/{RETRY_COUNT}: 连接错误")
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_DELAY * attempt)
                continue
            else:
                return None, "503", "连接错误 (重试 3 次后仍失败)"

        except Exception as e:
            print(f"   ❌ [{lang}] 尝试 {attempt}/{RETRY_COUNT}: {e}")
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_DELAY * attempt)
                continue
            else:
                return None, "500", f"未知错误: {str(e)}"

    return None, "500", "未知错误"


def translate_file(rel_path, source_content, state, config_data):
    """
    翻译单个文件的所有启用语种
    返回: (has_error, is_fatal)
    """
    active_locales = config_data.get("active", ["zh-Hans"])
    target_prompts = config_data.get("prompts", {})

    # 获取当前 MD5
    current_md5 = compute_md5(os.path.join(DOCS_DIR, rel_path))

    # 检查状态
    file_state = state.get(rel_path, {})
    cached_md5 = file_state.get("md5")
    translations = file_state.get("translations", {})

    # 如果 MD5 不匹配，清空 translations
    if cached_md5 != current_md5:
        print(f"   📝 MD5 变化，清空旧翻译状态")
        translations = {}
        file_state["translations"] = translations
        state[rel_path] = file_state

    has_error = False
    is_fatal = False
    error_details = []

    for lang in active_locales:
        # 检查该语种是否已成功翻译
        lang_status = translations.get(lang, {})
        if lang_status.get("status") == "success":
            # 已成功，跳过
            print(f"   ✅ [{lang}] 已翻译，跳过")
            continue

        # 需要翻译
        system_prompt = target_prompts.get(lang)
        if not system_prompt:
            print(f"   ⚠️ [{lang}] 未找到 Prompt，跳过")
            continue

        print(f"   🌐 [{lang}] 翻译中...")

        translated_text, error_code, error_msg = call_deepseek_api(
            system_prompt, source_content, lang, rel_path
        )

        if translated_text is not None:
            # 翻译成功
            target_dir = os.path.join(
                I18N_DIR, lang, "docusaurus-plugin-content-docs", "current",
                os.path.dirname(rel_path)
            )
            target_file = os.path.join(target_dir, os.path.basename(rel_path))
            os.makedirs(target_dir, exist_ok=True)

            with open(target_file, "w", encoding="utf-8") as f:
                f.write(translated_text)

            translations[lang] = {
                "status": "success",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            print(f"   ✅ [{lang}] 翻译成功")
        else:
            # 翻译失败
            translations[lang] = {
                "status": "failed",
                "error": error_msg or "未知错误",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            print(f"   ❌ [{lang}] 翻译失败: {error_msg}")

            if is_fatal_error(int(error_code) if error_code and error_code.isdigit() else 0):
                is_fatal = True
                error_details.append(f"[{lang}] {error_msg}")
            else:
                has_error = True

        # 每次翻译后保存状态，防止中断丢失进度
        state[rel_path] = file_state
        save_state_atomic(state)

    if is_fatal:
        print(f"\n   🛑 致命错误: {', '.join(error_details)}")
        return has_error, is_fatal

    if has_error:
        print(f"   ⚠️ 部分语种翻译失败")

    return has_error, is_fatal


def process_translation():
    """主翻译流程"""
    print("\n" + "=" * 60)
    print("MikroTik 文档同步工具 - 翻译阶段")
    print("=" * 60)

    # 1. 检查 docs 目录
    if not os.path.exists(DOCS_DIR):
        print(f"⚠️ 未找到 {DOCS_DIR} 目录，结束执行。")
        return 1

    # 2. 加载配置
    config_data = get_locales_config()
    active_locales = config_data.get("active", ["zh-Hans"])
    print(f"📝 启用语种: {active_locales}")

    # 3. 加载状态
    state = load_state()

    # 4. 收集需要处理的文件
    files_to_process = []
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md") or file.endswith(".mdx"):
                rel_path = os.path.relpath(os.path.join(root, file), DOCS_DIR)
                files_to_process.append(rel_path)

    print(f"📄 共发现 {len(files_to_process)} 个文档")

    if not files_to_process:
        print("⚠️ 没有文档需要翻译，结束执行。")
        return 1

    # 5. 处理每个文件
    total_failed = 0
    fatal_error = False

    for idx, rel_path in enumerate(files_to_process, 1):
        print(f"\n[{idx}/{len(files_to_process)}] 处理: {rel_path}")

        source_file = os.path.join(DOCS_DIR, rel_path)
        with open(source_file, "r", encoding="utf-8") as f:
            source_content = f.read()

        has_error, is_fatal = translate_file(rel_path, source_content, state, config_data)

        if has_error:
            total_failed += 1
        if is_fatal:
            fatal_error = True
            break  # 致命错误立即停止

    # 6. 最终状态检查
    print("\n" + "-" * 60)

    if fatal_error:
        print("❌ 检测到致命错误（余额不足或认证失败），翻译流程终止。")
        print("💡 请检查 API Key 或账户余额后重新运行。")
        return 1

    # 统计最终失败数
    final_failed = 0
    failed_files = []
    for rel_path, file_state in state.items():
        translations = file_state.get("translations", {})
        for lang, status in translations.items():
            if status.get("status") == "failed":
                final_failed += 1
                failed_files.append(f"{rel_path} [{lang}]: {status.get('error', '未知错误')}")

    if final_failed > 0:
        print(f"❌ 翻译完成，但有 {final_failed} 个翻译失败：")
        for item in failed_files[:10]:  # 只显示前10个
            print(f"   - {item}")
        if len(failed_files) > 10:
            print(f"   ... 还有 {len(failed_files) - 10} 个失败")
        print("\n💡 这些失败会在下次运行时自动重试。")
        print("⚠️ 由于存在失败，将不会触发 Docusaurus 构建。")
        return 1

    print("✅ 所有翻译成功完成！")
    print("📊 状态文件已更新，将触发 Docusaurus 构建。")
    return 0


# ========== 主入口 ==========
if __name__ == "__main__":
    try:
        exit_code = process_translation()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n🛑 用户中断，退出。")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生未预期的错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
