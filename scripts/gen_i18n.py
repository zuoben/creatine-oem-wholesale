#!/usr/bin/env python3
"""Generate creatine i18n TS modules for 16 locales."""
from __future__ import annotations
import json
from pathlib import Path

OUT = Path("/workspace/creatine-oem-wholesale/src/i18n")
LOCALES = ["en","zh-tw","hi","es","ar","fr","bn","pt","ru","ur","id","de","ja","ko","vi","th"]

def ser(val, indent=0):
    pad = " " * indent
    pad2 = " " * (indent + 2)
    if isinstance(val, str):
        return json.dumps(val, ensure_ascii=False)
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, list):
        if not val:
            return "[]"
        return "[\n" + ",\n".join(f"{pad2}{ser(v, indent+2)}" for v in val) + f",\n{pad}]"
    if isinstance(val, dict):
        parts = []
        for k, v in val.items():
            key = k if k.isidentifier() and "-" not in k else json.dumps(k)
            parts.append(f"{pad2}{key}: {ser(v, indent+2)},")
        return "{\n" + "\n".join(parts) + f"\n{pad}}}"
    return "null"

def locale_key(loc: str) -> str:
    return f"'{loc}'" if "-" in loc else loc

def write_record(varname: str, typename: str, data: dict) -> str:
    for loc in LOCALES:
        assert loc in data, f"missing {loc} in {varname}"
    lines = [f"const {varname}: Record<Locale, {typename}> = {{"]
    for loc in LOCALES:
        lines.append(f"  {locale_key(loc)}: {ser(data[loc], 2)},")
    lines.append("};")
    return "\n".join(lines)

def L(row: dict) -> dict:
    """Expand a locale->string map; require all locales."""
    for loc in LOCALES:
        if loc not in row:
            raise KeyError(f"missing {loc}: {row.get('en','?')[:40]}")
    return row

