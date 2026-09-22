export type DesignerCommentStatus = 'new' | 'reviewed' | 'replied' | 'archived' | 'spam';

export interface DesignerCommentRow {
  id: string;
  name: string;
  email: string;
  topic: string | null;
  message: string;
  source_page: string | null;
  source_site: string | null;
  user_agent: string | null;
  ip_address: string | null;
  country: string | null;
  country_code: string | null;
  region: string | null;
  status: DesignerCommentStatus;
  notes: string;
  extra: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}

export interface DesignerCommentInsert {
  name: string;
  email: string;
  topic?: string | null;
  message?: string;
  source_page?: string | null;
  source_site?: string | null;
  user_agent?: string | null;
  ip_address?: string | null;
  country?: string | null;
  country_code?: string | null;
  region?: string | null;
  status?: DesignerCommentStatus;
  notes?: string;
  extra?: Record<string, unknown>;
}

export interface DesignerCommentUpdate {
  status?: DesignerCommentStatus;
  notes?: string;
  name?: string;
  email?: string;
  topic?: string | null;
  message?: string;
}

export const DESIGNER_COMMENT_STATUSES: {
  value: DesignerCommentStatus;
  label: string;
  tone: string;
}[] = [
  { value: 'new', label: '新评论', tone: 'sky' },
  { value: 'reviewed', label: '已查看', tone: 'amber' },
  { value: 'replied', label: '已回复', tone: 'emerald' },
  { value: 'archived', label: '已归档', tone: 'slate' },
  { value: 'spam', label: '垃圾', tone: 'rose' },
];
