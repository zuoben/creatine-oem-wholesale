export const LOCALES = ['en'] as const;
export type Locale = (typeof LOCALES)[number];
export const DEFAULT_LOCALE: Locale = 'en';

export const LOCALE_META: Record<
  Locale,
  { name: string; htmlLang: string; ogLocale: string; dir: 'ltr' }
> = {
  en: { name: 'English', htmlLang: 'en', ogLocale: 'en_US', dir: 'ltr' },
};

export function isLocale(value: string | undefined): value is Locale {
  return Boolean(value && (LOCALES as readonly string[]).includes(value));
}

export function getLocaleFromPath(_pathname: string): Locale {
  return 'en';
}

export function stripLocale(pathname: string): string {
  return pathname.split('?')[0].split('#')[0].replace(/\/+$/, '') || '/';
}

export function localizePath(path: string, _locale: Locale = 'en'): string {
  return stripLocale(path);
}

export function getHreflangMap(pathname: string): Record<Locale, string> | null {
  const key = stripLocale(pathname);
  const pages = ['/', '/oem', '/wholesale', '/quality', '/about', '/contact', '/privacy', '/terms'];
  if (!pages.includes(key)) return null;
  return { en: key };
}

export const WHATSAPP_BY_LOCALE: Record<Locale, string> = {
  en: 'Hello, I would like to inquire about private label creatine / wholesale creatine. Please send MOQ, sample options, and pricing. Thank you!',
};
