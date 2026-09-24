import type { Disclaimer, Input, Textarea } from '~/types';
import type { Locale } from './locales';

type FormCopy = {
  inputs: Input[];
  textarea: Textarea;
  disclaimer: Disclaimer;
  button: string;
  description: string;
  close: string;
  preferChat: string;
  waLead: {
    title: string;
    subtitle: string;
    button: string;
    description: string;
    disclaimerLabel: string;
  };
};

const FORMS: Record<Locale, FormCopy> = {
  en: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "I am a",
        placeholder: "Select…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Brand",
          },
          {
            value: "Distributor",
            label: "Distributor",
          },
          {
            value: "Gym or retailer",
            label: "Gym or retailer",
          },
          {
            value: "Online seller",
            label: "Online seller",
          },
          {
            value: "Other",
            label: "Other",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "I'm looking for",
        placeholder: "Select…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / Private label",
          },
          {
            value: "Wholesale pricing",
            label: "Wholesale pricing",
          },
          {
            value: "Sample",
            label: "Sample",
          },
          {
            value: "Bulk powder",
            label: "Bulk powder",
          },
          {
            value: "Bulk gummies",
            label: "Bulk gummies",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Expected volume",
        placeholder: "Select…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Sample",
          },
          {
            value: "Trial MOQ",
            label: "Trial MOQ",
          },
          {
            value: "Container/pallet",
            label: "Container / pallet",
          },
          {
            value: "Ongoing monthly",
            label: "Ongoing monthly",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Name",
        placeholder: "Your name",
      },
      {
        type: "email",
        name: "email",
        label: "Email",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "Message",
      name: "message",
      placeholder: "SKU interest (powder / gummies), flavor, packaging, ship-to country, timeline, certifications needed…",
      rows: 3,
    },
    disclaimer: {
      label: "I agree to be contacted by Crest Creatine regarding OEM, private label, and wholesale inquiries.",
    },
    button: "Get B2B Quote Now",
    description: "Tell us your buyer type and volume — we reply with MOQ tiers, sample options, and next steps within 24 hours on working days.",
    close: "Close",
    preferChat: "Prefer chat?",
    waLead: {
      title: "Chat on WhatsApp",
      subtitle: "Quick details first — factory quote follows in chat.",
      button: "Continue to WhatsApp",
      description: "We save your quote request, then open WhatsApp.",
      disclaimerLabel: "You agree we may contact you about this OEM / wholesale inquiry via email or WhatsApp.",
    },
  },
  'zh-tw': {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "我是",
        placeholder: "請選擇…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "品牌",
          },
          {
            value: "Distributor",
            label: "經銷商",
          },
          {
            value: "Gym or retailer",
            label: "健身房或零售商",
          },
          {
            value: "Online seller",
            label: "電商賣家",
          },
          {
            value: "Other",
            label: "其他",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "我想了解",
        placeholder: "請選擇…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM／私標",
          },
          {
            value: "Wholesale pricing",
            label: "批發報價",
          },
          {
            value: "Sample",
            label: "樣品",
          },
          {
            value: "Bulk powder",
            label: "散裝粉",
          },
          {
            value: "Bulk gummies",
            label: "散裝軟糖",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "預估量",
        placeholder: "請選擇…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "樣品",
          },
          {
            value: "Trial MOQ",
            label: "試產 MOQ",
          },
          {
            value: "Container/pallet",
            label: "貨櫃／棧板",
          },
          {
            value: "Ongoing monthly",
            label: "每月持續",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "姓名",
        placeholder: "您的姓名",
      },
      {
        type: "email",
        name: "email",
        label: "電子郵件",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "訊息",
      name: "message",
      placeholder: "感興趣的 SKU（粉／軟糖）、口味、包裝、目的地國家、時程、所需認證…",
      rows: 3,
    },
    disclaimer: {
      label: "我同意 Crest Creatine 就 OEM、私標與批發詢價與我聯絡。",
    },
    button: "立即取得 B2B 報價",
    description: "告訴我們買家類型與量級 — 我們於工作日 24 小時內回覆 MOQ 層級、樣品方案與下一步。",
    close: "關閉",
    preferChat: "想用即時通訊？",
    waLead: {
      title: "WhatsApp 聊聊",
      subtitle: "先填簡要資料 — 工廠報價在聊天中繼續。",
      button: "繼續到 WhatsApp",
      description: "我們先儲存您的詢價，再開啟 WhatsApp。",
      disclaimerLabel: "您同意我們可透過電子郵件或 WhatsApp 就此 OEM／批發詢價與您聯絡。",
    },
  },
  hi: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "मैं हूँ",
        placeholder: "चुनें…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "ब्रांड",
          },
          {
            value: "Distributor",
            label: "वितरक",
          },
          {
            value: "Gym or retailer",
            label: "जिम या रिटेलर",
          },
          {
            value: "Online seller",
            label: "ऑनलाइन विक्रेता",
          },
          {
            value: "Other",
            label: "अन्य",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "मुझे चाहिए",
        placeholder: "चुनें…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / प्राइवेट लेबल",
          },
          {
            value: "Wholesale pricing",
            label: "थोक मूल्य",
          },
          {
            value: "Sample",
            label: "सैंपल",
          },
          {
            value: "Bulk powder",
            label: "बल्क पाउडर",
          },
          {
            value: "Bulk gummies",
            label: "बल्क गमी",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "अपेक्षित मात्रा",
        placeholder: "चुनें…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "सैंपल",
          },
          {
            value: "Trial MOQ",
            label: "ट्रायल MOQ",
          },
          {
            value: "Container/pallet",
            label: "कंटेनर / पैलेट",
          },
          {
            value: "Ongoing monthly",
            label: "मासिक निरंतर",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "नाम",
        placeholder: "आपका नाम",
      },
      {
        type: "email",
        name: "email",
        label: "ईमेल",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "संदेश",
      name: "message",
      placeholder: "SKU रुचि (पाउडर / गमी), फ्लेवर, पैकेजिंग, शिप-टू देश, समयसीमा, आवश्यक प्रमाणपत्र…",
      rows: 3,
    },
    disclaimer: {
      label: "मैं OEM, प्राइवेट लेबल और थोक पूछताछ के लिए Crest Creatine से संपर्क स्वीकार करता/करती हूँ।",
    },
    button: "अभी B2B कोट प्राप्त करें",
    description: "अपना खरीदार प्रकार और मात्रा बताएं — हम कार्य दिवसों में 24 घंटे में MOQ स्तर, सैंपल विकल्प और अगले चरण भेजते हैं।",
    close: "बंद करें",
    preferChat: "चैट पसंद है?",
    waLead: {
      title: "WhatsApp पर चैट",
      subtitle: "पहले संक्षिप्त विवरण — फैक्टरी कोट चैट में जारी।",
      button: "WhatsApp पर जारी रखें",
      description: "हम आपका कोट अनुरोध सहेजते हैं, फिर WhatsApp खोलते हैं।",
      disclaimerLabel: "आप सहमत हैं कि हम इस OEM / थोक पूछताछ के लिए ईमेल या WhatsApp से संपर्क कर सकते हैं।",
    },
  },
  es: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "Soy",
        placeholder: "Seleccionar…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Marca",
          },
          {
            value: "Distributor",
            label: "Distribuidor",
          },
          {
            value: "Gym or retailer",
            label: "Gimnasio o minorista",
          },
          {
            value: "Online seller",
            label: "Vendedor online",
          },
          {
            value: "Other",
            label: "Otro",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "Busco",
        placeholder: "Seleccionar…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / marca privada",
          },
          {
            value: "Wholesale pricing",
            label: "Precios mayoreo",
          },
          {
            value: "Sample",
            label: "Muestra",
          },
          {
            value: "Bulk powder",
            label: "Polvo a granel",
          },
          {
            value: "Bulk gummies",
            label: "Gomitas a granel",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Volumen esperado",
        placeholder: "Seleccionar…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Muestra",
          },
          {
            value: "Trial MOQ",
            label: "MOQ de prueba",
          },
          {
            value: "Container/pallet",
            label: "Contenedor / pallet",
          },
          {
            value: "Ongoing monthly",
            label: "Mensual continuo",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Nombre",
        placeholder: "Su nombre",
      },
      {
        type: "email",
        name: "email",
        label: "Correo",
        placeholder: "usted@empresa.com",
      },
    ],
    textarea: {
      label: "Mensaje",
      name: "message",
      placeholder: "SKU de interés (polvo / gomitas), sabor, empaque, país de envío, plazos, certificaciones…",
      rows: 3,
    },
    disclaimer: {
      label: "Acepto que Crest Creatine me contacte sobre consultas OEM, marca privada y mayoreo.",
    },
    button: "Obtener cotización B2B",
    description: "Indique tipo de comprador y volumen — respondemos con MOQ, muestras y siguientes pasos en 24 h laborables.",
    close: "Cerrar",
    preferChat: "¿Prefiere chat?",
    waLead: {
      title: "Chatear por WhatsApp",
      subtitle: "Primero datos rápidos — la cotización de fábrica sigue en el chat.",
      button: "Continuar a WhatsApp",
      description: "Guardamos su solicitud de cotización y abrimos WhatsApp.",
      disclaimerLabel: "Acepta que le contactemos sobre esta consulta OEM / mayoreo por correo o WhatsApp.",
    },
  },
  ar: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "أنا",
        placeholder: "اختر…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "علامة تجارية",
          },
          {
            value: "Distributor",
            label: "موزّع",
          },
          {
            value: "Gym or retailer",
            label: "صالة رياضية أو تاجر تجزئة",
          },
          {
            value: "Online seller",
            label: "بائع عبر الإنترنت",
          },
          {
            value: "Other",
            label: "أخرى",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "أبحث عن",
        placeholder: "اختر…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / علامة خاصة",
          },
          {
            value: "Wholesale pricing",
            label: "أسعار الجملة",
          },
          {
            value: "Sample",
            label: "عينة",
          },
          {
            value: "Bulk powder",
            label: "مسحوق بالجملة",
          },
          {
            value: "Bulk gummies",
            label: "علكات بالجملة",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "الحجم المتوقع",
        placeholder: "اختر…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "عينة",
          },
          {
            value: "Trial MOQ",
            label: "حد أدنى تجريبي",
          },
          {
            value: "Container/pallet",
            label: "حاوية / منصة",
          },
          {
            value: "Ongoing monthly",
            label: "شهري مستمر",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "الاسم",
        placeholder: "اسمك",
      },
      {
        type: "email",
        name: "email",
        label: "البريد الإلكتروني",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "الرسالة",
      name: "message",
      placeholder: "الاهتمام بالمنتج (مسحوق / علكات)، النكهة، التغليف، بلد الشحن، الجدول الزمني، الشهادات المطلوبة…",
      rows: 3,
    },
    disclaimer: {
      label: "أوافق على تواصل Crest Creatine معي بخصوص استفسارات OEM والعلامة الخاصة والجملة.",
    },
    button: "احصل على عرض سعر B2B الآن",
    description: "أخبرنا بنوع المشتري والحجم — نرد بطبقات الحد الأدنى والعينات والخطوات التالية خلال 24 ساعة في أيام العمل.",
    close: "إغلاق",
    preferChat: "تفضل الدردشة؟",
    waLead: {
      title: "الدردشة عبر واتساب",
      subtitle: "تفاصيل سريعة أولاً — عرض المصنع يتابع في الدردشة.",
      button: "المتابعة إلى واتساب",
      description: "نحفظ طلب عرض السعر ثم نفتح واتساب.",
      disclaimerLabel: "توافق على تواصلنا بخصوص استفسار OEM / الجملة عبر البريد أو واتساب.",
    },
  },
  fr: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "Je suis",
        placeholder: "Sélectionner…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Marque",
          },
          {
            value: "Distributor",
            label: "Distributeur",
          },
          {
            value: "Gym or retailer",
            label: "Salle de sport ou détaillant",
          },
          {
            value: "Online seller",
            label: "Vendeur en ligne",
          },
          {
            value: "Other",
            label: "Autre",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "Je cherche",
        placeholder: "Sélectionner…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / marque blanche",
          },
          {
            value: "Wholesale pricing",
            label: "Tarifs gros",
          },
          {
            value: "Sample",
            label: "Échantillon",
          },
          {
            value: "Bulk powder",
            label: "Poudre en vrac",
          },
          {
            value: "Bulk gummies",
            label: "Gummies en vrac",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Volume prévu",
        placeholder: "Sélectionner…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Échantillon",
          },
          {
            value: "Trial MOQ",
            label: "MOQ d’essai",
          },
          {
            value: "Container/pallet",
            label: "Conteneur / palette",
          },
          {
            value: "Ongoing monthly",
            label: "Mensuel récurrent",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Nom",
        placeholder: "Votre nom",
      },
      {
        type: "email",
        name: "email",
        label: "E-mail",
        placeholder: "vous@entreprise.com",
      },
    ],
    textarea: {
      label: "Message",
      name: "message",
      placeholder: "SKU d’intérêt (poudre / gummies), arôme, emballage, pays de livraison, délai, certifications…",
      rows: 3,
    },
    disclaimer: {
      label: "J’accepte d’être contacté(e) par Crest Creatine pour des demandes OEM, marque blanche et gros.",
    },
    button: "Obtenir un devis B2B",
    description: "Indiquez votre type d’acheteur et le volume — réponse sous 24 h ouvrées avec MOQ, échantillons et prochaines étapes.",
    close: "Fermer",
    preferChat: "Préférez le chat ?",
    waLead: {
      title: "Discuter sur WhatsApp",
      subtitle: "Détails rapides d’abord — le devis usine suit dans le chat.",
      button: "Continuer vers WhatsApp",
      description: "Nous enregistrons votre demande puis ouvrons WhatsApp.",
      disclaimerLabel: "Vous acceptez d’être contacté(e) pour cette demande OEM / gros par e-mail ou WhatsApp.",
    },
  },
  bn: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "আমি",
        placeholder: "নির্বাচন…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "ব্র্যান্ড",
          },
          {
            value: "Distributor",
            label: "ডিস্ট্রিবিউটর",
          },
          {
            value: "Gym or retailer",
            label: "জিম বা খুচরা বিক্রেতা",
          },
          {
            value: "Online seller",
            label: "অনলাইন বিক্রেতা",
          },
          {
            value: "Other",
            label: "অন্যান্য",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "আমি খুঁজছি",
        placeholder: "নির্বাচন…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / প্রাইভেট লেবেল",
          },
          {
            value: "Wholesale pricing",
            label: "হোলসেল মূল্য",
          },
          {
            value: "Sample",
            label: "নমুনা",
          },
          {
            value: "Bulk powder",
            label: "বাল্ক পাউডার",
          },
          {
            value: "Bulk gummies",
            label: "বাল্ক গামি",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "প্রত্যাশিত পরিমাণ",
        placeholder: "নির্বাচন…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "নমুনা",
          },
          {
            value: "Trial MOQ",
            label: "ট্রায়াল MOQ",
          },
          {
            value: "Container/pallet",
            label: "কন্টেইনার / প্যালেট",
          },
          {
            value: "Ongoing monthly",
            label: "মাসিক চলমান",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "নাম",
        placeholder: "আপনার নাম",
      },
      {
        type: "email",
        name: "email",
        label: "ইমেইল",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "বার্তা",
      name: "message",
      placeholder: "SKU আগ্রহ (পাউডার / গামি), ফ্লেভার, প্যাকেজিং, শিপ-টু দেশ, সময়সীমা, প্রয়োজনীয় সার্টিফিকেশন…",
      rows: 3,
    },
    disclaimer: {
      label: "আমি OEM, প্রাইভেট লেবেল ও হোলসেল অনুসন্ধান বিষয়ে Crest Creatine-এর যোগাযোগে সম্মত।",
    },
    button: "এখনই B2B কোট নিন",
    description: "ক্রেতার ধরন ও পরিমাণ জানান — কর্মদিবসে ২৪ ঘণ্টার মধ্যে MOQ স্তর, নমুনা ও পরবর্তী ধাপ জানাই।",
    close: "বন্ধ",
    preferChat: "চ্যাট পছন্দ?",
    waLead: {
      title: "WhatsApp-এ চ্যাট",
      subtitle: "আগে সংক্ষিপ্ত তথ্য — কারখানার কোট চ্যাটে চলবে।",
      button: "WhatsApp-এ চালিয়ে যান",
      description: "আমরা আপনার কোট অনুরোধ সংরক্ষণ করে WhatsApp খুলি।",
      disclaimerLabel: "আপনি সম্মত যে আমরা এই OEM / হোলসেল অনুসন্ধান বিষয়ে ইমেইল বা WhatsApp-এ যোগাযোগ করতে পারি।",
    },
  },
  pt: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "Sou",
        placeholder: "Selecionar…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Marca",
          },
          {
            value: "Distributor",
            label: "Distribuidor",
          },
          {
            value: "Gym or retailer",
            label: "Academia ou varejista",
          },
          {
            value: "Online seller",
            label: "Vendedor online",
          },
          {
            value: "Other",
            label: "Outro",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "Procuro",
        placeholder: "Selecionar…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / private label",
          },
          {
            value: "Wholesale pricing",
            label: "Preços atacado",
          },
          {
            value: "Sample",
            label: "Amostra",
          },
          {
            value: "Bulk powder",
            label: "Pó a granel",
          },
          {
            value: "Bulk gummies",
            label: "Gummies a granel",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Volume esperado",
        placeholder: "Selecionar…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Amostra",
          },
          {
            value: "Trial MOQ",
            label: "MOQ de teste",
          },
          {
            value: "Container/pallet",
            label: "Contêiner / pallet",
          },
          {
            value: "Ongoing monthly",
            label: "Mensal contínuo",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Nome",
        placeholder: "Seu nome",
      },
      {
        type: "email",
        name: "email",
        label: "E-mail",
        placeholder: "voce@empresa.com",
      },
    ],
    textarea: {
      label: "Mensagem",
      name: "message",
      placeholder: "SKU de interesse (pó / gummies), sabor, embalagem, país de destino, prazo, certificações…",
      rows: 3,
    },
    disclaimer: {
      label: "Concordo em ser contatado(a) pela Crest Creatine sobre consultas OEM, private label e atacado.",
    },
    button: "Obter orçamento B2B",
    description: "Informe o tipo de comprador e volume — respondemos com MOQ, amostras e próximos passos em até 24 h úteis.",
    close: "Fechar",
    preferChat: "Prefere chat?",
    waLead: {
      title: "Conversar no WhatsApp",
      subtitle: "Detalhes rápidos primeiro — orçamento de fábrica segue no chat.",
      button: "Continuar no WhatsApp",
      description: "Salvamos sua solicitação e abrimos o WhatsApp.",
      disclaimerLabel: "Você concorda que possamos contatá-lo(a) sobre esta consulta OEM / atacado por e-mail ou WhatsApp.",
    },
  },
  ru: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "Я",
        placeholder: "Выберите…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Бренд",
          },
          {
            value: "Distributor",
            label: "Дистрибьютор",
          },
          {
            value: "Gym or retailer",
            label: "Зал или ритейл",
          },
          {
            value: "Online seller",
            label: "Онлайн-продавец",
          },
          {
            value: "Other",
            label: "Другое",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "Мне нужно",
        placeholder: "Выберите…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / private label",
          },
          {
            value: "Wholesale pricing",
            label: "Оптовые цены",
          },
          {
            value: "Sample",
            label: "Образец",
          },
          {
            value: "Bulk powder",
            label: "Порошок оптом",
          },
          {
            value: "Bulk gummies",
            label: "Жевательные оптом",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Ожидаемый объём",
        placeholder: "Выберите…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Образец",
          },
          {
            value: "Trial MOQ",
            label: "Пробный MOQ",
          },
          {
            value: "Container/pallet",
            label: "Контейнер / паллет",
          },
          {
            value: "Ongoing monthly",
            label: "Ежемесячно",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Имя",
        placeholder: "Ваше имя",
      },
      {
        type: "email",
        name: "email",
        label: "Эл. почта",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "Сообщение",
      name: "message",
      placeholder: "Интерес к SKU (порошок / жевательные), вкус, упаковка, страна доставки, сроки, сертификаты…",
      rows: 3,
    },
    disclaimer: {
      label: "Соглашаюсь на связь с Crest Creatine по запросам OEM, private label и опта.",
    },
    button: "Получить B2B КП",
    description: "Укажите тип покупателя и объём — ответим с уровнями MOQ, образцами и следующими шагами в течение 24 часов в рабочие дни.",
    close: "Закрыть",
    preferChat: "Предпочитаете чат?",
    waLead: {
      title: "Чат в WhatsApp",
      subtitle: "Сначала краткие данные — заводское КП продолжим в чате.",
      button: "Перейти в WhatsApp",
      description: "Сохраняем заявку и открываем WhatsApp.",
      disclaimerLabel: "Вы соглашаетесь, что мы можем связаться по этому OEM / оптовому запросу по email или WhatsApp.",
    },
  },
  ur: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "میں ہوں",
        placeholder: "منتخب کریں…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "برانڈ",
          },
          {
            value: "Distributor",
            label: "ڈسٹری بیوٹر",
          },
          {
            value: "Gym or retailer",
            label: "جم یا ریٹیلر",
          },
          {
            value: "Online seller",
            label: "آن لائن فروخت کنندہ",
          },
          {
            value: "Other",
            label: "دیگر",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "میں تلاش کر رہا/رہی ہوں",
        placeholder: "منتخب کریں…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / پرائیویٹ لیبل",
          },
          {
            value: "Wholesale pricing",
            label: "ہول سیل قیمت",
          },
          {
            value: "Sample",
            label: "سیمپل",
          },
          {
            value: "Bulk powder",
            label: "بلک پاؤڈر",
          },
          {
            value: "Bulk gummies",
            label: "بلک گمیز",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "متوقع مقدار",
        placeholder: "منتخب کریں…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "سیمپل",
          },
          {
            value: "Trial MOQ",
            label: "ٹرائل MOQ",
          },
          {
            value: "Container/pallet",
            label: "کنٹینر / پیلیٹ",
          },
          {
            value: "Ongoing monthly",
            label: "ماہانہ جاری",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "نام",
        placeholder: "آپ کا نام",
      },
      {
        type: "email",
        name: "email",
        label: "ای میل",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "پیغام",
      name: "message",
      placeholder: "SKU دلچسپی (پاؤڈر / گمیز)، فلیور، پیکجنگ، شپ ٹو ملک، ٹائم لائن، سرٹیفیکیشنز…",
      rows: 3,
    },
    disclaimer: {
      label: "میں OEM، پرائیویٹ لیبل اور ہول سیل استفسارات کے بارے میں Crest Creatine سے رابطے پر رضامند ہوں۔",
    },
    button: "ابھی B2B کوٹ حاصل کریں",
    description: "اپنا خریدار کی قسم اور مقدار بتائیں — ہم کاروباری دنوں میں 24 گھنٹوں میں MOQ درجات، سیمپل اور اگلے مراحل بھیجتے ہیں۔",
    close: "بند کریں",
    preferChat: "چیٹ پسند ہے؟",
    waLead: {
      title: "WhatsApp پر چیٹ",
      subtitle: "پہلے مختصر تفصیلات — فیکٹری کوٹ چیٹ میں جاری۔",
      button: "WhatsApp پر جاری رکھیں",
      description: "ہم آپ کی کوٹ درخواست محفوظ کر کے WhatsApp کھولتے ہیں۔",
      disclaimerLabel: "آپ رضامند ہیں کہ ہم اس OEM / ہول سیل استفسار کے لیے ای میل یا WhatsApp سے رابطہ کر سکتے ہیں۔",
    },
  },
  id: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "Saya adalah",
        placeholder: "Pilih…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Merek",
          },
          {
            value: "Distributor",
            label: "Distributor",
          },
          {
            value: "Gym or retailer",
            label: "Gym atau retailer",
          },
          {
            value: "Online seller",
            label: "Penjual online",
          },
          {
            value: "Other",
            label: "Lainnya",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "Saya mencari",
        placeholder: "Pilih…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / private label",
          },
          {
            value: "Wholesale pricing",
            label: "Harga grosir",
          },
          {
            value: "Sample",
            label: "Sampel",
          },
          {
            value: "Bulk powder",
            label: "Bubuk curah",
          },
          {
            value: "Bulk gummies",
            label: "Gummy curah",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Volume yang diharapkan",
        placeholder: "Pilih…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Sampel",
          },
          {
            value: "Trial MOQ",
            label: "MOQ uji coba",
          },
          {
            value: "Container/pallet",
            label: "Kontainer / palet",
          },
          {
            value: "Ongoing monthly",
            label: "Bulanan berkelanjutan",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Nama",
        placeholder: "Nama Anda",
      },
      {
        type: "email",
        name: "email",
        label: "Email",
        placeholder: "anda@perusahaan.com",
      },
    ],
    textarea: {
      label: "Pesan",
      name: "message",
      placeholder: "Minat SKU (bubuk / gummy), rasa, kemasan, negara tujuan, timeline, sertifikasi…",
      rows: 3,
    },
    disclaimer: {
      label: "Saya setuju dihubungi Crest Creatine terkait pertanyaan OEM, private label, dan grosir.",
    },
    button: "Dapatkan penawaran B2B",
    description: "Beritahu tipe pembeli dan volume — kami balas dengan tingkatan MOQ, opsi sampel, dan langkah berikutnya dalam 24 jam hari kerja.",
    close: "Tutup",
    preferChat: "Lebih suka chat?",
    waLead: {
      title: "Chat di WhatsApp",
      subtitle: "Detail singkat dulu — penawaran pabrik lanjut di chat.",
      button: "Lanjut ke WhatsApp",
      description: "Kami menyimpan permintaan penawaran, lalu membuka WhatsApp.",
      disclaimerLabel: "Anda setuju kami dapat menghubungi Anda tentang pertanyaan OEM / grosir ini via email atau WhatsApp.",
    },
  },
  de: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "Ich bin",
        placeholder: "Auswählen…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Marke",
          },
          {
            value: "Distributor",
            label: "Distributor",
          },
          {
            value: "Gym or retailer",
            label: "Studio oder Einzelhandel",
          },
          {
            value: "Online seller",
            label: "Online-Händler",
          },
          {
            value: "Other",
            label: "Sonstiges",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "Ich suche",
        placeholder: "Auswählen…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / Private Label",
          },
          {
            value: "Wholesale pricing",
            label: "Großhandelspreise",
          },
          {
            value: "Sample",
            label: "Muster",
          },
          {
            value: "Bulk powder",
            label: "Bulk-Pulver",
          },
          {
            value: "Bulk gummies",
            label: "Bulk-Gummies",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Erwartetes Volumen",
        placeholder: "Auswählen…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Muster",
          },
          {
            value: "Trial MOQ",
            label: "Probe-MOQ",
          },
          {
            value: "Container/pallet",
            label: "Container / Palette",
          },
          {
            value: "Ongoing monthly",
            label: "Laufend monatlich",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Name",
        placeholder: "Ihr Name",
      },
      {
        type: "email",
        name: "email",
        label: "E-Mail",
        placeholder: "sie@firma.com",
      },
    ],
    textarea: {
      label: "Nachricht",
      name: "message",
      placeholder: "SKU-Interesse (Pulver / Gummies), Geschmack, Verpackung, Zielland, Zeitplan, Zertifikate…",
      rows: 3,
    },
    disclaimer: {
      label: "Ich stimme zu, dass Crest Creatine mich zu OEM-, Private-Label- und Großhandelsanfragen kontaktiert.",
    },
    button: "Jetzt B2B-Angebot erhalten",
    description: "Nennen Sie Käufertyp und Volumen — Antwort mit MOQ-Stufen, Mustern und nächsten Schritten innerhalb von 24 Stunden an Werktagen.",
    close: "Schließen",
    preferChat: "Lieber chat?",
    waLead: {
      title: "Per WhatsApp chatten",
      subtitle: "Zuerst Kurzinfos — Fabrikangebot folgt im Chat.",
      button: "Weiter zu WhatsApp",
      description: "Wir speichern Ihre Anfrage und öffnen WhatsApp.",
      disclaimerLabel: "Sie stimmen zu, dass wir Sie zu dieser OEM-/Großhandelsanfrage per E-Mail oder WhatsApp kontaktieren dürfen.",
    },
  },
  ja: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "私は",
        placeholder: "選択…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "ブランド",
          },
          {
            value: "Distributor",
            label: "代理店",
          },
          {
            value: "Gym or retailer",
            label: "ジム／小売",
          },
          {
            value: "Online seller",
            label: "ネット販売",
          },
          {
            value: "Other",
            label: "その他",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "ご用件",
        placeholder: "選択…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM／プライベートラベル",
          },
          {
            value: "Wholesale pricing",
            label: "卸売価格",
          },
          {
            value: "Sample",
            label: "サンプル",
          },
          {
            value: "Bulk powder",
            label: "バルク粉末",
          },
          {
            value: "Bulk gummies",
            label: "バルク・グミ",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "想定数量",
        placeholder: "選択…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "サンプル",
          },
          {
            value: "Trial MOQ",
            label: "トライアルMOQ",
          },
          {
            value: "Container/pallet",
            label: "コンテナ／パレット",
          },
          {
            value: "Ongoing monthly",
            label: "毎月継続",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "お名前",
        placeholder: "お名前",
      },
      {
        type: "email",
        name: "email",
        label: "メール",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "メッセージ",
      name: "message",
      placeholder: "ご関心SKU（粉末／グミ）、フレーバー、包装、出荷先国、希望時期、必要な認証…",
      rows: 3,
    },
    disclaimer: {
      label: "OEM・プライベートラベル・卸売の問い合わせについてCrest Creatineからの連絡に同意します。",
    },
    button: "B2B見積を今すぐ",
    description: "バイヤー種別と数量をお知らせください。営業日24時間以内にMOQ階層・サンプル・次のステップをご返信します。",
    close: "閉じる",
    preferChat: "チャット希望？",
    waLead: {
      title: "WhatsAppでチャット",
      subtitle: "まず簡単な情報 — 工場見積はチャットで続きます。",
      button: "WhatsAppへ進む",
      description: "見積依頼を保存してからWhatsAppを開きます。",
      disclaimerLabel: "本OEM／卸売のお問い合わせについて、メールまたはWhatsAppでの連絡に同意します。",
    },
  },
  ko: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "저는",
        placeholder: "선택…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "브랜드",
          },
          {
            value: "Distributor",
            label: "유통사",
          },
          {
            value: "Gym or retailer",
            label: "헬스장 또는 리테일",
          },
          {
            value: "Online seller",
            label: "온라인 판매자",
          },
          {
            value: "Other",
            label: "기타",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "문의 유형",
        placeholder: "선택…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / 프라이빗 라벨",
          },
          {
            value: "Wholesale pricing",
            label: "도매 가격",
          },
          {
            value: "Sample",
            label: "샘플",
          },
          {
            value: "Bulk powder",
            label: "벌크 파우더",
          },
          {
            value: "Bulk gummies",
            label: "벌크 구미",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "예상 물량",
        placeholder: "선택…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "샘플",
          },
          {
            value: "Trial MOQ",
            label: "시험 MOQ",
          },
          {
            value: "Container/pallet",
            label: "컨테이너 / 팔레트",
          },
          {
            value: "Ongoing monthly",
            label: "월간 지속",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "이름",
        placeholder: "성함",
      },
      {
        type: "email",
        name: "email",
        label: "이메일",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "메시지",
      name: "message",
      placeholder: "관심 SKU(파우더/구미), 맛, 포장, 배송국, 일정, 필요 인증…",
      rows: 3,
    },
    disclaimer: {
      label: "OEM, 프라이빗 라벨, 도매 문의와 관련하여 Crest Creatine의 연락에 동의합니다.",
    },
    button: "지금 B2B 견적 받기",
    description: "구매자 유형과 물량을 알려 주세요. 영업일 기준 24시간 내 MOQ 구간, 샘플 옵션, 다음 단계를 회신합니다.",
    close: "닫기",
    preferChat: "채팅을 원하시나요?",
    waLead: {
      title: "WhatsApp 채팅",
      subtitle: "먼저 간단한 정보 — 공장 견적은 채팅에서 이어집니다.",
      button: "WhatsApp으로 계속",
      description: "견적 요청을 저장한 뒤 WhatsApp을 엽니다.",
      disclaimerLabel: "본 OEM/도매 문의와 관련하여 이메일 또는 WhatsApp으로 연락할 수 있음에 동의합니다.",
    },
  },
  vi: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "Tôi là",
        placeholder: "Chọn…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "Thương hiệu",
          },
          {
            value: "Distributor",
            label: "Nhà phân phối",
          },
          {
            value: "Gym or retailer",
            label: "Phòng gym hoặc bán lẻ",
          },
          {
            value: "Online seller",
            label: "Người bán online",
          },
          {
            value: "Other",
            label: "Khác",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "Tôi cần",
        placeholder: "Chọn…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / nhãn riêng",
          },
          {
            value: "Wholesale pricing",
            label: "Giá sỉ",
          },
          {
            value: "Sample",
            label: "Mẫu",
          },
          {
            value: "Bulk powder",
            label: "Bột số lượng lớn",
          },
          {
            value: "Bulk gummies",
            label: "Kẹo dẻo số lượng lớn",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "Khối lượng dự kiến",
        placeholder: "Chọn…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "Mẫu",
          },
          {
            value: "Trial MOQ",
            label: "MOQ thử",
          },
          {
            value: "Container/pallet",
            label: "Container / pallet",
          },
          {
            value: "Ongoing monthly",
            label: "Hàng tháng liên tục",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "Họ tên",
        placeholder: "Tên của bạn",
      },
      {
        type: "email",
        name: "email",
        label: "Email",
        placeholder: "ban@congty.com",
      },
    ],
    textarea: {
      label: "Tin nhắn",
      name: "message",
      placeholder: "SKU quan tâm (bột / kẹo dẻo), hương vị, bao bì, quốc gia giao hàng, thời gian, chứng nhận…",
      rows: 3,
    },
    disclaimer: {
      label: "Tôi đồng ý để Crest Creatine liên hệ về yêu cầu OEM, nhãn riêng và bán sỉ.",
    },
    button: "Nhận báo giá B2B ngay",
    description: "Cho chúng tôi biết loại người mua và khối lượng — phản hồi MOQ, mẫu và bước tiếp theo trong 24 giờ làm việc.",
    close: "Đóng",
    preferChat: "Thích chat hơn?",
    waLead: {
      title: "Chat trên WhatsApp",
      subtitle: "Thông tin ngắn trước — báo giá nhà máy tiếp tục trên chat.",
      button: "Tiếp tục tới WhatsApp",
      description: "Chúng tôi lưu yêu cầu báo giá rồi mở WhatsApp.",
      disclaimerLabel: "Bạn đồng ý chúng tôi có thể liên hệ về yêu cầu OEM / bán sỉ này qua email hoặc WhatsApp.",
    },
  },
  th: {
    inputs: [
      {
        type: "select",
        name: "company",
        label: "ฉันเป็น",
        placeholder: "เลือก…",
        required: true,
        options: [
          {
            value: "Brand",
            label: "แบรนด์",
          },
          {
            value: "Distributor",
            label: "ตัวแทนจำหน่าย",
          },
          {
            value: "Gym or retailer",
            label: "ยิมหรือร้านค้าปลีก",
          },
          {
            value: "Online seller",
            label: "ผู้ขายออนไลน์",
          },
          {
            value: "Other",
            label: "อื่นๆ",
          },
        ],
      },
      {
        type: "select",
        name: "channel",
        label: "ฉันต้องการ",
        placeholder: "เลือก…",
        required: true,
        options: [
          {
            value: "OEM/Private label",
            label: "OEM / ไพรเวทเลเบล",
          },
          {
            value: "Wholesale pricing",
            label: "ราคาขายส่ง",
          },
          {
            value: "Sample",
            label: "ตัวอย่าง",
          },
          {
            value: "Bulk powder",
            label: "ผงปริมาณมาก",
          },
          {
            value: "Bulk gummies",
            label: "กัมมี่ปริมาณมาก",
          },
        ],
      },
      {
        type: "select",
        name: "volume",
        label: "ปริมาณที่คาดหวัง",
        placeholder: "เลือก…",
        required: true,
        options: [
          {
            value: "Sample",
            label: "ตัวอย่าง",
          },
          {
            value: "Trial MOQ",
            label: "MOQ ทดลอง",
          },
          {
            value: "Container/pallet",
            label: "ตู้คอนเทนเนอร์ / พาเลท",
          },
          {
            value: "Ongoing monthly",
            label: "รายเดือนต่อเนื่อง",
          },
        ],
      },
      {
        type: "text",
        name: "name",
        label: "ชื่อ",
        placeholder: "ชื่อของคุณ",
      },
      {
        type: "email",
        name: "email",
        label: "อีเมล",
        placeholder: "you@company.com",
      },
    ],
    textarea: {
      label: "ข้อความ",
      name: "message",
      placeholder: "SKU ที่สนใจ (ผง / กัมมี่) รสชาติ บรรจุภัณฑ์ ประเทศจัดส่ง ไทม์ไลน์ การรับรองที่ต้องการ…",
      rows: 3,
    },
    disclaimer: {
      label: "ฉันยินยอมให้ Crest Creatine ติดต่อเกี่ยวกับการสอบถาม OEM ไพรเวทเลเบล และขายส่ง",
    },
    button: "รับใบเสนอราคา B2B ทันที",
    description: "บอกประเภทผู้ซื้อและปริมาณ — เราตอบกลับชั้น MOQ ตัวเลือกตัวอย่าง และขั้นตอนถัดไปภายใน 24 ชั่วโมงในวันทำการ",
    close: "ปิด",
    preferChat: "ชอบแชท?",
    waLead: {
      title: "แชทบน WhatsApp",
      subtitle: "รายละเอียดสั้นก่อน — ใบเสนอราคาโรงงานต่อในแชท",
      button: "ไปต่อที่ WhatsApp",
      description: "เราบันทึกคำขอใบเสนอราคาแล้วเปิด WhatsApp",
      disclaimerLabel: "คุณยินยอมให้เราติดต่อเกี่ยวกับการสอบถาม OEM / ขายส่งนี้ทางอีเมลหรือ WhatsApp",
    },
  },
};

export function getInquiryForm(locale: Locale = 'en') {
  const f = FORMS[locale] ?? FORMS.en;
  const waLead = {
    inputs: f.inputs,
    textarea: { ...f.textarea, rows: 2 },
    disclaimer: { label: f.waLead.disclaimerLabel },
    button: f.waLead.button,
    description: f.waLead.description,
    title: f.waLead.title,
    subtitle: f.waLead.subtitle,
  };
  return {
    inputs: f.inputs,
    textarea: f.textarea,
    disclaimer: f.disclaimer,
    button: f.button,
    description: f.description,
    close: f.close,
    preferChat: f.preferChat,
    waLead,
  };
}
