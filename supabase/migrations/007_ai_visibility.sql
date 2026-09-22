-- AI 可见度看板：探针问题 + 人工录入检查结果
-- 在 Supabase SQL Editor 中执行

-- 探针问题库
create table if not exists public.ai_probe_queries (
  id uuid primary key default gen_random_uuid(),
  query text not null,
  intent text,
  priority integer not null default 0,
  target_url text,
  active boolean not null default true,
  notes text not null default '',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create unique index if not exists idx_ai_probe_queries_query_unique
  on public.ai_probe_queries (lower(query));
create index if not exists idx_ai_probe_queries_priority
  on public.ai_probe_queries (priority desc);
create index if not exists idx_ai_probe_queries_active
  on public.ai_probe_queries (active);

-- 检查结果（人工在 AI 引擎提问后录入）
create table if not exists public.ai_visibility_checks (
  id uuid primary key default gen_random_uuid(),
  probe_id uuid references public.ai_probe_queries (id) on delete set null,
  query text not null,
  engine text not null
    check (engine in (
      'chatgpt',
      'gemini',
      'google_aio',
      'bing_copilot',
      'other'
    )),
  checked_at date not null default (timezone('Asia/Shanghai', now()))::date,
  brand_mentioned boolean not null default false,
  domain_cited boolean not null default false,
  position_hint text not null default 'none'
    check (position_hint in ('none', 'footnote', 'mid', 'top')),
  competitors text not null default '',
  snippet text not null default '',
  notes text not null default '',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_ai_visibility_checks_checked_at
  on public.ai_visibility_checks (checked_at desc);
create index if not exists idx_ai_visibility_checks_engine
  on public.ai_visibility_checks (engine);
create index if not exists idx_ai_visibility_checks_query
  on public.ai_visibility_checks (query);

create or replace function public.set_ai_probe_queries_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

create or replace function public.set_ai_visibility_checks_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists trg_ai_probe_queries_updated_at on public.ai_probe_queries;
create trigger trg_ai_probe_queries_updated_at
  before update on public.ai_probe_queries
  for each row execute function public.set_ai_probe_queries_updated_at();

drop trigger if exists trg_ai_visibility_checks_updated_at on public.ai_visibility_checks;
create trigger trg_ai_visibility_checks_updated_at
  before update on public.ai_visibility_checks
  for each row execute function public.set_ai_visibility_checks_updated_at();

alter table public.ai_probe_queries enable row level security;
alter table public.ai_visibility_checks enable row level security;

drop policy if exists "Allow public read on ai_probe_queries" on public.ai_probe_queries;
drop policy if exists "Allow public insert on ai_probe_queries" on public.ai_probe_queries;
drop policy if exists "Allow public update on ai_probe_queries" on public.ai_probe_queries;
drop policy if exists "Allow public delete on ai_probe_queries" on public.ai_probe_queries;

create policy "Allow public read on ai_probe_queries"
  on public.ai_probe_queries for select using (true);
create policy "Allow public insert on ai_probe_queries"
  on public.ai_probe_queries for insert with check (true);
create policy "Allow public update on ai_probe_queries"
  on public.ai_probe_queries for update using (true);
create policy "Allow public delete on ai_probe_queries"
  on public.ai_probe_queries for delete using (true);

drop policy if exists "Allow public read on ai_visibility_checks" on public.ai_visibility_checks;
drop policy if exists "Allow public insert on ai_visibility_checks" on public.ai_visibility_checks;
drop policy if exists "Allow public update on ai_visibility_checks" on public.ai_visibility_checks;
drop policy if exists "Allow public delete on ai_visibility_checks" on public.ai_visibility_checks;

create policy "Allow public read on ai_visibility_checks"
  on public.ai_visibility_checks for select using (true);
create policy "Allow public insert on ai_visibility_checks"
  on public.ai_visibility_checks for insert with check (true);
create policy "Allow public update on ai_visibility_checks"
  on public.ai_visibility_checks for update using (true);
create policy "Allow public delete on ai_visibility_checks"
  on public.ai_visibility_checks for delete using (true);

-- 默认探针（可在看板中继续添加；已存在同文问题则跳过）
insert into public.ai_probe_queries (query, intent, priority, target_url)
select v.query, v.intent, v.priority, v.target_url
from (
  values
    ('menstrual cup manufacturer China OEM MOQ', 'commercial', 100, '/manufacturer'),
    ('ISO 13485 menstrual cup private label factory', 'commercial', 95, '/manufacturer/private-label'),
    ('wholesale menstrual disc supplier FDA CE', 'commercial', 90, '/menstrual/menstrual-discs'),
    ('best menstrual cup OEM factory for Amazon sellers', 'commercial', 90, '/manufacturer/wholesale'),
    ('medical grade silicone menstrual cup manufacturer MOQ 500', 'transactional', 85, '/menstrual/menstrual-cups'),
    ('Furuize menstrual cup factory', 'navigational', 80, '/'),
    ('menstrual cup private label cost breakdown OEM', 'commercial', 75, '/private-label-menstrual-cup-cost-breakdown'),
    ('how to choose menstrual cup supplier China', 'informational', 70, '/how-to-choose-menstrual-cup-supplier'),
    ('menstrual cup factory tour China OEM audit', 'commercial', 65, '/manufacturing/factory-tour'),
    ('CE FDA ISO 13485 menstrual cup manufacturer documentation', 'commercial', 85, '/certifications')
) as v(query, intent, priority, target_url)
where not exists (
  select 1 from public.ai_probe_queries p where lower(p.query) = lower(v.query)
);
