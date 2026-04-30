const fs = require('fs');
const path = require('path');

const baseDir = '/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/multi_lang_v1';

const languages38 = [
    { code: 'en', name: 'English', native: 'English' },
    { code: 'ar', name: 'Arabic', native: 'العربية' },
    { code: 'de', name: 'German', native: 'Deutsch' },
    { code: 'es', name: 'Spanish', native: 'Español' },
    { code: 'fr', name: 'French', native: 'Français' },
    { code: 'it', name: 'Italian', native: 'Italiano' },
    { code: 'ja', name: 'Japanese', native: '日本語' },
    { code: 'ko', name: 'Korean', native: '한국어' },
    { code: 'pt', name: 'Portuguese', native: 'Português' },
    { code: 'ru', name: 'Russian', native: 'Русский' },
    { code: 'tr', name: 'Turkish', native: 'Türkçe' },
    { code: 'hi', name: 'Hindi', native: 'हिन्दी' },
    { code: 'bn', name: 'Bengali', native: 'বাংলা' },
    { code: 'id', name: 'Indonesian', native: 'Bahasa Indonesia' },
    { code: 'vi', name: 'Vietnamese', native: 'Tiếng Việt' },
    { code: 'th', name: 'Thai', native: 'ไทย' },
    { code: 'pl', name: 'Polish', native: 'Polski' },
    { code: 'nl', name: 'Dutch', native: 'Nederlands' },
    { code: 'fa', name: 'Persian', native: 'فارسی' },
    { code: 'ur', name: 'Urdu', native: 'اردو' },
    { code: 'cs', name: 'Czech', native: 'Čeština' },
    { code: 'da', name: 'Danish', native: 'Dansk' },
    { code: 'el', name: 'Greek', native: 'Ελληνικά' },
    { code: 'hu', name: 'Hungarian', native: 'Magyar' },
    { code: 'sv', name: 'Swedish', native: 'Svenska' },
    { code: 'fi', name: 'Finnish', native: 'Suomi' },
    { code: 'kk', name: 'Kazakh', native: 'Қазақша' },
    { code: 'no', name: 'Norwegian', native: 'Norsk' },
    { code: 'ro', name: 'Romanian', native: 'Română' },
    { code: 'sr', name: 'Serbian', native: 'Srpski' },
    { code: 'ky', name: 'Kyrgyz', native: 'Кыргызча' },
    { code: 'tg', name: 'Tajik', native: 'Тоҷикӣ' },
    { code: 'tk', name: 'Turkmen', native: 'Türkmen' },
    { code: 'uz', name: 'Uzbek', native: 'O\'zbek' },
    { code: 'my', name: 'Burmese', native: 'မြန်မာစာ' },
    { code: 'km', name: 'Khmer', native: 'ភាសាខ្មែរ' },
    { code: 'ne', name: 'Nepali', native: 'नेपाली' },
    { code: 'az', name: 'Azerbaijani', native: 'Azərbaycan' }
];

