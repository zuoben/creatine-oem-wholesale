-- Remove Perplexity from AI Visibility engines
-- Run in Supabase SQL Editor if 007 already applied with perplexity allowed.

-- Map historical rows so check constraint can drop 'perplexity'
update public.ai_visibility_checks
set engine = 'other'
where engine = 'perplexity';

alter table public.ai_visibility_checks
  drop constraint if exists ai_visibility_checks_engine_check;

alter table public.ai_visibility_checks
  add constraint ai_visibility_checks_engine_check
  check (engine in (
    'chatgpt',
    'gemini',
    'google_aio',
    'bing_copilot',
    'other'
  ));
