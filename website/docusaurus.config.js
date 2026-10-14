// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'My Site',
  tagline: 'Dinosaurs are cool',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        respectPrefersColorScheme: true,
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

export default config;
