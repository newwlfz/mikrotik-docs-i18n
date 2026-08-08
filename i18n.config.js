// 项目多语言全局配置文件
const SUPPORTED_LOCALES = {
  // ================= 默认开启语种 =================
  'zh-Hans': {
    enabled: true,
    label: '简体中文',
    promptName: '简体中文（请使用中国大陆网络工程及路由技术标准专业术语）',
    detectPrefixes: ['zh-cn', 'zh-sg', 'zh'],
    announcement: '🤖 本文档由 DeepSeek AI 通过 GitHub Actions 自动翻译（最后更新于：{time}），内容仅供参考。',
    dropdownLabels: {
      hover: '🔍 悬停显示原文',
      collapse: '📖 折叠显示原文',
      clean: '📄 仅显示中文',
    },
  },
  'zh-Hant': {
    enabled: false,
    label: '繁體中文',
    promptName: '繁體中文（請使用台灣/香港網絡工程及路由技術標準專業術語）',
    detectPrefixes: ['zh-tw', 'zh-hk', 'zh-mo', 'zh-hant'],
    announcement: '🤖 本文檔由 DeepSeek AI 透過 GitHub Actions 自動翻譯（最後更新於：{time}），內容僅供參考。',
    dropdownLabels: {
      hover: '🔍 懸停顯示原文',
      collapse: '📖 折疊顯示原文',
      clean: '📄 僅顯示中文',
    },
  },

  // ================= 预置扩展语种（将 enabled 改为 true 即可一键启用） =================
  ja: {
    enabled: false,
    label: '日本語',
    promptName: '日本語（日本のネットワーク工学およびルーター技術の標準専門用語を使用してください）',
    detectPrefixes: ['ja'],
    announcement: '🤖 本ドキュメントは GitHub Actions 経由で DeepSeek AI により自動翻訳されています（最終更新：{time}）。参考情報としてのみご活用ください。',
    dropdownLabels: {
      hover: '🔍 ホバーで原文表示',
      collapse: '📖 折りたたみ表示',
      clean: '📄 翻訳のみ表示',
    },
  },
  ko: {
    enabled: false,
    label: '한국어',
    promptName: '한국어（대한민국 네트워크 공학 및 라우팅 기술 표준 전문 용어를 사용하십시오）',
    detectPrefixes: ['ko'],
    announcement: '🤖 본 문서의 번역은 GitHub Actions를 통해 DeepSeek AI로 자동 생성되었으며（최종 업데이트: {time}）, 참고용으로만 제공됩니다.',
    dropdownLabels: {
      hover: '🔍 원문 호버 보기',
      collapse: '📖 접기/펼치기',
      clean: '📄 번역만 보기',
    },
  },
  es: {
    enabled: false,
    label: 'Español',
    promptName: 'Spanish (Use standard network engineering and routing technical terminology used in Spain and Latin America)',
    detectPrefixes: ['es'],
    announcement: '🤖 Documento traducido automáticamente por DeepSeek AI mediante GitHub Actions (Última actualización: {time}). Solo para referencia.',
    dropdownLabels: {
      hover: '🔍 Pasamiento para original',
      collapse: '📖 Plegar original',
      clean: '📄 Solo traducción',
    },
  },
  pt: {
    enabled: false,
    label: 'Português',
    promptName: 'Portuguese (Use standard network engineering and routing technical terminology used in Brazil and Portugal)',
    detectPrefixes: ['pt'],
    announcement: '🤖 Documento traduzido automaticamente pelo DeepSeek AI via GitHub Actions (Última atualização: {time}). Apenas para referência.',
    dropdownLabels: {
      hover: '🔍 Passe para ver original',
      collapse: '📖 Recolher original',
      clean: '📄 Apenas tradução',
    },
  },
  fr: {
    enabled: false,
    label: 'Français',
    promptName: 'French (Use standard network engineering and routing technical terminology used in France and Francophone regions)',
    detectPrefixes: ['fr'],
    announcement: '🤖 Ce document est traduit automatiquement par DeepSeek AI via GitHub Actions (Dernière mise à jour : {time}). À titre indicatif uniquement.',
    dropdownLabels: {
      hover: '🔍 Survoler pour l\'original',
      collapse: '📖 Masquer l\'original',
      clean: '📄 Traduction uniquement',
    },
  },
  de: {
    enabled: false,
    label: 'Deutsch',
    promptName: 'German (Use standard network engineering and routing technical terminology used in Germany, Austria, and Switzerland)',
    detectPrefixes: ['de'],
    announcement: '🤖 Dieses Dokument wurde automatisch von DeepSeek AI über GitHub Actions übersetzt (Letzte Aktualisierung: {time}). Nur zur Information.',
    dropdownLabels: {
      hover: '🔍 Hover für Original',
      collapse: '📖 Original einklappen',
      clean: '📄 Nur Übersetzung',
    },
  },
  ru: {
    enabled: false,
    label: 'Русский',
    promptName: 'Russian (Используйте стандартную техническую терминологию сетевой инженерии и маршрутизации)',
    detectPrefixes: ['ru'],
    announcement: '🤖 Этот документ автоматически переведен DeepSeek AI через GitHub Actions (Последнее обновление: {time}). Только для справки.',
    dropdownLabels: {
      hover: '🔍 Оригинал при наведении',
      collapse: '📖 Свернуть оригинал',
      clean: '📄 Только перевод',
    },
  },
  it: {
    enabled: false,
    label: 'Italiano',
    promptName: 'Italian (Use standard network engineering and routing technical terminology used in Italy)',
    detectPrefixes: ['it'],
    announcement: '🤖 Questo documento è tradotto automaticamente da DeepSeek AI tramite GitHub Actions (Ultimo aggiornamento: {time}). Solo a scopo di riferimento.',
    dropdownLabels: {
      hover: '🔍 Passa sopra per originale',
      collapse: '📖 Comprimi originale',
      clean: '📄 Solo traduzione',
    },
  },
  tr: {
    enabled: false,
    label: 'Türkçe',
    promptName: 'Turkish (Lütfen Türkiye\'deki ağ mühendisliği ve yönlendirme teknolojisi standart terimlerini kullanın)',
    detectPrefixes: ['tr'],
    announcement: '🤖 Bu belge GitHub Actions aracılığıyla DeepSeek AI tarafından otomatik olarak çevrilmiştir (Son güncelleme: {time}). Yalnızca referans içindir.',
    dropdownLabels: {
      hover: '🔍 Orijinali görmek için üzerine gelin',
      collapse: '📖 Orijinali gizle',
      clean: '📄 Sadece çeviri',
    },
  },
  vi: {
    enabled: false,
    label: 'Tiếng Việt',
    promptName: 'Tiếng Việt (Vui lòng sử dụng thuật ngữ kỹ thuật tiêu chuẩn về kỹ thuật mạng và định tuyến tại Việt Nam)',
    detectPrefixes: ['vi'],
    announcement: '🤖 Tài liệu này được dịch tự động bởi DeepSeek AI qua GitHub Actions (Cập nhật lần cuối: {time}). Chỉ mang tính chất tham khảo.',
    dropdownLabels: {
      hover: '🔍 Di chuột để xem gốc',
      collapse: '📖 Thu gọn văn bản gốc',
      clean: '📄 Chỉ hiển thị bản dịch',
    },
  },
  th: {
    enabled: false,
    label: 'ไทย',
    promptName: 'Thai (โปรดใช้คำศัพท์ทางเทคนิคมาตรฐานวิศวกรรมเครือข่ายและการเส้นทางในประเทศไทย)',
    detectPrefixes: ['th'],
    announcement: '🤖 เอกสารนี้ได้รับการแปลโดยออโตเมติกโดย DeepSeek AI ผ่าน GitHub Actions (อัปเดตล่าสุด: {time}) เพื่อการอ้างอิงเท่านั้น',
    dropdownLabels: {
      hover: '🔍 วางเมาส์เพื่อดูต้นฉบับ',
      collapse: '📖 พับเก็บต้นฉบับ',
      clean: '📄 แสดงเฉพาะคำแปล',
    },
  },
  ar: {
    enabled: false,
    label: 'العربية',
    promptName: 'Arabic (Please use standard network engineering and routing technical terminology used in the Arab world)',
    detectPrefixes: ['ar'],
    announcement: '🤖 تم ترجمة هذه الوثيقة تلقائيًا بواسطة DeepSeek AI عبر GitHub Actions (آخر تحديث: {time}). للإشارة فقط.',
    dropdownLabels: {
      hover: '🔍 مرر للرؤية الأصلي',
      collapse: '📖 طي النص الأصلي',
      clean: '📄 الترجمة فقط',
    },
  },
};

const activeLocales = Object.keys(SUPPORTED_LOCALES).filter(
  (key) => SUPPORTED_LOCALES[key].enabled
);

module.exports = {
  SUPPORTED_LOCALES,
  activeLocales,
};
