/** UTM on URLs meant for LLM citation so AI traffic survives stripped referrers. */
export const LLM_UTM = {
  utm_source: 'ai',
  utm_medium: 'llm',
  utm_campaign: 'llms_txt',
} as const;

const SKIP_PATHS = new Set(['/sitemap-index.xml', '/robots.txt', '/llms.txt', '/llms-full.txt', '/rss.xml']);

export function withLlmUtm(url: string): string {
  let parsed: URL;
  try {
    parsed = new URL(url);
  } catch {
    return url;
  }

  if (parsed.hostname.replace(/^www\./, '').toLowerCase() !== 'mahjonggsupplies.com') {
    return url;
  }
  if (SKIP_PATHS.has(parsed.pathname)) return url;

  parsed.searchParams.set('utm_source', LLM_UTM.utm_source);
  parsed.searchParams.set('utm_medium', LLM_UTM.utm_medium);
  parsed.searchParams.set('utm_campaign', LLM_UTM.utm_campaign);
  return parsed.toString();
}

/** Rewrite https://mahjonggsupplies.com/... links in markdown / plain text. */
export function tagMahjonggLinksForLlm(body: string): string {
  return body.replace(/https:\/\/mahjonggsupplies\.com\/[^\s)>\]]*/g, (url) => {
    const trimmed = url.replace(/[.,;:]+$/, '');
    return withLlmUtm(trimmed) + url.slice(trimmed.length);
  });
}
