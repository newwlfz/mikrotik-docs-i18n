// docusaurus.config.js
// @ts-check
const { SUPPORTED_LOCALES, activeLocales } = require('./i18n.config');

const buildDate = new Date().toISOString().split('T')[0];

const localeConfigs = {
  en: { label: 'English', direction: 'ltr' },
};
activeLocales.forEach((code) => {
  localeConfigs[code] = {
    label: SUPPORTED_LOCALES[code].label,
    direction: 'ltr',
  };
});

// 构建特定语种跳转映射
const redirectionLogic = activeLocales
  .map((code) => {
    const prefixes = SUPPORTED_LOCALES[code].detectPrefixes;
    const cond = prefixes
      .map((p) => "userLang.indexOf('" + p + "') === 0")
      .join(' || ');
    return "if (" + cond + ") { matchedLang = '" + code + "'; }";
  })
  .join(' else ');

const activeDropdownUI = {};
activeLocales.forEach((code) => {
  const item = SUPPORTED_LOCALES[code];
  activeDropdownUI[code] = {
    ...item.dropdownLabels,
    announcement: item.announcement ? item.announcement.replace('{time}', buildDate) : '',
  };
});

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'MikroTik RouterOS Documentation',
  tagline: 'AI-Powered Multilingual Mirror & Localization',
  favicon: 'img/favicon.ico',

  url: 'https://newwlfz.github.io',
  baseUrl: '/mikrotik-docs-i18n/',
  organizationName: 'newwlfz',
  projectName: 'mikrotik-docs-i18n',

  onBrokenLinks: 'ignore',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  headTags: [
    {
      tagName: 'script',
      attributes: { type: 'text/javascript' },
      innerHTML: `
        window.__ACTIVE_I18N_UI__ = ${JSON.stringify(activeDropdownUI)};

        (function() {
          function setCookie(name, val) {
            document.cookie = name + "=" + val + "; path=/; max-age=" + (30 * 24 * 60 * 60);
            try { localStorage.setItem(name, val); } catch(e) {}
          }

          function getCookie(name) {
            var value = "; " + document.cookie;
            var parts = value.split("; " + name + "=");
            if (parts.length === 2) return parts.pop().split(";").shift();
            try { return localStorage.getItem(name); } catch(e) {}
            return null;
          }

          var path = window.location.pathname;
          var activeLocales = ${JSON.stringify(activeLocales)};
          var cleanPath = path.endsWith('/') ? path.slice(0, -1) : path;

          // 1. 如果当前页面本身就是某个语言子路径（例如 /zh-Hans/...），刷新 Cookie 记录
          var matchedPathLocale = activeLocales.find(function(code) {
            return path.indexOf('/mikrotik-docs-i18n/' + code) === 0;
          });

          if (matchedPathLocale) {
            setCookie('pref_lang', matchedPathLocale);
            return;
          }

          // 2. 如果当前处于根目录路径 (/mikrotik-docs-i18n)
          if (cleanPath === '/mikrotik-docs-i18n') {
            var savedLang = getCookie('pref_lang');

            // 如果没有记录，才按浏览器语言自动判断
            if (!savedLang) {
              var userLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
              var matchedLang = '';
              ${redirectionLogic}
              savedLang = matchedLang || 'en';
              setCookie('pref_lang', savedLang);
            }

            // 当且仅当 Cookie 中明确记录的不是 en 时才进行跳转
            if (savedLang && savedLang !== 'en') {
              window.location.replace('/mikrotik-docs-i18n/' + savedLang + '/');
            }
          }
        })();
      `,
    },
  ],

  i18n: {
    defaultLocale: 'en',
    locales: ['en', ...activeLocales],
    localeConfigs: localeConfigs,
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/',
        },
        blog: false,
        theme: { customCss: require.resolve('./src/css/custom.css') },
      }),
    ],
  ],

  scripts: [
    {
      src: '/mikrotik-docs-i18n/mode-switch.js',
      defer: true,
    },
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'MikroTik Docs i18n',
        logo: {
          alt: 'MikroTik Logo',
          src: 'img/logo.svg', // 使用本地 static/img/logo.svg
        },
        items: [
          // Navbar 中间的 Announcement
          {
            type: 'html',
            position: 'left',
            value: '<div id="nav-announcement-bar" class="nav-announcement-inline" style="display:none;"></div>',
          },
          // 模式切换下拉框
          {
            type: 'html',
            position: 'right',
            value: '<select id="mode-switcher" class="mode-select-dropdown" style="display:none;"></select>',
          },
          { type: 'localeDropdown', position: 'right' },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} MikroTik Docs Multilingual Mirror. Powered by Docusaurus & DeepSeek.`,
      },
    }),
};

module.exports = config;