const translations = {
    tr: {
        title: "Modern Endüstriyel Mükemmellik",
        logo: "IndEx Corp",
        heroTitle: "Endüstriyel Teknolojinin Geleceğine Öncülük Ediyoruz",
        heroSub: "Hassas mühendislik, küresel etki ve sürdürülebilir inovasyon.",
        servicesTitle: "Hizmetlerimiz",
        s1Title: "Gelişmiş Üretim",
        s1Desc: "Eşsiz hassasiyet için yapay zeka ve robotik kullanan son teknoloji tesisler.",
        s2Title: "Sürdürülebilir Enerji",
        s2Desc: "Temiz enerji teknolojisi ile daha yeşil bir endüstriyel gelecek için yenilikçi çözümler.",
        s3Title: "Küresel Lojistik",
        s3Desc: "Kesintisiz küresel operasyonlar sağlayan akıllı tedarik zinciri yönetim sistemleri.",
        footer: "© 2026 Industrial Excellence Corp. Tüm hakları saklıdır."
    },
    hi: {
        title: "आधुनिक औद्योगिक उत्कृष्टता",
        logo: "इंडेक्स कॉर्प",
        heroTitle: "औद्योगिक प्रौद्योगिकी के भविष्य का नेतृत्व",
        heroSub: "सटीक इंजीनियरिंग, वैश्विक प्रभाव और टिकाऊ नवाचार।",
        servicesTitle: "हमारी सेवाएँ",
        s1Title: "उन्नत विनिर्माण",
        s1Desc: "बेजोड़ सटीकता के लिए एआई और रोबोटिक्स का उपयोग करने वाली अत्याधुनिक सुविधाएं।",
        s2Title: "टिकाऊ ऊर्जा",
        s2Desc: "स्वच्छ ऊर्जा प्रौद्योगिकी के माध्यम से हरित औद्योगिक भविष्य के लिए अभिनov समाधान।",
        s3Title: "वैश्विक रसद",
        s3Desc: "निर्बाध वैश्विक संचालन सुनिश्चित करने वाली स्मार्ट आपूर्ति श्रृंखला प्रबंधन प्रणाली।",
        footer: "© 2026 इंडस्ट्रियल एक्सीलेंस कॉर्प। सर्वाधिकार सुरक्षित।"
    },
    bn: {
        title: "আধুনিক শিল্প উৎকর্ষতা",
        logo: "ইনডেক্স কর্পোরেশন",
        heroTitle: "শিল্প প্রযুক্তির ভবিষ্যতের পথপ্রদর্শক",
        heroSub: "নির্ভুল প্রকৌশল, বৈশ্বিক প্রভাব এবং টেকসই উদ্ভাবন।",
        servicesTitle: "আমাদের সেবাসমূহ",
        s1Title: "উন্নত উৎপাদন",
        s1Desc: "অতুলনীয় নির্ভুলতার জন্য এআই এবং রোবোটিক্স ব্যবহার করে অত্যাধুনিক সুবিধা।",
        s2Title: "টেকসই শক্তি",
        s2Desc: "পরিচ্ছন্ন শক্তি প্রযুক্তির মাধ্যমে একটি সবুজ শিল্প ভবিষ্যতের জন্য উদ্ভাবনী সমাধান।",
        s3Title: "বৈশ্বিক লজিস্টিকস",
        s3Desc: "স্মার্ট সাপ্লাই চেইন ম্যানেজমেন্ট সিস্টেম যা নিরবচ্ছিন্ন বিশ্বব্যাপী কার্যক্রম নিশ্চিত করে।",
        footer: "© 2026 ইন্ডাস্ট্রিয়াল এক্সিলেন্স কর্প। সর্বস্বত্ব সংরক্ষিত।"
    },
    id: {
        title: "Keunggulan Industri Modern",
        logo: "IndEx Corp",
        heroTitle: "Merintis Masa Depan Teknologi Industri",
        heroSub: "Rekayasa presisi, dampak global, dan inovasi berkelanjutan.",
        servicesTitle: "Layanan Kami",
        s1Title: "Manufaktur Maju",
        s1Desc: "Fasilitas mutakhir yang menggunakan AI dan robotika untuk presisi yang tak tertandingi.",
        s2Title: "Energi Terbarukan",
        s2Desc: "Solusi inovatif untuk masa depan industri yang lebih hijau melalui teknologi energi bersih.",
        s3Title: "Logistik Global",
        s3Desc: "Sistem manajemen rantai pasokan cerdas yang memastikan operasi global yang mulus.",
        footer: "© 2026 Industrial Excellence Corp. Semua hak dilindungi undang-undang."
    },
    vi: {
        title: "Sự Xuất Sắc Công Nghiệp Hiện Đại",
        logo: "IndEx Corp",
        heroTitle: "Tiên Phong Tương Lai Của Công Nghệ Công Nghiệp",
        heroSub: "Kỹ thuật chính xác, tác động toàn cầu và đổi mới bền vững.",
        servicesTitle: "Dịch Vụ Của Chúng Tôi",
        s1Title: "Sản Xuất Tiên Tiến",
        s1Desc: "Các cơ sở hiện đại sử dụng AI và robot để đạt được độ chính xác vô song.",
        s2Title: "Năng Lượng Bền Vững",
        s2Desc: "Giải pháp sáng tạo cho tương lai công nghiệp xanh hơn thông qua công nghệ năng lượng sạch.",
        s3Title: "Logistics Toàn Cầu",
        s3Desc: "Hệ thống quản lý chuỗi cung ứng thông minh đảm bảo hoạt động toàn cầu liền mạch.",
        footer: "© 2026 Industrial Excellence Corp. Bảo lưu mọi quyền."
    },
    th: {
        title: "ความเป็นเลิศทางอุตสาหกรรมสมัยใหม่",
        logo: "IndEx Corp",
        heroTitle: "บุกเบิกอนาคตของเทคโนโลยีอุตสาหกรรม",
        heroSub: "วิศวกรรมที่แม่นยำ ผลกระทบระดับโลก และนวัตกรรมที่ยั่งยืน",
        servicesTitle: "บริการของเรา",
        s1Title: "การผลิตขั้นสูง",
        s1Desc: "สิ่งอำนวยความสะดวกที่ทันสมัยโดยใช้ AI และหุ่นยนต์เพื่อความแม่นยำที่ไม่มีใครเทียบได้",
        s2Title: "พลังงานที่ยั่งยืน",
        s2Desc: "โซลูชั่นนวัตกรรมเพื่ออนาคตอุตสาหกรรมที่เป็นมิตรต่อสิ่งแวดล้อมผ่านเทคโนโลยีพลังงานสะอาด",
        s3Title: "โลจิสติกส์ระดับโลก",
        s3Desc: "ระบบการจัดการห่วงโซ่อุปทานอัจฉริยะที่ช่วยให้การดำเนินงานทั่วโลกเป็นไปอย่างราบรื่น",
        footer: "© 2026 Industrial Excellence Corp. สงวนลิขสิทธิ์"
    },
    pl: {
        title: "Nowoczesna Doskonałość Przemysłowa",
        logo: "IndEx Corp",
        heroTitle: "Pionierzy Przyszłości Technologii Przemysłowej",
        heroSub: "Precyzyjna inżynieria, globalny zasięg i zrównoważone innowacje.",
        servicesTitle: "Nasze Usługi",
        s1Title: "Zaawansowana Produkcja",
        s1Desc: "Najnowocześniejsze zakłady wykorzystujące AI i robotykę dla niezrównanej precyzji.",
        s2Title: "Zrównoważona Energia",
        s2Desc: "Innowacyjne rozwiązania dla bardziej ekologicznej przyszłości przemysłowej dzięki technologii czystej energii.",
        s3Title: "Globalna Logistyka",
        s3Desc: "Inteligentne systemy zarządzania łańcuchem dostaw zapewniające płynne operacje globalne.",
        footer: "© 2026 Industrial Excellence Corp. Wszelkie prawa zastrzeżone."
    },
    nl: {
        title: "Moderne Industriële Uitmuntendheid",
        logo: "IndEx Corp",
        heroTitle: "Pionierswerk in de Toekomst van Industriële Technologie",
        heroSub: "Precisie-engineering, wereldwijde impact en duurzame innovatie.",
        servicesTitle: "Onze Diensten",
        s1Title: "Geavanceerde Productie",
        s1Desc: "Geavanceerde faciliteiten die AI en robotica gebruiken voor ongeëvenaarde precisie.",
        s2Title: "Duurzame Energie",
        s2Desc: "Innovatieve oplossingen voor een groenere industriële toekomst via schone energietechnologie.",
        s3Title: "Wereldwijde Logistiek",
        s3Desc: "Slimme supply chain managementsystemen die naadloze wereldwijde activiteiten garanderen.",
        footer: "© 2026 Industrial Excellence Corp. Alle rechten voorbehouden."
    },
    fa: {
        title: "تعالی صنعتی مدرن",
        logo: "شرکت IndEx",
        heroTitle: "پیشرو در آینده تکنولوژی صنعتی",
        heroSub: "مهندسی دقیق، تاثیر جهانی، و نوآوری پایدار.",
        servicesTitle: "خدمات ما",
        s1Title: "تولید پیشرفته",
        s1Desc: "امکانات پیشرفته با استفاده از هوش مصنوعی و رباتیک برای دقت بی‌نظیر.",
        s2Title: "انرژی پایدار",
        s2Desc: "راهکارهای نوآورانه برای آینده صنعتی سبزتر از طریق تکنولوژی انرژی پاک.",
        s3Title: "لجستیک جهانی",
        s3Desc: "سیستم‌های مدیریت زنجیره تامین هوشمند که عملیات جهانی بدون وقفه را تضمین می‌کند.",
        footer: "© 2026 شرکت Industrial Excellence. تمامی حقوق محفوظ است."
    },
    ur: {
        title: "جدید صنعتی عمدگی",
        logo: "انڈیکس کارپوریشن",
        heroTitle: "صنعتی ٹیکنالوجی کے مستقبل کی رہنمائی",
        heroSub: "درست انجینئرنگ، عالمی اثرات، اور پائیدار جدت۔",
        servicesTitle: "ہماری خدمات",
        s1Title: "جدید مینوفیکچرنگ",
        s1Desc: "بے مثال درستگی کے لیے اے آئی اور روبوٹکس کا استعمال کرنے والی جدید ترین سہولیات۔",
        s2Title: "پائیدار توانائی",
        s2Desc: "کلین انرجی ٹیکنالوجی کے ذریعے سبز صنعتی مستقبل کے لیے اختراعی حل۔",
        s3Title: "عالمی لاجسٹکس",
        s3Desc: "اسمارٹ سپلائی چین مینجمنٹ سسٹم جو ہموار عالمی آپریشنز کو یقینی بناتا ہے۔",
        footer: "© 2026 انڈسٹریل ایکسی لینس کارپوریشن۔ جملہ حقوق محفوظ ہیں۔"
    }
};

