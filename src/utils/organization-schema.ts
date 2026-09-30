import { getSiteUrl } from '~/utils/site-url';

export const ORGANIZATION_ID = `${getSiteUrl()}/#organization`;

export function buildOrganizationSchema() {
  const siteUrl = getSiteUrl();
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    '@id': ORGANIZATION_ID,
    name: 'Crest Creatine',
    alternateName: ['Crest Creatine OEM', 'Private Label Creatine Manufacturer'],
    url: `${siteUrl}/`,
    logo: `${siteUrl}/brand/logo-mark.png`,
    description:
      'B2B creatine manufacturer offering OEM / private label creatine powder and gummies, wholesale carton supply, samples, COA and third-party testing support for brands, distributors, gyms, and online sellers.',
    image: `${siteUrl}/brand/logo-mark.png`,
    address: {
      '@type': 'PostalAddress',
      addressCountry: 'CN',
    },
    areaServed: 'Worldwide',
    knowsAbout: [
      'Private label creatine',
      'Wholesale creatine',
      'Creatine manufacturer',
      'Private label creatine gummies',
      'Bulk creatine wholesale',
      'Creatine monohydrate OEM',
    ],
    contactPoint: [
      {
        '@type': 'ContactPoint',
        contactType: 'sales',
        availableLanguage: ['English'],
        areaServed: 'Worldwide',
      },
    ],
  };
}

export function buildManufacturingPlantSchema() {
  const siteUrl = getSiteUrl();
  return {
    '@context': 'https://schema.org',
    '@type': 'ManufacturingPlant',
    '@id': `${siteUrl}/quality/#manufacturing-plant`,
    name: 'Crest Creatine Production',
    url: `${siteUrl}/quality`,
    parentOrganization: { '@id': ORGANIZATION_ID },
    address: {
      '@type': 'PostalAddress',
      addressCountry: 'CN',
    },
    description:
      'Supplement manufacturing for creatine monohydrate powder and creatine gummies — private label OEM and wholesale carton programs with COA and third-party testing pathways.',
    areaServed: 'Worldwide',
    knowsAbout: [
      'Creatine monohydrate powder',
      'Creatine gummies private label',
      'Dietary supplement OEM',
      'Wholesale creatine cartons',
    ],
  };
}

export function buildAboutPageSchema() {
  const siteUrl = getSiteUrl();
  return {
    '@context': 'https://schema.org',
    '@type': 'AboutPage',
    '@id': `${siteUrl}/quality/#webpage`,
    url: `${siteUrl}/quality`,
    name: 'Quality & Compliance | Crest Creatine',
    description:
      'Quality, testing, and US dietary supplement compliance overview for Crest Creatine OEM and wholesale partners.',
    isPartOf: { '@type': 'WebSite', url: `${siteUrl}/` },
    about: { '@id': ORGANIZATION_ID },
  };
}

export function buildContactPageSchema() {
  const siteUrl = getSiteUrl();
  return {
    '@context': 'https://schema.org',
    '@type': 'ContactPage',
    '@id': `${siteUrl}/contact/#webpage`,
    url: `${siteUrl}/contact`,
    name: 'Contact Crest Creatine',
    description:
      'Request private label creatine OEM quotes, wholesale price lists, and samples from Crest Creatine.',
    isPartOf: { '@type': 'WebSite', url: `${siteUrl}/` },
    mainEntity: { '@id': ORGANIZATION_ID },
  };
}

/** Real Crest OEM product lines (same three programs as /products). No list prices. */
export type CrestProductProgram = {
  name: string;
  description: string;
  url: string;
  image: string;
  category: string;
  moq: string;
};

export function getCrestProductPrograms(
  siteUrl: string,
  productsPath: string,
  labels?: {
    gummiesTitle: string;
    gummiesIntro: string;
    powderTitle: string;
    powderIntro: string;
    capsTitle: string;
    capsIntro: string;
  },
): CrestProductProgram[] {
  const L = labels ?? {
    gummiesTitle: 'Creatine gummies',
    gummiesIntro:
      'A convenient, pre-portioned creatine monohydrate gummy program for brands that want a scoop-free daily sports-nutrition SKU.',
    powderTitle: 'Creatine monohydrate powder',
    powderIntro: 'Pure creatine monohydrate powder in retail-ready tubs, pouches, or bulk formats.',
    capsTitle: 'Creatine capsules',
    capsIntro: 'A scoop-free creatine monohydrate format for travel and convenience channels.',
  };

  return [
    {
      name: L.gummiesTitle,
      description: L.gummiesIntro,
      url: `${siteUrl}${productsPath}#gummies`,
      image: `${siteUrl}/images/products/creatine-gummies.svg`,
      category: 'Creatine gummies OEM',
      moq: 'Trial/program MOQs commonly start around 1,000 units for standard bottle programs.',
    },
    {
      name: L.powderTitle,
      description: L.powderIntro,
      url: `${siteUrl}${productsPath}#powder`,
      image: `${siteUrl}/images/products/creatine-powder.svg`,
      category: 'Creatine monohydrate powder OEM',
      moq: 'Trial private-label powder often in the 500–1,000 unit range.',
    },
    {
      name: L.capsTitle,
      description: L.capsIntro,
      url: `${siteUrl}${productsPath}#capsules`,
      image: `${siteUrl}/images/products/creatine-capsules.svg`,
      category: 'Creatine capsules OEM',
      moq: 'Capsule programs commonly start around 1,000 bottles.',
    },
  ];
}

export function buildProductItemListSchema(
  products: CrestProductProgram[],
  listName = 'Crest Creatine OEM product programs',
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: listName,
    itemListElement: products.map((product, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      item: {
        '@type': 'Product',
        name: product.name,
        description: product.description,
        image: product.image,
        url: product.url,
        brand: { '@type': 'Brand', name: 'Crest Creatine' },
        category: product.category,
        offers: {
          '@type': 'Offer',
          url: product.url,
          availability: 'https://schema.org/InStock',
          description: product.moq,
        },
      },
    })),
  };
}
