-- Google SEO 策略看板数据表
-- 在 Supabase SQL Editor 中执行此脚本

create table if not exists public.seo_strategy_items (
  id uuid primary key default gen_random_uuid(),
  category text not null check (category in (
    'target_market',
    'customer_persona',
    'keyword_primary',
    'keyword_longtail',
    'keyword_brand',
    'keyword_competitor',
    'technical_seo',
    'on_page_seo',
    'content_strategy',
    'link_building',
    'local_seo',
    'competitor_analysis',
    'custom'
  )),
  title text not null,
  description text,
  tags text[] default '{}',
  metadata jsonb default '{}',
  priority integer not null default 0,
  status text not null default 'active' check (status in ('active', 'planned', 'archived')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_seo_strategy_items_category on public.seo_strategy_items (category);
create index if not exists idx_seo_strategy_items_priority on public.seo_strategy_items (priority desc);
create index if not exists idx_seo_strategy_items_status on public.seo_strategy_items (status);

-- 自动更新 updated_at
create or replace function public.set_seo_strategy_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists trg_seo_strategy_updated_at on public.seo_strategy_items;
create trigger trg_seo_strategy_updated_at
  before update on public.seo_strategy_items
  for each row execute function public.set_seo_strategy_updated_at();

alter table public.seo_strategy_items enable row level security;

-- 内部工具：允许匿名读写（生产环境建议改为 authenticated 或 service role API）
create policy "Allow public read on seo_strategy_items"
  on public.seo_strategy_items for select
  using (true);

create policy "Allow public insert on seo_strategy_items"
  on public.seo_strategy_items for insert
  with check (true);

create policy "Allow public update on seo_strategy_items"
  on public.seo_strategy_items for update
  using (true);

create policy "Allow public delete on seo_strategy_items"
  on public.seo_strategy_items for delete
  using (true);

-- 可选：插入示例数据
insert into public.seo_strategy_items (category, title, description, tags, metadata, priority, status) values
  ('target_market', '北美 B2B', 'Menstrual cup OEM 主要出口市场', array['英语', 'FDA'], '{"region": "北美", "language": "English", "market_size": "高增长", "competition": "high", "entry_priority": "P0"}', 100, 'active'),
  ('customer_persona', 'DTC 品牌创始人', '寻求 OEM/ODM 快速上市的独立品牌', array['亚马逊', 'Shopify'], '{"role": "品牌创始人", "company_type": "DTC", "pain_points": "合规认证、MOQ、交期", "goals": "3个月内上架"}', 90, 'active'),
  ('keyword_primary', 'menstrual cup manufacturer', '核心商业词，指向制造商主页', null, '{"search_volume": "2400", "difficulty": 45, "intent": "commercial", "target_page": "/manufacturer"}', 100, 'active'),
  ('technical_seo', 'Core Web Vitals 优化', 'LCP、INP、CLS 达标', null, '{"checklist_item": "Core Web Vitals", "current_status": "in_progress", "tool": "PageSpeed Insights"}', 80, 'active'),
  ('on_page_seo', '制造商主页', 'Title/Meta/H1 优化', null, '{"page_url": "/manufacturer", "title_tag": "Medical Grade Menstrual Cup Manufacturer | OEM/ODM", "h1": "Menstrual Cup Manufacturer"}', 90, 'active');