-- 跟进人：Viggie / Annie
-- 在 Supabase SQL Editor 中执行（已有 contact_inquiries 表时）

alter table public.contact_inquiries
  add column if not exists assignee text;

-- 允许 NULL（未分配）或 Viggie / Annie
alter table public.contact_inquiries
  drop constraint if exists contact_inquiries_assignee_check;

alter table public.contact_inquiries
  add constraint contact_inquiries_assignee_check
  check (assignee is null or assignee in ('Viggie', 'Annie'));

create index if not exists idx_contact_inquiries_assignee
  on public.contact_inquiries (assignee);
