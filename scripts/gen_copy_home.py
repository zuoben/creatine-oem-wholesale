#!/usr/bin/env python3
"""Generate copy-home.ts with substantial B2B translations for all 16 locales."""
from __future__ import annotations
import json
from pathlib import Path

OUT = Path("/workspace/creatine-oem-wholesale/src/i18n/copy-home.ts")
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
            key = k if str(k).isidentifier() and "-" not in str(k) else json.dumps(k)
            parts.append(f"{pad2}{key}: {ser(v, indent+2)},")
        return "{\n" + "\n".join(parts) + f"\n{pad}}}"
    return "null"

def lk(loc):
    return f"'{loc}'" if "-" in loc else loc

# Each locale: full home copy dict matching English meaning
# Specs/numbers stay consistent; marketing copy localized.

HOME = {}

HOME["en"] = {
  "title": "Private Label Creatine OEM & Wholesale | Crest Creatine",
  "description": "B2B creatine manufacturer — OEM / private label creatine gummies, powder & capsules, wholesale carton pricing, samples, COA & third-party testing. Quote within 24 hours.",
  "tagline": "B2B Creatine Manufacturer",
  "hero1": "Private Label Creatine &",
  "hero2": "Wholesale Supply",
  "heroSub": "Crest Creatine helps brands and distributors source creatine monohydrate gummies, powder, and capsules — OEM / private label programs and standard wholesale cartons, with samples, COA support, and quotes within 24 hours.",
  "ctaOem": "OEM / Private Label",
  "ctaWholesale": "Wholesale",
  "trustTag": "Why partners choose us",
  "trustTitle": "Built for B2B creatine sourcing",
  "trustSub": "MOQ clarity, sample-first OEM, documentation, and fast quotes — without retail cart noise.",
  "trustItems": [
    {"title": "Flexible MOQ", "description": "Trial MOQs for private label pilots; carton MOQs for wholesale SKUs.", "icon": "tabler:package"},
    {"title": "Samples available", "description": "Approve formula, flavor, and packaging before bulk production.", "icon": "tabler:flask"},
    {"title": "COA & testing", "description": "Lot COA pathways and third-party testing support for US-bound brands.", "icon": "tabler:file-certificate"},
    {"title": "24h quote", "description": "Working-day reply on OEM RFQs and wholesale price-list requests.", "icon": "tabler:clock"},
  ],
  "buyTag": "Two ways to buy",
  "buyTitle": "OEM / Private Label or Wholesale",
  "buyOemTitle": "OEM / Private Label",
  "buyOemDesc": "Custom creatine gummies, powder, and capsules — flavors, packaging, branding, and compliance docs for your label. Ideal for brands launching or expanding a creatine SKU.",
  "buyWhTitle": "Wholesale",
  "buyWhDesc": "Standard carton specs for distributors, gyms, retailers, and online sellers. Request a price list and account guidance via the wholesale inquiry form.",
  "prodTag": "Product programs",
  "prodTitle": "Gummies, powder & capsules",
  "prodSub": "Starting configurations for private label and wholesale — dose, pack, and MOQ guidance confirmed on quote.",
  "gummiesTitle": "Creatine gummies",
  "gummiesDesc": "Hero format: ~1,000 mg/gummy or ~5 g across 3 gummies; 60/90-count bottles; pectin-based options; flavor development.",
  "gummiesCta": "View gummies",
  "powderTitle": "Creatine powder",
  "powderDesc": "300 g / 500 g / 1 kg tubs or pouches; 25 kg drums; mesh options for fill/dispersion; unflavored + flavors.",
  "powderCta": "View powder",
  "capsTitle": "Creatine capsules",
  "capsDesc": "Approx. 750–1,000 mg/capsule; 60–240 counts; gelatin, HPMC, or pullulan shells subject to program.",
  "capsCta": "View capsules",
  "stepsTitle": "How sourcing works",
  "steps": [
    {"title": "Tell us your channel", "description": "OEM project or wholesale account — buyer type, volume, and ship-to country.", "icon": "tabler:message"},
    {"title": "Get MOQ & samples", "description": "We reply with tiered MOQs, sample options, and documentation available for your market.", "icon": "tabler:package"},
    {"title": "Approve & produce", "description": "Lock formula, flavor, and packaging (OEM) or carton SKUs (wholesale), then schedule production.", "icon": "tabler:circle-check-filled"},
    {"title": "Ship & reorder", "description": "Export packing support and repeat-order pathways for ongoing monthly volume.", "icon": "tabler:truck-delivery"},
  ],
  "faqTitle": "Creatine OEM & wholesale FAQ",
  "faqs": [
    {"title": "Do you offer both OEM / private label and wholesale?", "description": "Yes. <strong>OEM / private label</strong> for brands that need custom formulas, flavors, and packaging; <strong>wholesale</strong> for distributors, gyms, and online sellers buying standard carton SKUs."},
    {"title": "What creatine formats can you private-label?", "description": "Creatine monohydrate <strong>gummies</strong>, <strong>powder</strong>, and <strong>capsules</strong>, with custom flavors, serving sizes, and branded packaging options subject to MOQ."},
    {"title": "Can I get samples before placing a bulk order?", "description": "Yes. Sample-first is recommended for flavor, texture, and label review. Ask via the inquiry form."},
    {"title": "Do you provide COA or third-party testing?", "description": "We support lot-level documentation and third-party testing pathways appropriate for dietary supplement buyers. Details are confirmed during quote."},
    {"title": "Is this a US consumer retail store?", "description": "No. Crest Creatine is a <strong>B2B</strong> OEM and wholesale site for brands and channel partners — not a DTC subscribe or add-to-cart shop."},
  ],
  "ctaTitle": "Ready for a factory quote?",
  "ctaSub": "Share buyer type, looking-for, and volume — we respond on working days within 24 hours.",
  "ctaForm": "Open inquiry form",
  "ctaProducts": "Product programs",
  "ctaOemDetails": "OEM details",
  "ctaWhDetails": "Wholesale details",
  "dshea": "Dietary supplement notice: Products are intended as dietary supplements under DSHEA. Statements have not been evaluated by the FDA. Not intended to diagnose, treat, cure, or prevent any disease.",
}

# Helper to clone structure with translated strings — full professional translations per locale
def T(**kwargs):
    base = dict(HOME["en"])
    base.update(kwargs)
    return base

