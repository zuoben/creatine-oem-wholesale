import type { Disclaimer, Input, Textarea } from '~/types';

/** Structured quote fields — shared by /contact and WhatsApp lead gate. */

export const inquiryFormInputs: Input[] = [
  {
    type: 'select',
    name: 'company',
    label: 'I am a',
    placeholder: 'Select…',
    required: true,
    options: [
      { value: 'Brand', label: 'Brand' },
      { value: 'Distributor', label: 'Distributor' },
      { value: 'Gym or retailer', label: 'Gym or retailer' },
      { value: 'Online seller', label: 'Online seller' },
      { value: 'Other', label: 'Other' },
    ],
  },
  {
    type: 'select',
    name: 'channel',
    label: "I'm looking for",
    placeholder: 'Select…',
    required: true,
    options: [
      { value: 'OEM/Private label', label: 'OEM / Private label' },
      { value: 'Wholesale pricing', label: 'Wholesale pricing' },
      { value: 'Sample', label: 'Sample' },
      { value: 'Bulk powder', label: 'Bulk powder' },
      { value: 'Bulk gummies', label: 'Bulk gummies' },
    ],
  },
  {
    type: 'select',
    name: 'volume',
    label: 'Expected volume',
    placeholder: 'Select…',
    required: true,
    options: [
      { value: 'Sample', label: 'Sample' },
      { value: 'Trial MOQ', label: 'Trial MOQ' },
      { value: 'Container/pallet', label: 'Container / pallet' },
      { value: 'Ongoing monthly', label: 'Ongoing monthly' },
    ],
  },
  { type: 'text', name: 'name', label: 'Name', placeholder: 'Your name' },
  { type: 'email', name: 'email', label: 'Email', placeholder: 'you@company.com' },
];

export const inquiryFormTextarea: Textarea = {
  label: 'Message',
  name: 'message',
  placeholder: 'SKU interest (powder / gummies), flavor, packaging, ship-to country, timeline, certifications needed…',
  rows: 3,
};

export const inquiryFormDisclaimer: Disclaimer = {
  label: 'I agree to be contacted by Crest Creatine regarding OEM, private label, and wholesale inquiries.',
};

export const inquiryFormButton = 'Get B2B Quote Now';

export const inquiryFormDescription =
  'Tell us your buyer type and volume — we reply with MOQ tiers, sample options, and next steps within 24 hours on working days.';

export const inquiryWhatsAppLead = {
  inputs: inquiryFormInputs,
  textarea: { ...inquiryFormTextarea, rows: 2 },
  disclaimer: {
    label: 'You agree we may contact you about this OEM / wholesale inquiry via email or WhatsApp.',
  },
  button: 'Continue to WhatsApp',
  description: 'We save your quote request, then open WhatsApp.',
  title: 'Chat on WhatsApp',
  subtitle: 'Quick details first — factory quote follows in chat.',
};
