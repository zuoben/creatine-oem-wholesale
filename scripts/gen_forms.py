#!/usr/bin/env python3
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
            key = k if str(k).isidentifier() and "-" not in str(k) else json.dumps(k)
            parts.append(f"{pad2}{key}: {ser(v, indent+2)},")
        return "{\n" + "\n".join(parts) + f"\n{pad}}}"
    return "null"

def lk(loc):
    return f"'{loc}'" if "-" in loc else loc

def L(row):
    for loc in LOCALES:
        if loc not in row:
            raise KeyError(f"missing {loc}")
    return row

F = {
"iAmA": L({"en":"I am a","zh-tw":"我是","hi":"मैं हूँ","es":"Soy","ar":"أنا","fr":"Je suis","bn":"আমি","pt":"Sou","ru":"Я","ur":"میں ہوں","id":"Saya adalah","de":"Ich bin","ja":"私は","ko":"저는","vi":"Tôi là","th":"ฉันเป็น"}),
"lookingFor": L({"en":"I'm looking for","zh-tw":"我想了解","hi":"मुझे चाहिए","es":"Busco","ar":"أبحث عن","fr":"Je cherche","bn":"আমি খুঁজছি","pt":"Procuro","ru":"Мне нужно","ur":"میں تلاش کر رہا/رہی ہوں","id":"Saya mencari","de":"Ich suche","ja":"ご用件","ko":"문의 유형","vi":"Tôi cần","th":"ฉันต้องการ"}),
"volume": L({"en":"Expected volume","zh-tw":"預估量","hi":"अपेक्षित मात्रा","es":"Volumen esperado","ar":"الحجم المتوقع","fr":"Volume prévu","bn":"প্রত্যাশিত পরিমাণ","pt":"Volume esperado","ru":"Ожидаемый объём","ur":"متوقع مقدار","id":"Volume yang diharapkan","de":"Erwartetes Volumen","ja":"想定数量","ko":"예상 물량","vi":"Khối lượng dự kiến","th":"ปริมาณที่คาดหวัง"}),
"name": L({"en":"Name","zh-tw":"姓名","hi":"नाम","es":"Nombre","ar":"الاسم","fr":"Nom","bn":"নাম","pt":"Nome","ru":"Имя","ur":"نام","id":"Nama","de":"Name","ja":"お名前","ko":"이름","vi":"Họ tên","th":"ชื่อ"}),
"email": L({"en":"Email","zh-tw":"電子郵件","hi":"ईमेल","es":"Correo","ar":"البريد الإلكتروني","fr":"E-mail","bn":"ইমেইল","pt":"E-mail","ru":"Эл. почта","ur":"ای میل","id":"Email","de":"E-Mail","ja":"メール","ko":"이메일","vi":"Email","th":"อีเมล"}),
"message": L({"en":"Message","zh-tw":"訊息","hi":"संदेश","es":"Mensaje","ar":"الرسالة","fr":"Message","bn":"বার্তা","pt":"Mensagem","ru":"Сообщение","ur":"پیغام","id":"Pesan","de":"Nachricht","ja":"メッセージ","ko":"메시지","vi":"Tin nhắn","th":"ข้อความ"}),
"select": L({"en":"Select…","zh-tw":"請選擇…","hi":"चुनें…","es":"Seleccionar…","ar":"اختر…","fr":"Sélectionner…","bn":"নির্বাচন…","pt":"Selecionar…","ru":"Выберите…","ur":"منتخب کریں…","id":"Pilih…","de":"Auswählen…","ja":"選択…","ko":"선택…","vi":"Chọn…","th":"เลือก…"}),
"brand": L({"en":"Brand","zh-tw":"品牌","hi":"ब्रांड","es":"Marca","ar":"علامة تجارية","fr":"Marque","bn":"ব্র্যান্ড","pt":"Marca","ru":"Бренд","ur":"برانڈ","id":"Merek","de":"Marke","ja":"ブランド","ko":"브랜드","vi":"Thương hiệu","th":"แบรนด์"}),
"distributor": L({"en":"Distributor","zh-tw":"經銷商","hi":"वितरक","es":"Distribuidor","ar":"موزّع","fr":"Distributeur","bn":"ডিস্ট্রিবিউটর","pt":"Distribuidor","ru":"Дистрибьютор","ur":"ڈسٹری بیوٹر","id":"Distributor","de":"Distributor","ja":"代理店","ko":"유통사","vi":"Nhà phân phối","th":"ตัวแทนจำหน่าย"}),
"gym": L({"en":"Gym or retailer","zh-tw":"健身房或零售商","hi":"जिम या रिटेलर","es":"Gimnasio o minorista","ar":"صالة رياضية أو تاجر تجزئة","fr":"Salle de sport ou détaillant","bn":"জিম বা খুচরা বিক্রেতা","pt":"Academia ou varejista","ru":"Зал или ритейл","ur":"جم یا ریٹیلر","id":"Gym atau retailer","de":"Studio oder Einzelhandel","ja":"ジム／小売","ko":"헬스장 또는 리테일","vi":"Phòng gym hoặc bán lẻ","th":"ยิมหรือร้านค้าปลีก"}),
"online": L({"en":"Online seller","zh-tw":"電商賣家","hi":"ऑनलाइन विक्रेता","es":"Vendedor online","ar":"بائع عبر الإنترنت","fr":"Vendeur en ligne","bn":"অনলাইন বিক্রেতা","pt":"Vendedor online","ru":"Онлайн-продавец","ur":"آن لائن فروخت کنندہ","id":"Penjual online","de":"Online-Händler","ja":"ネット販売","ko":"온라인 판매자","vi":"Người bán online","th":"ผู้ขายออนไลน์"}),
"other": L({"en":"Other","zh-tw":"其他","hi":"अन्य","es":"Otro","ar":"أخرى","fr":"Autre","bn":"অন্যান্য","pt":"Outro","ru":"Другое","ur":"دیگر","id":"Lainnya","de":"Sonstiges","ja":"その他","ko":"기타","vi":"Khác","th":"อื่นๆ"}),
"oemOpt": L({"en":"OEM / Private label","zh-tw":"OEM／私標","hi":"OEM / प्राइवेट लेबल","es":"OEM / marca privada","ar":"OEM / علامة خاصة","fr":"OEM / marque blanche","bn":"OEM / প্রাইভেট লেবেল","pt":"OEM / private label","ru":"OEM / private label","ur":"OEM / پرائیویٹ لیبل","id":"OEM / private label","de":"OEM / Private Label","ja":"OEM／プライベートラベル","ko":"OEM / 프라이빗 라벨","vi":"OEM / nhãn riêng","th":"OEM / 하이프갓"}),
"wholesaleOpt": L({"en":"Wholesale pricing","zh-tw":"批發報價","hi":"थोक मूल्य","es":"Precios mayoreo","ar":"أسعار الجملة","fr":"Tarifs gros","bn":"হোলসেল মূল্য","pt":"Preços atacado","ru":"Оптовые цены","ur":"ہول سیل قیمت","id":"Harga grosir","de":"Großhandelspreise","ja":"卸売価格","ko":"도매 가격","vi":"Giá sỉ","th":"ราคาขายส่ง"}),
"sampleOpt": L({"en":"Sample","zh-tw":"樣品","hi":"सैंपल","es":"Muestra","ar":"عينة","fr":"Échantillon","bn":"নমুনা","pt":"Amostra","ru":"Образец","ur":"سیمپل","id":"Sampel","de":"Muster","ja":"サンプル","ko":"샘플","vi":"Mẫu","th":"ตัวอย่าง"}),
"bulkPowder": L({"en":"Bulk powder","zh-tw":"散裝粉","hi":"बल्क पाउडर","es":"Polvo a granel","ar":"مسحوق بالجملة","fr":"Poudre en vrac","bn":"বাল্ক পাউডার","pt":"Pó a granel","ru":"Порошок оптом","ur":"بلک پاؤڈر","id":"Bubuk curah","de":"Bulk-Pulver","ja":"バルク粉末","ko":"벌크 파우더","vi":"Bột số lượng lớn","th":"ผงปริมาณมาก"}),
"bulkGummies": L({"en":"Bulk gummies","zh-tw":"散裝軟糖","hi":"बल्क गमी","es":"Gomitas a granel","ar":"علكات بالجملة","fr":"Gummies en vrac","bn":"বাল্ক গামি","pt":"Gummies a granel","ru":"Жевательные оптом","ur":"بلک گمیز","id":"Gummy curah","de":"Bulk-Gummies","ja":"バルク・グミ","ko":"벌크 구미","vi":"Kẹo dẻo số lượng lớn","th":"กัมมี่ปริมาณมาก"}),
"trialMoq": L({"en":"Trial MOQ","zh-tw":"試產 MOQ","hi":"ट्रायल MOQ","es":"MOQ de prueba","ar":"حد أدنى تجريبي","fr":"MOQ d’essai","bn":"ট্রায়াল MOQ","pt":"MOQ de teste","ru":"Пробный MOQ","ur":"ٹرائل MOQ","id":"MOQ uji coba","de":"Probe-MOQ","ja":"トライアルMOQ","ko":"시험 MOQ","vi":"MOQ thử","th":"MOQ ทดลอง"}),
"container": L({"en":"Container / pallet","zh-tw":"貨櫃／棧板","hi":"कंटेनर / पैलेट","es":"Contenedor / pallet","ar":"حاوية / منصة","fr":"Conteneur / palette","bn":"কন্টেইনার / প্যালেট","pt":"Contêiner / pallet","ru":"Контейнер / паллет","ur":"کنٹینر / پیلیٹ","id":"Kontainer / palet","de":"Container / Palette","ja":"コンテナ／パレット","ko":"컨테이너 / 팔레트","vi":"Container / pallet","th":"ตู้คอนเทนเนอร์ / พาเลท"}),
"monthly": L({"en":"Ongoing monthly","zh-tw":"每月持續","hi":"मासिक निरंतर","es":"Mensual continuo","ar":"شهري مستمر","fr":"Mensuel récurrent","bn":"মাসিক চলমান","pt":"Mensal contínuo","ru":"Ежемесячно","ur":"ماہانہ جاری","id":"Bulanan berkelanjutan","de":"Laufend monatlich","ja":"毎月継続","ko":"월간 지속","vi":"Hàng tháng liên tục","th":"รายเดือนต่อเนื่อง"}),
"namePh": L({"en":"Your name","zh-tw":"您的姓名","hi":"आपका नाम","es":"Su nombre","ar":"اسمك","fr":"Votre nom","bn":"আপনার নাম","pt":"Seu nome","ru":"Ваше имя","ur":"آپ کا نام","id":"Nama Anda","de":"Ihr Name","ja":"お名前","ko":"성함","vi":"Tên của bạn","th":"ชื่อของคุณ"}),
"emailPh": L({"en":"you@company.com","zh-tw":"you@company.com","hi":"you@company.com","es":"usted@empresa.com","ar":"you@company.com","fr":"vous@entreprise.com","bn":"you@company.com","pt":"voce@empresa.com","ru":"you@company.com","ur":"you@company.com","id":"anda@perusahaan.com","de":"sie@firma.com","ja":"you@company.com","ko":"you@company.com","vi":"ban@congty.com","th":"you@company.com"}),
"msgPh": L({
  "en":"SKU interest (powder / gummies), flavor, packaging, ship-to country, timeline, certifications needed…",
  "zh-tw":"感興趣的 SKU（粉／軟糖）、口味、包裝、目的地國家、時程、所需認證…",
  "hi":"SKU रुचि (पाउडर / गमी), फ्लेवर, पैकेजिंग, शिप-टू देश, समयसीमा, आवश्यक प्रमाणपत्र…",
  "es":"SKU de interés (polvo / gomitas), sabor, empaque, país de envío, plazos, certificaciones…",
  "ar":"الاهتمام بالمنتج (مسحوق / علكات)، النكهة، التغليف، بلد الشحن، الجدول الزمني، الشهادات المطلوبة…",
  "fr":"SKU d’intérêt (poudre / gummies), arôme, emballage, pays de livraison, délai, certifications…",
  "bn":"SKU আগ্রহ (পাউডার / গামি), ফ্লেভার, প্যাকেজিং, শিপ-টু দেশ, সময়সীমা, প্রয়োজনীয় সার্টিফিকেশন…",
  "pt":"SKU de interesse (pó / gummies), sabor, embalagem, país de destino, prazo, certificações…",
  "ru":"Интерес к SKU (порошок / жевательные), вкус, упаковка, страна доставки, сроки, сертификаты…",
  "ur":"SKU دلچسپی (پاؤڈر / گمیز)، فلیور، پیکجنگ، شپ ٹو ملک، ٹائم لائن، سرٹیفیکیشنز…",
  "id":"Minat SKU (bubuk / gummy), rasa, kemasan, negara tujuan, timeline, sertifikasi…",
  "de":"SKU-Interesse (Pulver / Gummies), Geschmack, Verpackung, Zielland, Zeitplan, Zertifikate…",
  "ja":"ご関心SKU（粉末／グミ）、フレーバー、包装、出荷先国、希望時期、必要な認証…",
  "ko":"관심 SKU(파우더/구미), 맛, 포장, 배송국, 일정, 필요 인증…",
  "vi":"SKU quan tâm (bột / kẹo dẻo), hương vị, bao bì, quốc gia giao hàng, thời gian, chứng nhận…",
  "th":"SKU ที่สนใจ (ผง / กัมมี่) รสชาติ บรรจุภัณฑ์ ประเทศจัดส่ง ไทม์ไลน์ การรับรองที่ต้องการ…",
}),
"disclaimer": L({
  "en":"I agree to be contacted by Crest Creatine regarding OEM, private label, and wholesale inquiries.",
  "zh-tw":"我同意 Crest Creatine 就 OEM、私標與批發詢價與我聯絡。",
  "hi":"मैं OEM, प्राइवेट लेबल और थोक पूछताछ के लिए Crest Creatine से संपर्क स्वीकार करता/करती हूँ।",
  "es":"Acepto que Crest Creatine me contacte sobre consultas OEM, marca privada y mayoreo.",
  "ar":"أوافق على تواصل Crest Creatine معي بخصوص استفسارات OEM والعلامة الخاصة والجملة.",
  "fr":"J’accepte d’être contacté(e) par Crest Creatine pour des demandes OEM, marque blanche et gros.",
  "bn":"আমি OEM, প্রাইভেট লেবেল ও হোলসেল অনুসন্ধান বিষয়ে Crest Creatine-এর যোগাযোগে সম্মত।",
  "pt":"Concordo em ser contatado(a) pela Crest Creatine sobre consultas OEM, private label e atacado.",
  "ru":"Соглашаюсь на связь с Crest Creatine по запросам OEM, private label и опта.",
  "ur":"میں OEM، پرائیویٹ لیبل اور ہول سیل استفسارات کے بارے میں Crest Creatine سے رابطے پر رضامند ہوں۔",
  "id":"Saya setuju dihubungi Crest Creatine terkait pertanyaan OEM, private label, dan grosir.",
  "de":"Ich stimme zu, dass Crest Creatine mich zu OEM-, Private-Label- und Großhandelsanfragen kontaktiert.",
  "ja":"OEM・プライベートラベル・卸売の問い合わせについてCrest Creatineからの連絡に同意します。",
  "ko":"OEM, 프라이빗 라벨, 도매 문의와 관련하여 Crest Creatine의 연락에 동의합니다.",
  "vi":"Tôi đồng ý để Crest Creatine liên hệ về yêu cầu OEM, nhãn riêng và bán sỉ.",
  "th":"ฉันยินยอมให้ Crest Creatine ติดต่อเกี่ยวกับการสอบถาม OEM ไพรเวทเลเบล และขายส่ง",
}),
"button": L({"en":"Get B2B Quote Now","zh-tw":"立即取得 B2B 報價","hi":"अभी B2B कोट प्राप्त करें","es":"Obtener cotización B2B","ar":"احصل على عرض سعر B2B الآن","fr":"Obtenir un devis B2B","bn":"এখনই B2B কোট নিন","pt":"Obter orçamento B2B","ru":"Получить B2B КП","ur":"ابھی B2B کوٹ حاصل کریں","id":"Dapatkan penawaran B2B","de":"Jetzt B2B-Angebot erhalten","ja":"B2B見積を今すぐ","ko":"지금 B2B 견적 받기","vi":"Nhận báo giá B2B ngay","th":"รับใบเสนอราคา B2B ทันที"}),
"description": L({
  "en":"Tell us your buyer type and volume — we reply with MOQ tiers, sample options, and next steps within 24 hours on working days.",
  "zh-tw":"告訴我們買家類型與量級 — 我們於工作日 24 小時內回覆 MOQ 層級、樣品方案與下一步。",
  "hi":"अपना खरीदार प्रकार और मात्रा बताएं — हम कार्य दिवसों में 24 घंटे में MOQ स्तर, सैंपल विकल्प और अगले चरण भेजते हैं।",
  "es":"Indique tipo de comprador y volumen — respondemos con MOQ, muestras y siguientes pasos en 24 h laborables.",
  "ar":"أخبرنا بنوع المشتري والحجم — نرد بطبقات الحد الأدنى والعينات والخطوات التالية خلال 24 ساعة في أيام العمل.",
  "fr":"Indiquez votre type d’acheteur et le volume — réponse sous 24 h ouvrées avec MOQ, échantillons et prochaines étapes.",
  "bn":"ক্রেতার ধরন ও পরিমাণ জানান — কর্মদিবসে ২৪ ঘণ্টার মধ্যে MOQ স্তর, নমুনা ও পরবর্তী ধাপ জানাই।",
  "pt":"Informe o tipo de comprador e volume — respondemos com MOQ, amostras e próximos passos em até 24 h úteis.",
  "ru":"Укажите тип покупателя и объём — ответим с уровнями MOQ, образцами и следующими шагами в течение 24 часов в рабочие дни.",
  "ur":"اپنا خریدار کی قسم اور مقدار بتائیں — ہم کاروباری دنوں میں 24 گھنٹوں میں MOQ درجات، سیمپل اور اگلے مراحل بھیجتے ہیں۔",
  "id":"Beritahu tipe pembeli dan volume — kami balas dengan tingkatan MOQ, opsi sampel, dan langkah berikutnya dalam 24 jam hari kerja.",
  "de":"Nennen Sie Käufertyp und Volumen — Antwort mit MOQ-Stufen, Mustern und nächsten Schritten innerhalb von 24 Stunden an Werktagen.",
  "ja":"バイヤー種別と数量をお知らせください。営業日24時間以内にMOQ階層・サンプル・次のステップをご返信します。",
  "ko":"구매자 유형과 물량을 알려 주세요. 영업일 기준 24시간 내 MOQ 구간, 샘플 옵션, 다음 단계를 회신합니다.",
  "vi":"Cho chúng tôi biết loại người mua và khối lượng — phản hồi MOQ, mẫu và bước tiếp theo trong 24 giờ làm việc.",
  "th":"บอกประเภทผู้ซื้อและปริมาณ — เราตอบกลับชั้น MOQ ตัวเลือกตัวอย่าง และขั้นตอนถัดไปภายใน 24 ชั่วโมงในวันทำการ",
}),
"close": L({"en":"Close","zh-tw":"關閉","hi":"बंद करें","es":"Cerrar","ar":"إغلاق","fr":"Fermer","bn":"বন্ধ","pt":"Fechar","ru":"Закрыть","ur":"بند کریں","id":"Tutup","de":"Schließen","ja":"閉じる","ko":"닫기","vi":"Đóng","th":"ปิด"}),
"preferChat": L({"en":"Prefer chat?","zh-tw":"想用即時通訊？","hi":"चैट पसंद है?","es":"¿Prefiere chat?","ar":"تفضل الدردشة؟","fr":"Préférez le chat ?","bn":"চ্যাট পছন্দ?","pt":"Prefere chat?","ru":"Предпочитаете чат?","ur":"چیٹ پسند ہے؟","id":"Lebih suka chat?","de":"Lieber chat?","ja":"チャット希望？","ko":"채팅을 원하시나요?","vi":"Thích chat hơn?","th":"ชอบแชท?"}),
"waTitle": L({"en":"Chat on WhatsApp","zh-tw":"WhatsApp 聊聊","hi":"WhatsApp पर चैट","es":"Chatear por WhatsApp","ar":"الدردشة عبر واتساب","fr":"Discuter sur WhatsApp","bn":"WhatsApp-এ চ্যাট","pt":"Conversar no WhatsApp","ru":"Чат в WhatsApp","ur":"WhatsApp پر چیٹ","id":"Chat di WhatsApp","de":"Per WhatsApp chatten","ja":"WhatsAppでチャット","ko":"WhatsApp 채팅","vi":"Chat trên WhatsApp","th":"แชทบน WhatsApp"}),
"waSubtitle": L({
  "en":"Quick details first — factory quote follows in chat.",
  "zh-tw":"先填簡要資料 — 工廠報價在聊天中繼續。",
  "hi":"पहले संक्षिप्त विवरण — फैक्टरी कोट चैट में जारी।",
  "es":"Primero datos rápidos — la cotización de fábrica sigue en el chat.",
  "ar":"تفاصيل سريعة أولاً — عرض المصنع يتابع في الدردشة.",
  "fr":"Détails rapides d’abord — le devis usine suit dans le chat.",
  "bn":"আগে সংক্ষিপ্ত তথ্য — কারখানার কোট চ্যাটে চলবে।",
  "pt":"Detalhes rápidos primeiro — orçamento de fábrica segue no chat.",
  "ru":"Сначала краткие данные — заводское КП продолжим в чате.",
  "ur":"پہلے مختصر تفصیلات — فیکٹری کوٹ چیٹ میں جاری۔",
  "id":"Detail singkat dulu — penawaran pabrik lanjut di chat.",
  "de":"Zuerst Kurzinfos — Fabrikangebot folgt im Chat.",
  "ja":"まず簡単な情報 — 工場見積はチャットで続きます。",
  "ko":"먼저 간단한 정보 — 공장 견적은 채팅에서 이어집니다.",
  "vi":"Thông tin ngắn trước — báo giá nhà máy tiếp tục trên chat.",
  "th":"รายละเอียดสั้นก่อน — ใบเสนอราคาโรงงานต่อในแชท",
}),
"waButton": L({"en":"Continue to WhatsApp","zh-tw":"繼續到 WhatsApp","hi":"WhatsApp पर जारी रखें","es":"Continuar a WhatsApp","ar":"المتابعة إلى واتساب","fr":"Continuer vers WhatsApp","bn":"WhatsApp-এ চালিয়ে যান","pt":"Continuar no WhatsApp","ru":"Перейти в WhatsApp","ur":"WhatsApp پر جاری رکھیں","id":"Lanjut ke WhatsApp","de":"Weiter zu WhatsApp","ja":"WhatsAppへ進む","ko":"WhatsApp으로 계속","vi":"Tiếp tục tới WhatsApp","th":"ไปต่อที่ WhatsApp"}),
"waDesc": L({
  "en":"We save your quote request, then open WhatsApp.",
  "zh-tw":"我們先儲存您的詢價，再開啟 WhatsApp。",
  "hi":"हम आपका कोट अनुरोध सहेजते हैं, फिर WhatsApp खोलते हैं।",
  "es":"Guardamos su solicitud de cotización y abrimos WhatsApp.",
  "ar":"نحفظ طلب عرض السعر ثم نفتح واتساب.",
  "fr":"Nous enregistrons votre demande puis ouvrons WhatsApp.",
  "bn":"আমরা আপনার কোট অনুরোধ সংরক্ষণ করে WhatsApp খুলি।",
  "pt":"Salvamos sua solicitação e abrimos o WhatsApp.",
  "ru":"Сохраняем заявку и открываем WhatsApp.",
  "ur":"ہم آپ کی کوٹ درخواست محفوظ کر کے WhatsApp کھولتے ہیں۔",
  "id":"Kami menyimpan permintaan penawaran, lalu membuka WhatsApp.",
  "de":"Wir speichern Ihre Anfrage und öffnen WhatsApp.",
  "ja":"見積依頼を保存してからWhatsAppを開きます。",
  "ko":"견적 요청을 저장한 뒤 WhatsApp을 엽니다.",
  "vi":"Chúng tôi lưu yêu cầu báo giá rồi mở WhatsApp.",
  "th":"เราบันทึกคำขอใบเสนอราคาแล้วเปิด WhatsApp",
}),
"waDisclaimer": L({
  "en":"You agree we may contact you about this OEM / wholesale inquiry via email or WhatsApp.",
  "zh-tw":"您同意我們可透過電子郵件或 WhatsApp 就此 OEM／批發詢價與您聯絡。",
  "hi":"आप सहमत हैं कि हम इस OEM / थोक पूछताछ के लिए ईमेल या WhatsApp से संपर्क कर सकते हैं।",
  "es":"Acepta que le contactemos sobre esta consulta OEM / mayoreo por correo o WhatsApp.",
  "ar":"توافق على تواصلنا بخصوص استفسار OEM / الجملة عبر البريد أو واتساب.",
  "fr":"Vous acceptez d’être contacté(e) pour cette demande OEM / gros par e-mail ou WhatsApp.",
  "bn":"আপনি সম্মত যে আমরা এই OEM / হোলসেল অনুসন্ধান বিষয়ে ইমেইল বা WhatsApp-এ যোগাযোগ করতে পারি।",
  "pt":"Você concorda que possamos contatá-lo(a) sobre esta consulta OEM / atacado por e-mail ou WhatsApp.",
  "ru":"Вы соглашаетесь, что мы можем связаться по этому OEM / оптовому запросу по email или WhatsApp.",
  "ur":"آپ رضامند ہیں کہ ہم اس OEM / ہول سیل استفسار کے لیے ای میل یا WhatsApp سے رابطہ کر سکتے ہیں۔",
  "id":"Anda setuju kami dapat menghubungi Anda tentang pertanyaan OEM / grosir ini via email atau WhatsApp.",
  "de":"Sie stimmen zu, dass wir Sie zu dieser OEM-/Großhandelsanfrage per E-Mail oder WhatsApp kontaktieren dürfen.",
  "ja":"本OEM／卸売のお問い合わせについて、メールまたはWhatsAppでの連絡に同意します。",
  "ko":"본 OEM/도매 문의와 관련하여 이메일 또는 WhatsApp으로 연락할 수 있음에 동의합니다.",
  "vi":"Bạn đồng ý chúng tôi có thể liên hệ về yêu cầu OEM / bán sỉ này qua email hoặc WhatsApp.",
  "th":"คุณยินยอมให้เราติดต่อเกี่ยวกับการสอบถาม OEM / ขายส่งนี้ทางอีเมลหรือ WhatsApp",
}),
}

