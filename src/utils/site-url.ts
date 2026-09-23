import { SITE } from 'astrowind:config';

export function getSiteUrl(): string {
  return (SITE?.site ?? 'https://creatine.tradeglo.net').replace(/\/$/, '');
}
