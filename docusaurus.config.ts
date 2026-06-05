import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const githubRepository = process.env.GITHUB_REPOSITORY;
const githubOwner = process.env.GITHUB_OWNER ?? githubRepository?.split('/')[0] ?? 'daabin';
const githubProject = process.env.GITHUB_PROJECT ?? githubRepository?.split('/')[1] ?? 'The-Pragmatic-Programmer';
const githubPagesUrl = `https://${githubOwner}.github.io`;
const githubPagesBaseUrl =
  githubProject === `${githubOwner}.github.io` ? '/' : `/${githubProject}/`;

const config: Config = {
  title: 'The Pragmatic Programmer',
  tagline: 'A static reading edition built from the Markdown archive',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
    faster: false,
  },

  url: process.env.NODE_ENV === 'production' ? githubPagesUrl : 'http://127.0.0.1:3000',
  baseUrl: process.env.NODE_ENV === 'production' ? githubPagesBaseUrl : '/',
  organizationName: githubOwner,
  projectName: githubProject,

  onBrokenLinks: 'warn',
  onBrokenAnchors: 'warn',
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  markdown: {
    format: 'md',
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs-en',
          routeBasePath: '/',
          include: ['**/*.md'],
          sidebarPath: './sidebars.ts',
          showLastUpdateAuthor: false,
          showLastUpdateTime: false,
        },
        blog: false,
        pages: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'zh-cn',
        path: 'zh-CN',
        routeBasePath: 'zh-CN',
        include: ['**/*.md'],
        sidebarPath: './sidebars.zh-CN.ts',
        showLastUpdateAuthor: false,
        showLastUpdateTime: false,
      },
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'The Pragmatic Programmer',
      logo: {
        alt: 'The Pragmatic Programmer',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: '/',
          position: 'left',
          label: 'English',
        },
        {
          to: '/zh-CN/',
          position: 'left',
          label: '简体中文',
        },
        {
          href: 'https://panzhongxian.cn/en/the-pragmatic-programmer/0_toc.html',
          label: 'Source',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'light',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Reading Index',
              to: '/',
            },
          ],
        },
        {
          title: 'Source',
          items: [
            {
              label: 'Original TOC',
              href: 'https://panzhongxian.cn/en/the-pragmatic-programmer/0_toc.html',
            },
          ],
        },
        {
          title: 'Archive',
          items: [
            {
              label: 'Reading Index',
              to: '/',
            },
          ],
        },
      ],
      copyright: `Built with Docusaurus for local reading.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