# Fix th oemOpt typo
F["oemOpt"]["th"] = "OEM / ไพรเวทเลเบล"

# Keep option values in English for form matching; labels localized
FORMS = {}
for loc in LOCALES:
    f = {k: v[loc] for k, v in F.items()}
    FORMS[loc] = {
        "inputs": [
            {"type":"select","name":"company","label":f["iAmA"],"placeholder":f["select"],"required":True,"options":[
                {"value":"Brand","label":f["brand"]},
                {"value":"Distributor","label":f["distributor"]},
                {"value":"Gym or retailer","label":f["gym"]},
                {"value":"Online seller","label":f["online"]},
                {"value":"Other","label":f["other"]},
            ]},
            {"type":"select","name":"channel","label":f["lookingFor"],"placeholder":f["select"],"required":True,"options":[
                {"value":"OEM/Private label","label":f["oemOpt"]},
                {"value":"Wholesale pricing","label":f["wholesaleOpt"]},
                {"value":"Sample","label":f["sampleOpt"]},
                {"value":"Bulk powder","label":f["bulkPowder"]},
                {"value":"Bulk gummies","label":f["bulkGummies"]},
            ]},
            {"type":"select","name":"volume","label":f["volume"],"placeholder":f["select"],"required":True,"options":[
                {"value":"Sample","label":f["sampleOpt"]},
                {"value":"Trial MOQ","label":f["trialMoq"]},
                {"value":"Container/pallet","label":f["container"]},
                {"value":"Ongoing monthly","label":f["monthly"]},
            ]},
            {"type":"text","name":"name","label":f["name"],"placeholder":f["namePh"]},
            {"type":"email","name":"email","label":f["email"],"placeholder":f["emailPh"]},
        ],
        "textarea": {"label":f["message"],"name":"message","placeholder":f["msgPh"],"rows":3},
        "disclaimer": {"label":f["disclaimer"]},
        "button": f["button"],
        "description": f["description"],
        "close": f["close"],
        "preferChat": f["preferChat"],
        "waLead": {
            "title": f["waTitle"],
            "subtitle": f["waSubtitle"],
            "button": f["waButton"],
            "description": f["waDesc"],
            "disclaimerLabel": f["waDisclaimer"],
        },
    }

