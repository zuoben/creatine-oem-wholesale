-- 网站运营数据日报
-- 在 Supabase SQL Editor 中执行

create table if not exists public.analytics_daily_records (
  id uuid primary key default gen_random_uuid(),
  date date not null unique,
  page_views integer not null default 0,
  users integer not null default 0,
  whatsapp_clicks integer not null default 0,
  whatsapp_inquiries integer not null default 0,
  form_submissions integer not null default 0,
  phone_clicks integer not null default 0,
  email_clicks integer not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_analytics_daily_date on public.analytics_daily_records (date desc);

create or replace function public.set_analytics_daily_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists trg_analytics_daily_updated_at on public.analytics_daily_records;
create trigger trg_analytics_daily_updated_at
  before update on public.analytics_daily_records
  for each row execute function public.set_analytics_daily_updated_at();

alter table public.analytics_daily_records enable row level security;

drop policy if exists "Allow public read on analytics_daily_records" on public.analytics_daily_records;
drop policy if exists "Allow public insert on analytics_daily_records" on public.analytics_daily_records;
drop policy if exists "Allow public update on analytics_daily_records" on public.analytics_daily_records;
drop policy if exists "Allow public delete on analytics_daily_records" on public.analytics_daily_records;

create policy "Allow public read on analytics_daily_records"
  on public.analytics_daily_records for select using (true);
create policy "Allow public insert on analytics_daily_records"
  on public.analytics_daily_records for insert with check (true);
create policy "Allow public update on analytics_daily_records"
  on public.analytics_daily_records for update using (true);
create policy "Allow public delete on analytics_daily_records"
  on public.analytics_daily_records for delete using (true);

insert into public.analytics_daily_records (
  date, page_views, users, whatsapp_clicks, whatsapp_inquiries,
  form_submissions, phone_clicks, email_clicks
)
values
  ('2026-06-30', 0, 381, 27, 0, 0, 0, 0),
  ('2026-06-29', 0, 514, 35, 0, 2, 1, 0),
  ('2026-06-28', 1264, 114, 6, 0, 1, 0, 0),
  ('2026-06-27', 1383, 104, 8, 0, 6, 1, 0),
  ('2026-06-26', 1308, 132, 4, 0, 1, 0, 0),
  ('2026-06-25', 1264, 104, 2, 0, 0, 0, 1),
  ('2026-06-24', 1293, 98, 4, 0, 0, 0, 0),
  ('2026-06-23', 1423, 117, 0, 0, 1, 0, 0),
  ('2026-06-22', 1487, 114, 1, 0, 2, 1, 0),
  ('2026-06-21', 1326, 78, 0, 0, 0, 0, 0),
  ('2026-06-20', 1191, 73, 0, 0, 0, 0, 0),
  ('2026-06-19', 1225, 108, 0, 0, 0, 0, 0),
  ('2026-06-18', 1280, 116, 1, 0, 0, 1, 0),
  ('2026-06-17', 1380, 99, 0, 0, 0, 0, 1),
  ('2026-06-16', 2977, 97, 0, 0, 1, 0, 0),
  ('2026-06-15', 1395, 106, 2, 0, 3, 0, 0),
  ('2026-06-14', 1326, 73, 0, 0, 1, 0, 1),
  ('2026-06-13', 1337, 84, 0, 0, 2, 0, 0),
  ('2026-06-12', 1304, 106, 1, 0, 2, 1, 1),
  ('2026-06-11', 1449, 98, 1, 0, 1, 0, 1),
  ('2026-06-10', 1469, 99, 1, 0, 0, 0, 0),
  ('2026-06-09', 1547, 94, 0, 0, 3, 0, 0),
  ('2026-06-08', 1591, 83, 0, 0, 0, 0, 0),
  ('2026-06-07', 1561, 56, 0, 0, 2, 0, 0),
  ('2026-06-06', 1531, 50, 0, 0, 1, 0, 0),
  ('2026-06-05', 1565, 100, 0, 0, 6, 0, 0),
  ('2026-06-04', 1701, 96, 0, 0, 1, 0, 0),
  ('2026-06-03', 1497, 91, 0, 0, 0, 0, 0),
  ('2026-06-02', 1432, 86, 0, 0, 1, 0, 0),
  ('2026-06-01', 1585, 75, 0, 0, 1, 0, 0),
  ('2026-05-31', 49435, 532, 0, 0, 13, 0, 0),
  ('2026-04-30', 39761, 0, 0, 0, 14, 0, 0),
  ('2026-03-31', 36011, 0, 0, 0, 19, 0, 0),
  ('2026-02-28', 32165, 0, 0, 0, 16, 0, 0),
  ('2026-01-31', 35635, 0, 0, 0, 6, 0, 0)
on conflict (date) do nothing;
