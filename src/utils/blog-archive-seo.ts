// Do not append brand here — Layout titleTemplate already adds " | Hi Mah Jongg".
const BLOG_OG_DEFAULT = { url: '/manjongg/sets/hero-celadon-classic.jpg', width: 1200, height: 628 };

const categoryDescriptions: Record<string, string> = {
  'Sourcing Guide':
    'B2B sourcing articles on American Mah Jongg OEM, wholesale MOQ, custom artwork, private label, and factory partnerships from Hi Mah Jongg.',
  'Product Knowledge':
    'American Mah Jongg product knowledge for brands and distributors — multi-layer acrylic tiles, set composition, and catalog planning.',
};

const categoryTitles: Record<string, string> = {
  'Sourcing Guide': 'American Mah Jongg Sourcing Guide',
  'Product Knowledge': 'American Mah Jongg Product Knowledge',
};

export function getBlogArchiveOpenGraph(_categoryTitle?: string) {
  return { type: 'website' as const, images: [BLOG_OG_DEFAULT] };
}

export function getBlogListMetadata(page: number) {
  const pageSuffix = page > 1 ? ` — Page ${page}` : '';
  return {
    title: `American Mah Jongg OEM Blog${pageSuffix}`,
    description:
      'OEM sourcing guides for custom American Mah Jongg sets, wholesale buyers, private label, and factory-direct tile production.',
    openGraph: getBlogArchiveOpenGraph(),
  };
}

export function getBlogCategoryMetadata(categoryTitle: string, page: number) {
  const pageSuffix = page > 1 ? ` — Page ${page}` : '';
  const title = categoryTitles[categoryTitle] ?? categoryTitle;
  const description =
    categoryDescriptions[categoryTitle] ??
    `Articles in ${categoryTitle} from Hi Mah Jongg — American Mah Jongg OEM insights for wholesale buyers.`;

  return {
    title: `${title}${pageSuffix}`,
    description,
    openGraph: getBlogArchiveOpenGraph(categoryTitle),
  };
}

export function getBlogTagMetadata(tagTitle: string, page: number) {
  const pageSuffix = page > 1 ? ` — Page ${page}` : '';
  return {
    title: `${tagTitle} Articles${pageSuffix}`,
    description: `Blog posts tagged "${tagTitle}" — B2B American Mah Jongg manufacturing, sourcing, and private label insights from Hi Mah Jongg.`,
    openGraph: getBlogArchiveOpenGraph(),
  };
}
