// @ts-check
// Docusaurus config using CommonJS (Cloudflare + Node 22/24 compatible)

const prismThemes = require('prism-react-renderer').themes;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'My Site',
  tagline: 'Dinosaurs are cool',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://your-docusaurus-site.example.com',
  baseUrl: 'website/src/pages/index.js',

  organizationName: 'facebook',
  projectName: 'docusaurus',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    prism: {
      theme: prismThemes.dracula,
    },
    navbar: {
      title: 'TriadicFrameworks',
      logo: {
        alt: 'TriadicFrameworks Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: '/docs/book/overview', label: 'Canon', position: 'left' },
        { to: '/docs/book/AI_Edition/overview', label: 'AI Edition', position: 'left' },
        { to: '/docs/speeches/overview', label: 'Speeches', position: 'left' },
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
          title: 'AI Edition',
          items: [
            { label: 'Overview', to: '/docs/book/AI_Edition/overview' },
            { label: 'Book 1', to: '/docs/book/AI_Edition/Book1_Framework_Field_Theory/overview' },
            { label: 'Book 2', to: '/docs/book/AI_Edition/Book2_The_Inverted_Star/overview' },
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
  },
};

module.exports = config;
