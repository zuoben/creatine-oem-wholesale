export const LOCALES = [
  'en',
  'zh-tw',
  'hi',
  'es',
  'ar',
  'fr',
  'bn',
  'pt',
  'ru',
  'ur',
  'id',
  'de',
  'ja',
  'ko',
  'vi',
  'th',
] as const;
export type Locale = (typeof LOCALES)[number];
export const DEFAULT_LOCALE: Locale = 'en';
export const I18N_LOCALES = LOCALES.filter((l): l is Exclude<Locale, 'en'> => l !== 'en');

export const LOCALE_META: Record<
  Locale,
  { name: string; htmlLang: string; ogLocale: string; dir: 'ltr' | 'rtl' }
> = {
  en: { name: 'English', htmlLang: 'en', ogLocale: 'en_US', dir: 'ltr' },
  'zh-tw': { name: '繁體中文', htmlLang: 'zh-Hant', ogLocale: 'zh_TW', dir: 'ltr' },
  hi: { name: 'हिन्दी', htmlLang: 'hi', ogLocale: 'hi_IN', dir: 'ltr' },
  es: { name: 'Español', htmlLang: 'es', ogLocale: 'es', dir: 'ltr' },
  ar: { name: 'العربية', htmlLang: 'ar', ogLocale: 'ar_SA', dir: 'rtl' },
  fr: { name: 'Français', htmlLang: 'fr', ogLocale: 'fr_FR', dir: 'ltr' },
  bn: { name: 'বাংলা', htmlLang: 'bn', ogLocale: 'bn_BD', dir: 'ltr' },
  pt: { name: 'Português', htmlLang: 'pt', ogLocale: 'pt_BR', dir: 'ltr' },
  ru: { name: 'Русский', htmlLang: 'ru', ogLocale: 'ru_RU', dir: 'ltr' },
  ur: { name: 'اردو', htmlLang: 'ur', ogLocale: 'ur_PK', dir: 'rtl' },
  id: { name: 'Bahasa Indonesia', htmlLang: 'id', ogLocale: 'id_ID', dir: 'ltr' },
  de: { name: 'Deutsch', htmlLang: 'de', ogLocale: 'de_DE', dir: 'ltr' },
  ja: { name: '日本語', htmlLang: 'ja', ogLocale: 'ja_JP', dir: 'ltr' },
  ko: { name: '한국어', htmlLang: 'ko', ogLocale: 'ko_KR', dir: 'ltr' },
  vi: { name: 'Tiếng Việt', htmlLang: 'vi', ogLocale: 'vi_VN', dir: 'ltr' },
  th: { name: 'ไทย', htmlLang: 'th', ogLocale: 'th_TH', dir: 'ltr' },
};

const PAGE_KEYS = [
  '/',
  '/oem',
  '/wholesale',
  '/products',
  '/quality',
  '/contact',
  '/about',
  '/faq',
  '/privacy',
  '/terms',
] as const;

export function isLocale(value: string | undefined): value is Locale {
  return Boolean(value && (LOCALES as readonly string[]).includes(value));
}

export function getLocaleFromPath(pathname: string): Locale {
  const first = pathname.split('/').filter(Boolean)[0];
  return isLocale(first) ? first : 'en';
}

export function stripLocale(pathname: string): string {
  const path = pathname.split('?')[0].split('#')[0].replace(/\/+$/, '') || '/';
  const parts = path.split('/').filter(Boolean);
  if (parts[0] && isLocale(parts[0])) {
    const rest = parts.slice(1).join('/');
    return rest ? `/${rest}` : '/';
  }
  return path;
}

export function localizePath(path: string, locale: Locale): string {
  const clean = stripLocale(path);
  if (locale === 'en') return clean;
  return clean === '/' ? `/${locale}` : `/${locale}${clean}`;
}

