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
          path: '.',
          routeBasePath: '/',
          include: [
            'README.md',
            '00 Foreword/**/*.md',
            '00 Preface First Edition/**/*.md',
            '00 Preface Second Edition/**/*.md',
            '01 Pragmatic Philosophy/**/*.md',
            '02 Pragmatic Approach/**/*.md',
            '03 Basic Tools/**/*.md',
            '04 Pragmatic Paranoia/**/*.md',
            '05 Bend or Break/**/*.md',
            '06 Concurrency/**/*.md',
            '07 While Coding/**/*.md',
            '08 Before the Project/**/*.md',
            '09 Pragmatic Projects/**/*.md',
            '10 Postface/**/*.md',
            'A1 Bibliography/**/*.md',
            'A2 Exercise Answers/**/*.md',
          ],
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
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Chapters',
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
