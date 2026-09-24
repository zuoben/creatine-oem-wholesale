#!/usr/bin/env python3
"""Complete HOME dict and write copy-home.ts — continues from gen_copy_home.py logic inline."""
from __future__ import annotations
import json, importlib.util
from pathlib import Path

# Re-exec core of gen_copy_home by importing its HOME via run
# Simpler: rewrite complete file with all locales fully filled.

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

# Load partial from previous run by re-running and capturing via a dump approach
# Instead: load JSON if we dump HOME from part1

# Execute part1 to get HOME into a json file
import subprocess, sys
code = open("/workspace/creatine-oem-wholesale/scripts/gen_copy_home.py").read()
# Append dump at end
code += '''
import json
from pathlib import Path
Path("/tmp/home_partial.json").write_text(json.dumps(HOME, ensure_ascii=False), encoding="utf-8")
print("dumped", len(HOME))
'''
exec(compile(code, "gen_copy_home.py", "exec"), {"__name__":"__main__"})

HOME = json.loads(Path("/tmp/home_partial.json").read_text(encoding="utf-8"))

MORE = {
"pt": {
  "trustItems":[
    {"title":"MOQ flexível","description":"MOQs de teste para pilotos private label; MOQs por caixa para SKUs de atacado.","icon":"tabler:package"},
    {"title":"Amostras disponíveis","description":"Aprove fórmula, sabor e embalagem antes da produção em volume.","icon":"tabler:flask"},
    {"title":"COA e testes","description":"Caminhos de COA por lote e testes de terceiros para marcas com destino aos EUA.","icon":"tabler:file-certificate"},
    {"title":"Orçamento em 24 h","description":"Resposta em dias úteis a RFQs OEM e listas de preços atacado.","icon":"tabler:clock"},
  ],
  "buyTag":"Duas formas de comprar","buyTitle":"OEM / Private label ou Atacado",
  "buyOemTitle":"OEM / Private label","buyOemDesc":"Gummies, pó e cápsulas de creatina sob medida — sabores, embalagem, branding e documentos de conformidade. Ideal para marcas que lançam ou expandem um SKU de creatina.",
  "buyWhTitle":"Atacado","buyWhDesc":"Especificações de caixa padrão para distribuidores, academias, varejistas e vendedores online. Solicite lista de preços e orientação de conta.",
  "prodTag":"Programas de produto","prodTitle":"Gummies, pó e cápsulas","prodSub":"Configurações iniciais para private label e atacado — dose, pack e MOQ confirmados no orçamento.",
  "gummiesTitle":"Gummies de creatina","gummiesDesc":"Formato hero: ~1.000 mg/gummy ou ~5 g em 3 gummies; frascos 60/90; opções de pectina; desenvolvimento de sabores.","gummiesCta":"Ver gummies",
  "powderTitle":"Creatina em pó","powderDesc":"Potes ou pouches 300 g / 500 g / 1 kg; tambores 25 kg; opções de mesh; sem sabor + sabores.","powderCta":"Ver pó",
  "capsTitle":"Cápsulas de creatina","capsDesc":"Aprox. 750–1.000 mg/cápsula; contagens 60–240; gelatina, HPMC ou pullulan conforme programa.","capsCta":"Ver cápsulas",
  "stepsTitle":"Como funciona o sourcing",
  "steps":[
    {"title":"Conte seu canal","description":"Projeto OEM ou conta atacado — tipo de comprador, volume e país de destino.","icon":"tabler:message"},
    {"title":"Obtenha MOQ e amostras","description":"Respondemos com MOQs escalonados, opções de amostra e documentação.","icon":"tabler:package"},
    {"title":"Aprove e produza","description":"Trave fórmula, sabor e embalagem (OEM) ou SKUs de caixa (atacado), depois agende a produção.","icon":"tabler:circle-check-filled"},
    {"title":"Envie e reordene","description":"Suporte de embalagem de exportação e reordens mensais.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"FAQ OEM e atacado de creatina",
  "faqs":[
    {"title":"Vocês oferecem OEM / private label e atacado?","description":"Sim. <strong>OEM / private label</strong> para marcas que precisam de fórmulas, sabores e embalagens sob medida; <strong>atacado</strong> para distribuidores, academias e vendedores online com SKUs de caixa padrão."},
    {"title":"Quais formatos de creatina podem ser private label?","description":"Creatina monohidratada em <strong>gummies</strong>, <strong>pó</strong> e <strong>cápsulas</strong>, com sabores, porções e embalagem de marca sujeitos a MOQ."},
    {"title":"Posso obter amostras antes de um pedido grande?","description":"Sim. Amostra primeiro é recomendada para sabor, textura e rótulo. Peça pelo formulário."},
    {"title":"Vocês fornecem COA ou testes de terceiros?","description":"Apoiamos documentação por lote e caminhos de testes de terceiros para compradores de suplementos. Detalhes no orçamento."},
    {"title":"Isto é uma loja retail para consumidores nos EUA?","description":"Não. Crest Creatine é um site <strong>B2B</strong> de OEM e atacado para marcas e parceiros de canal — não uma loja DTC."},
  ],
  "ctaTitle":"Pronto para um orçamento de fábrica?","ctaSub":"Compartilhe tipo de comprador, necessidade e volume — respondemos em dias úteis em até 24 horas.",
  "ctaForm":"Abrir formulário","ctaProducts":"Programas de produto","ctaOemDetails":"Detalhes OEM","ctaWhDetails":"Detalhes atacado",
},
"ja": {
  "trustItems":[
    {"title":"柔軟なMOQ","description":"プライベートラベル試産向けトライアルMOQ；卸売SKU向けカートンMOQ。","icon":"tabler:package"},
    {"title":"サンプル対応","description":"量産前に処方・フレーバー・包装を承認。","icon":"tabler:flask"},
    {"title":"COA・試験","description":"ロットCOA経路と米国向けブランド向け第三者試験サポート。","icon":"tabler:file-certificate"},
    {"title":"24時間見積","description":"OEM RFQ・卸売価格表を営業日に回答。","icon":"tabler:clock"},
  ],
  "buyTag":"2つの購入方法","buyTitle":"OEM／プライベートラベルまたは卸売",
  "buyOemTitle":"OEM／プライベートラベル","buyOemDesc":"カスタムクレアチングミ・粉末・カプセル — フレーバー、包装、ブランディング、コンプライアンス文書。クレアチンSKUの立ち上げ・拡充に最適。",
  "buyWhTitle":"卸売","buyWhDesc":"代理店・ジム・小売・ネット販売向け標準カートン仕様。価格表とアカウント案内を卸売フォームで依頼。",
  "prodTag":"製品プログラム","prodTitle":"グミ・粉末・カプセル","prodSub":"プライベートラベルと卸売の開始仕様 — 用量・パック・MOQは見積で確定。",
  "gummiesTitle":"クレアチン・グミ","gummiesDesc":"主力：約1,000 mg／粒または3粒で約5 g；60／90本；ペクチン可；フレーバー開発。","gummiesCta":"グミを見る",
  "powderTitle":"クレアチン粉末","powderDesc":"300 g／500 g／1 kgタブまたはパウチ；25 kgドラム；メッシュ選択肢；無香料＋フレーバー。","powderCta":"粉末を見る",
  "capsTitle":"クレアチン・カプセル","capsDesc":"約750–1,000 mg／カプセル；60–240；ゼラチン／HPMC／プルランはプログラム次第。","capsCta":"カプセルを見る",
  "stepsTitle":"調達の流れ",
  "steps":[
    {"title":"チャネルを伝える","description":"OEM案件または卸売口座 — バイヤー種別、数量、出荷先国。","icon":"tabler:message"},
    {"title":"MOQとサンプルを取得","description":"段階的MOQ、サンプル、市場向け文書で回答。","icon":"tabler:package"},
    {"title":"承認して生産","description":"処方・フレーバー・包装（OEM）またはカートンSKU（卸売）を確定し生産計画。","icon":"tabler:circle-check-filled"},
    {"title":"出荷と再注文","description":"輸出梱包サポートと月次リピート注文。","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"クレアチンOEM・卸売FAQ",
  "faqs":[
    {"title":"OEM／プライベートラベルと卸売の両方ありますか？","description":"はい。<strong>OEM／プライベートラベル</strong>はカスタム処方・フレーバー・包装が必要なブランド向け；<strong>卸売</strong>は標準カートンSKUを買う代理店・ジム・ネット販売向けです。"},
    {"title":"どのクレアチン剤形をプライベートラベルできますか？","description":"クレアチンモノハイドレートの<strong>グミ</strong>・<strong>粉末</strong>・<strong>カプセル</strong>。フレーバー、1回量、ブランド包装はMOQに応じます。"},
    {"title":"大口注文前にサンプルは取れますか？","description":"はい。味・食感・ラベル確認のためサンプル優先を推奨。問い合わせフォームから依頼してください。"},
    {"title":"COAや第三者試験は提供しますか？","description":"ロット単位の文書と、ダイエタリーサプリメントバイヤー向け第三者試験経路に対応。詳細は見積時に確認。"},
    {"title":"米国消費者向け小売店ですか？","description":"いいえ。Crest Creatineはブランドとチャネル向けの<strong>B2B</strong> OEM・卸売サイトであり、DTCショップではありません。"},
  ],
  "ctaTitle":"工場見積の準備はできましたか？","ctaSub":"バイヤー種別・ご用件・数量をお知らせください — 営業日24時間以内に回答します。",
  "ctaForm":"問い合わせフォームを開く","ctaProducts":"製品プログラム","ctaOemDetails":"OEM詳細","ctaWhDetails":"卸売詳細",
},
"ko": {
  "trustItems":[
    {"title":"유연한 MOQ","description":"프라이빗 라벨 파일럿용 시험 MOQ; 도매 SKU용 카톤 MOQ.","icon":"tabler:package"},
    {"title":"샘플 제공","description":"대량 생산 전 처방·맛·포장 승인.","icon":"tabler:flask"},
    {"title":"COA 및 시험","description":"로트 COA 경로와 미국향 브랜드용 제3자 시험 지원.","icon":"tabler:file-certificate"},
    {"title":"24시간 견적","description":"OEM RFQ 및 도매 가격표에 영업일 회신.","icon":"tabler:clock"},
  ],
  "buyTag":"두 가지 구매 방식","buyTitle":"OEM / 프라이빗 라벨 또는 도매",
  "buyOemTitle":"OEM / 프라이빗 라벨","buyOemDesc":"맞춤 크레아틴 구미·파우더·캡슐 — 맛, 포장, 브랜딩, 컴플라이언스 문서. 크레아틴 SKU 출시·확장 브랜드에 적합.",
  "buyWhTitle":"도매","buyWhDesc":"유통사·헬스장·리테일·온라인 판매자용 표준 카톤 스펙. 가격표와 계정 안내를 도매 문의로 요청.",
  "prodTag":"제품 프로그램","prodTitle":"구미, 파우더 & 캡슐","prodSub":"프라이빗 라벨·도매 시작 구성 — 용량·팩·MOQ는 견적에서 확정.",
  "gummiesTitle":"크레아틴 구미","gummiesDesc":"히어로 포맷: ~1,000 mg/구미 또는 3개 ~5 g; 60/90병; 펙틴 옵션; 맛 개발.","gummiesCta":"구미 보기",
  "powderTitle":"크레아틴 파우더","powderDesc":"300 g / 500 g / 1 kg 통 또는 파우치; 25 kg 드럼; 메시 옵션; 무향 + 맛.","powderCta":"파우더 보기",
  "capsTitle":"크레아틴 캡슐","capsDesc":"약 750–1,000 mg/캡슐; 60–240; 젤라틴·HPMC·풀루란은 프로그램에 따름.","capsCta":"캡슐 보기",
  "stepsTitle":"소싱 진행 방식",
  "steps":[
    {"title":"채널 알려주기","description":"OEM 프로젝트 또는 도매 계정 — 구매자 유형, 물량, 배송국.","icon":"tabler:message"},
    {"title":"MOQ와 샘플 받기","description":"단계별 MOQ, 샘플 옵션, 시장 문서로 회신.","icon":"tabler:package"},
    {"title":"승인 후 생산","description":"처방·맛·포장(OEM) 또는 카톤 SKU(도매) 확정 후 생산 일정.","icon":"tabler:circle-check-filled"},
    {"title":"출하 및 재주문","description":"수출 포장 지원과 월간 재주문 경로.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"크레아틴 OEM & 도매 FAQ",
  "faqs":[
    {"title":"OEM / 프라이빗 라벨과 도매를 모두 제공하나요?","description":"네. <strong>OEM / 프라이빗 라벨</strong>은 맞춤 처방·맛·포장이 필요한 브랜드용; <strong>도매</strong>는 표준 카톤 SKU를 구매하는 유통사·헬스장·온라인 판매자용입니다."},
    {"title":"어떤 크레아틴 제형을 프라이빗 라벨할 수 있나요?","description":"크레아틴 모노하이드레이트 <strong>구미</strong>, <strong>파우더</strong>, <strong>캡슐</strong> — 맛, 1회 분량, 브랜드 포장은 MOQ에 따름."},
    {"title":"대량 주문 전 샘플을 받을 수 있나요?","description":"네. 맛·질감·라벨 확인을 위해 샘플 우선을 권장합니다. 문의 양식으로 요청하세요."},
    {"title":"COA 또는 제3자 시험을 제공하나요?","description":"로트 단위 문서와 식이보충제 구매자용 제3자 시험 경로를 지원합니다. 세부 사항은 견적 시 확정."},
    {"title":"미국 소비자 리테일 스토어인가요?","description":"아니요. Crest Creatine은 브랜드와 채널 파트너를 위한 <strong>B2B</strong> OEM·도매 사이트이며 DTC 상점이 아닙니다."},
  ],
  "ctaTitle":"공장 견적 준비가 되셨나요?","ctaSub":"구매자 유형, 문의 내용, 물량을 공유해 주세요 — 영업일 기준 24시간 내 회신합니다.",
  "ctaForm":"문의 양식 열기","ctaProducts":"제품 프로그램","ctaOemDetails":"OEM 상세","ctaWhDetails":"도매 상세",
},
"vi": {
  "trustItems":[
    {"title":"MOQ linh hoạt","description":"MOQ thử cho pilot nhãn riêng; MOQ carton cho SKU bán sỉ.","icon":"tabler:package"},
    {"title":"Có mẫu","description":"Phê duyệt công thức, hương vị và bao bì trước sản xuất số lượng lớn.","icon":"tabler:flask"},
    {"title":"COA & kiểm nghiệm","description":"Đường dẫn COA theo lô và hỗ trợ kiểm nghiệm bên thứ ba cho thương hiệu hướng Mỹ.","icon":"tabler:file-certificate"},
    {"title":"Báo giá 24 giờ","description":"Phản hồi ngày làm việc cho RFQ OEM và bảng giá sỉ.","icon":"tabler:clock"},
  ],
  "buyTag":"Hai cách mua","buyTitle":"OEM / Nhãn riêng hoặc Bán sỉ",
  "buyOemTitle":"OEM / Nhãn riêng","buyOemDesc":"Kẹo dẻo, bột và viên nang creatine tùy chỉnh — hương vị, bao bì, thương hiệu và tài liệu tuân thủ. Phù hợp thương hiệu ra mắt hoặc mở rộng SKU creatine.",
  "buyWhTitle":"Bán sỉ","buyWhDesc":"Thông số carton chuẩn cho nhà phân phối, phòng gym, bán lẻ và người bán online. Yêu cầu bảng giá và hướng dẫn tài khoản.",
  "prodTag":"Chương trình sản phẩm","prodTitle":"Kẹo dẻo, bột & viên nang","prodSub":"Cấu hình khởi đầu cho nhãn riêng và bán sỉ — liều, pack và MOQ xác nhận khi báo giá.",
  "gummiesTitle":"Kẹo dẻo creatine","gummiesDesc":"Định dạng chính: ~1.000 mg/viên hoặc ~5 g qua 3 viên; chai 60/90; tùy chọn pectin; phát triển hương vị.","gummiesCta":"Xem kẹo dẻo",
  "powderTitle":"Bột creatine","powderDesc":"Hũ hoặc túi 300 g / 500 g / 1 kg; thùng 25 kg; tùy chọn mesh; không vị + hương vị.","powderCta":"Xem bột",
  "capsTitle":"Viên nang creatine","capsDesc":"Khoảng 750–1.000 mg/viên; số lượng 60–240; gelatin, HPMC hoặc pullulan tùy chương trình.","capsCta":"Xem viên nang",
  "stepsTitle":"Quy trình sourcing",
  "steps":[
    {"title":"Cho biết kênh","description":"Dự án OEM hoặc tài khoản sỉ — loại người mua, khối lượng và quốc gia giao hàng.","icon":"tabler:message"},
    {"title":"Nhận MOQ & mẫu","description":"Phản hồi MOQ theo bậc, tùy chọn mẫu và tài liệu thị trường.","icon":"tabler:package"},
    {"title":"Phê duyệt & sản xuất","description":"Khóa công thức, hương vị và bao bì (OEM) hoặc SKU carton (sỉ), rồi lên lịch sản xuất.","icon":"tabler:circle-check-filled"},
    {"title":"Giao hàng & đặt lại","description":"Hỗ trợ đóng gói xuất khẩu và đường dẫn đặt lại hàng tháng.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"FAQ OEM & bán sỉ creatine",
  "faqs":[
    {"title":"Bạn có cả OEM / nhãn riêng và bán sỉ không?","description":"Có. <strong>OEM / nhãn riêng</strong> cho thương hiệu cần công thức, hương vị và bao bì tùy chỉnh; <strong>bán sỉ</strong> cho nhà phân phối, phòng gym và người bán online mua SKU carton chuẩn."},
    {"title":"Những dạng creatine nào có thể làm nhãn riêng?","description":"Creatine monohydrate dạng <strong>kẹo dẻo</strong>, <strong>bột</strong> và <strong>viên nang</strong>, với hương vị, khẩu phần và bao bì thương hiệu theo MOQ."},
    {"title":"Tôi có thể lấy mẫu trước đơn lớn không?","description":"Có. Nên mẫu trước để xem hương vị, kết cấu và nhãn. Yêu cầu qua biểu mẫu."},
    {"title":"Bạn có cung cấp COA hoặc kiểm nghiệm bên thứ ba không?","description":"Chúng tôi hỗ trợ tài liệu theo lô và đường dẫn kiểm nghiệm bên thứ ba cho người mua thực phẩm bổ sung. Chi tiết khi báo giá."},
    {"title":"Đây có phải cửa hàng bán lẻ tiêu dùng Mỹ không?","description":"Không. Crest Creatine là site <strong>B2B</strong> OEM và bán sỉ cho thương hiệu và đối tác kênh — không phải cửa hàng DTC."},
  ],
  "ctaTitle":"Sẵn sàng báo giá nhà máy?","ctaSub":"Chia sẻ loại người mua, nhu cầu và khối lượng — phản hồi trong 24 giờ làm việc.",
  "ctaForm":"Mở biểu mẫu","ctaProducts":"Chương trình sản phẩm","ctaOemDetails":"Chi tiết OEM","ctaWhDetails":"Chi tiết bán sỉ",
},
"id": {
  "trustItems":[
    {"title":"MOQ fleksibel","description":"MOQ uji coba untuk pilot private label; MOQ karton untuk SKU grosir.","icon":"tabler:package"},
    {"title":"Sampel tersedia","description":"Setujui formula, rasa, dan kemasan sebelum produksi massal.","icon":"tabler:flask"},
    {"title":"COA & pengujian","description":"Jalur COA per lot dan dukungan uji pihak ketiga untuk merek menuju AS.","icon":"tabler:file-certificate"},
    {"title":"Penawaran 24 jam","description":"Balasan hari kerja untuk RFQ OEM dan daftar harga grosir.","icon":"tabler:clock"},
  ],
  "buyTag":"Dua cara membeli","buyTitle":"OEM / Private label atau Grosir",
  "buyOemTitle":"OEM / Private label","buyOemDesc":"Gummy, bubuk, dan kapsul creatine kustom — rasa, kemasan, branding, dan dokumen kepatuhan. Ideal untuk merek yang meluncurkan atau memperluas SKU creatine.",
  "buyWhTitle":"Grosir","buyWhDesc":"Spesifikasi karton standar untuk distributor, gym, retailer, dan penjual online. Minta daftar harga dan panduan akun.",
  "prodTag":"Program produk","prodTitle":"Gummy, bubuk & kapsul","prodSub":"Konfigurasi awal untuk private label dan grosir — dosis, pack, dan MOQ dikonfirmasi pada penawaran.",
  "gummiesTitle":"Gummy creatine","gummiesDesc":"Format utama: ~1.000 mg/gummy atau ~5 g dalam 3 gummy; botol 60/90; opsi pektin; pengembangan rasa.","gummiesCta":"Lihat gummy",
  "powderTitle":"Bubuk creatine","powderDesc":"Toples atau pouch 300 g / 500 g / 1 kg; drum 25 kg; opsi mesh; tanpa rasa + rasa.","powderCta":"Lihat bubuk",
  "capsTitle":"Kapsul creatine","capsDesc":"Sekitar 750–1.000 mg/kapsul; jumlah 60–240; gelatin, HPMC, atau pullulan sesuai program.","capsCta":"Lihat kapsul",
  "stepsTitle":"Cara kerja sourcing",
  "steps":[
    {"title":"Ceritakan saluran Anda","description":"Proyek OEM atau akun grosir — tipe pembeli, volume, dan negara tujuan.","icon":"tabler:message"},
    {"title":"Dapatkan MOQ & sampel","description":"Kami balas dengan MOQ berjenjang, opsi sampel, dan dokumentasi.","icon":"tabler:package"},
    {"title":"Setujui & produksi","description":"Kunci formula, rasa, dan kemasan (OEM) atau SKU karton (grosir), lalu jadwalkan produksi.","icon":"tabler:circle-check-filled"},
    {"title":"Kirim & pesan ulang","description":"Dukungan kemasan ekspor dan jalur pemesanan ulang bulanan.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"FAQ OEM & grosir creatine",
  "faqs":[
    {"title":"Apakah Anda menawarkan OEM / private label dan grosir?","description":"Ya. <strong>OEM / private label</strong> untuk merek yang butuh formula, rasa, dan kemasan kustom; <strong>grosir</strong> untuk distributor, gym, dan penjual online yang membeli SKU karton standar."},
    {"title":"Format creatine apa yang bisa private-label?","description":"Creatine monohydrate <strong>gummy</strong>, <strong>bubuk</strong>, dan <strong>kapsul</strong>, dengan rasa, porsi, dan kemasan merek sesuai MOQ."},
    {"title":"Bisakah saya mendapat sampel sebelum pesanan besar?","description":"Ya. Disarankan sampel dulu untuk rasa, tekstur, dan label. Ajukan lewat formulir."},
    {"title":"Apakah Anda menyediakan COA atau uji pihak ketiga?","description":"Kami mendukung dokumentasi tingkat lot dan jalur uji pihak ketiga untuk pembeli suplemen. Detail dikonfirmasi saat penawaran."},
    {"title":"Apakah ini toko retail konsumen AS?","description":"Tidak. Crest Creatine adalah situs <strong>B2B</strong> OEM dan grosir untuk merek dan mitra saluran — bukan toko DTC."},
  ],
  "ctaTitle":"Siap untuk penawaran pabrik?","ctaSub":"Bagikan tipe pembeli, kebutuhan, dan volume — kami balas dalam 24 jam hari kerja.",
  "ctaForm":"Buka formulir","ctaProducts":"Program produk","ctaOemDetails":"Detail OEM","ctaWhDetails":"Detail grosir",
},
"ru": {
  "trustItems":[
    {"title":"Гибкий MOQ","description":"Пробные MOQ для пилотов private label; коробочные MOQ для оптовых SKU.","icon":"tabler:package"},
    {"title":"Образцы доступны","description":"Утвердите формулу, вкус и упаковку до массового производства.","icon":"tabler:flask"},
    {"title":"COA и тесты","description":"Пути COA по партиям и сторонние тесты для брендов на рынок США.","icon":"tabler:file-certificate"},
    {"title":"КП за 24 часа","description":"Ответ в рабочие дни на OEM RFQ и оптовые прайсы.","icon":"tabler:clock"},
  ],
  "buyTag":"Два способа покупки","buyTitle":"OEM / Private label или опт",
  "buyOemTitle":"OEM / Private label","buyOemDesc":"Кастомные жевательные, порошок и капсулы креатина — вкусы, упаковка, брендинг и документы соответствия. Идеально для запуска или расширения SKU креатина.",
  "buyWhTitle":"Опт","buyWhDesc":"Стандартные спецификации коробок для дистрибьюторов, залов, ритейла и онлайн-продавцов. Запросите прайс и гайд по аккаунту.",
  "prodTag":"Продуктовые программы","prodTitle":"Жевательные, порошок и капсулы","prodSub":"Стартовые конфигурации для private label и опта — доза, упаковка и MOQ подтверждаются в КП.",
  "gummiesTitle":"Жевательный креатин","gummiesDesc":"Основной формат: ~1 000 мг/шт. или ~5 г на 3 шт.; банки 60/90; пектин; разработка вкусов.","gummiesCta":"Смотреть жевательные",
  "powderTitle":"Креатин порошок","powderDesc":"Банки или pouches 300 г / 500 г / 1 кг; барабаны 25 кг; варианты mesh; без вкуса + вкусы.","powderCta":"Смотреть порошок",
  "capsTitle":"Креатин капсулы","capsDesc":"Примерно 750–1 000 мг/капсула; 60–240 шт.; желатин, HPMC или пуллулан по программе.","capsCta":"Смотреть капсулы",
  "stepsTitle":"Как проходит закупка",
  "steps":[
    {"title":"Расскажите о канале","description":"OEM-проект или оптовый аккаунт — тип покупателя, объём и страна доставки.","icon":"tabler:message"},
    {"title":"Получите MOQ и образцы","description":"Ответим ступенчатыми MOQ, образцами и документацией.","icon":"tabler:package"},
    {"title":"Утвердите и производите","description":"Зафиксируйте формулу, вкус и упаковку (OEM) или коробочные SKU (опт), затем план производства.","icon":"tabler:circle-check-filled"},
    {"title":"Отгрузка и повторные заказы","description":"Поддержка экспортной упаковки и ежемесячные повторные заказы.","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"FAQ OEM и опта креатина",
  "faqs":[
    {"title":"Вы предлагаете OEM / private label и опт?","description":"Да. <strong>OEM / private label</strong> для брендов с кастомными формулами, вкусами и упаковкой; <strong>опт</strong> для дистрибьюторов, залов и онлайн-продавцов со стандартными коробочными SKU."},
    {"title":"Какие формы креатина можно private-label?","description":"Креатин моногидрат в <strong>жевательных</strong>, <strong>порошке</strong> и <strong>капсулах</strong>, со вкусами, порциями и брендовой упаковкой по MOQ."},
    {"title":"Можно ли получить образцы до крупного заказа?","description":"Да. Рекомендуем сначала образец для вкуса, текстуры и этикетки. Запросите через форму."},
    {"title":"Предоставляете ли COA или сторонние тесты?","description":"Поддерживаем документацию по партиям и пути сторонних тестов для покупателей БАД. Детали в КП."},
    {"title":"Это розничный магазин для потребителей США?","description":"Нет. Crest Creatine — <strong>B2B</strong> сайт OEM и опта для брендов и партнёров канала, а не DTC-магазин."},
  ],
  "ctaTitle":"Готовы к заводскому КП?","ctaSub":"Укажите тип покупателя, потребность и объём — ответим в рабочие дни за 24 часа.",
  "ctaForm":"Открыть форму","ctaProducts":"Продуктовые программы","ctaOemDetails":"Детали OEM","ctaWhDetails":"Детали опта",
},
"hi": {
  "trustItems":[
    {"title":"लचीला MOQ","description":"प्राइवेट लेबल पायलट के लिए ट्रायल MOQ; थोक SKU के लिए कार्टन MOQ।","icon":"tabler:package"},
    {"title":"सैंपल उपलब्ध","description":"बल्क उत्पादन से पहले फॉर्मूला, फ्लेवर और पैकेजिंग स्वीकार करें।","icon":"tabler:flask"},
    {"title":"COA और टेस्टिंग","description":"लॉट COA पथ और US-बाउंड ब्रांड के लिए थर्ड-पार्टी टेस्टिंग सपोर्ट।","icon":"tabler:file-certificate"},
    {"title":"24 घंटे कोट","description":"OEM RFQ और थोक मूल्य सूची पर कार्य दिवस जवाब।","icon":"tabler:clock"},
  ],
  "buyTag":"खरीदने के दो तरीके","buyTitle":"OEM / प्राइवेट लेबल या थोक",
  "buyOemTitle":"OEM / प्राइवेट लेबल","buyOemDesc":"कस्टम क्रिएटिन गमी, पाउडर और कैप्सूल — फ्लेवर, पैकेजिंग, ब्रांडिंग और अनुपालन दस्तावेज़। क्रिएटिन SKU लॉन्च या विस्तार के लिए आदर्श।",
  "buyWhTitle":"थोक","buyWhDesc":"डिस्ट्रीब्यूटर, जिम, रिटेलर और ऑनलाइन विक्रेताओं के लिए मानक कार्टन स्पेक। मूल्य सूची और अकाउंट गाइडेंस अनुरोध करें।",
  "prodTag":"उत्पाद प्रोग्राम","prodTitle":"गमी, पाउडर और कैप्सूल","prodSub":"प्राइवेट लेबल और थोक के लिए शुरुआती कॉन्फ़िगरेशन — डोज़, पैक और MOQ कोट पर पुष्टि।",
  "gummiesTitle":"क्रिएटिन गमी","gummiesDesc":"हीरो फ़ॉर्मेट: ~1,000 mg/गमी या 3 गमी में ~5 g; 60/90 बोतल; पेक्टिन विकल्प; फ्लेवर डेवलपमेंट।","gummiesCta":"गमी देखें",
  "powderTitle":"क्रिएटिन पाउडर","powderDesc":"300 g / 500 g / 1 kg टब या पाउच; 25 kg ड्रम; मेश विकल्प; अनफ्लेवर्ड + फ्लेवर।","powderCta":"पाउडर देखें",
  "capsTitle":"क्रिएटिन कैप्सूल","capsDesc":"लगभग 750–1,000 mg/कैप्सूल; 60–240 काउंट; जिलेटिन, HPMC या पुलुलन प्रोग्राम के अनुसार।","capsCta":"कैप्सूल देखें",
  "stepsTitle":"सोर्सिंग कैसे काम करती है",
  "steps":[
    {"title":"अपना चैनल बताएं","description":"OEM प्रोजेक्ट या थोक अकाउंट — खरीदार प्रकार, मात्रा और शिप-टू देश।","icon":"tabler:message"},
    {"title":"MOQ और सैंपल पाएं","description":"स्तरीय MOQ, सैंपल विकल्प और दस्तावेज़ के साथ जवाब।","icon":"tabler:package"},
    {"title":"स्वीकृत करें और उत्पादन","description":"फॉर्मूला, फ्लेवर और पैकेजिंग (OEM) या कार्टन SKU (थोक) लॉक करें, फिर उत्पादन शेड्यूल करें।","icon":"tabler:circle-check-filled"},
    {"title":"शिप और रीऑर्डर","description":"एक्सपोर्ट पैकिंग सपोर्ट और मासिक रीऑर्डर पथ।","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"क्रिएटिन OEM और थोक FAQ",
  "faqs":[
    {"title":"क्या आप OEM / प्राइवेट लेबल और थोक दोनों देते हैं?","description":"हाँ। <strong>OEM / प्राइवेट लेबल</strong> कस्टम फॉर्मूला, फ्लेवर और पैकेजिंग वाले ब्रांड के लिए; <strong>थोक</strong> मानक कार्टन SKU खरीदने वाले डिस्ट्रीब्यूटर, जिम और ऑनलाइन विक्रेताओं के लिए।"},
    {"title":"किन क्रिएटिन फ़ॉर्मैट को प्राइवेट-लेबल कर सकते हैं?","description":"क्रिएटिन मोनohydrate <strong>गमी</strong>, <strong>पाउडर</strong> और <strong>कैप्सूल</strong>, कस्टम फ्लेवर, सर्विंग और ब्रांडेड पैकेजिंग MOQ के अधीन।"},
    {"title":"बल्क ऑर्डर से पहले सैंपल मिल सकता है?","description":"हाँ। फ्लेवर, टेक्सचर और लेबल समीक्षा के लिए सैंपल-फर्स्ट अनुशंसित। फॉर्म से पूछें।"},
    {"title":"क्या आप COA या थर्ड-पार्टी टेस्टिंग देते हैं?","description":"हम लॉट-स्तरीय दस्तावेज़ और डायटरी सप्लीमेंट खरीदारों के लिए थर्ड-पार्टी टेस्टिंग पथ सपोर्ट करते हैं। विवरण कोट पर।"},
    {"title":"क्या यह US कंज़्यूमर रिटेल स्टोर है?","description":"नहीं। Crest Creatine ब्रांड और चैनल पार्टनर के लिए <strong>B2B</strong> OEM और थोक साइट है — DTC शॉप नहीं।"},
  ],
  "ctaTitle":"फ़ैक्टरी कोट के लिए तैयार?","ctaSub":"खरीदार प्रकार, ज़रूरत और मात्रा बताएं — कार्य दिवसों में 24 घंटे में जवाब।",
  "ctaForm":"फ़ॉर्म खोलें","ctaProducts":"उत्पाद प्रोग्राम","ctaOemDetails":"OEM विवरण","ctaWhDetails":"थोक विवरण",
},
"bn": {
  "trustItems":[
    {"title":"নমনীয় MOQ","description":"প্রাইভেট লেবেল পাইলটের জন্য ট্রায়াল MOQ; হোলসেল SKU-এর জন্য কার্টন MOQ।","icon":"tabler:package"},
    {"title":"নমুনা পাওয়া যায়","description":"বাল্ক উৎপাদনের আগে ফর্মুলা, ফ্লেভার ও প্যাকেজিং অনুমোদন করুন।","icon":"tabler:flask"},
    {"title":"COA ও পরীক্ষা","description":"লট COA পথ এবং US-গামী ব্র্যান্ডের জন্য তৃতীয় পক্ষের পরীক্ষা সহায়তা।","icon":"tabler:file-certificate"},
    {"title":"২৪ ঘণ্টায় কোট","description":"OEM RFQ ও হোলসেল মূল্য তালিকায় কর্মদিবসে উত্তর।","icon":"tabler:clock"},
  ],
  "buyTag":"কেনার দুই উপায়","buyTitle":"OEM / প্রাইভেট লেবেল বা হোলসেল",
  "buyOemTitle":"OEM / প্রাইভেট লেবেল","buyOemDesc":"কাস্টম ক্রিয়েটিন গামি, পাউডার ও ক্যাপসুল — ফ্লেভার, প্যাকেজিং, ব্র্যান্ডিং ও কমপ্লায়েন্স ডকুমেন্ট। ক্রিয়েটিন SKU লঞ্চ বা সম্প্রসারণের জন্য আদর্শ।",
  "buyWhTitle":"হোলসেল","buyWhDesc":"ডিস্ট্রিবিউটর, জিম, খুচরা ও অনলাইন বিক্রেতাদের জন্য স্ট্যান্ডার্ড কার্টন স্পেক। মূল্য তালিকা ও অ্যাকাউন্ট গাইডেন্স অনুরোধ করুন।",
  "prodTag":"পণ্য প্রোগ্রাম","prodTitle":"গামি, পাউডার ও ক্যাপসুল","prodSub":"প্রাইভেট লেবেল ও হোলসেলের শুরুর কনফিগারেশন — ডোজ, প্যাক ও MOQ কোটে নিশ্চিত।",
  "gummiesTitle":"ক্রিয়েটিন গামি","gummiesDesc":"হিরো ফরম্যাট: ~১,০০০ mg/গামি বা ৩ গামিতে ~৫ g; ৬০/৯০ বোতল; পেকটিন অপশন; ফ্লেভার ডেভেলপমেন্ট।","gummiesCta":"গামি দেখুন",
  "powderTitle":"ক্রিয়েটিন পাউডার","powderDesc":"৩০০ g / ৫০০ g / ১ kg টাব বা পাউচ; ২৫ kg ড্রাম; মেশ অপশন; আনফ্লেভার্ড + ফ্লেভার।","powderCta":"পাউডার দেখুন",
  "capsTitle":"ক্রিয়েটিন ক্যাপসুল","capsDesc":"প্রায় ৭৫০–১,০০০ mg/ক্যাপসুল; ৬০–২৪০ কাউন্ট; জেলatin, HPMC বা পুলুলান প্রোগ্রাম অনুযায়ী।","capsCta":"ক্যাপসুল দেখুন",
  "stepsTitle":"সোর্সিং কীভাবে কাজ করে",
  "steps":[
    {"title":"আপনার চ্যানেল বলুন","description":"OEM প্রজেক্ট বা হোলসেল অ্যাকাউন্ট — ক্রেতার ধরন, পরিমাণ ও শিপ-টু দেশ।","icon":"tabler:message"},
    {"title":"MOQ ও নমুনা পান","description":"স্তরভিত্তিক MOQ, নমুনা অপশন ও ডকুমেন্টেশনসহ উত্তর।","icon":"tabler:package"},
    {"title":"অনুমোদন ও উৎপাদন","description":"ফর্মুলা, ফ্লেভার ও প্যাকেজিং (OEM) বা কার্টন SKU (হোলসেল) লক করে উৎপাদন নির্ধারণ।","icon":"tabler:circle-check-filled"},
    {"title":"শিপ ও রিঅর্ডার","description":"রপ্তানি প্যাকিং সাপোর্ট ও মাসিক রিঅর্ডার পথ।","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"ক্রিয়েটিন OEM ও হোলসেল FAQ",
  "faqs":[
    {"title":"আপনি কি OEM / প্রাইভেট লেবেল ও হোলসেল দুটোই দেন?","description":"হ্যাঁ। <strong>OEM / প্রাইভেট লেবেল</strong> কাস্টম ফর্মুলা, ফ্লেভার ও প্যাকেজিং চাওয়া ব্র্যান্ডের জন্য; <strong>হোলসেল</strong> স্ট্যান্ডার্ড কার্টন SKU কেনা ডিস্ট্রিবিউটর, জিম ও অনলাইন বিক্রেতাদের জন্য।"},
    {"title":"কোন ক্রিয়েটিন ফরম্যাট প্রাইভেট-লেবেল করা যায়?","description":"ক্রিয়েটিন মনোহাইড্রেট <strong>গামি</strong>, <strong>পাউডার</strong> ও <strong>ক্যাপসুল</strong>, কাস্টম ফ্লেভার, সার্ভিং ও ব্র্যান্ডেড প্যাকেজিং MOQ সাপেক্ষে।"},
    {"title":"বড় অর্ডারের আগে নমুনা পাওয়া যায়?","description":"হ্যাঁ। স্বাদ, টেক্সচার ও লেবেল পর্যালোচনার জন্য স্যাম্পল-ফার্স্ট সুপারিশকৃত। ফর্ম দিয়ে জানান।"},
    {"title":"আপনি কি COA বা তৃতীয় পক্ষের পরীক্ষা দেন?","description":"আমরা লট-স্তরের ডকুমেন্টেশন ও ডায়েটারি সাপ্লিমেন্ট ক্রেতাদের জন্য তৃতীয় পক্ষের পরীক্ষা পথ সাপোর্ট করি। বিস্তারিত কোটে।"},
    {"title":"এটা কি US কনজিউমার রিটেইল স্টোর?","description":"না। Crest Creatine ব্র্যান্ড ও চ্যানেল পার্টনারদের জন্য <strong>B2B</strong> OEM ও হোলসেল সাইট — DTC শপ নয়।"},
  ],
  "ctaTitle":"ফ্যাক্টরি কোটের জন্য প্রস্তুত?","ctaSub":"ক্রেতার ধরন, চাহিদা ও পরিমাণ জানান — কর্মদিবসে ২৪ ঘণ্টার মধ্যে উত্তর।",
  "ctaForm":"ফর্ম খুলুন","ctaProducts":"পণ্য প্রোগ্রাম","ctaOemDetails":"OEM বিবরণ","ctaWhDetails":"হোলসেল বিবরণ",
},
"ur": {
  "trustItems":[
    {"title":"لچکدار MOQ","description":"پرائیویٹ لیبل پائلٹ کے لیے ٹرائل MOQ؛ ہول سیل SKU کے لیے کارٹن MOQ۔","icon":"tabler:package"},
    {"title":"سیمپل دستیاب","description":"بلک پروڈکشن سے پہلے فارمولا، فلیور اور پیکجنگ منظور کریں۔","icon":"tabler:flask"},
    {"title":"COA اور ٹیسٹنگ","description":"لاٹ COA راستے اور US-باؤنڈ برانڈز کے لیے تھرڈ پارٹی ٹیسٹنگ سپورٹ۔","icon":"tabler:file-certificate"},
    {"title":"24 گھنٹے کوٹ","description":"OEM RFQ اور ہول سیل قیمت فہرست پر کاروباری دن جواب۔","icon":"tabler:clock"},
  ],
  "buyTag":"خریدنے کے دو طریقے","buyTitle":"OEM / پرائیویٹ لیبل یا ہول سیل",
  "buyOemTitle":"OEM / پرائیویٹ لیبل","buyOemDesc":"کسٹم کریٹائن گمیز، پاؤڈر اور کیپسولز — فلیور، پیکجنگ، برانڈنگ اور کمپلائنس دستاویزات۔ کریٹائن SKU لانچ یا توسیع کے لیے مثالی۔",
  "buyWhTitle":"ہول سیل","buyWhDesc":"ڈسٹری بیوٹرز، جم، ریٹیلرز اور آن لائن فروخت کنندگان کے لیے معیاری کارٹن اسپیکس۔ قیمت فہرست اور اکاؤنٹ رہنمائی کی درخواست کریں۔",
  "prodTag":"پروڈکٹ پروگرامز","prodTitle":"گمیز، پاؤڈر اور کیپسولز","prodSub":"پرائیویٹ لیبل اور ہول سیل کی ابتدائی کنفیگریشنز — خوراک، پیک اور MOQ کوٹ پر تصدیق۔",
  "gummiesTitle":"کریٹائن گمیز","gummiesDesc":"ہیرو فارمیٹ: ~1,000 mg/گمی یا 3 گمیز میں ~5 g؛ 60/90 بوتلیں؛ پیکٹین آپشنز؛ فلیور ڈیولپمنٹ۔","gummiesCta":"گمیز دیکھیں",
  "powderTitle":"کریٹائن پاؤڈر","powderDesc":"300 g / 500 g / 1 kg ٹب یا پاؤچ؛ 25 kg ڈرم؛ میش آپشنز؛ ان فلیورڈ + فلیورز۔","powderCta":"پاؤڈر دیکھیں",
  "capsTitle":"کریٹائن کیپسولز","capsDesc":"تقریباً 750–1,000 mg/کیپسول؛ 60–240 کاؤنٹس؛ جیلیٹن، HPMC یا پلولان پروگرام کے مطابق۔","capsCta":"کیپسولز دیکھیں",
  "stepsTitle":"سورسنگ کیسے کام کرتی ہے",
  "steps":[
    {"title":"اپنا چینل بتائیں","description":"OEM پروجیکٹ یا ہول سیل اکاؤنٹ — خریدار کی قسم، مقدار اور شپ ٹو ملک۔","icon":"tabler:message"},
    {"title":"MOQ اور سیمپل حاصل کریں","description":"درجہ وار MOQ، سیمپل آپشنز اور دستاویزات کے ساتھ جواب۔","icon":"tabler:package"},
    {"title":"منظور کریں اور تیار کریں","description":"فارمولا، فلیور اور پیکجنگ (OEM) یا کارٹن SKUs (ہول سیل) لاک کریں، پھر پروڈکشن شیڈول کریں۔","icon":"tabler:circle-check-filled"},
    {"title":"شپ اور ری آرڈر","description":"ایکسپورٹ پیکنگ سپورٹ اور ماہانہ ری آرڈر راستے۔","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"کریٹائن OEM اور ہول سیل FAQ",
  "faqs":[
    {"title":"کیا آپ OEM / پرائیویٹ لیبل اور ہول سیل دونوں دیتے ہیں؟","description":"ہاں۔ <strong>OEM / پرائیویٹ لیبل</strong> کسٹم فارمولے، فلیور اور پیکجنگ والے برانڈز کے لیے؛ <strong>ہول سیل</strong> معیاری کارٹن SKU خریدنے والے ڈسٹری بیوٹرز، جم اور آن لائن فروخت کنندگان کے لیے۔"},
    {"title":"کون سے کریٹائن فارمیٹس پرائیویٹ لیبل کر سکتے ہیں؟","description":"کریٹائن مونو ہائیڈریٹ <strong>گمیز</strong>، <strong>پاؤڈر</strong> اور <strong>کیپسولز</strong>، کسٹم فلیور، سرونگ اور برانڈڈ پیکجنگ MOQ کے تابع۔"},
    {"title":"بڑے آرڈر سے پہلے سیمپل مل سکتا ہے؟","description":"ہاں۔ فلیور، ساخت اور لیبل جائزے کے لیے سیمپل فرسٹ تجویز کیا جاتا ہے۔ فارم سے پوچھیں۔"},
    {"title":"کیا آپ COA یا تھرڈ پارٹی ٹیسٹنگ دیتے ہیں؟","description":"ہم لاٹ سطح کی دستاویزات اور ڈائٹری سپلیمنٹ خریداروں کے لیے تھرڈ پارٹی ٹیسٹنگ راستے سپورٹ کرتے ہیں۔ تفصیلات کوٹ پر۔"},
    {"title":"کیا یہ US صارف ریٹیل اسٹور ہے؟","description":"نہیں۔ Crest Creatine برانڈز اور چینل پارٹنرز کے لیے <strong>B2B</strong> OEM اور ہول سیل سائٹ ہے — DTC شاپ نہیں۔"},
  ],
  "ctaTitle":"فیکٹری کوٹ کے لیے تیار؟","ctaSub":"خریدار کی قسم، ضرورت اور مقدار بتائیں — کاروباری دنوں میں 24 گھنٹوں میں جواب۔",
  "ctaForm":"فارم کھولیں","ctaProducts":"پروڈکٹ پروگرامز","ctaOemDetails":"OEM تفصیلات","ctaWhDetails":"ہول سیل تفصیلات",
},
"th": {
  "trustItems":[
    {"title":"MOQ ยืดหยุ่น","description":"MOQ ทดลองสำหรับไพรเวทเลเบลนำร่อง; MOQ ลังสำหรับ SKU ขายส่ง","icon":"tabler:package"},
    {"title":"มีตัวอย่าง","description":"อนุมัติสูตร รสชาติ และบรรจุภัณฑ์ก่อนผลิตจำนวนมาก","icon":"tabler:flask"},
    {"title":"COA และการทดสอบ","description":"เส้นทาง COA รายล็อต และการทดสอบบุคคลที่สามสำหรับแบรนด์ส่งสหรัฐฯ","icon":"tabler:file-certificate"},
    {"title":"ใบเสนอราคา 24 ชม.","description":"ตอบกลับวันทำการสำหรับ RFQ OEM และรายการราคาขายส่ง","icon":"tabler:clock"},
  ],
  "buyTag":"สองวิธีในการซื้อ","buyTitle":"OEM / ไพรเวทเลเบล หรือ ขายส่ง",
  "buyOemTitle":"OEM / ไพรเวทเลเบล","buyOemDesc":"กัมมี่ ผง และแคปซูลครีเอทีนตามสั่ง — รสชาติ บรรจุภัณฑ์ แบรนด์ และเอกสารการปฏิบัติตาม เหมาะกับแบรนด์ที่เปิดหรือขยาย SKU ครีเอทีน",
  "buyWhTitle":"ขายส่ง","buyWhDesc":"สเปกลังมาตรฐานสำหรับตัวแทนจำหน่าย ยิม ร้านค้าปลีก และผู้ขายออนไลน์ ขอรายการราคาและคำแนะนำบัญชี",
  "prodTag":"โปรแกรมผลิตภัณฑ์","prodTitle":"กัมมี่ ผง และแคปซูล","prodSub":"การกำหนดค่าเริ่มต้นสำหรับไพรเวทเลเบลและขายส่ง — ขนาด แพ็ก และ MOQ ยืนยันในใบเสนอราคา",
  "gummiesTitle":"ครีเอทีนกัมมี่","gummiesDesc":"รูปแบบหลัก: ~1,000 มก./กัมมี่ หรือ ~5 ก. จาก 3 กัมมี่; ขวด 60/90; ตัวเลือกเพกติน; พัฒนารสชาติ","gummiesCta":"ดูกัมมี่",
  "powderTitle":"ครีเอทีนผง","powderDesc":"กระป๋องหรือซอง 300 ก. / 500 ก. / 1 กก.; ถัง 25 กก.; ตัวเลือกเมช; ไม่มีรส + รสชาติ","powderCta":"ดูผง",
  "capsTitle":"ครีเอทีนแคปซูล","capsDesc":"ประมาณ 750–1,000 มก./แคปซูล; จำนวน 60–240; เจลาติน HPMC หรือพูลลูแลนตามโปรแกรม","capsCta":"ดูแคปซูล",
  "stepsTitle":"การจัดหาทำงานอย่างไร",
  "steps":[
    {"title":"บอกช่องทางของคุณ","description":"โครงการ OEM หรือบัญชีขายส่ง — ประเภทผู้ซื้อ ปริมาณ และประเทศจัดส่ง","icon":"tabler:message"},
    {"title":"รับ MOQ และตัวอย่าง","description":"เราตอบด้วย MOQ แบบขั้น ตัวเลือกตัวอย่าง และเอกสาร","icon":"tabler:package"},
    {"title":"อนุมัติและผลิต","description":"ล็อกสูตร รสชาติ และบรรจุภัณฑ์ (OEM) หรือ SKU ลัง (ขายส่ง) แล้วจัดตารางผลิต","icon":"tabler:circle-check-filled"},
    {"title":"จัดส่งและสั่งซ้ำ","description":"รองรับการบรรจุส่งออก และเส้นทางการสั่งซ้ำรายเดือน","icon":"tabler:truck-delivery"},
  ],
  "faqTitle":"FAQ OEM และขายส่งครีเอทีน",
  "faqs":[
    {"title":"คุณมีทั้ง OEM / ไพรเวทเลเบล และขายส่งหรือไม่?","description":"มี <strong>OEM / ไพรเวทเลเบล</strong> สำหรับแบรนด์ที่ต้องการสูตร รสชาติ และบรรจุภัณฑ์ตามสั่ง; <strong>ขายส่ง</strong> สำหรับตัวแทนจำหน่าย ยิม และผู้ขายออนไลน์ที่ซื้อ SKU ลังมาตรฐาน"},
    {"title":"รูปแบบครีเอทีนใดที่ทำไพรเวทเลเบลได้?","description":"ครีเอทีนโมโนไฮเดรตแบบ <strong>กัมมี่</strong> <strong>ผง</strong> และ <strong>แคปซูล</strong> พร้อมรสชาติ ปริมาณต่อครั้ง และบรรจุภัณฑ์แบรนด์ตาม MOQ"},
    {"title":"ขอตัวอย่างก่อนสั่งจำนวนมากได้ไหม?","description":"ได้ แนะนำเริ่มจากตัวอย่างเพื่อตรวจรสชาติ เนื้อสัมผัส และฉลาก ขอผ่านแบบฟอร์ม"},
    {"title":"มี COA หรือการทดสอบบุคคลที่สามไหม?","description":"เรารองรับเอกสารระดับล็อต และเส้นทางการทดสอบบุคคลที่สามสำหรับผู้ซื้ออาหารเสริม รายละเอียดในใบเสนอราคา"},
    {"title":"นี่คือร้านค้าปลีกผู้บริโภคสหรัฐฯ หรือไม่?","description":"ไม่ใช่ Crest Creatine เป็นไซต์ <strong>B2B</strong> OEM และขายส่งสำหรับแบรนด์และพาร์ทเนอร์ช่องทาง — ไม่ใช่ร้าน DTC"},
  ],
  "ctaTitle":"พร้อมใบเสนอราคาโรงงานหรือยัง?","ctaSub":"แชร์ประเภทผู้ซื้อ ความต้องการ และปริมาณ — เราตอบภายใน 24 ชั่วโมงในวันทำการ",
  "ctaForm":"เปิดแบบฟอร์ม","ctaProducts":"โปรแกรมผลิตภัณฑ์","ctaOemDetails":"รายละเอียด OEM","ctaWhDetails":"รายละเอียดขายส่ง",
},
}

for loc, s in MORE.items():
    HOME[loc].update(s)

# Verify all locales have non-EN trust titles (except en)
for loc in LOCALES:
    assert loc in HOME, loc
    assert "title" in HOME[loc]
    if loc != "en":
        assert HOME[loc]["trustItems"][0]["title"] != HOME["en"]["trustItems"][0]["title"] or loc in ("zh-tw","es","ar","fr","de"), loc

lines = [
    "import type { Locale } from './locales';",
    "",
    "export type FaqItem = { title: string; description: string };",
    "",
    "export type HomeCopy = {",
    "  title: string;",
    "  description: string;",
    "  tagline: string;",
    "  hero1: string;",
    "  hero2: string;",
    "  heroSub: string;",
    "  ctaOem: string;",
    "  ctaWholesale: string;",
    "  trustTag: string;",
    "  trustTitle: string;",
    "  trustSub: string;",
    "  trustItems: { title: string; description: string; icon: string }[];",
    "  buyTag: string;",
    "  buyTitle: string;",
    "  buyOemTitle: string;",
    "  buyOemDesc: string;",
    "  buyWhTitle: string;",
    "  buyWhDesc: string;",
    "  prodTag: string;",
    "  prodTitle: string;",
    "  prodSub: string;",
    "  gummiesTitle: string;",
    "  gummiesDesc: string;",
    "  gummiesCta: string;",
    "  powderTitle: string;",
    "  powderDesc: string;",
    "  powderCta: string;",
    "  capsTitle: string;",
    "  capsDesc: string;",
    "  capsCta: string;",
    "  stepsTitle: string;",
    "  steps: { title: string; description: string; icon: string }[];",
    "  faqTitle: string;",
    "  faqs: FaqItem[];",
    "  ctaTitle: string;",
    "  ctaSub: string;",
    "  ctaForm: string;",
    "  ctaProducts: string;",
    "  ctaOemDetails: string;",
    "  ctaWhDetails: string;",
    "  dshea: string;",
    "};",
    "",
    "const HOME: Record<Locale, HomeCopy> = {",
]
for loc in LOCALES:
    lines.append(f"  {lk(loc)}: {ser(HOME[loc], 2)},")
lines.append("};")
lines.append("")
lines.append("export function getHomeCopy(locale: Locale = 'en'): HomeCopy {")
lines.append("  return HOME[locale] ?? HOME.en;")
lines.append("}")
lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("Wrote", OUT, OUT.stat().st_size)
for loc in LOCALES:
    t = HOME[loc]["hero1"]
    print(loc, "→", t[:50])
