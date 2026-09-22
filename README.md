# Crest Creatine — OEM + Wholesale (Astro)

B2B static site for **private label / OEM creatine** and **wholesale creatine** (powder & gummies). Built with Astro (static output) for Cloudflare Pages.

Provisional brand: **Crest Creatine**  
Provisional URL: `https://creatine-oem-wholesale.pages.dev`

## Pages

| Path | Purpose |
|------|---------|
| `/` | Dual funnel home (OEM + Wholesale CTAs) |
| `/oem` | Private label / OEM capabilities |
| `/wholesale` | Wholesale cartons / price list CTA |
| `/quality` | Quality + DSHEA-style disclaimer |
| `/contact` | Shared B2B inquiry form |
| `/privacy`, `/terms` | Legal |

## Develop

```bash
npm install
npm run dev
```

Node **20.19+** recommended. If Astro 6 requires Node 22 on your machine, use Node 22 via `nvm`/`fnm`.

## Build

```bash
npm run build
```

Output: `dist/`

## Cloudflare Pages

1. Connect repo `zuoben/creatine-oem-wholesale`
2. Build command: `npm run build`
3. Output directory: `dist`
4. Framework preset: Astro (or None)
5. Optional env (form): `PUBLIC_SUPABASE_URL`, `PUBLIC_SUPABASE_ANON_KEY`, `PUBLIC_TURNSTILE_SITE_KEY` — form no-ops gracefully if unset (same pattern as mahjong site)

Custom domain can replace the `*.pages.dev` URL in `src/config.yaml` later.

## SEO seeds (on-page)

private label creatine · wholesale creatine · creatine manufacturer · private label creatine gummies · bulk creatine wholesale
