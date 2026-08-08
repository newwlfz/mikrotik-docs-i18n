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
      .map((p) => `userLang.indexOf('${p}') === 0`)
      .join(' || ');
    return `if (${cond}) { matchedLang = '${code}'; }`;
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
          function getCookie(name) {
            var value = "; " + document.cookie;
            var parts = value.split("; " + name + "=");
            if (parts.length === 2) return parts.pop().split(";").shift();
            return null;
          }

          var savedLang = getCookie('pref_lang') || localStorage.getItem('pref_lang');
          var path = window.location.pathname;

          // 提取当前路径中的语言标识
          var pathSegments = path.split('/').filter(Boolean);
          var activeLocales = ${JSON.stringify(activeLocales)};
          var currentPathLang = activeLocales.find(function(code) { return pathSegments.includes(code); }) || 'en';

          // 如果访问根路径或域名入口
          var isBaseRoot = (path.replace(/\\/$/, '') === '/mikrotik-docs-i18n');

          if (isBaseRoot) {
            var targetLang = savedLang;

            if (!targetLang) {
              // 没有记录时按浏览器语言判断
              var userLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
              var matchedLang = '';
              ${redirectionLogic}
              targetLang = matchedLang || 'en';

              // 记录到 Cookie (保留 30 天) 和 localStorage
              document.cookie = "pref_lang=" + targetLang + "; path=/; max-age=" + (30 * 24 * 60 * 60);
              localStorage.setItem('pref_lang', targetLang);
            }

            if (targetLang !== 'en') {
              window.location.replace('/mikrotik-docs-i18n/' + targetLang + '/');
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
        title: 'MikroTik Docs',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentation',
          },
          // 预留中间红框位置：AI 翻译免责声明
          {
            type: 'html',
            position: 'left',
            value: '<div id="nav-announcement-bar" class="nav-announcement-inline" style="display:none;"></div>',
          },
          // 预留右侧位置：模式切换下拉菜单
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
