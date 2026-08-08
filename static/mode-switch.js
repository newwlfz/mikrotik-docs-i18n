window.switchBilingualMode = function (mode) {
  document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
  document.body.classList.add('mode-' + mode);
  localStorage.setItem('bilingual-mode', mode);
};

function initBilingualUI() {
  const path = window.location.pathname;
  const switcher = document.getElementById('mode-switcher');
  const activeMap = window.__ACTIVE_I18N_UI__ || {};

  const announcementBar = document.querySelector('.announcementBar_src-theme-AnnouncementBar-styles-module, [class*="announcementBar"]');

  // 精确拆分 URL 路径段，兼容 GitHub Pages 二级目录
  // 例如 "/mikrotik-docs-i18n/zh-Hans/docs/intro" -> ["mikrotik-docs-i18n", "zh-Hans", "docs", "intro"]
  const pathSegments = path.split('/').filter(Boolean);

  // 判断路径中是否包含已激活的语种 Key
  const currentLocaleKey = Object.keys(activeMap).find((key) =>
    pathSegments.includes(key)
  );

  // 1. 处于纯英文原生页面
  if (!currentLocaleKey) {
    if (switcher) switcher.style.display = 'none';
    if (announcementBar) announcementBar.style.display = 'none';
    document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
    return;
  }

  // 2. 处于已开启的翻译语种页面
  if (announcementBar) {
    announcementBar.style.display = 'block';
    const innerTextElement = announcementBar.querySelector('div') || announcementBar;
    if (activeMap[currentLocaleKey] && activeMap[currentLocaleKey].announcement) {
      innerTextElement.innerHTML = activeMap[currentLocaleKey].announcement;
    }
  }

  if (!switcher) return;

  switcher.style.display = 'inline-block';
  const labels = activeMap[currentLocaleKey];

  if (labels) {
    switcher.innerHTML = `
      <option value="hover">${labels.hover}</option>
      <option value="collapse">${labels.collapse}</option>
      <option value="clean">${labels.clean}</option>
    `;
  }

  const savedMode = localStorage.getItem('bilingual-mode') || 'hover';
  window.switchBilingualMode(savedMode);
  switcher.value = savedMode;

  switcher.onchange = function (e) {
    window.switchBilingualMode(e.target.value);
  };
}

document.addEventListener('DOMContentLoaded', initBilingualUI);

let lastPath = window.location.pathname;
const observer = new MutationObserver(() => {
  if (window.location.pathname !== lastPath) {
    lastPath = window.location.pathname;
    setTimeout(initBilingualUI, 100);
  }
});

document.addEventListener('DOMContentLoaded', () => {
  observer.observe(document.body, { childList: true, subtree: true });
});