HOME["zh-tw"] = T(
  title="肌酸私標 OEM 與批發｜Crest Creatine",
  description="B2B 肌酸製造商 — OEM／私標肌酸軟糖、粉與膠囊，批發箱規報價、樣品、COA 與第三方檢測。工作日 24 小時內報價。",
  tagline="B2B 肌酸製造商",
  hero1="肌酸私標與",
  hero2="批發供應",
  heroSub="Crest Creatine 協助品牌與經銷商採購一水肌酸軟糖、粉劑與膠囊 — OEM／私標方案與標準批發箱規，含樣品、COA 支援，工作日 24 小時內報價。",
  ctaOem="OEM／私標",
  ctaWholesale="批發",
  trustTag="合作夥伴為何選擇我們",
  trustTitle="專為 B2B 肌酸採購打造",
  trustSub="MOQ 清晰、樣品優先的 OEM、文件齊備、快速報價 — 沒有零售購物車干擾。",
  trustItems=[
    {"title":"彈性 MOQ","description":"私標試產有試產 MOQ；批發 SKU 有箱規 MOQ。","icon":"tabler:package"},
    {"title":"可提供樣品","description":"量產前確認配方、口味與包裝。","icon":"tabler:flask"},
    {"title":"COA 與檢測","description":"批次 COA 路徑與第三方檢測，支援銷美品牌。","icon":"tabler:file-certificate"},
    {"title":"24 小時報價","description":"OEM 詢價與批發價目表於工作日回覆。","icon":"tabler:clock"},
  ],
  buyTag="兩種採購方式",
  buyTitle="OEM／私標或批發",
  buyOemTitle="OEM／私標",
  buyOemDesc="客製肌酸軟糖、粉與膠囊 — 口味、包裝、品牌與合規文件。適合推出或擴充肌酸 SKU 的品牌。",
  buyWhTitle="批發",
  buyWhDesc="標準箱規，服務經銷商、健身房、零售與電商。透過批發詢價表索取價目與開戶指引。",
  prodTag="產品方案",
  prodTitle="軟糖、粉劑與膠囊",
  prodSub="私標與批發的起始規格 — 劑量、包裝與 MOQ 於報價確認。",
  gummiesTitle="肌酸軟糖",
  gummiesDesc="主力劑型：約 1,000 mg／顆或 3 顆約 5 g；60／90 瓶裝；果膠配方可選；口味開發。",
  gummiesCta="查看軟糖",
  powderTitle="肌酸粉",
  powderDesc="300 g／500 g／1 kg 桶或袋；25 kg 桶；目數選項；原味與口味。",
  powderCta="查看粉劑",
  capsTitle="肌酸膠囊",
  capsDesc="約 750–1,000 mg／粒；60–240 粒；明膠、HPMC 或普魯蘭殼依方案。",
  capsCta="查看膠囊",
  stepsTitle="採購流程",
  steps=[
    {"title":"說明通路","description":"OEM 專案或批發帳戶 — 買家類型、量級與目的地國家。","icon":"tabler:message"},
    {"title":"取得 MOQ 與樣品","description":"回覆分層 MOQ、樣品方案與市場文件。","icon":"tabler:package"},
    {"title":"確認與生產","description":"鎖定配方／口味／包裝（OEM）或箱規 SKU（批發），再排產。","icon":"tabler:circle-check-filled"},
    {"title":"出貨與回購","description":"出口包裝支援與每月回購路徑。","icon":"tabler:truck-delivery"},
  ],
  faqTitle="肌酸 OEM 與批發常見問題",
  faqs=[
    {"title":"是否同時提供 OEM／私標與批發？","description":"是。<strong>OEM／私標</strong>適合需要客製配方、口味與包裝的品牌；<strong>批發</strong>適合採購標準箱規的經銷商、健身房與電商。"},
    {"title":"可私標哪些肌酸劑型？","description":"一水肌酸<strong>軟糖</strong>、<strong>粉劑</strong>與<strong>膠囊</strong>，可客製口味、份量與品牌包裝（視 MOQ）。"},
    {"title":"量產前可以拿樣嗎？","description":"可以。建議先樣確認口味、質地與標籤。請透過詢價表提出。"},
    {"title":"是否提供 COA 或第三方檢測？","description":"我們支援批次文件與適合膳食補充劑買家的第三方檢測路徑。細節於報價確認。"},
    {"title":"這是美國消費者零售店嗎？","description":"否。Crest Creatine 是面向品牌與通路夥伴的<strong>B2B</strong> OEM 與批發網站 — 非 DTC 訂閱或購物車商店。"},
  ],
  ctaTitle="準備好工廠報價了嗎？",
  ctaSub="告訴我們買家類型、需求與量級 — 工作日 24 小時內回覆。",
  ctaForm="開啟詢價表",
  ctaProducts="產品方案",
  ctaOemDetails="OEM 詳情",
  ctaWhDetails="批發詳情",
  dshea="膳食補充劑聲明：產品擬作為 DSHEA 下的膳食補充劑。相關敘述未經 FDA 評估。無意診斷、治療、治癒或預防任何疾病。",
)

# For remaining locales, provide full professional translations (compact but complete)
def make_locale(loc, **kw):
    HOME[loc] = T(**kw)

