// static/mode-switch.js
function setPrefLang(lang) {
  document.cookie = "pref_lang=" + lang + "; path=/; max-age=" + (30 * 24 * 60 * 60);
  try { localStorage.setItem('pref_lang', lang); } catch(e) {}
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

  // 1. 处于纯英文原生页面：显式覆盖记忆为 en
  if (!currentLocaleKey) {
    if (switcher) switcher.style.display = 'none';
    if (announcementContainer) announcementContainer.style.display = 'none';
    document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
    setPrefLang('en');
    return;
  }

  // 2. 处于已激活的翻译语种页面：更新记忆为当前语种
  setPrefLang(currentLocaleKey);

  if (announcementContainer) {
    if (activeMap[currentLocaleKey] && activeMap[currentLocaleKey].announcement) {
      announcementContainer.innerHTML = activeMap[currentLocaleKey].announcement;
      announcementContainer.style.display = 'inline-block';
    } else {
      announcementContainer.style.display = 'none';
    }
  }

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

document.addEventListener('DOMContentLoaded', initBilingualUI);

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
