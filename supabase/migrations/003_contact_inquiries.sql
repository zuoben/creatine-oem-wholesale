-- 询盘 / 客户线索表
-- 在 Supabase SQL Editor 中执行此脚本

create table if not exists public.contact_inquiries (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  email text not null,
  message text not null default '',
  company text,
  channel text,
  product_interest text,
  source_page text,
  user_agent text,
  ip_address text,
  country text,
  country_code text,
  region text,
  status text not null default 'new'
    check (status in ('new', 'contacted', 'qualified', 'closed', 'spam')),
  assignee text
    check (assignee is null or assignee in ('Viggie', 'Annie')),
  lead_source text
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
    ),
  notes text not null default '',
  extra jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_contact_inquiries_created_at
  on public.contact_inquiries (created_at desc);
create index if not exists idx_contact_inquiries_status
  on public.contact_inquiries (status);
create index if not exists idx_contact_inquiries_email
  on public.contact_inquiries (email);
create index if not exists idx_contact_inquiries_assignee
  on public.contact_inquiries (assignee);
create index if not exists idx_contact_inquiries_lead_source
  on public.contact_inquiries (lead_source);

create or replace function public.set_contact_inquiries_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists trg_contact_inquiries_updated_at on public.contact_inquiries;
create trigger trg_contact_inquiries_updated_at
  before update on public.contact_inquiries
  for each row execute function public.set_contact_inquiries_updated_at();

alter table public.contact_inquiries enable row level security;

drop policy if exists "Allow public read on contact_inquiries" on public.contact_inquiries;
drop policy if exists "Allow public insert on contact_inquiries" on public.contact_inquiries;
drop policy if exists "Allow public update on contact_inquiries" on public.contact_inquiries;
drop policy if exists "Allow public delete on contact_inquiries" on public.contact_inquiries;

-- 与现有内部看板一致：anon key + RLS 开放读写（路径 noindex，依赖内部链接）
create policy "Allow public read on contact_inquiries"
  on public.contact_inquiries for select using (true);
create policy "Allow public insert on contact_inquiries"
  on public.contact_inquiries for insert with check (true);
create policy "Allow public update on contact_inquiries"
  on public.contact_inquiries for update using (true);
create policy "Allow public delete on contact_inquiries"
  on public.contact_inquiries for delete using (true);
