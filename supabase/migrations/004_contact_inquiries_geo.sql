-- 为已有 contact_inquiries 表补充 IP 地理位置字段
-- 若已完整执行过带 geo 字段的 003，本脚本可安全重复执行

alter table public.contact_inquiries
  add column if not exists ip_address text,
  add column if not exists country text,
  add column if not exists country_code text,
  add column if not exists region text;

create index if not exists idx_contact_inquiries_country
  on public.contact_inquiries (country);