make_locale("es",
  title="Creatina marca privada OEM y mayoreo | Crest Creatine",
  description="Fabricante B2B de creatina — OEM / marca privada gomitas, polvo y cápsulas, precios por caja, muestras, COA y pruebas de terceros. Cotización en 24 horas.",
  tagline="Fabricante B2B de creatina",
  hero1="Creatina marca privada y",
  hero2="suministro al mayoreo",
  heroSub="Crest Creatine ayuda a marcas y distribuidores a abastecer gomitas, polvo y cápsulas de creatina monohidrato — programas OEM / marca privada y cajas estándar al mayoreo, con muestras, soporte COA y cotizaciones en 24 horas.",
  ctaOem="OEM / Marca privada", ctaWholesale="Mayoreo",
  trustTag="Por qué nos eligen los socios", trustTitle="Hecho para sourcing B2B de creatina",
  trustSub="MOQ claros, OEM con muestra primero, documentación y cotizaciones rápidas — sin carrito retail.",
  trustItems=[
    {"title":"MOQ flexible","description":"MOQ de prueba para pilotos de marca privada; MOQ por caja para SKUs de mayoreo.","icon":"tabler:package"},
    {"title":"Muestras disponibles","description":"Apruebe fórmula, sabor y empaque antes de la producción.","icon":"tabler:flask"},
    {"title":"COA y pruebas","description":"Rutas de COA por lote y pruebas de terceros para marcas hacia EE. UU.","icon":"tabler:file-certificate"},
    {"title":"Cotización 24 h","description":"Respuesta en días hábiles a RFQ OEM y listas de precios mayoreo.","icon":"tabler:clock"},
  ],
  buyTag="Dos formas de comprar", buyTitle="OEM / Marca privada o Mayoreo",
  buyOemTitle="OEM / Marca privada",
  buyOemDesc="Gomitas, polvo y cápsulas de creatina a medida — sabores, empaque, branding y documentos de cumplimiento. Ideal para marcas que lanzan o amplían un SKU de creatina.",
  buyWhTitle="Mayoreo",
  buyWhDesc="Especificaciones de caja estándar para distribuidores, gimnasios, retailers y vendedores online. Solicite lista de precios y guía de cuenta.",
  prodTag="Programas de producto", prodTitle="Gomitas, polvo y cápsulas",
  prodSub="Configuraciones iniciales para marca privada y mayoreo — dosis, pack y MOQ se confirman en la cotización.",
  gummiesTitle="Gomitas de creatina", gummiesDesc="Formato héroe: ~1.000 mg/gomita o ~5 g en 3 gomitas; frascos 60/90; opciones de pectina; desarrollo de sabores.",
  gummiesCta="Ver gomitas", powderTitle="Creatina en polvo",
  powderDesc="Tarros o pouches 300 g / 500 g / 1 kg; tambores 25 kg; opciones de malla; sin sabor + sabores.",
  powderCta="Ver polvo", capsTitle="Cápsulas de creatina",
  capsDesc="Aprox. 750–1.000 mg/cápsula; conteos 60–240; cápsulas de gelatina, HPMC o pullulan según programa.",
  capsCta="Ver cápsulas", stepsTitle="Cómo funciona el sourcing",
  steps=[
    {"title":"Cuéntenos su canal","description":"Proyecto OEM o cuenta mayoreo — tipo de comprador, volumen y país de destino.","icon":"tabler:message"},
    {"title":"Obtenga MOQ y muestras","description":"Respondemos con MOQ escalonados, opciones de muestra y documentación.","icon":"tabler:package"},
    {"title":"Apruebe y produzca","description":"Fije fórmula, sabor y empaque (OEM) o SKUs de caja (mayoreo), luego programe producción.","icon":"tabler:circle-check-filled"},
    {"title":"Envíe y reordene","description":"Soporte de empaque de exportación y reórdenes mensuales.","icon":"tabler:truck-delivery"},
  ],
  faqTitle="FAQ OEM y mayoreo de creatina",
  faqs=[
    {"title":"¿Ofrecen OEM / marca privada y mayoreo?","description":"Sí. <strong>OEM / marca privada</strong> para marcas que necesitan fórmulas, sabores y empaque a medida; <strong>mayoreo</strong> para distribuidores, gimnasios y vendedores online con SKUs de caja estándar."},
    {"title":"¿Qué formatos de creatina pueden marcar en privado?","description":"Creatina monohidrato en <strong>gomitas</strong>, <strong>polvo</strong> y <strong>cápsulas</strong>, con sabores, porciones y empaque de marca sujetos a MOQ."},
    {"title":"¿Puedo obtener muestras antes de un pedido grande?","description":"Sí. Se recomienda muestra primero para sabor, textura y etiqueta. Solicite en el formulario."},
    {"title":"¿Proveen COA o pruebas de terceros?","description":"Apoyamos documentación por lote y rutas de pruebas de terceros para compradores de suplementos. Detalles en la cotización."},
    {"title":"¿Es una tienda retail para consumidores en EE. UU.?","description":"No. Crest Creatine es un sitio <strong>B2B</strong> de OEM y mayoreo para marcas y socios de canal — no una tienda DTC."},
  ],
  ctaTitle="¿Listo para una cotización de fábrica?",
  ctaSub="Comparta tipo de comprador, necesidad y volumen — respondemos en días hábiles en 24 horas.",
  ctaForm="Abrir formulario", ctaProducts="Programas de producto", ctaOemDetails="Detalles OEM", ctaWhDetails="Detalles mayoreo",
  dshea="Aviso de suplemento dietético: Los productos se destinan como suplementos dietéticos bajo DSHEA. Las declaraciones no han sido evaluadas por la FDA. No destinados a diagnosticar, tratar, curar o prevenir ninguna enfermedad.",
)

# Continue with other locales in a compact but complete way - write remaining to JSON then assemble
# To keep script size manageable, generate remaining locales programmatically from translation tables for key fields
# and structured FAQ/trust items.

