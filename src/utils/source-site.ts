/**
 * Canonical website id stored on shared contact_inquiries.source_site.
 */

export function hostnameFromUrl(value: string | null | undefined): string | null {
  if (!value) return null;
  const raw = value.trim();
  if (!raw) return null;

  try {
    const url = raw.includes('://') ? new URL(raw) : new URL(`https://${raw}`);
    return stripWww(url.hostname);
  } catch {
    return stripWww(raw.split('/')[0] ?? '');
  }
}

export function stripWww(host: string): string {
  return host.trim().toLowerCase().replace(/^www\./, '');
}

const CREATINE_ALIASES = new Set([
  'creatine.tradeglo.net',
  'creatine-oem-wholesale.pages.dev',
  'creatine-oem-wholesale.carefree-phalange.workers.dev',
  'localhost',
  '127.0.0.1',
]);

export function canonicalSourceSite(value: string | null | undefined, fallback: string): string {
  const host = hostnameFromUrl(value);
  if (!host) return stripWww(fallback);
  if (CREATINE_ALIASES.has(host)) return 'creatine.tradeglo.net';
  return host;
}

export function sourceSiteFromConfig(siteUrl: string | undefined): string {
  return hostnameFromUrl(siteUrl) ?? 'creatine.tradeglo.net';
}