# ═══════════════════════ NAV ═══════════════════════
NAV_KEYS = {
  "home": L({"en":"Home","zh-tw":"首頁","hi":"होम","es":"Inicio","ar":"الرئيسية","fr":"Accueil","bn":"হোম","pt":"Início","ru":"Главная","ur":"ہوم","id":"Beranda","de":"Start","ja":"ホーム","ko":"홈","vi":"Trang chủ","th":"หน้าแรก"}),
  "products": L({"en":"Products","zh-tw":"產品","hi":"उत्पाद","es":"Productos","ar":"المنتجات","fr":"Produits","bn":"পণ্য","pt":"Produtos","ru":"Продукты","ur":"مصنوعات","id":"Produk","de":"Produkte","ja":"製品","ko":"제품","vi":"Sản phẩm","th":"ผลิตภัณฑ์"}),
  "oem": L({"en":"OEM","zh-tw":"OEM","hi":"OEM","es":"OEM","ar":"OEM","fr":"OEM","bn":"OEM","pt":"OEM","ru":"OEM","ur":"OEM","id":"OEM","de":"OEM","ja":"OEM","ko":"OEM","vi":"OEM","th":"OEM"}),
  "wholesale": L({"en":"Wholesale","zh-tw":"批發","hi":"थोक","es":"Mayoreo","ar":"الجملة","fr":"Gros","bn":"হোলসেল","pt":"Atacado","ru":"Опт","ur":"ہول سیل","id":"Grosir","de":"Großhandel","ja":"卸売","ko":"도매","vi":"Bán sỉ","th":"ขายส่ง"}),
  "quality": L({"en":"Quality","zh-tw":"品質","hi":"गुणवत्ता","es":"Calidad","ar":"الجودة","fr":"Qualité","bn":"গুণমান","pt":"Qualidade","ru":"Качество","ur":"کوالٹی","id":"Kualitas","de":"Qualität","ja":"品質","ko":"품질","vi":"Chất lượng","th":"คุณภาพ"}),
  "contact": L({"en":"Contact","zh-tw":"聯絡","hi":"संपर्क","es":"Contacto","ar":"اتصل بنا","fr":"Contact","bn":"যোগাযোগ","pt":"Contato","ru":"Контакты","ur":"رابطہ","id":"Kontak","de":"Kontakt","ja":"お問い合わせ","ko":"문의","vi":"Liên hệ","th":"ติดต่อ"}),
  "quote": L({"en":"Request Quote","zh-tw":"索取報價","hi":"कोट अनुरोध","es":"Solicitar cotización","ar":"طلب عرض سعر","fr":"Demander un devis","bn":"কোট অনুরোধ","pt":"Solicitar orçamento","ru":"Запросить КП","ur":"کوٹ کی درخواست","id":"Minta penawaran","de":"Angebot anfordern","ja":"見積依頼","ko":"견적 요청","vi":"Yêu cầu báo giá","th":"ขอใบเสนอราคา"}),
  "company": L({"en":"Company","zh-tw":"公司","hi":"कंपनी","es":"Empresa","ar":"الشركة","fr":"Entreprise","bn":"কোম্পানি","pt":"Empresa","ru":"Компания","ur":"کمپنی","id":"Perusahaan","de":"Unternehmen","ja":"会社","ko":"회사","vi":"Công ty","th":"บริษัท"}),
  "qualityCompliance": L({"en":"Quality & Compliance","zh-tw":"品質與合規","hi":"गुणवत्ता और अनुपालन","es":"Calidad y cumplimiento","ar":"الجودة والامتثال","fr":"Qualité et conformité","bn":"গুণমান ও সম্মতি","pt":"Qualidade e conformidade","ru":"Качество и соответствие","ur":"کوالٹی اور کمپلائنس","id":"Kualitas & kepatuhan","de":"Qualität & Compliance","ja":"品質・コンプライアンス","ko":"품질 및 컴플라이언스","vi":"Chất lượng & tuân thủ","th":"คุณภาพและการปฏิบัติตาม"}),
  "programs": L({"en":"Programs","zh-tw":"方案","hi":"प्रोग्राम","es":"Programas","ar":"البرامج","fr":"Programmes","bn":"প্রোগ্রাম","pt":"Programas","ru":"Программы","ur":"پروگرامز","id":"Program","de":"Programme","ja":"プログラム","ko":"프로그램","vi":"Chương trình","th":"โปรแกรม"}),
  "allProducts": L({"en":"All products","zh-tw":"全部產品","hi":"सभी उत्पाद","es":"Todos los productos","ar":"جميع المنتجات","fr":"Tous les produits","bn":"সব পণ্য","pt":"Todos os produtos","ru":"Все продукты","ur":"تمام مصنوعات","id":"Semua produk","de":"Alle Produkte","ja":"全製品","ko":"전체 제품","vi":"Tất cả sản phẩm","th":"ผลิตภัณฑ์ทั้งหมด"}),
  "gummies": L({"en":"Creatine Gummies","zh-tw":"肌酸軟糖","hi":"क्रिएटिन गमी","es":"Gomitas de creatina","ar":"علكات الكرياتين","fr":"Gummies créatine","bn":"ক্রিয়েটিন গামি","pt":"Gummies de creatina","ru":"Жевательный креатин","ur":"کریٹائن گمیز","id":"Gummy creatine","de":"Creatin-Gummies","ja":"クレアチン・グミ","ko":"크레아틴 구미","vi":"Kẹo dẻo creatine","th":"ครีเอทีนกัมมี่"}),
  "powder": L({"en":"Creatine Powder","zh-tw":"肌酸粉","hi":"क्रिएटिन पाउडर","es":"Creatina en polvo","ar":"مسحوق الكرياتين","fr":"Créatine en poudre","bn":"ক্রিয়েটিন পাউডার","pt":"Creatina em pó","ru":"Креатин порошок","ur":"کریٹائن پاؤڈر","id":"Bubuk creatine","de":"Creatin-Pulver","ja":"クレアチン粉末","ko":"크레아틴 파우더","vi":"Bột creatine","th":"ครีเอทีนผง"}),
  "capsules": L({"en":"Creatine Capsules","zh-tw":"肌酸膠囊","hi":"क्रिएटिन कैप्सूल","es":"Cápsulas de creatina","ar":"كبسولات الكرياتين","fr":"Capsules de créatine","bn":"ক্রিয়েটিন ক্যাপসুল","pt":"Cápsulas de creatina","ru":"Креатин капсулы","ur":"کریٹائن کیپسولز","id":"Kapsul creatine","de":"Creatin-Kapseln","ja":"クレアチン・カプセル","ko":"크레아틴 캡슐","vi":"Viên nang creatine","th":"ครีเอทีนแคปซูล"}),
  "oemPrivate": L({"en":"OEM / Private Label","zh-tw":"OEM／私標","hi":"OEM / प्राइवेट लेबल","es":"OEM / marca privada","ar":"OEM / علامة خاصة","fr":"OEM / marque blanche","bn":"OEM / প্রাইভেট লেবেল","pt":"OEM / private label","ru":"OEM / private label","ur":"OEM / پرائیویٹ لیبل","id":"OEM / private label","de":"OEM / Private Label","ja":"OEM／プライベートラベル","ko":"OEM / 프라이빗 라벨","vi":"OEM / nhãn riêng","th":"OEM / ไพรเวทเลเบล"}),
  "support": L({"en":"Support","zh-tw":"支援","hi":"सहायता","es":"Soporte","ar":"الدعم","fr":"Support","bn":"সহায়তা","pt":"Suporte","ru":"Поддержка","ur":"سپورٹ","id":"Dukungan","de":"Support","ja":"サポート","ko":"지원","vi":"Hỗ trợ","th":"สนับสนุน"}),
  "oemQuote": L({"en":"OEM Quote","zh-tw":"OEM 報價","hi":"OEM कोट","es":"Cotización OEM","ar":"عرض سعر OEM","fr":"Devis OEM","bn":"OEM কোট","pt":"Orçamento OEM","ru":"КП OEM","ur":"OEM کوٹ","id":"Penawaran OEM","de":"OEM-Angebot","ja":"OEM見積","ko":"OEM 견적","vi":"Báo giá OEM","th":"ใบเสนอราคา OEM"}),
  "wholesalePrice": L({"en":"Wholesale Price List","zh-tw":"批發價目表","hi":"थोक मूल्य सूची","es":"Lista de precios mayoreo","ar":"قائمة أسعار الجملة","fr":"Tarif gros","bn":"হোলসেল মূল্য তালিকা","pt":"Lista de preços atacado","ru":"Оптовый прайс","ur":"ہول سیل قیمت فہرست","id":"Daftar harga grosir","de":"Großhandelspreisliste","ja":"卸売価格表","ko":"도매 가격표","vi":"Bảng giá sỉ","th":"รายการราคาขายส่ง"}),
  "sampleRequest": L({"en":"Sample Request","zh-tw":"索樣","hi":"सैंपल अनुरोध","es":"Solicitud de muestra","ar":"طلب عينة","fr":"Demande d’échantillon","bn":"নমুনা অনুরোধ","pt":"Pedido de amostra","ru":"Запрос образца","ur":"سیمپل کی درخواست","id":"Permintaan sampel","de":"Musteranfrage","ja":"サンプル依頼","ko":"샘플 요청","vi":"Yêu cầu mẫu","th":"ขอตัวอย่าง"}),
  "faq": L({"en":"FAQ","zh-tw":"常見問題","hi":"FAQ","es":"FAQ","ar":"الأسئلة الشائعة","fr":"FAQ","bn":"FAQ","pt":"FAQ","ru":"FAQ","ur":"FAQ","id":"FAQ","de":"FAQ","ja":"FAQ","ko":"FAQ","vi":"FAQ","th":"FAQ"}),
  "terms": L({"en":"Terms","zh-tw":"條款","hi":"नियम","es":"Términos","ar":"الشروط","fr":"Conditions","bn":"শর্তাবলী","pt":"Termos","ru":"Условия","ur":"شرائط","id":"Syarat","de":"AGB","ja":"利用規約","ko":"이용약관","vi":"Điều khoản","th":"ข้อกำหนด"}),
  "privacy": L({"en":"Privacy Policy","zh-tw":"隱私權政策","hi":"गोपनीयता नीति","es":"Política de privacidad","ar":"سياسة الخصوصية","fr":"Politique de confidentialité","bn":"গোপনীয়তা নীতি","pt":"Política de privacidade","ru":"Политика конфиденциальности","ur":"رازداری کی پالیسی","id":"Kebijakan privasi","de":"Datenschutz","ja":"プライバシーポリシー","ko":"개인정보 처리방침","vi":"Chính sách bảo mật","th":"นโยบายความเป็นส่วนตัว"}),
  "footnote": L({
    "en":'Made by <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · B2B creatine OEM & wholesale · All rights reserved.',
    "zh-tw":'由 <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> 製作 · B2B 肌酸 OEM 與批發 · 版權所有。',
    "hi":'द्वारा <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · B2B क्रिएटिन OEM और थोक · सर्वाधिकार सुरक्षित।',
    "es":'Hecho por <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · OEM y mayoreo B2B de creatina · Todos los derechos reservados.',
    "ar":'من إعداد <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · كرياتين OEM وجملة B2B · جميع الحقوق محفوظة.',
    "fr":'Par <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · OEM et gros B2B créatine · Tous droits réservés.',
    "bn":'<a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> দ্বারা · B2B ক্রিয়েটিন OEM ও হোলসেল · সর্বস্বত্ব সংরক্ষিত।',
    "pt":'Feito por <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · OEM e atacado B2B de creatina · Todos os direitos reservados.',
    "ru":'Сделано <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · B2B креатин OEM и опт · Все права защищены.',
    "ur":'بنایا گیا <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · B2B کریٹائن OEM اور ہول سیل · جملہ حقوق محفوظ۔',
    "id":'Dibuat oleh <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · OEM & grosir creatine B2B · Hak cipta dilindungi.',
    "de":'Von <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · B2B Creatin OEM & Großhandel · Alle Rechte vorbehalten.',
    "ja":'<a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · B2BクレアチンOEM＆卸売 · 無断転載禁止',
    "ko":'Made by <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · B2B 크레아틴 OEM & 도매 · All rights reserved.',
    "vi":'Thực hiện bởi <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · OEM & bán sỉ creatine B2B · Bảo lưu mọi quyền.',
    "th":'จัดทำโดย <a class="text-primary underline dark:text-accent" href="{home}">Crest Creatine</a> · OEM และขายส่งครีเอทีน B2B · สงวนลิขสิทธิ์',
  }),
}

