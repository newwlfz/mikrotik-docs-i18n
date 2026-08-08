// static/mode-switch.js
function setPrefLangCookie(lang) {
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

  // 1. 如果处于纯英文原生页面
  if (!currentLocaleKey) {
    if (switcher) switcher.style.display = 'none';
    if (announcementContainer) announcementContainer.style.display = 'none';
    document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
    setPrefLangCookie('en');
    return;
  }

  // 2. 处于已开启的翻译语种页面
  setPrefLangCookie(currentLocaleKey);

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

// 拦截全局 Navbar 语言下拉框点击事件：点击切换 English 时立即使 Cookie 生效为 'en'
document.addEventListener('click', function(e) {
  const target = e.target.closest('a');
  if (target && target.classList.contains('dropdown__link')) {
    const href = target.getAttribute('href') || '';
    // 如果点击的是切换到英文（根目录路径或包含 /en/）
    if (href === '/mikrotik-docs-i18n/' || href.includes('/mikrotik-docs-i18n/en/')) {
      setPrefLangCookie('en');
    } else {
      // 提取目标语种
      const matches = href.match(/\/mikrotik-docs-i18n\/([^\/]+)\//);
      if (matches && matches[1]) {
        setPrefLangCookie(matches[1]);
      }
    }
  }
});

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
