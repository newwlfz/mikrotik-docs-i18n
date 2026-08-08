// @ts-check

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'MikroTik RouterOS 文档（中文镜像）',
  tagline: '基于 AI 自动同步与地道本土化翻译',
  favicon: 'img/favicon.ico',

  url: 'https://newwlfz.github.io', // 部署时替换为你的 GitHub 用户名
  baseUrl: '/mikrotik-docs-zh/',
  organizationName: 'newwlfz', // 替换为你的 GitHub 用户名
  projectName: 'mikrotik-docs-zh',

  onBrokenLinks: 'ignore',
    markdown: {
      hooks: {
        onBrokenMarkdownLinks: 'warn',
      },
    },

  // 1. 多语言配置 (简体 / 繁体 / 英文)
  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans', 'zh-Hant', 'en'],
    localeConfigs: {
      'zh-Hans': { label: '简体中文' },
      'zh-Hant': { label: '繁體中文' },
      'en': { label: 'English (Original)' },
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/', // 让文档直接作为网站首页展示
        },
        blog: false, // 禁用博客功能
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  // 注入双语模式控制脚本
  scripts: [
    {
      src: '/mikrotik-docs-zh/mode-switch.js',
      defer: true,
    },
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'MikroTik 文档',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: '用户手册',
          },
          // 右侧：双语交互模式切换下拉框
          {
            type: 'html',
            position: 'right',
            value: `
              <select id="mode-switcher" class="mode-select-dropdown" onchange="window.switchBilingualMode(this.value)">
                <option value="hover">🔍 模式：悬停显示原文</option>
                <option value="collapse">📂 模式：折叠显示原文</option>
                <option value="clean">📖 模式：仅看中文译文</option>
              </select>
            `,
          },
          // 多语言下拉切换
          {
            type: 'localeDropdown',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} MikroTik Docs Chinese Mirror. Powered by Docusaurus & DeepSeek.`,
      },
    }),
};

module.exports = config;
