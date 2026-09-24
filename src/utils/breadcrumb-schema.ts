import { getSiteUrl } from '~/utils/site-url';

export type BreadcrumbCrumb = {
  name: string;
  path: string;
};

export const BREADCRUMB_HOME = { en: 'Home' };
export const BREADCRUMB_ABOUT = { en: 'Quality' };
export const BREADCRUMB_OEM = { en: 'OEM' };
export const BREADCRUMB_WHOLESALE = { en: 'Wholesale' };
export const BREADCRUMB_PRODUCTS = { en: 'Products' };
export const BREADCRUMB_CONTACT = { en: 'Contact' };

export function buildBreadcrumbList(crumbs: BreadcrumbCrumb[]) {
  const siteUrl = getSiteUrl();

  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: crumbs.map((crumb, index) => {
      const item = crumb.path.startsWith('http')
        ? crumb.path
        : crumb.path === '/'
          ? siteUrl
          : `${siteUrl}${crumb.path}`;

      return {
        '@type': 'ListItem',
        position: index + 1,
        name: crumb.name,
        item,
      };
    }),
  };
}
