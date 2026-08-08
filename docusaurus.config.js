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

// 构建激活语种的前缀匹配逻辑
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
          function setPref(lang) {
            document.cookie = "pref_lang=" + lang + "; path=/; max-age=" + (30 * 24 * 60 * 60);
            try { localStorage.setItem('pref_lang', lang); } catch(e) {}
          }

          function getPref() {
            var value = "; " + document.cookie;
            var parts = value.split("; pref_lang=");
            if (parts.length === 2) return parts.pop().split(";").shift();
            try { return localStorage.getItem('pref_lang'); } catch(e) {}
            return null;
          }

          var rawPath = window.location.pathname;
          var cleanPath = rawPath.endsWith('/') ? rawPath.slice(0, -1) : rawPath;
          var activeLocales = ${JSON.stringify(activeLocales)};

          // 检测当前 URL 究竟处于哪个语种路径下
          var pathSegments = cleanPath.split('/').filter(Boolean);
          var currentPathLang = activeLocales.find(function(code) {
            return pathSegments.indexOf(code) !== -1;
          }) || 'en';

          // 核心点：当用户已经在某个语言页面时，刷新该语言的持久化记忆
          if (cleanPath !== '/mikrotik-docs-i18n') {
            setPref(currentPathLang);
          }

          // 如果访问的是根路径 /mikrotik-docs-i18n 或 /mikrotik-docs-i18n/
          if (cleanPath === '/mikrotik-docs-i18n') {
            var savedLang = getPref();

            // 首次访问无任何记忆时，依据浏览器语言判断并写入记忆
            if (!savedLang) {
              var userLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
              var matchedLang = '';
              ${redirectionLogic}
              savedLang = matchedLang || 'en';
              setPref(savedLang);
            }

            // 如果记忆语种为非默认英文（如 zh-Hans），跳转到对应语言目录
            if (savedLang !== 'en') {
              window.location.replace('/mikrotik-docs-i18n/' + savedLang + '/');
            } else {
              // 记忆明确为英文时，保持停留在根路径并确认记忆为 en
              setPref('en');
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
          src: 'https://manual.mikrotik.com/img/logo.svg',
        },
        items: [
          {
            type: 'html',
            position: 'left',
            value: '<div id="nav-announcement-bar" class="nav-announcement-inline" style="display:none;"></div>',
          },
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
