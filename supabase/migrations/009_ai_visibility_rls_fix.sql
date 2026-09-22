-- Fix: "new row violates row-level security policy" on AI Visibility save
-- Cause: RLS enabled on tables/storage without working INSERT policies for anon key.
-- Run in Supabase Dashboard → SQL Editor (safe to re-run).

-- ========== Table: ai_probe_queries ==========
alter table if exists public.ai_probe_queries enable row level security;

drop policy if exists "Allow public read on ai_probe_queries" on public.ai_probe_queries;
drop policy if exists "Allow public insert on ai_probe_queries" on public.ai_probe_queries;
drop policy if exists "Allow public update on ai_probe_queries" on public.ai_probe_queries;
drop policy if exists "Allow public delete on ai_probe_queries" on public.ai_probe_queries;

create policy "Allow public read on ai_probe_queries"
  on public.ai_probe_queries for select
  to anon, authenticated
  using (true);
create policy "Allow public insert on ai_probe_queries"
  on public.ai_probe_queries for insert
  to anon, authenticated
  with check (true);
create policy "Allow public update on ai_probe_queries"
  on public.ai_probe_queries for update
  to anon, authenticated
  using (true)
  with check (true);
create policy "Allow public delete on ai_probe_queries"
  on public.ai_probe_queries for delete
  to anon, authenticated
  using (true);

grant select, insert, update, delete on public.ai_probe_queries to anon, authenticated;

-- ========== Table: ai_visibility_checks ==========
alter table if exists public.ai_visibility_checks enable row level security;

drop policy if exists "Allow public read on ai_visibility_checks" on public.ai_visibility_checks;
drop policy if exists "Allow public insert on ai_visibility_checks" on public.ai_visibility_checks;
drop policy if exists "Allow public update on ai_visibility_checks" on public.ai_visibility_checks;
drop policy if exists "Allow public delete on ai_visibility_checks" on public.ai_visibility_checks;

create policy "Allow public read on ai_visibility_checks"
  on public.ai_visibility_checks for select
  to anon, authenticated
  using (true);
create policy "Allow public insert on ai_visibility_checks"
  on public.ai_visibility_checks for insert
  to anon, authenticated
  with check (true);
create policy "Allow public update on ai_visibility_checks"
  on public.ai_visibility_checks for update
  to anon, authenticated
  using (true)
  with check (true);
create policy "Allow public delete on ai_visibility_checks"
  on public.ai_visibility_checks for delete
  to anon, authenticated
  using (true);

grant select, insert, update, delete on public.ai_visibility_checks to anon, authenticated;

-- ========== Storage bucket: ai-visibility (screenshots) ==========
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'ai-visibility',
  'ai-visibility',
  true,
  5242880,
  array['image/jpeg', 'image/png', 'image/webp', 'image/gif']
)
on conflict (id) do update
set
  public = excluded.public,
  file_size_limit = excluded.file_size_limit,
  allowed_mime_types = excluded.allowed_mime_types;

drop policy if exists "ai_visibility_storage_select" on storage.objects;
drop policy if exists "ai_visibility_storage_insert" on storage.objects;
drop policy if exists "ai_visibility_storage_update" on storage.objects;
drop policy if exists "ai_visibility_storage_delete" on storage.objects;

create policy "ai_visibility_storage_select"
  on storage.objects for select
  to anon, authenticated
  using (bucket_id = 'ai-visibility');

create policy "ai_visibility_storage_insert"
  on storage.objects for insert
  to anon, authenticated
  with check (bucket_id = 'ai-visibility');

create policy "ai_visibility_storage_update"
  on storage.objects for update
  to anon, authenticated
  using (bucket_id = 'ai-visibility')
  with check (bucket_id = 'ai-visibility');

create policy "ai_visibility_storage_delete"
  on storage.objects for delete
  to anon, authenticated
  using (bucket_id = 'ai-visibility');
