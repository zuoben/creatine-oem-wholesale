-- 客户来源（Google自然流量 / Google广告 / ChatGPT / Yahoo 等）
-- 在 Supabase SQL Editor 中执行

alter table public.contact_inquiries
  add column if not exists lead_source text;

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

create index if not exists idx_contact_inquiries_lead_source
  on public.contact_inquiries (lead_source);
