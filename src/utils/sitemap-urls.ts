import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

import type { SitemapItem } from '@astrojs/sitemap';

/** Locale prefixes used in URL paths (not hreflang codes). */
export const SITEMAP_LOCALE_PREFIXES = ['zh-tw', 'hi', 'es', 'ar', 'fr', 'bn', 'pt', 'ru', 'ur', 'id', 'de', 'ja', 'ko', 'vi', 'th'] as const;

/** Match trailingSlash: false — origin home has no slash; other paths have no trailing slash. */
export function canonicalizeSitemapUrl(url: string): string {
  try {
    const u = new URL(url);
    u.hash = '';
    const path = u.pathname.replace(/\/+$/, '') || '/';
    if (path === '/') return u.origin;
    return `${u.origin}${path}${u.search}`;
  } catch {
    return url.replace(/\/+$/, '');
  }
}

function englishSitemapUrl(item: SitemapItem): string {
  const fromLinks = item.links?.find((l) => l.lang === 'en')?.url;
  if (fromLinks) return canonicalizeSitemapUrl(fromLinks);
  return canonicalizeSitemapUrl(item.url);
}

/** Align loc/hreflang (no trailing slash) and add x-default. */
export function serializeSitemapItem(item: SitemapItem): SitemapItem {
  item.url = canonicalizeSitemapUrl(item.url);
  const links = (item.links ?? []).map((l) => ({
    ...l,
    url: canonicalizeSitemapUrl(l.url),
  }));
  const enUrl = englishSitemapUrl({ ...item, links });
  if (!links.some((l) => l.lang === 'en')) {
    links.push({ url: enUrl, lang: 'en' });
  }
  if (!links.some((l) => l.lang === 'x-default')) {
    links.push({ url: enUrl, lang: 'x-default' });
  }
  item.links = links;
  return item;
}

/** Strip origin trailing slash that `new URL().href` puts back on xhtml:link. */
export function rewriteSitemapTrailingSlash(distDir: string): void {
  const files = readdirSync(distDir).filter((name) => /^sitemap.*\.xml$/i.test(name));
  for (const name of files) {
    const path = join(distDir, name);
    const xml = readFileSync(path, 'utf8');
    const next = xml
      .replace(/(<loc>)(https?:\/\/[^/<]+)\/(<\/loc>)/g, '$1$2$3')
      .replace(/(href=")(https?:\/\/[^/<]+)\/(")/g, '$1$2$3');
    if (next !== xml) writeFileSync(path, next);
  }
}

/** Path without locale prefix, no trailing slash. */
export function sitemapPathnameKey(page: string): string {
  const pathname = new URL(page).pathname.replace(/\/+$/, '') || '/';
  const parts = pathname.split('/').filter(Boolean);
  const first = parts[0];
  if (first && (SITEMAP_LOCALE_PREFIXES as readonly string[]).includes(first)) {
    const rest = parts.slice(1).join('/');
    return rest ? `/${rest}` : '/';
  }
  return pathname;
}

/** Keep sitemap aligned with indexable URLs only. */
export function isIndexableSitemapPage(page: string): boolean {
  try {
    const key = sitemapPathnameKey(page);
    if (/^\/(internal|landing)(\/|$)/.test(key)) return false;
    if (/^\/tag(\/|$)/.test(key)) return false;
    if (/^\/blog\/\d+$/.test(key)) return false;
    if (/^\/category\/[^/]+\/\d+$/.test(key)) return false;
    return true;
  } catch {
    return false;
  }
}
