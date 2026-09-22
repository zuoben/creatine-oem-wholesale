
import type { Locale } from './locales';

export function getContactCopy(_locale: Locale = 'en') {
  return {
    formTitle: 'B2B inquiry',
    formSub: 'Tell us what you need — OEM or wholesale.',
    wa: 'WhatsApp',
  };
}
