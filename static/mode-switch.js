// 切换模式并保存至 LocalStorage
window.switchBilingualMode = function (mode) {
  document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
  document.body.classList.add('mode-' + mode);
  localStorage.setItem('bilingual-mode', mode);
};

document.addEventListener('DOMContentLoaded', function () {
  const path = window.location.pathname;
  const switcher = document.getElementById('mode-switcher');

  if (!switcher) return;

  // 判断是否为英文原版页面（根目录或 /en/ 开头）
  // 注意：以你的 baseUrl (/mikrotik-docs-i18n/) 为基准
  const isEnglish = path.endsWith('/en/') || path.includes('/en/doc') || 
                    (path.includes('/mikrotik-docs-i18n/') && !path.includes('/zh-Hans/') && !path.includes('/zh-Hant/'));

  if (isEnglish) {
    // 1. 英文版：只有原文，隐藏模式切换菜单
    switcher.style.display = 'none';
    document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
    return;
  }

  // 2. 翻译版页面：显示下拉菜单，并根据当前语言动态匹配菜单选项文本
  switcher.style.display = 'inline-block';

  const isHant = path.includes('/zh-Hant/');
  
  // 多语言下拉菜单选项字典
  const labels = isHant ? {
    hover: '🔍 懸停顯示原文',
    collapse: '📖 折疊顯示原文',
    clean: '📄 僅顯示中文'
  } : {
    hover: '🔍 悬停显示原文',
    collapse: '📖 折叠显示原文',
    clean: '📄 仅显示中文'
  };

  // 动态更新下拉框中的 option 文本
  switcher.innerHTML = `
    <option value="hover">${labels.hover}</option>
    <option value="collapse">${labels.collapse}</option>
    <option value="clean">${labels.clean}</option>
  `;

  // 读取上次保存的模式，还原生效
  const savedMode = localStorage.getItem('bilingual-mode') || 'hover';
  window.switchBilingualMode(savedMode);
  switcher.value = savedMode;

  // 绑定切换事件
  switcher.addEventListener('change', function (e) {
    window.switchBilingualMode(e.target.value);
  });
});
