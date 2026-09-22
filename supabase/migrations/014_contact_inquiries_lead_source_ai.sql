-- Generic AI / llms.txt citation source (not ChatGPT-specific)
-- Run in the shared common-services-db SQL Editor

alter table public.contact_inquiries
  drop constraint if exists contact_inquiries_lead_source_check;

alter table public.contact_inquiries
  add constraint contact_inquiries_lead_source_check
  check (
    lead_source is null
    or lead_source in (
      'google_organic',
      'google_ads',
      'chatgpt',
      'ai',
      'yahoo',
      'bing',
      'baidu',
      'alibaba',
      'facebook',
      'linkedin',
      'whatsapp',
      'email',
      'direct',
      'other'
    )
  );