NAV = {loc: {k: v[loc] for k, v in NAV_KEYS.items()} for loc in LOCALES}

nav_ts = '''import { localizePath, type Locale } from './locales';

''' + write_record("NAV", "{ home: string; products: string; oem: string; wholesale: string; quality: string; contact: string; quote: string; company: string; qualityCompliance: string; programs: string; allProducts: string; gummies: string; powder: string; capsules: string; oemPrivate: string; support: string; oemQuote: string; wholesalePrice: string; sampleRequest: string; faq: string; terms: string; privacy: string; footnote: string }", NAV) + '''

export function getHeaderFooter(locale: Locale = 'en') {
  const n = NAV[locale] ?? NAV.en;
  const p = (path: string) => localizePath(path, locale);
  const home = p('/');
  return {
    header: {
      links: [
        { text: n.home, href: home },
        { text: n.products, href: p('/products') },
        { text: n.oem, href: p('/oem') },
        { text: n.wholesale, href: p('/wholesale') },
        { text: n.quality, href: p('/quality') },
        { text: n.contact, href: p('/contact') },
      ],
      actions: [{ text: n.quote, href: `${p('/contact')}#inquiry-form`, variant: 'primary' as const }],
    },
    footer: {
      links: [
        {
          title: n.company,
          links: [
            { text: n.home, href: home },
            { text: n.qualityCompliance, href: p('/quality') },
            { text: n.contact, href: `${p('/contact')}#inquiry-form` },
          ],
        },
        {
          title: n.programs,
          links: [
            { text: n.allProducts, href: p('/products') },
            { text: n.gummies, href: `${p('/products')}#gummies` },
            { text: n.powder, href: `${p('/products')}#powder` },
            { text: n.capsules, href: `${p('/products')}#capsules` },
            { text: n.oemPrivate, href: p('/oem') },
            { text: n.wholesale, href: p('/wholesale') },
          ],
        },
        {
          title: n.support,
          links: [
            { text: n.oemQuote, href: `${p('/contact')}?looking=OEM%2FPrivate%20label#inquiry-form` },
            { text: n.wholesalePrice, href: `${p('/contact')}?looking=Wholesale%20pricing#inquiry-form` },
            { text: n.sampleRequest, href: `${p('/contact')}?looking=Sample#inquiry-form` },
            { text: n.faq, href: `${home}#faq` },
          ],
        },
      ],
      secondaryLinks: [
        { text: n.terms, href: p('/terms') },
        { text: n.privacy, href: p('/privacy') },
      ],
      socialLinks: [],
      footNote: n.footnote.replaceAll('{home}', home),
    },
  };
}
'''
(OUT / "nav.ts").write_text(nav_ts, encoding="utf-8")
print("Wrote nav.ts")

# Dump NAV_KEYS for forms continuation in part 2
(OUT / "_nav_keys.json").write_text(json.dumps(NAV_KEYS, ensure_ascii=False), encoding="utf-8")
print("OK part1")
