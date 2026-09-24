/**
 * /llms.txt — LLM-oriented site guide (https://llmstxt.org/)
 */
import { tagSiteLinksForLlm } from '~/utils/llm-urls';

export const prerender = true;

const BODY = `# Crest Creatine

> B2B creatine manufacturer for OEM / private label and wholesale. Site: https://creatine.tradeglo.net/

Crest Creatine supplies creatine monohydrate gummies, powder, and capsules for brands, distributors, gyms, and online sellers — not consumer checkout. Dietary supplement framing only; no disease-treatment claims.

## Core pages

- [Home](https://creatine.tradeglo.net/): Dual OEM + wholesale overview and quote CTA
- [OEM / Private Label](https://creatine.tradeglo.net/oem): Private label creatine programs
- [Wholesale](https://creatine.tradeglo.net/wholesale): Carton supply and price-list requests
- [Products](https://creatine.tradeglo.net/products): Gummies, powder, capsules hub
- [Quality & Compliance](https://creatine.tradeglo.net/quality): COA / testing / US supplement overview
- [Contact](https://creatine.tradeglo.net/contact): RFQ and sample requests

## Company

- [About](https://creatine.tradeglo.net/about): Redirects to quality / company overview
- [FAQ](https://creatine.tradeglo.net/faq): Buyer FAQ for OEM and wholesale

## Legal

- [Privacy](https://creatine.tradeglo.net/privacy)
- [Terms](https://creatine.tradeglo.net/terms)
- [Sitemap](https://creatine.tradeglo.net/sitemap-index.xml)
`;

export const GET = async () => {
  const body = tagSiteLinksForLlm(BODY.replace(/^\uFEFF/, '').trimStart()) + '\n';

  return new Response(body, {
    status: 200,
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      'Cache-Control': 'public, max-age=3600, must-revalidate',
      'X-Content-Type-Options': 'nosniff',
    },
  });
};
