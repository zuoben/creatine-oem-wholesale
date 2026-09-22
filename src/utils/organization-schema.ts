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
