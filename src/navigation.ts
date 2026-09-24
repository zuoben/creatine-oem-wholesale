import { getPermalink } from './utils/permalinks';

export const headerData = {
  en: {
    links: [
      { text: 'Home', href: '/' },
      { text: 'Products', href: getPermalink('/products') },
      { text: 'OEM', href: getPermalink('/oem') },
      { text: 'Wholesale', href: getPermalink('/wholesale') },
      { text: 'Quality', href: getPermalink('/quality') },
      { text: 'Contact', href: getPermalink('/contact') },
    ],
    actions: [{ text: 'Request Quote', href: '/contact#inquiry-form', variant: 'primary' }],
  },
};

export const footerData = {
  en: {
    links: [
      {
        title: 'Company',
        links: [
          { text: 'Home', href: '/' },
          { text: 'Quality & Compliance', href: '/quality' },
          { text: 'Contact', href: '/contact#inquiry-form' },
        ],
      },
      {
        title: 'Programs',
        links: [
          { text: 'All products', href: '/products' },
          { text: 'Creatine Gummies', href: '/products#gummies' },
          { text: 'Creatine Powder', href: '/products#powder' },
          { text: 'Creatine Capsules', href: '/products#capsules' },
          { text: 'OEM / Private Label', href: '/oem' },
          { text: 'Wholesale', href: '/wholesale' },
        ],
      },
      {
        title: 'Support',
        links: [
          { text: 'OEM Quote', href: '/contact?looking=OEM%2FPrivate%20label#inquiry-form' },
          { text: 'Wholesale Price List', href: '/contact?looking=Wholesale%20pricing#inquiry-form' },
          { text: 'Sample Request', href: '/contact?looking=Sample#inquiry-form' },
          { text: 'FAQ', href: '/faq' },
        ],
      },
    ],
    secondaryLinks: [
      { text: 'Terms', href: getPermalink('/terms') },
      { text: 'Privacy Policy', href: getPermalink('/privacy') },
    ],
    socialLinks: [],
    footNote: `
      Made by <a class="text-primary underline dark:text-accent" href="/">Crest Creatine</a> · B2B creatine OEM & wholesale · All rights reserved.
    `,
  },
};
