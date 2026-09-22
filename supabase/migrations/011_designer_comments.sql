-- Designer page discussion comments (separate from B2B contact_inquiries)
-- Run in Supabase SQL Editor after 003_contact_inquiries.sql

create table if not exists public.designer_comments (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  email text not null,
  -- Topic select: Feature request / Bug / Export / UX / Other
  topic text,
  message text not null default '',
  source_page text,
  user_agent text,
  ip_address text,
  country text,
  country_code text,
  region text,
  status text not null default 'new'
    check (status in ('new', 'reviewed', 'replied', 'archived', 'spam')),
  notes text not null default '',
  extra jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_designer_comments_created_at
  on public.designer_comments (created_at desc);
create index if not exists idx_designer_comments_status
  on public.designer_comments (status);
create index if not exists idx_designer_comments_email
  on public.designer_comments (email);
create index if not exists idx_designer_comments_topic
  on public.designer_comments (topic);

create or replace function public.set_designer_comments_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists trg_designer_comments_updated_at on public.designer_comments;
create trigger trg_designer_comments_updated_at
  before update on public.designer_comments
  for each row execute function public.set_designer_comments_updated_at();

alter table public.designer_comments enable row level security;

drop policy if exists "Allow public read on designer_comments" on public.designer_comments;
drop policy if exists "Allow public insert on designer_comments" on public.designer_comments;
drop policy if exists "Allow public update on designer_comments" on public.designer_comments;
drop policy if exists "Allow public delete on designer_comments" on public.designer_comments;

-- Match contact_inquiries pattern (anon insert from site forms; tighten later if needed)
create policy "Allow public read on designer_comments"
  on public.designer_comments for select using (true);
create policy "Allow public insert on designer_comments"
  on public.designer_comments for insert with check (true);
create policy "Allow public update on designer_comments"
  on public.designer_comments for update using (true);
create policy "Allow public delete on designer_comments"
  on public.designer_comments for delete using (true);