export function getHreflangMap(pathname: string): Record<Locale, string> | null {
  const key = stripLocale(pathname);
  const isStaticPage = (PAGE_KEYS as readonly string[]).includes(key);
  if (!isStaticPage) return null;
  return Object.fromEntries(LOCALES.map((locale) => [locale, localizePath(key, locale)])) as Record<
    Locale,
    string
  >;
}

export function switchLocalePath(pathname: string, target: Locale): string {
  const hash = pathname.includes('#') ? `#${pathname.split('#')[1]}` : '';
  const map = getHreflangMap(pathname);
  if (map) return map[target] + hash;
  if (target === 'en') return stripLocale(pathname) + hash;
  return localizePath('/', target) + hash;
}

export const WHATSAPP_BY_LOCALE: Record<Locale, string> = {
  en: 'Hello, I would like to inquire about private label creatine / wholesale creatine. Please send MOQ, sample options, and pricing. Thank you!',
  'zh-tw': '您好，想詢問肌酸私標／OEM 與批發。請提供 MOQ、樣品方案與報價，謝謝。',
  hi: 'नमस्ते, मैं प्राइवेट लेबल क्रिएटिन / होलसेल क्रिएटिन के बारे में पूछताछ करना चाहता/चाहती हूँ। कृपया MOQ, सैंपल विकल्प और मूल्य भेजें। धन्यवाद!',
  es: 'Hola, quiero consultar creatina marca privada / OEM y mayoreo. Por favor envíen MOQ, muestras y precios. Gracias.',
  ar: 'مرحباً، أود الاستفسار عن الكرياتين بالعلامة الخاصة / الجملة. يرجى إرسال الحد الأدنى للطلب والعينات والأسعار. شكراً.',
  fr: 'Bonjour, je souhaite un devis pour de la créatine marque blanche / OEM et gros. Merci d’envoyer MOQ, échantillons et tarifs.',
  bn: 'হ্যালো, আমি প্রাইভেট লেবেল ক্রিয়েটিন / হোলসেল ক্রিয়েটিন সম্পর্কে জানতে চাই। অনুগ্রহ করে MOQ, নমুনার অপশন এবং মূল্য পাঠান। ধন্যবাদ!',
  pt: 'Olá, quero consultar creatina private label / OEM e atacado. Por favor enviem MOQ, amostras e preços. Obrigado.',
  ru: 'Здравствуйте! Хочу запросить креатин private label / OEM и оптовые поставки. Пришлите MOQ, образцы и цены. Спасибо!',
  ur: 'السلام علیکم، میں پرائیویٹ لیبل کریٹائن / ہول سیل کریٹائن کے بارے میں پوچھنا چاہتا/چاہتی ہوں۔ براہ کرم MOQ، سیمپل آپشنز اور قیمت بھیجیں۔ شکریہ!',
  id: 'Halo, saya ingin menanyakan creatine private label / OEM dan grosir. Mohon kirim MOQ, opsi sampel, dan harga. Terima kasih.',
  de: 'Hallo, ich möchte Creatin Private Label / OEM und Großhandel anfragen. Bitte senden Sie MOQ, Musteroptionen und Preise. Danke!',
  ja: 'こんにちは。クレアチンのプライベートラベル／OEMおよび卸売について問い合わせたいです。MOQ・サンプル・価格をお送りください。',
  ko: '안녕하세요. 크레아틴 프라이빗 라벨/OEM 및 도매 문의드립니다. MOQ, 샘플, 가격을 보내주세요.',
  vi: 'Xin chào, tôi muốn hỏi báo giá creatine private label / OEM và bán sỉ. Vui lòng gửi MOQ, mẫu và bảng giá. Cảm ơn!',
  th: 'สวัสดีครับ/ค่ะ ต้องการสอบถามครีเอทีนไพรเวทเลเบล/OEM และขายส่ง กรุณาส่ง MOQ ตัวเลือกตัวอย่าง และราคา ขอบคุณครับ/ค่ะ',
};
