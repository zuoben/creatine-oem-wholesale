-- Shared multi-site inquiries: tag every row with the originating website.
-- Run in the common-services-db project SQL Editor
-- (https://xwxnxlxulkqpevlafovu.supabase.co).
--
-- source_site = brand hostname, no www (e.g. mahjonggsupplies.com).
-- source_page remains the actual URL (including ads.ersashopline.com landings).

alter table public.contact_inquiries
  add column if not exists source_site text;

create index if not exists idx_contact_inquiries_source_site
  on public.contact_inquiries (source_site);

alter table public.designer_comments
  add column if not exists source_site text;

create index if not exists idx_designer_comments_source_site
  on public.designer_comments (source_site);

-- Normalize www. and empty strings. Does not remap ad hosts — forms send the brand host.
create or replace function public.normalize_source_site(raw text)
returns text
language sql
immutable
as $$
  select case
    when raw is null or btrim(raw) = '' then null
    when raw ~* '^https?://' then
      nullif(
        lower(regexp_replace(
          split_part(regexp_replace(btrim(raw), '^https?://', ''), '/', 1),
          '^www\.',
          ''
        )),
        ''
      )
    else
      nullif(lower(regexp_replace(btrim(raw), '^www\.', '')), '')
  end
$$;

create or replace function public.set_contact_inquiries_source_site()
returns trigger
language plpgsql
as $$
begin
  new.source_site := coalesce(
    public.normalize_source_site(new.source_site),
    public.normalize_source_site(new.source_page)
  );
  return new;
end;
$$;

drop trigger if exists trg_contact_inquiries_source_site on public.contact_inquiries;
create trigger trg_contact_inquiries_source_site
  before insert or update on public.contact_inquiries
  for each row execute function public.set_contact_inquiries_source_site();

create or replace function public.set_designer_comments_source_site()
returns trigger
language plpgsql
as $$
begin
  new.source_site := coalesce(
    public.normalize_source_site(new.source_site),
    public.normalize_source_site(new.source_page)
  );
  return new;
end;
$$;

drop trigger if exists trg_designer_comments_source_site on public.designer_comments;
create trigger trg_designer_comments_source_site
  before insert or update on public.designer_comments
  for each row execute function public.set_designer_comments_source_site();

-- Backfill this project's historical mahjong rows (ad domain + local previews).
update public.contact_inquiries
set source_site = case
  when source_page ~* 'mahjonggsupplies\.com' then 'mahjonggsupplies.com'
  when source_page ~* 'ads\.ersashopline\.com' then 'mahjonggsupplies.com'
  when source_page ~* '(localhost|127\.0\.0\.1)' then 'mahjonggsupplies.com'
  else public.normalize_source_site(source_page)
end
where source_site is null;

update public.designer_comments
set source_site = case
  when source_page ~* 'mahjonggsupplies\.com' then 'mahjonggsupplies.com'
  when source_page ~* 'ads\.ersashopline\.com' then 'mahjonggsupplies.com'
  when source_page ~* '(localhost|127\.0\.0\.1)' then 'mahjonggsupplies.com'
  else public.normalize_source_site(source_page)
end
where source_site is null;
