/** Maps hub-duplicate blog slugs to commercial owner URLs when needed. */

export const BLOG_COMMERCIAL_CANONICAL: Record<string, string> = {};

const CTA_LABELS: Record<string, string> = {
  '/': 'Product Catalog',
  '/designer': '3D Tile Designer',
  '/contact#inquiry-form': 'Request Factory Quote',
  '/about': 'About the Factory',
  '/#oem': 'Custom OEM Capabilities',
  '/#wholesale': 'Wholesale Programs',
  '/custom-mahjong-set': 'Custom Mahjong Set Hub',
  '/custom-mahjong-tiles': 'Custom Mahjong Tiles Hub',
  '/american-mahjong-mat-factory': 'Mahjong Mat Factory',
  '/wholesale-private-label-mahjong': 'Wholesale & Private Label',
};

const BLOG_CTA_PATHS: Record<string, string> = {
  'how-to-choose-american-mah-jongg-supplier': '/wholesale-private-label-mahjong',
  'custom-mahjong-set-oem-process': '/custom-mahjong-set',
  'wholesale-american-mah-jongg-moq-pricing': '/wholesale-private-label-mahjong',
  'multi-layer-acrylic-mahjong-tiles-buyers-guide': '/custom-mahjong-tiles',
  'custom-mahjong-sets-complete-guide': '/custom-mahjong-set',
  '2026-custom-american-mahjong-set-styles': '/custom-mahjong-set',
  'whats-in-a-custom-mahjong-set': '/custom-mahjong-set',
  'american-mahjong-table-covers': '/american-mahjong-mat-factory',
  'festival-celebration-american-mahjong-set': '/custom-mahjong-set',
  'midnight-galaxy-american-mahjong-set': '/custom-mahjong-set',
  'twilight-cobweb-halloween-mahjong-set': '/custom-mahjong-set',
  'custom-vs-ready-made-american-mahjong': '/custom-mahjong-set',
  'how-to-order-custom-mahjong-tiles-from-factory': '/custom-mahjong-tiles',
  'oem-private-label-mahjong-mat-wholesale-primer': '/american-mahjong-mat-factory',
};

export const BLOG_COMMERCIAL_CANONICAL_SLUGS = new Set(Object.keys(BLOG_COMMERCIAL_CANONICAL));

export function isBlogCommercialCanonicalSlug(slug: string): boolean {
  return BLOG_COMMERCIAL_CANONICAL_SLUGS.has(slug);
}

export function isCommercialCanonicalBlogPostPath(pathname: string): boolean {
  const slug = pathname.replace(/\/+$/, '').replace(/^\//, '');
  if (!slug || slug.includes('/')) return false;
  return isBlogCommercialCanonicalSlug(slug);
}

export function getBlogCommercialCanonicalPath(slug: string): string | undefined {
  return BLOG_COMMERCIAL_CANONICAL[slug];
}

export function getBlogPostCtaTarget(slug: string): { href: string; label: string } {
  const href = BLOG_CTA_PATHS[slug] ?? '/contact#inquiry-form';
  return { href, label: CTA_LABELS[href] ?? 'Custom OEM Programs' };
}