const generateHtml = (langCode, trans) => {
    const isRtl = ['ar', 'fa', 'ur', 'ps', 'prs'].includes(langCode);
    const dir = isRtl ? 'rtl' : 'ltr';
    
    let dropdownHtml = languages38.map(l => {
        const selected = l.code === langCode ? ' selected' : '';
        return `                <option value="/${l.code}/"${selected}>${l.native} (${l.code.toUpperCase()})</option>`;
    }).join('\n');

    return `<!DOCTYPE html>
<html lang="${langCode}" dir="${dir}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${trans.title}</title>
    <style>
        :root {
            --primary: #f97316;
            --bg: #0f172a;
            --text: #f1f5f9;
            --card-bg: #1e293b;
        }
        body {
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            ${isRtl ? 'text-align: right;' : ''}
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 5%;
            background: rgba(15, 23, 42, 0.9);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .lang-switcher select {
            background: var(--card-bg);
            color: var(--text);
            border: 1px solid #334155;
            padding: 0.5rem;
            border-radius: 4px;
        }
        .hero {
            padding: 100px 5%;
            text-align: center;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border-bottom: 4px solid var(--primary);
        }
        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            font-weight: 900;
        }
        .hero p {
            font-size: 1.25rem;
            color: #94a3b8;
            max-width: 800px;
            margin: 0 auto;
        }
        .services {
            padding: 80px 5%;
        }
        .services h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        .card {
            background: var(--card-bg);
            padding: 2.5rem;
            border-radius: 8px;
            border-top: 4px solid var(--primary);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-10px);
        }
        .card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        footer {
            padding: 40px 5%;
            text-align: center;
            border-top: 1px solid #334155;
            color: #64748b;
        }
        [dir="rtl"] {
            text-align: right;
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">${trans.logo}</div>
        <div class="lang-switcher">
            <select onchange="window.location.href=this.value">
${dropdownHtml}
            </select>
        </div>
    </header>

    <section class="hero">
        <h1>${trans.heroTitle}</h1>
        <p>${trans.heroSub}</p>
    </section>

    <section class="services">
        <h2>${trans.servicesTitle}</h2>
        <div class="grid">
            <div class="card">
                <h3>${trans.s1Title}</h3>
                <p>${trans.s1Desc}</p>
            </div>
            <div class="card">
                <h3>${trans.s2Title}</h3>
                <p>${trans.s2Desc}</p>
            </div>
            <div class="card">
                <h3>${trans.s3Title}</h3>
                <p>${trans.s3Desc}</p>
            </div>
        </div>
    </section>

    <footer>
        <p>${trans.footer}</p>
    </footer>
</body>
</html>`;
};

const targetLangs = ['tr', 'hi', 'bn', 'id', 'vi', 'th', 'pl', 'nl', 'fa', 'ur'];

targetLangs.forEach(lang => {
    const dirPath = path.join(baseDir, lang);
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
    }
    const html = generateHtml(lang, translations[lang]);
    fs.writeFileSync(path.join(dirPath, 'index.html'), html);
    console.log(`Generated ${lang}/index.html`);
});
