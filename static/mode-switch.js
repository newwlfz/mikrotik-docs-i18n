window.switchBilingualMode = function (mode) {
  document.body.classList.remove('mode-hover', 'mode-collapse', 'mode-clean');
  document.body.classList.add('mode-' + mode);
  localStorage.setItem('bilingual-mode', mode);
};

document.addEventListener('DOMContentLoaded', function () {
  const savedMode = localStorage.getItem('bilingual-mode') || 'hover';
  window.switchBilingualMode(savedMode);
  const switcher = document.getElementById('mode-switcher');
  if (switcher) switcher.value = savedMode;
});
