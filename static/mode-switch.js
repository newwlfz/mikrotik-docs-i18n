// 模式切换函数
window.switchBilingualMode = function (mode) {
  document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
  document.body.classList.add('mode-' + mode);
  localStorage.setItem('bilingual-mode', mode);
};

document.addEventListener('DOMContentLoaded', function () {
  // 读取与设置交互模式
  const savedMode = localStorage.getItem('bilingual-mode') || 'hover';
  window.switchBilingualMode(savedMode);
  const switcher = document.getElementById('mode-switcher');
  if (switcher) switcher.value = savedMode;

  // 监听 URL 语言变化 (zh-Hans / zh-Hant / en)
  const currentPath = window.location.pathname;
  
  if (currentPath.includes('/en/')) {
    // 如果选择 English：将所有 span 替换为其 data-original 的英文原文
    document.querySelectorAll('.bilingual-text').forEach(el => {
      const orig = el.getAttribute('data-original');
      if (orig) el.textContent = orig;
    });
  } else if (currentPath.includes('/zh-Hant/')) {
    // 如果选择繁体中文：简易字符替换/转化（亦可引入 opencc-js）
    document.querySelectorAll('.bilingual-text').forEach(el => {
      el.textContent = el.textContent
        .replace(/软件/g, '軟體').replace(/网络/g, '網路')
        .replace(/服务器/g, '伺服器').replace(/独立/g, '獨立');
    });
  }
});