# I'll write the remaining locales as complete objects in a second data blob
remaining = {
"ar": {
  "title":"كرياتين علامة خاصة OEM والجملة | Crest Creatine",
  "description":"مصنّع كرياتين B2B — علكات ومسحوق وكبسولات علامة خاصة، أسعار صناديق الجملة، عينات، COA واختبارات طرف ثالث. عرض سعر خلال 24 ساعة.",
  "tagline":"مصنّع كرياتين B2B","hero1":"كرياتين علامة خاصة و","hero2":"توريد بالجملة",
  "heroSub":"تساعد Crest Creatine العلامات والموزّعين على توريد علكات ومسحوق وكبسولات كرياتين مونوهيدرات — برامج OEM / علامة خاصة وصناديق جملة قياسية، مع عينات ودعم COA وعروض خلال 24 ساعة.",
  "ctaOem":"OEM / علامة خاصة","ctaWholesale":"الجملة",
  "trustTag":"لماذا يختارنا الشركاء","trustTitle":"مصمم لتوريد الكرياتين B2B",
  "trustSub":"وضوح الحد الأدنى، OEM يبدأ بالعينة، وثائق وعروض سريعة — بدون سلة تجزئة.",
  "dshea":"إشعار المكمل الغذائي: المنتجات مخصصة كمكملات غذائية بموجب DSHEA. لم تُقيَّم التصريحات من قِبل إدارة الغذاء والدواء. غير مخصصة لتشخيص أو علاج أو شفاء أو الوقاية من أي مرض.",
},
"fr": {
  "title":"Créatine marque blanche OEM & gros | Crest Creatine",
  "description":"Fabricant B2B de créatine — gummies, poudre et capsules OEM / marque blanche, tarifs cartons, échantillons, COA et tests tiers. Devis sous 24 h.",
  "tagline":"Fabricant B2B de créatine","hero1":"Créatine marque blanche &","hero2":"approvisionnement gros",
  "heroSub":"Crest Creatine aide marques et distributeurs à sourcer gummies, poudre et capsules de créatine monohydrate — programmes OEM / marque blanche et cartons standard, avec échantillons, support COA et devis sous 24 h.",
  "ctaOem":"OEM / Marque blanche","ctaWholesale":"Gros",
  "trustTag":"Pourquoi les partenaires nous choisissent","trustTitle":"Conçu pour le sourcing B2B créatine",
  "trustSub":"MOQ clairs, OEM échantillon d’abord, documentation et devis rapides — sans panier retail.",
  "dshea":"Avis complément alimentaire : Les produits sont destinés comme compléments alimentaires au sens du DSHEA. Les déclarations n’ont pas été évaluées par la FDA. Non destinés à diagnostiquer, traiter, guérir ou prévenir une maladie.",
},
"de": {
  "title":"Creatin Private Label OEM & Großhandel | Crest Creatine",
  "description":"B2B-Creatin-Hersteller — OEM / Private Label Gummies, Pulver & Kapseln, Kartonpreise, Muster, COA & Drittlabor. Angebot in 24 Stunden.",
  "tagline":"B2B-Creatin-Hersteller","hero1":"Creatin Private Label &","hero2":"Großhandelsversorgung",
  "heroSub":"Crest Creatine hilft Marken und Distributoren, Creatin-Monohydrat als Gummies, Pulver und Kapseln zu beziehen — OEM / Private-Label-Programme und Standard-Kartons, mit Mustern, COA-Support und Angeboten in 24 Stunden.",
  "ctaOem":"OEM / Private Label","ctaWholesale":"Großhandel",
  "trustTag":"Warum Partner uns wählen","trustTitle":"Für B2B-Creatin-Sourcing gebaut",
  "trustSub":"Klare MOQs, sample-first OEM, Dokumentation und schnelle Angebote — ohne Retail-Warenkorb.",
  "dshea":"Hinweis Nahrungsergänzung: Produkte sind als Nahrungsergänzungsmittel unter DSHEA vorgesehen. Aussagen wurden nicht von der FDA bewertet. Nicht zur Diagnose, Behandlung, Heilung oder Vorbeugung von Krankheiten bestimmt.",
},
"pt": {
  "title":"Creatina private label OEM e atacado | Crest Creatine",
  "description":"Fabricante B2B de creatina — gummies, pó e cápsulas OEM / private label, preços por caixa, amostras, COA e testes de terceiros. Orçamento em 24 horas.",
  "tagline":"Fabricante B2B de creatina","hero1":"Creatina private label e","hero2":"suprimento no atacado",
  "heroSub":"A Crest Creatine ajuda marcas e distribuidores a abastecer gummies, pó e cápsulas de creatina monohidratada — programas OEM / private label e caixas padrão no atacado, com amostras, suporte COA e orçamentos em 24 horas.",
  "ctaOem":"OEM / Private label","ctaWholesale":"Atacado",
  "trustTag":"Por que os parceiros nos escolhem","trustTitle":"Feito para sourcing B2B de creatina",
  "trustSub":"MOQ claros, OEM com amostra primeiro, documentação e orçamentos rápidos — sem carrinho retail.",
  "dshea":"Aviso de suplemento alimentar: Os produtos destinam-se a suplementos alimentares sob o DSHEA. As declarações não foram avaliadas pela FDA. Não destinados a diagnosticar, tratar, curar ou prevenir qualquer doença.",
},
"ja": {
  "title":"クレアチン プライベートラベル OEM・卸売｜Crest Creatine",
  "description":"B2Bクレアチン製造 — OEM／プライベートラベルのグミ・粉末・カプセル、卸売カートン価格、サンプル、COA・第三者試験。営業日24時間以内に見積。",
  "tagline":"B2Bクレアチンメーカー","hero1":"プライベートラベルクレアチン＆","hero2":"卸売供給",
  "heroSub":"Crest Creatineはブランド・代理店向けにクレアチンモノハイドレートのグミ・粉末・カプセルを供給します。OEM／プライベートラベルと標準卸売カートン、サンプル・COA対応、24時間以内の見積。",
  "ctaOem":"OEM／プライベートラベル","ctaWholesale":"卸売",
  "trustTag":"パートナーに選ばれる理由","trustTitle":"B2Bクレアチン調達向けに設計",
  "trustSub":"明確なMOQ、サンプル優先のOEM、文書、迅速見積 — 小売カートなし。",
  "dshea":"ダイエタリーサプリメント表示：製品はDSHEAに基づくダイエタリーサプリメントとして意図されています。表示はFDAの評価を受けていません。疾病の診断・治療・治癒・予防を目的としません。",
},
"ko": {
  "title":"크레아틴 프라이빗 라벨 OEM & 도매 | Crest Creatine",
  "description":"B2B 크레아틴 제조 — OEM/프라이빗 라벨 구미·파우더·캡슐, 도매 카톤 가격, 샘플, COA 및 제3자 시험. 영업일 24시간 내 견적.",
  "tagline":"B2B 크레아틴 제조사","hero1":"프라이빗 라벨 크레아틴 &","hero2":"도매 공급",
  "heroSub":"Crest Creatine은 브랜드와 유통사가 크레아틴 모노하이드레이트 구미·파우더·캡슐을 조달하도록 돕습니다 — OEM/프라이빗 라벨과 표준 도매 카톤, 샘플·COA 지원, 24시간 내 견적.",
  "ctaOem":"OEM / 프라이빗 라벨","ctaWholesale":"도매",
  "trustTag":"파트너가 우리를 선택하는 이유","trustTitle":"B2B 크레아틴 소싱을 위해 설계",
  "trustSub":"명확한 MOQ, 샘플 우선 OEM, 문서화, 빠른 견적 — 리테일 카트 없음.",
  "dshea":"건강기능식품(식이보충제) 고지: 제품은 DSHEA에 따른 식이보충제로 의도됩니다. 관련 문구는 FDA의 평가를 받지 않았습니다. 질병의 진단, 치료, 치유 또는 예방을 목적으로 하지 않습니다.",
},
"vi": {
  "title":"Creatine nhãn riêng OEM & bán sỉ | Crest Creatine",
  "description":"Nhà sản xuất creatine B2B — kẹo dẻo, bột & viên nang OEM / nhãn riêng, giá carton sỉ, mẫu, COA & kiểm nghiệm bên thứ ba. Báo giá trong 24 giờ.",
  "tagline":"Nhà sản xuất creatine B2B","hero1":"Creatine nhãn riêng &","hero2":"cung ứng bán sỉ",
  "heroSub":"Crest Creatine giúp thương hiệu và nhà phân phối sourcing kẹo dẻo, bột và viên nang creatine monohydrate — chương trình OEM / nhãn riêng và carton sỉ chuẩn, kèm mẫu, hỗ trợ COA và báo giá trong 24 giờ.",
  "ctaOem":"OEM / Nhãn riêng","ctaWholesale":"Bán sỉ",
  "trustTag":"Vì sao đối tác chọn chúng tôi","trustTitle":"Thiết kế cho sourcing creatine B2B",
  "trustSub":"MOQ rõ ràng, OEM ưu tiên mẫu, tài liệu và báo giá nhanh — không giỏ hàng bán lẻ.",
  "dshea":"Thông báo thực phẩm bổ sung: Sản phẩm được dùng như thực phẩm bổ sung theo DSHEA. Các tuyên bố chưa được FDA đánh giá. Không nhằm chẩn đoán, điều trị, chữa khỏi hoặc phòng ngừa bất kỳ bệnh nào.",
},
"id": {
  "title":"Creatine private label OEM & grosir | Crest Creatine",
  "description":"Produsen creatine B2B — gummy, bubuk & kapsul OEM / private label, harga karton grosir, sampel, COA & uji pihak ketiga. Penawaran dalam 24 jam.",
  "tagline":"Produsen creatine B2B","hero1":"Creatine private label &","hero2":"pasokan grosir",
  "heroSub":"Crest Creatine membantu merek dan distributor mendapatkan gummy, bubuk, dan kapsul creatine monohydrate — program OEM / private label dan karton grosir standar, dengan sampel, dukungan COA, dan penawaran dalam 24 jam.",
  "ctaOem":"OEM / Private label","ctaWholesale":"Grosir",
  "trustTag":"Mengapa mitra memilih kami","trustTitle":"Dibangun untuk sourcing creatine B2B",
  "trustSub":"MOQ jelas, OEM sampel dulu, dokumentasi, dan penawaran cepat — tanpa keranjang retail.",
  "dshea":"Pemberitahuan suplemen makanan: Produk dimaksudkan sebagai suplemen makanan di bawah DSHEA. Pernyataan belum dievaluasi FDA. Tidak dimaksudkan untuk mendiagnosis, mengobati, menyembuhkan, atau mencegah penyakit apa pun.",
},
"ru": {
  "title":"Креатин private label OEM и опт | Crest Creatine",
  "description":"B2B-производитель креатина — жевательные, порошок и капсулы OEM / private label, оптовые цены по коробкам, образцы, COA и сторонние тесты. КП за 24 часа.",
  "tagline":"B2B-производитель креатина","hero1":"Креатин private label и","hero2":"оптовые поставки",
  "heroSub":"Crest Creatine помогает брендам и дистрибьюторам закупать креатин моногидрат в жевательных формах, порошке и капсулах — программы OEM / private label и стандартные оптовые коробки, с образцами, поддержкой COA и КП за 24 часа.",
  "ctaOem":"OEM / Private label","ctaWholesale":"Опт",
  "trustTag":"Почему нас выбирают партнёры","trustTitle":"Создано для B2B-закупок креатина",
  "trustSub":"Понятные MOQ, OEM с образцом сначала, документы и быстрые КП — без розничной корзины.",
  "dshea":"Уведомление о БАД: Продукты предназначены как биологически активные добавки в рамках DSHEA. Заявления не оценивались FDA. Не предназначены для диагностики, лечения, излечения или профилактики заболеваний.",
},
"hi": {
  "title":"प्राइवेट लेबल क्रिएटिन OEM और थोक | Crest Creatine",
  "description":"B2B क्रिएटिन निर्माता — OEM / प्राइवेट लेबल गमी, पाउडर और कैप्सूल, थोक कार्टन मूल्य, सैंपल, COA और थर्ड-पार्टी टेस्टिंग। 24 घंटे में कोट।",
  "tagline":"B2B क्रिएटिन निर्माता","hero1":"प्राइवेट लेबल क्रिएटिन और","hero2":"थोक आपूर्ति",
  "heroSub":"Crest Creatine ब्रांड और डिस्ट्रीब्यूटर को क्रिएटिन मोनohydrate गमी, पाउडर और कैप्सूल सोर्स करने में मदद करता है — OEM / प्राइवेट लेबल और मानक थोक कार्टन, सैंपल, COA सपोर्ट और 24 घंटे में कोट।",
  "ctaOem":"OEM / प्राइवेट लेबल","ctaWholesale":"थोक",
  "trustTag":"पार्टनर हमें क्यों चुनते हैं","trustTitle":"B2B क्रिएटिन सोर्सिंग के लिए बनाया गया",
  "trustSub":"स्पष्ट MOQ, सैंपल-फर्स्ट OEM, दस्तावेज़ और तेज़ कोट — बिना रिटेल कार्ट।",
  "dshea":"डायटरी सप्लीमेंट सूचना: उत्पाद DSHEA के अंतर्गत डायटरी सप्लीमेंट के रूप में हैं। कथन FDA द्वारा मूल्यांकित नहीं। किसी रोग का निदान, उपचार, इलाज या रोकथाम हेतु नहीं।",
},
"bn": {
  "title":"প্রাইভেট লেবেল ক্রিয়েটিন OEM ও হোলসেল | Crest Creatine",
  "description":"B2B ক্রিয়েটিন প্রস্তুতকারক — OEM / প্রাইভেট লেবেল গামি, পাউডার ও ক্যাপসুল, হোলসেল কার্টন মূল্য, নমুনা, COA ও তৃতীয় পক্ষের পরীক্ষা। ২৪ ঘণ্টায় কোট।",
  "tagline":"B2B ক্রিয়েটিন প্রস্তুতকারক","hero1":"প্রাইভেট লেবেল ক্রিয়েটিন ও","hero2":"হোলসেল সরবরাহ",
  "heroSub":"Crest Creatine ব্র্যান্ড ও ডিস্ট্রিবিউটরকে ক্রিয়েটিন মনোহাইড্রেট গামি, পাউডার ও ক্যাপসুল সোর্স করতে সাহায্য করে — OEM / প্রাইভেট লেবেল ও স্ট্যান্ডার্ড হোলসেল কার্টন, নমুনা, COA সাপোর্ট এবং ২৪ ঘণ্টায় কোট।",
  "ctaOem":"OEM / প্রাইভেট লেবেল","ctaWholesale":"হোলসেল",
  "trustTag":"পার্টনাররা কেন আমাদের বেছে নেয়","trustTitle":"B2B ক্রিয়েটিন সোর্সিংয়ের জন্য তৈরি",
  "trustSub":"স্পষ্ট MOQ, স্যাম্পল-ফার্স্ট OEM, ডকুমেন্টেশন ও দ্রুত কোট — রিটেইল কার্ট ছাড়া।",
  "dshea":"ডায়েটারি সাপ্লিমেন্ট নোটিশ: পণ্য DSHEA-এর অধীনে ডায়েটারি সাপ্লিমেন্ট হিসেবে উদ্দিষ্ট। বিবৃতি FDA দ্বারা মূল্যায়িত নয়। কোনো রোগ নির্ণয়, চিকিৎসা, নিরাময় বা প্রতিরোধের জন্য নয়।",
},
"ur": {
  "title":"پرائیویٹ لیبل کریٹائن OEM اور ہول سیل | Crest Creatine",
  "description":"B2B کریٹائن مینوفیکچرر — OEM / پرائیویٹ لیبل گمیز، پاؤڈر اور کیپسولز، ہول سیل کارٹن قیمتیں، سیمپل، COA اور تھرڈ پارٹی ٹیسٹنگ۔ 24 گھنٹوں میں کوٹ۔",
  "tagline":"B2B کریٹائن مینوفیکچرر","hero1":"پرائیویٹ لیبل کریٹائن اور","hero2":"ہول سیل سپلائی",
  "heroSub":"Crest Creatine برانڈز اور ڈسٹری بیوٹرز کو کریٹائن مونو ہائیڈریٹ گمیز، پاؤڈر اور کیپسولز سورس کرنے میں مدد دیتا ہے — OEM / پرائیویٹ لیبل اور معیاری ہول سیل کارٹنز، سیمپل، COA سپورٹ اور 24 گھنٹوں میں کوٹ۔",
  "ctaOem":"OEM / پرائیویٹ لیبل","ctaWholesale":"ہول سیل",
  "trustTag":"پارٹنرز ہمیں کیوں چنتے ہیں","trustTitle":"B2B کریٹائن سورسنگ کے لیے بنایا گیا",
  "trustSub":"واضح MOQ، سیمپل فرسٹ OEM، دستاویزات اور تیز کوٹ — ریٹیل کارٹ کے بغیر۔",
  "dshea":"ڈائٹری سپلیمنٹ نوٹس: مصنوعات DSHEA کے تحت ڈائٹری سپلیمنٹس کے طور پر ہیں۔ بیانات FDA نے جانچے نہیں۔ کسی بیماری کی تشخیص، علاج، شفا یا روک تھام کے لیے نہیں۔",
},
"th": {
  "title":"ครีเอทีนไพรเวทเลเบล OEM และขายส่ง | Crest Creatine",
  "description":"ผู้ผลิตครีเอทีน B2B — กัมมี่ ผง และแคปซูล OEM / ไพรเวทเลเบล ราคาลังขายส่ง ตัวอย่าง COA และการทดสอบบุคคลที่สาม ใบเสนอราคาภายใน 24 ชั่วโมง",
  "tagline":"ผู้ผลิตครีเอทีน B2B","hero1":"ครีเอทีนไพรเวทเลเบล และ","hero2":"การจัดหาขายส่ง",
  "heroSub":"Crest Creatine ช่วยแบรนด์และผู้จัดจำหน่ายจัดหาครีเอทีนโมโนไฮเดรตกัมมี่ ผง และแคปซูล — โปรแกรม OEM / ไพรเวทเลเบล และลังขายส่งมาตรฐาน พร้อมตัวอย่าง รองรับ COA และใบเสนอราคาภายใน 24 ชั่วโมง",
  "ctaOem":"OEM / ไพรเวทเลเบล","ctaWholesale":"ขายส่ง",
  "trustTag":"ทำไมพาร์ทเนอร์เลือกเรา","trustTitle":"ออกแบบมาเพื่อการจัดหาครีเอทีน B2B",
  "trustSub":"MOQ ชัดเจน OEM เริ่มจากตัวอย่าง เอกสาร และใบเสนอราคาเร็ว — ไม่มีตะกร้าขายปลีก",
  "dshea":"ประกาศอาหารเสริม: ผลิตภัณฑ์มีเจตนาเป็นอาหารเสริมภายใต้ DSHEA คำกล่าวไม่ได้ผ่านการประเมินโดย FDA ไม่ได้มีเจตนาเพื่อวินิจฉัย รักษา รักษาให้หาย หรือป้องกันโรคใดๆ",
},
}

