import type { Disclaimer, Input, Textarea } from '~/types';
import type { Locale } from './locales';
import {
  inquiryFormButton,
  inquiryFormDescription,
  inquiryFormDisclaimer,
  inquiryFormInputs,
  inquiryFormTextarea,
  inquiryWhatsAppLead,
} from '~/data/inquiry-form';

export function getInquiryForm(_locale: Locale = 'en') {
  const inputs: Input[] = inquiryFormInputs;
  const textarea: Textarea = inquiryFormTextarea;
  const disclaimer: Disclaimer = inquiryFormDisclaimer;
  return {
    inputs,
    textarea,
    disclaimer,
    button: inquiryFormButton,
    description: inquiryFormDescription,
    close: 'Close',
    preferChat: 'Prefer chat?',
    waLead: { ...inquiryWhatsAppLead },
  };
}
