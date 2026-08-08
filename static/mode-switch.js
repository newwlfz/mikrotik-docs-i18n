// static/mode-switch.js
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

  const pathSegments = path.split('/').filter(Boolean);

  const currentLocaleKey = Object.keys(activeMap).find((key) =>
    pathSegments.includes(key)
  );

  // 1. 处于英文原生页面
  if (!currentLocaleKey) {
    if (switcher) switcher.style.display = 'none';
    if (announcementBar) announcementBar.style.display = 'none';
    document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');

    // 主动切回英文时，移除重定向已完成标记
    sessionStorage.removeItem('i18n-redirected');
    return;
  }

  // 2. 处于激活的翻译语种页面
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
