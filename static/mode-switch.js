// static/mode-switch.js
function setPrefLangCookie(lang) {
  document.cookie = "pref_lang=" + lang + "; path=/; max-age=" + (30 * 24 * 60 * 60);
  localStorage.setItem('pref_lang', lang);
}

window.switchBilingualMode = function (mode) {
  document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
  document.body.classList.add('mode-' + mode);
  localStorage.setItem('bilingual-mode', mode);
};

function initBilingualUI() {
  const path = window.location.pathname;
  const activeMap = window.__ACTIVE_I18N_UI__ || {};

  const pathSegments = path.split('/').filter(Boolean);
  const currentLocaleKey = Object.keys(activeMap).find((key) =>
    pathSegments.includes(key)
  );

  const switcher = document.getElementById('mode-switcher');
  const announcementContainer = document.getElementById('nav-announcement-bar');

  // 1. 如果处于纯英文原生页面
  if (!currentLocaleKey) {
    if (switcher) switcher.style.display = 'none';
    if (announcementContainer) announcementContainer.style.display = 'none';
    document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');

    // 监听：如果用户在原生 LocaleDropdown 中手动切到了英文，更新 Cookie 记录为 'en'
    setPrefLangCookie('en');
    return;
  }

  // 2. 如果处于已开启的翻译语种页面
  setPrefLangCookie(currentLocaleKey);

  // 渲染 Navbar 中间的 Announcement
  if (announcementContainer) {
    if (activeMap[currentLocaleKey] && activeMap[currentLocaleKey].announcement) {
      announcementContainer.innerHTML = activeMap[currentLocaleKey].announcement;
      announcementContainer.style.display = 'inline-block';
    } else {
      announcementContainer.style.display = 'none';
    }
  }

  // 渲染 Navbar 右侧的模式切换下拉框
  if (switcher) {
    const labels = activeMap[currentLocaleKey];
    if (labels) {
      switcher.innerHTML = `
        <option value="hover">${labels.hover}</option>
        <option value="collapse">${labels.collapse}</option>
        <option value="clean">${labels.clean}</option>
      `;
      switcher.style.display = 'inline-block';
    }

    const savedMode = localStorage.getItem('bilingual-mode') || 'hover';
    window.switchBilingualMode(savedMode);
    switcher.value = savedMode;

    switcher.onchange = function (e) {
      window.switchBilingualMode(e.target.value);
    };
  }
}

// 初始化及单页应用（SPA）路由变更监听
document.addEventListener('DOMContentLoaded', initBilingualUI);

// 防止 React / Docusaurus 异步重新渲染丢失 DOM 节点
let lastPath = window.location.pathname;
const observer = new MutationObserver(() => {
  if (window.location.pathname !== lastPath || !document.getElementById('nav-announcement-bar')) {
    lastPath = window.location.pathname;
    setTimeout(initBilingualUI, 50);
  }
});

document.addEventListener('DOMContentLoaded', () => {
  observer.observe(document.body, { childList: true, subtree: true });
});
