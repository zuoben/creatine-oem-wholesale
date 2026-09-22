-- Staff-only CRM access for common-services-db
-- Canonical copy also lives in ../common-services-admin/supabase/migrations/013_staff_rls.sql
-- Run in Supabase SQL Editor AFTER creating login users in Authentication → Users
-- (auto-confirm email). Then insert those emails into staff_users below.
--
-- Effect:
--   website forms (anon)  → INSERT only
--   logged-in staff       → SELECT / UPDATE / DELETE
--   old /internal pages   → stop loading lists (anon SELECT is removed)

create table if not exists public.staff_users (
  email text primary key,
  role text not null default 'staff'
    check (role in ('staff', 'admin')),
  display_name text,
  created_at timestamptz not null default now()
);

create or replace function public.is_staff()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1
    from public.staff_users
    where lower(email) = lower(coalesce(auth.jwt() ->> 'email', ''))
  );
$$;

revoke all on function public.is_staff() from public;
grant execute on function public.is_staff() to authenticated;
grant select on table public.staff_users to authenticated;

alter table public.staff_users enable row level security;

drop policy if exists "staff can read staff_users" on public.staff_users;
create policy "staff can read staff_users"
  on public.staff_users
  for select
  to authenticated
  using (public.is_staff());

-- contact_inquiries: drop open read/update/delete; keep public insert for OEM forms
drop policy if exists "Allow public read on contact_inquiries" on public.contact_inquiries;
drop policy if exists "Allow public update on contact_inquiries" on public.contact_inquiries;
drop policy if exists "Allow public delete on contact_inquiries" on public.contact_inquiries;

drop policy if exists "staff read contact_inquiries" on public.contact_inquiries;
drop policy if exists "staff update contact_inquiries" on public.contact_inquiries;
drop policy if exists "staff delete contact_inquiries" on public.contact_inquiries;

create policy "staff read contact_inquiries"
  on public.contact_inquiries for select to authenticated
  using (public.is_staff());

create policy "staff update contact_inquiries"
  on public.contact_inquiries for update to authenticated
  using (public.is_staff())
  with check (public.is_staff());

create policy "staff delete contact_inquiries"
  on public.contact_inquiries for delete to authenticated
  using (public.is_staff());

-- designer_comments: same lock
drop policy if exists "Allow public read on designer_comments" on public.designer_comments;
drop policy if exists "Allow public update on designer_comments" on public.designer_comments;
drop policy if exists "Allow public delete on designer_comments" on public.designer_comments;

drop policy if exists "staff read designer_comments" on public.designer_comments;
drop policy if exists "staff update designer_comments" on public.designer_comments;
drop policy if exists "staff delete designer_comments" on public.designer_comments;

create policy "staff read designer_comments"
  on public.designer_comments for select to authenticated
  using (public.is_staff());

create policy "staff update designer_comments"
  on public.designer_comments for update to authenticated
  using (public.is_staff())
  with check (public.is_staff());

create policy "staff delete designer_comments"
  on public.designer_comments for delete to authenticated
  using (public.is_staff());

-- Public designer page still needs to show non-spam comments.
drop policy if exists "anon read published designer_comments" on public.designer_comments;
create policy "anon read published designer_comments"
  on public.designer_comments
  for select
  to anon
  using (status in ('new', 'reviewed', 'replied'));
