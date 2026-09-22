-- AI 可见度：检查记录截图（1 张）
-- 在 Supabase SQL Editor 中执行本文件

-- 1) 表字段：公开桶内对象路径，如 2026/03/uuid.webp
alter table public.ai_visibility_checks
  add column if not exists screenshot_path text;

comment on column public.ai_visibility_checks.screenshot_path is
  'Supabase Storage 路径（bucket: ai-visibility），公开读；删除检查记录时应同步删对象';

-- 2) 公开桶
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'ai-visibility',
  'ai-visibility',
  true,
  5242880, -- 5MB（压缩后仍应远小于此）
  array['image/jpeg', 'image/png', 'image/webp', 'image/gif']
)
on conflict (id) do update
set
  public = excluded.public,
  file_size_limit = excluded.file_size_limit,
  allowed_mime_types = excluded.allowed_mime_types;

-- 3) Storage 策略（与现有 internal 表一致：anon 可读写；仅 internal 使用）
drop policy if exists "ai_visibility_storage_select" on storage.objects;
drop policy if exists "ai_visibility_storage_insert" on storage.objects;
drop policy if exists "ai_visibility_storage_update" on storage.objects;
drop policy if exists "ai_visibility_storage_delete" on storage.objects;

create policy "ai_visibility_storage_select"
  on storage.objects for select
  using (bucket_id = 'ai-visibility');

create policy "ai_visibility_storage_insert"
  on storage.objects for insert
  with check (bucket_id = 'ai-visibility');

create policy "ai_visibility_storage_update"
  on storage.objects for update
  using (bucket_id = 'ai-visibility')
  with check (bucket_id = 'ai-visibility');

create policy "ai_visibility_storage_delete"
  on storage.objects for delete
  using (bucket_id = 'ai-visibility');
