import path from 'path';
import { fileURLToPath } from 'url';

import { defineConfig, envField } from 'astro/config';

import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';
import icon from 'astro-icon';
import compress from 'astro-compress';

import astrowind from './vendor/integration';

import { readingTimeRemarkPlugin, responsiveTablesRehypePlugin } from './src/utils/frontmatter';
import { isIndexableSitemapPage, rewriteSitemapTrailingSlash, serializeSitemapItem } from './src/utils/sitemap-urls';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  env: {
    schema: {
      PUBLIC_SUPABASE_URL: envField.string({
        context: 'client',
        access: 'public',
        optional: true,
      }),
      PUBLIC_SUPABASE_ANON_KEY: envField.string({
        context: 'client',
        access: 'public',
        optional: true,
      }),
      PUBLIC_TURNSTILE_SITE_KEY: envField.string({
        context: 'client',
        access: 'public',
        optional: true,
      }),
    },
  },

  site: 'https://creatine-oem-wholesale.pages.dev',

  output: 'static',

  integrations: [
    sitemap({
      filter: isIndexableSitemapPage,
      serialize: serializeSitemapItem,
    }),
    {
      name: 'sitemap-canonical-urls',
      hooks: {
        'astro:build:done': ({ dir }) => {
          rewriteSitemapTrailingSlash(fileURLToPath(dir));
        },
      },
    },
    mdx(),
    icon({
      include: {
        tabler: [
          'arrow-up',
          'box',
          'brand-facebook',
          'brand-linkedin',
          'brand-paypal',
          'brand-whatsapp',
          'brand-x',
          'building-bank',
          'building-factory',
          'building-factory-2',
          'building-store',
          'calendar-check',
          'chart-arrows-vertical',
          'check',
          'chevron-down',
          'chevron-left',
          'chevron-right',
          'circle-check-filled',
          'clock',
          'diamond',
          'discount',
          'file-certificate',
          'file-invoice',
          'flask',
          'headset',
          'heart-handshake',
          'layers-intersect',
          'layout-grid',
          'mail',
          'map-pin',
          'message',
          'package',
          'paint',
          'palette',
          'phone',
          'pill',
          'send',
          'shield-check',
          'shopping-cart',
          'stack',
          'star',
          'sun',
          'tag',
          'test-pipe',
          'tools',
          'truck-delivery',
          'user',
          'x',
        ],
      },
    }),

    compress({
      CSS: true,
      HTML: {
        'html-minifier-terser': {
          removeAttributeQuotes: false,
        },
      },
      Image: false,
      JavaScript: true,
      SVG: false,
      Logger: 1,
    }),

    astrowind({
      config: './src/config.yaml',
    }),
  ],

  image: {
    domains: ['cdn.pixabay.com'],
  },

  markdown: {
    remarkPlugins: [readingTimeRemarkPlugin],
    rehypePlugins: [responsiveTablesRehypePlugin],
  },

  vite: {
    plugins: [tailwindcss()],
    resolve: {
      alias: {
        '~': path.resolve(__dirname, './src'),
      },
    },
  },
});
