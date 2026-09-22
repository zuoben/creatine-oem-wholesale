import { localizePath, type Locale } from './locales';

export function getHeaderFooter(locale: Locale = 'en') {
  const p = (path: string) => localizePath(path, locale);
  const home = p('/');
  return {
    header: {
      links: [
        { text: 'Home', href: home },
        { text: 'OEM', href: p('/oem') },
        { text: 'Wholesale', href: p('/wholesale') },
        { text: 'Quality', href: p('/quality') },
        { text: 'Contact', href: p('/contact') },
      ],
      actions: [{ text: 'Request Quote', href: `${p('/contact')}#inquiry-form`, variant: 'primary' as const }],
    },
    footer: {
      links: [
        {
          title: 'Company',
          links: [
            { text: 'Home', href: home },
            { text: 'Quality & Compliance', href: p('/quality') },
            { text: 'Contact', href: `${p('/contact')}#inquiry-form` },
          ],
        },
        {
          title: 'Programs',
          links: [
            { text: 'OEM / Private Label', href: p('/oem') },
            { text: 'Wholesale', href: p('/wholesale') },
            { text: 'Creatine Powder', href: `${p('/oem')}#powder` },
            { text: 'Creatine Gummies', href: `${p('/oem')}#gummies` },
          ],
        },
        {
          title: 'Support',
          links: [
            { text: 'OEM Quote', href: `${p('/contact')}?looking=OEM%2FPrivate%20label#inquiry-form` },
            { text: 'Wholesale Price List', href: `${p('/contact')}?looking=Wholesale%20pricing#inquiry-form` },
            { text: 'Sample Request', href: `${p('/contact')}?looking=Sample#inquiry-form` },
            { text: 'FAQ', href: `${home}#faq` },
          ],
        },
      ],
      secondaryLinks: [
        { text: 'Terms', href: p('/terms') },
        { text: 'Privacy Policy', href: p('/privacy') },
      ],
      socialLinks: [],
      footNote: `Made by <a class="text-primary underline dark:text-accent" href="${home}">Crest Creatine</a> · B2B creatine OEM & wholesale · All rights reserved.`,
    },
  };
}