# Write forms.ts with a builder that reconstructs Input types
lines = [
    "import type { Disclaimer, Input, Textarea } from '~/types';",
    "import type { Locale } from './locales';",
    "",
    "type FormCopy = {",
    "  inputs: Input[];",
    "  textarea: Textarea;",
    "  disclaimer: Disclaimer;",
    "  button: string;",
    "  description: string;",
    "  close: string;",
    "  preferChat: string;",
    "  waLead: {",
    "    title: string;",
    "    subtitle: string;",
    "    button: string;",
    "    description: string;",
    "    disclaimerLabel: string;",
    "  };",
    "};",
    "",
    "const FORMS: Record<Locale, FormCopy> = {",
]
for loc in LOCALES:
    lines.append(f"  {lk(loc)}: {ser(FORMS[loc], 2)},")
lines.append("};")
lines.append("")
lines.append("export function getInquiryForm(locale: Locale = 'en') {")
lines.append("  const f = FORMS[locale] ?? FORMS.en;")
lines.append("  const waLead = {")
lines.append("    inputs: f.inputs,")
lines.append("    textarea: { ...f.textarea, rows: 2 },")
lines.append("    disclaimer: { label: f.waLead.disclaimerLabel },")
lines.append("    button: f.waLead.button,")
lines.append("    description: f.waLead.description,")
lines.append("    title: f.waLead.title,")
lines.append("    subtitle: f.waLead.subtitle,")
lines.append("  };")
lines.append("  return {")
lines.append("    inputs: f.inputs,")
lines.append("    textarea: f.textarea,")
lines.append("    disclaimer: f.disclaimer,")
lines.append("    button: f.button,")
lines.append("    description: f.description,")
lines.append("    close: f.close,")
lines.append("    preferChat: f.preferChat,")
lines.append("    waLead,")
lines.append("  };")
lines.append("}")
lines.append("")

(OUT / "forms.ts").write_text("\n".join(lines), encoding="utf-8")
print("Wrote forms.ts", (OUT/"forms.ts").stat().st_size)
