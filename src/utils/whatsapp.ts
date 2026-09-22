const WHATSAPP_PHONE = '8618302919628';

export const WHATSAPP_PHONES = [WHATSAPP_PHONE] as const;

export const DEFAULT_WHATSAPP_MESSAGE =
  'Hello, I would like to inquire about private label creatine / wholesale creatine. Please send MOQ, sample options, and pricing. Thank you!';

export function getWhatsAppPhoneNumber(_date: Date = new Date()): string {
  return WHATSAPP_PHONE;
}

export function getWhatsAppUrl(message: string = DEFAULT_WHATSAPP_MESSAGE, _date: Date = new Date()): string {
  return `https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(message)}`;
}
