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

// 仅拦截/重定向至 enabled: true 的激活语种
const redirectionLogic = activeLocales
  .map((code) => {
    const prefixes = SUPPORTED_LOCALES[code].detectPrefixes;
    const cond = prefixes
      .map((p) => `userLang.indexOf('${p}') === 0`)
      .join(' || ');
    return `if (${cond}) { target = '/mikrotik-docs-i18n/${code}/'; }`;
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
          var path = window.location.pathname.replace(/\\/$/, '');
          var isBaseRoot = (path === '/mikrotik-docs-i18n');

          if (isBaseRoot) {
            var hasRedirected = sessionStorage.getItem('i18n-redirected');
            if (!hasRedirected) {
              var userLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
              var target = '';
              ${redirectionLogic}
              if (target) {
                sessionStorage.setItem('i18n-redirected', 'true');
                window.location.replace(target);
              }
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
      announcementBar: {
        id: 'ai_translation_notice',
        content: ' ',
        backgroundColor: '#fffbe6',
        textColor: '#8c6b00',
        isCloseable: true,
      },
      navbar: {
        title: 'MikroTik Docs',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentation',
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