# Expand remaining with structured fields derived from en + overrides
for loc, ov in remaining.items():
    base = dict(HOME["en"])
    # Translate shared structural fields using locale-appropriate versions
    # Keep product numbers; localize titles/CTAs via ov + sensible defaults from similar languages
    base.update(ov)
    # Fill trust/buy/prod/steps/faq with localized approximations based on locale family
    # For locales not fully expanded above, build from Spanish/EN patterns with ov hero
    if "trustItems" not in ov:
        # create localized trust items from EN keys with locale labels embedded in ov when possible
        # Use EN structure with translated titles from a mini dict
        pass
    HOME[loc] = base

# Now flesh out missing structured fields for remaining locales with proper translations
STRUCT = {
"ar": {
  "trustItems":[
    {"title":"حد أدنى مرن","description":"حدود تجريبية لبرامج العلامة الخاصة؛ حدود صناديق لـ SKU الجملة.","icon":"tabler:package"},
    {"title":"عينات متاحة","description":"اعتماد الصيغة والنكهة والتغليف قبل الإنتاج الكمي.","icon":"tabler:flask"},
    {"title":"COA والاختبارات","description":"مسارات COA لكل دفعة ودعم اختبارات طرف ثالث للعلامات الموجهة للولايات المتحدة.","icon":"tabler:file-certificate"},
    {"title":"عرض خلال 24 ساعة","description":"رد في أيام العمل على طلبات OEM وقوائم أسعار الجملة.","icon":"tabler:clock"},
  ],
  "buyTag":"طريقتان للشراء","buyTitle":"OEM / علامة خاصة أو جملة",
  "buyOemTitle":"OEM / علامة خاصة","buyOemDesc":"علكات ومسحوق وكبسولات كرياتين مخصصة — نكهات وتغليف وعلامة ووثائق امتثال. مثالي لإطلاق أو توسيع SKU كرياتين.",
  "buyWhTitle":"الجملة","buyWhDesc":"مواصفات صناديق قياسية للموزّعين والصالات والتجار والبائعين عبر الإنترنت. اطلب قائمة أسعار وإرشاد الحساب.",
  "prodTag":"برامج المنتجات","prodTitle":"علكات ومسحوق وكبسولات","prodSub":"تكوينات ابتدائية للعلامة الخاصة والجملة — الجرعة والتعبئة والحد الأدنى تُؤكد عند العرض.",
  "gummiesTitle":"علكات الكرياتين","gummiesDesc":"الصيغة الرئيسية: ~1,000 ملغ/علكة أو ~5 غ عبر 3 علكات؛ عبوات 60/90؛ خيارات بكتين؛ تطوير نكهات.","gummiesCta":"عرض العلكات",
  "powderTitle":"مسحوق الكرياتين","powderDesc":"علب أو أكياس 300 غ / 500 غ / 1 كغ؛ براميل 25 كغ؛ خيارات شبكة؛ بدون نكهة + نكهات.","powderCta":"عرض المسحوق",
  "capsTitle":"كبسولات الكرياتين","capsDesc":"حوالي 750–1,000 ملغ/كبسولة؛ أعداد 60–240؛ جيلاتين أو HPMC أو بولولان حسب البرنامج.","capsCta":"عرض الكبسولات",
  "stepsTitle":"كيف يعمل التوريد",
  "steps":[
    {"title":"أخبرنا بقناتك","description":"مشروع OEM أو حساب جملة — نوع المشتري والحجم وبلد الشحن.","icon":"tabler:message"},
    {"title":"احصل على الحد الأدنى والعينات","description":"نرد بحدود متدرجة وخيارات عينات ووثائق لسوقك.","icon":"tabler:package"},
    {"title":"اعتمد وأنتج","description":"ثبّت الصيغة والنكهة والتغليف (OEM) أو SKU الصناديق (جملة)، ثم جدول الإنتاج.","icon":"tabler:circle-check-filled"},
    {"title":"اشحن وأعد الطلب","description":"دعم تعبئة التصدير ومسارات إعادة الطلب الشهرية.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"أسئلة شائعة حول OEM وجملة الكرياتين",
  "faqs":[
    {"title":"هل تقدمون OEM / علامة خاصة والجملة؟","description":"نعم. <strong>OEM / علامة خاصة</strong> للعلامات التي تحتاج صيغاً ونكهات وتغليفاً مخصصاً؛ <strong>الجملة</strong> للموزّعين والصالات والبائعين عبر الإنترنت الذين يشترون SKU صناديق قياسية."},
    {"title":"ما أشكال الكرياتين التي يمكن تعليمها كعلامة خاصة؟","description":"كرياتين مونوهيدرات <strong>علكات</strong> و<strong>مسحوق</strong> و<strong>كبسولات</strong>، مع نكهات وحصص وتغليف علامة حسب الحد الأدنى."},
    {"title":"هل يمكنني الحصول على عينات قبل طلب كبير؟","description":"نعم. يُفضل البدء بالعينة لمراجعة النكهة والقوام والملصق. اطلب عبر نموذج الاستفسار."},
    {"title":"هل توفرون COA أو اختبارات طرف ثالث؟","description":"ندعم وثائق على مستوى الدفعة ومسارات اختبارات طرف ثالث لمشتري المكملات. التفاصيل عند العرض."},
    {"title":"هل هذا متجر تجزئة للمستهلكين في الولايات المتحدة؟","description":"لا. Crest Creatine موقع <strong>B2B</strong> لـ OEM والجملة للعلامات وشركاء القناة — وليس متجر DTC."},
  ],
  "ctaTitle":"هل أنت مستعد لعرض سعر المصنع؟","ctaSub":"شارك نوع المشتري والاحتياج والحجم — نرد خلال 24 ساعة في أيام العمل.",
  "ctaForm":"افتح نموذج الاستفسار","ctaProducts":"برامج المنتجات","ctaOemDetails":"تفاصيل OEM","ctaWhDetails":"تفاصيل الجملة",
},
}

# Apply STRUCT for ar and create similar for other remaining locales more efficiently
for loc, s in STRUCT.items():
    HOME[loc].update(s)

# For locales that still have EN trustItems (fr, de, pt, ja, ko, vi, id, ru, hi, bn, ur, th), fill with proper translations
FILL = {
"fr": {
  "trustItems":[
    {"title":"MOQ flexible","description":"MOQ d’essai pour pilotes marque blanche ; MOQ carton pour SKU gros.","icon":"tabler:package"},
    {"title":"Échantillons disponibles","description":"Validez formule, arôme et emballage avant production en volume.","icon":"tabler:flask"},
    {"title":"COA & tests","description":"Parcours COA par lot et tests tiers pour marques destinées aux USA.","icon":"tabler:file-certificate"},
    {"title":"Devis 24 h","description":"Réponse en jours ouvrés aux RFQ OEM et listes de prix gros.","icon":"tabler:clock"},
  ],
  "buyTag":"Deux façons d’acheter","buyTitle":"OEM / Marque blanche ou Gros",
  "buyOemTitle":"OEM / Marque blanche","buyOemDesc":"Gummies, poudre et capsules de créatine sur mesure — arômes, emballage, branding et documents de conformité. Idéal pour lancer ou élargir un SKU créatine.",
  "buyWhTitle":"Gros","buyWhDesc":"Specs carton standard pour distributeurs, salles, retailers et vendeurs en ligne. Demandez tarif et guidance de compte.",
  "prodTag":"Programmes produits","prodTitle":"Gummies, poudre & capsules","prodSub":"Configurations de départ pour marque blanche et gros — dose, pack et MOQ confirmés au devis.",
  "gummiesTitle":"Gummies créatine","gummiesDesc":"Format phare : ~1 000 mg/gummy ou ~5 g sur 3 gummies ; flacons 60/90 ; options pectine ; développement d’arômes.","gummiesCta":"Voir gummies",
  "powderTitle":"Créatine en poudre","powderDesc":"Pots ou pouches 300 g / 500 g / 1 kg ; fûts 25 kg ; options de mesh ; nature + arômes.","powderCta":"Voir poudre",
  "capsTitle":"Capsules de créatine","capsDesc":"Env. 750–1 000 mg/capsule ; comptes 60–240 ; gélatine, HPMC ou pullulan selon programme.","capsCta":"Voir capsules",
  "stepsTitle":"Comment se déroule le sourcing",
  "steps":[
    {"title":"Indiquez votre canal","description":"Projet OEM ou compte gros — type d’acheteur, volume et pays de livraison.","icon":"tabler:message"},
    {"title":"Obtenez MOQ & échantillons","description":"Nous répondons avec MOQ échelonnés, options d’échantillon et documentation.","icon":"tabler:package"},
    {"title":"Validez & produisez","description":"Verrouillez formule, arôme et emballage (OEM) ou SKU carton (gros), puis planifiez la production.","icon":"tabler:circle-check-filled"},
    {"title":"Expédiez & recommandez","description":"Support emballage export et réassort mensuel.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"FAQ OEM & gros créatine",
  "faqs":[
    {"title":"Proposez-vous OEM / marque blanche et gros ?","description":"Oui. <strong>OEM / marque blanche</strong> pour les marques ayant besoin de formules, arômes et emballages sur mesure ; <strong>gros</strong> pour distributeurs, salles et vendeurs en ligne achetant des SKU carton standard."},
    {"title":"Quels formats de créatine pouvez-vous marque blanche ?","description":"Créatine monohydrate en <strong>gummies</strong>, <strong>poudre</strong> et <strong>capsules</strong>, avec arômes, portions et emballage de marque selon MOQ."},
    {"title":"Puis-je obtenir des échantillons avant un gros ordre ?","description":"Oui. L’échantillon d’abord est recommandé pour goût, texture et étiquette. Demandez via le formulaire."},
    {"title":"Fournissez-vous COA ou tests tiers ?","description":"Nous supportons la documentation par lot et des parcours de tests tiers pour acheteurs de compléments. Détails au devis."},
    {"title":"Est-ce un magasin retail US pour consommateurs ?","description":"Non. Crest Creatine est un site <strong>B2B</strong> OEM et gros pour marques et partenaires de canal — pas une boutique DTC."},
  ],
  "ctaTitle":"Prêt pour un devis usine ?","ctaSub":"Partagez type d’acheteur, besoin et volume — réponse sous 24 h ouvrées.",
  "ctaForm":"Ouvrir le formulaire","ctaProducts":"Programmes produits","ctaOemDetails":"Détails OEM","ctaWhDetails":"Détails gros",
},
"de": {
  "trustItems":[
    {"title":"Flexibles MOQ","description":"Probe-MOQs für Private-Label-Piloten; Karton-MOQs für Großhandels-SKUs.","icon":"tabler:package"},
    {"title":"Muster verfügbar","description":"Formel, Geschmack und Verpackung vor der Mengenproduktion freigeben.","icon":"tabler:flask"},
    {"title":"COA & Tests","description":"Losbezogene COA-Pfade und Drittlabor-Support für US-Marken.","icon":"tabler:file-certificate"},
    {"title":"Angebot in 24 h","description":"Werktagsantwort auf OEM-RFQs und Großhandelspreislisten.","icon":"tabler:clock"},
  ],
  "buyTag":"Zwei Kaufwege","buyTitle":"OEM / Private Label oder Großhandel",
  "buyOemTitle":"OEM / Private Label","buyOemDesc":"Individuelle Creatin-Gummies, -Pulver und -Kapseln — Geschmack, Verpackung, Branding und Compliance-Dokumente. Ideal für Marken, die ein Creatin-SKU launchen oder erweitern.",
  "buyWhTitle":"Großhandel","buyWhDesc":"Standard-Kartonspezifikationen für Distributoren, Studios, Retailer und Online-Händler. Preisliste und Kontoführung anfragen.",
  "prodTag":"Produktprogramme","prodTitle":"Gummies, Pulver & Kapseln","prodSub":"Startkonfigurationen für Private Label und Großhandel — Dosis, Pack und MOQ werden im Angebot bestätigt.",
  "gummiesTitle":"Creatin-Gummies","gummiesDesc":"Hero-Format: ~1.000 mg/Gummy oder ~5 g über 3 Gummies; 60/90-Flaschen; Pektin-Optionen; Geschmacksentwicklung.","gummiesCta":"Gummies ansehen",
  "powderTitle":"Creatin-Pulver","powderDesc":"300 g / 500 g / 1 kg Tubs oder Pouches; 25-kg-Fässer; Mesh-Optionen; unflavored + Flavors.","powderCta":"Pulver ansehen",
  "capsTitle":"Creatin-Kapseln","capsDesc":"Ca. 750–1.000 mg/Kapsel; 60–240 Stück; Gelatine, HPMC oder Pullulan je nach Programm.","capsCta":"Kapseln ansehen",
  "stepsTitle":"So läuft das Sourcing",
  "steps":[
    {"title":"Kanal nennen","description":"OEM-Projekt oder Großhandelskonto — Käufertyp, Volumen und Zielland.","icon":"tabler:message"},
    {"title":"MOQ & Muster erhalten","description":"Antwort mit gestaffelten MOQs, Musteroptionen und Dokumentation.","icon":"tabler:package"},
    {"title":"Freigeben & produzieren","description":"Formel, Geschmack und Verpackung (OEM) oder Karton-SKUs (Großhandel) fixieren, dann Produktion planen.","icon":"tabler:circle-check-filled"},
    {"title":"Versenden & nachbestellen","description":"Exportverpackung und monatliche Nachbestellpfade.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"FAQ Creatin OEM & Großhandel",
  "faqs":[
    {"title":"Bieten Sie OEM / Private Label und Großhandel an?","description":"Ja. <strong>OEM / Private Label</strong> für Marken mit individuellen Formeln, Geschmäckern und Verpackungen; <strong>Großhandel</strong> für Distributoren, Studios und Online-Händler mit Standard-Karton-SKUs."},
    {"title":"Welche Creatin-Formate können Sie private-labeln?","description":"Creatin-Monohydrat als <strong>Gummies</strong>, <strong>Pulver</strong> und <strong>Kapseln</strong>, mit Geschmack, Portionen und Markenverpackung je nach MOQ."},
    {"title":"Kann ich vor einer Großbestellung Muster erhalten?","description":"Ja. Sample-first wird für Geschmack, Textur und Etikett empfohlen. Über das Anfrageformular anfragen."},
    {"title":"Stellen Sie COA oder Drittlabor-Tests bereit?","description":"Wir unterstützen losbezogene Dokumentation und Drittlabor-Pfade für Nahrungsergänzungskäufer. Details im Angebot."},
    {"title":"Ist das ein US-Verbraucher-Retailshop?","description":"Nein. Crest Creatine ist eine <strong>B2B</strong>-OEM- und Großhandelsseite für Marken und Kanalpartner — kein DTC-Shop."},
  ],
  "ctaTitle":"Bereit für ein Fabrikangebot?","ctaSub":"Teilen Sie Käufertyp, Bedarf und Volumen — Antwort an Werktagen innerhalb von 24 Stunden.",
  "ctaForm":"Anfrageformular öffnen","ctaProducts":"Produktprogramme","ctaOemDetails":"OEM-Details","ctaWhDetails":"Großhandelsdetails",
},
}

for loc, s in FILL.items():
    HOME[loc].update(s)

# For remaining locales that still have EN trust items, apply a generic localized fill
# Check which still need filling
need = []
for loc in LOCALES:
    if HOME[loc]["trustItems"][0]["title"] == HOME["en"]["trustItems"][0]["title"] and loc != "en":
        need.append(loc)
print("Still EN trust:", need)

# Write a compact fill for remaining: pt,ja,ko,vi,id,ru,hi,bn,ur,th
# Load from external JSON file created inline
