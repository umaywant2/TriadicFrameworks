// @ts-check
// Docusaurus config using CommonJS (Node 20/24 compatible)

const prismThemes = require('prism-react-renderer').themes;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Triadic-docs',
  tagline: 'TriadicFrameworks Documentation',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://docs.triadicframeworks.org',
  baseUrl: '/',

  organizationName: 'TriadicFrameworks',
  projectName: 'triadic-docs',

  onBrokenLinks: 'throw',

  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },

    navbar: {
      title: 'Triadic-docs',
      logo: {
        alt: 'Triadic Docs Logo',
        src: 'img/triadic-logo.svg',
      },
      items: [
  
        { to: '/docs/book/book-overview', label: 'Canon', position: 'left' },
        { to: '/docs/speeches/speeches-overview', label: 'Speeches', position: 'left' },
        { to: '/docs/contributing', label: 'Contributing', position: 'right' },
        { href: 'https://www.triadicframeworks.org', label: 'Main Site', position: 'right' },
      ],
    },

    footer: {
      style: 'dark',
      links: [
        {
          title: 'Canon',
          items: [
            { label: 'Overview', to: '/docs/book/overview' },
            { label: 'Glossary', to: '/docs/book/glossary' },
            { label: 'Registry', to: '/docs/book/registry' },
          ],
        },
        {
          title: 'Speeches',
          items: [
            { label: 'Overview', to: '/docs/speeches/speeches-overview' },
            { label: 'Cadences', to: '/docs/speeches/speeches-index' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Contributing', to: '/docs/contributing' },
            { label: 'GitHub', href: 'https://github.com/umaywant2/TriadicFrameworks' },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} TriadicFrameworks — RTT Canon`,
    },

    prism: {
      theme: prismThemes.dracula,
    },
  },
};

module.exports = config;
