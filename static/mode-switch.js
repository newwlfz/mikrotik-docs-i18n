window.switchBilingualMode = function (mode) {
  document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
  document.body.classList.add('mode-' + mode);
  localStorage.setItem('bilingual-mode', mode);
};

function initBilingualUI() {
  const path = window.location.pathname;
  const switcher = document.getElementById('mode-switcher');
  const activeMap = window.__ACTIVE_I18N_UI__ || {};

  // 获取页面顶部的 AI 免责声明 Bar
  const announcementBar = document.querySelector('.announcementBar_src-theme-AnnouncementBar-styles-module, [class*="announcementBar"]');

  // 匹配当前 URL 是否处于某个【已激活语种】路径下
  const currentLocaleKey = Object.keys(activeMap).find((key) =>
    path.includes('/' + key + '/')
  );

  // 1. 处于英文原生页面：隐藏下拉菜单，隐藏顶栏 AI 免责声明
  if (!currentLocaleKey) {
    if (switcher) switcher.style.display = 'none';
    if (announcementBar) announcementBar.style.display = 'none';
    document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
    return;
  }

  // 2. 处于翻译语种页面：显示顶栏声明与更新时间
  if (announcementBar) {
    announcementBar.style.display = 'block';
    const innerTextElement = announcementBar.querySelector('div') || announcementBar;
    if (activeMap[currentLocaleKey].announcement) {
      innerTextElement.innerHTML = activeMap[currentLocaleKey].announcement;
    }
  }

  if (!switcher) return;

  switcher.style.display = 'inline-block';
  const labels = activeMap[currentLocaleKey];

  switcher.innerHTML = `
    <option value="hover">${labels.hover}</option>
    <option value="collapse">${labels.collapse}</option>
    <option value="clean">${labels.clean}</option>
  `;

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
