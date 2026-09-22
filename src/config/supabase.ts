/**
 * Shared inquiry database for all factory sites.
 *
 * Supabase dashboard project name: common-services-db
 * (ref xwxnxlxulkqpevlafovu — URL/keys do not change if the display name is renamed)
 *
 * All OEM sites insert into the same `contact_inquiries` table and tag
 * `source_site` with their brand hostname (see Form.astro data-source-site).
 *
 * URL 使用项目根地址，不要带 /rest/v1/
 * anon / publishable key 会暴露在浏览器端，数据安全依赖 RLS。
 */
export const SUPABASE_CONFIG = {
  url: 'https://xwxnxlxulkqpevlafovu.supabase.co',
  anonKey: 'sb_publishable_ofrpwjH4WCUYlHRG93pMEw_f7DQggrp',
} as const;

export function getFileSupabaseConfig() {
  const { url, anonKey } = SUPABASE_CONFIG;
  if (!url || !anonKey || url.includes('your-project')) return null;
  return { url, anonKey };
}