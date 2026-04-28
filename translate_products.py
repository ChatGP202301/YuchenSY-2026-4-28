import json
import os

translations = {
    "ar": {
        "name": "غلاف مرشح جامبو صناعي من الفولاذ المقاوم للصدأ 304/316L",
        "category": "غلاف المرشح",
        "desc": "غلاف من الفولاذ المقاوم للصدأ 304 عالي التحمل متاح بأحجام 10 بوصات و20 بوصة. متوافق مع أغشية UF، وفلاتر رواسب PP، وفلاتر كربون بلوك. مثالي لتطبيقات التدفق العالي. توريد مصنع بالجملة، قابل للتخصيص لـ OEM/ODM. معتمد من NSF/ISO لمعالجة المياه الصناعية والتجارية."
    },
    "cs": {
        "name": "Průmyslové nerezové pouzdro filtru Jumbo 304/316L",
        "category": "Pouzdro filtru",
        "desc": "Robustní pouzdro z nerezové oceli 304 dostupné v 10palcových a 20palcových velikostech. Kompatibilní s UF membránami, PP sedimentačními filtry a Carbon Block filtry. Ideální pro aplikace s vysokým průtokem. Velkoobchodní dodávky přímo z výroby, přizpůsobitelné pro OEM/ODM. Certifikace NSF/ISO pro průmyslovou a komerční úpravu vody."
    },
    "da": {
        "name": "304/316L rustfrit stål industrielt Jumbo filterhus",
        "category": "Filterhus",
        "desc": "Kraftigt 304 rustfrit stålhus fås i 10-tommer og 20-tommer størrelser. Kompatibel med UF-membraner, PP-sedimentfiltre og Carbon Block-filtre. Ideel til applikationer med høj gennemstrømning. Engros fabrikslevering, kan tilpasses til OEM/ODM. NSF/ISO certificeret til industriel og kommerciel vandbehandling."
    },
    "de": {
        "name": "304/316L Edelstahl Industrie Jumbo Filtergehäuse",
        "category": "Filtergehäuse",
        "desc": "Hochbelastbares Gehäuse aus 304er Edelstahl, erhältlich in 10-Zoll- und 20-Zoll-Größen. Kompatibel mit UF-Membranen, PP-Sedimentfiltern und Carbon-Block-Filtern. Ideal für Hochflussanwendungen. Großhandel ab Werk, anpassbar für OEM/ODM. NSF/ISO-zertifiziert für die industrielle und gewerbliche Wasseraufbereitung."
    },
    "el": {
        "name": "Βιομηχανικό περίβλημα φίλτρου Jumbo από ανοξείδωτο χάλυβα 304/316L",
        "category": "Περίβλημα φίλτρου",
        "desc": "Περίβλημα από ανοξείδωτο χάλυβα 304 βαρέως τύπου διαθέσιμο σε μεγέθη 10 ιντσών και 20 ιντσών. Συμβατό με μεμβράνες UF, φίλτρα ιζημάτων PP και φίλτρα Carbon Block. Ιδανικό για εφαρμογές υψηλής ροής. Χονδρική προμήθεια εργοστασίου, προσαρμόσιμη για OEM/ODM. Πιστοποίηση NSF/ISO για βιομηχανική και εμπορική επεξεργασία νερού."
    },
    "es": {
        "name": "Carcasa de filtro jumbo industrial de acero inoxidable 304/316L",
        "category": "Carcasa de filtro",
        "desc": "Carcasa de acero inoxidable 304 de alta resistencia disponible en tamaños de 10 y 20 pulgadas. Compatible con membranas UF, filtros de sedimentos de PP y filtros de bloque de carbón. Ideal para aplicaciones de alto flujo. Suministro de fábrica al por mayor, personalizable para OEM/ODM. Certificación NSF/ISO para tratamiento de agua industrial y comercial."
    },
    "fa": {
        "name": "هوزینگ فیلتر جامبو صنعتی استنلس استیل 304/316L",
        "category": "هوزینگ فیلتر",
        "desc": "هوزینگ استنلس استیل 304 سنگین موجود در سایزهای 10 اینچ و 20 اینچ. سازگار با غشاهای UF، فیلترهای رسوبی PP و فیلترهای کربن بلاک. ایده آل برای کاربردهای با دبی بالا. عرضه عمده کارخانه، قابل سفارشی سازی برای OEM/ODM. دارای گواهینامه NSF/ISO برای تصفیه آب صنعتی و تجاری."
    },
    "fi": {
        "name": "304/316L ruostumattomasta teräksestä valmistettu teollinen Jumbo-suodatinkotelo",
        "category": "Suodatinkotelo",
        "desc": "Raskaaseen käyttöön tarkoitettu 304 ruostumattomasta teräksestä valmistettu kotelo saatavilla 10 ja 20 tuuman koossa. Yhteensopiva UF-kalvojen, PP-sedimenttisuodattimien ja Carbon Block -suodattimien kanssa. Ihanteellinen suuren virtauksen sovelluksiin. Tehtaan tukkumyynti, räätälöitävissä OEM/ODM:lle. NSF/ISO-sertifioitu teolliseen ja kaupalliseen vedenkäsittelyyn."
    },
    "fr": {
        "name": "Porte-filtre Jumbo industriel en acier inoxydable 304/316L",
        "category": "Porte-filtre",
        "desc": "Boîtier robuste en acier inoxydable 304 disponible en tailles 10 pouces et 20 pouces. Compatible avec les membranes UF, les filtres à sédiments PP et les filtres Carbon Block. Idéal pour les applications à haut débit. Fourniture d'usine en gros, personnalisable pour OEM/ODM. Certifié NSF/ISO pour le traitement de l'eau industriel et commercial."
    },
    "ha": {
        "name": "304/316L Bakin Karfe Masana'antu Jumbo Filter Housing",
        "category": "Gidan Tace",
        "desc": "Heavy-duty 304 bakin karfe gida samuwa a cikin 10-inch da 20-inch masu girma dabam. Mai jituwa tare da UF membranes, PP sediment filters, da Carbon Block filters. Mafi dacewa don aikace-aikacen babban kwarara. Kayayyakin masana'anta na jumloli, masu iya daidaitawa don OEM/ODM. NSF/ISO bokan don masana'antu da kasuwanci na ruwa."
    },
    "he": {
        "name": "בית מסנן ג'מבו תעשייתי מפלדת אל-חלד 304/316L",
        "category": "בית מסנן",
        "desc": "בית פלדת אל-חלד 304 חזק במיוחד זמין בגדלים של 10 אינץ' ו-20 אינץ'. תואם לממברנות UF, מסנני משקעי PP ומסנני בלוק פחמן. אידיאלי ליישומי זרימה גבוהה. אספקה סיטונאית מהמפעל, ניתן להתאמה אישית עבור OEM/ODM. מוסמך NSF/ISO לטיפול במים תעשייתי ומסחרי."
    },
    "hu": {
        "name": "304/316L rozsdamentes acél ipari Jumbo szűrőház",
        "category": "Szűrőház",
        "desc": "Nagy teherbírású 304-es rozsdamentes acél ház 10 és 20 hüvelykes méretben. Kompatibilis az UF membránokkal, PP üledékszűrőkkel és szénblokk szűrőkkel. Ideális nagy átfolyású alkalmazásokhoz. Nagykereskedelmi gyári ellátás, testreszabható OEM/ODM számára. NSF/ISO tanúsítvánnyal ipari és kereskedelmi vízkezeléshez."
    },
    "id": {
        "name": "Housing Filter Jumbo Industri Stainless Steel 304/316L",
        "category": "Housing Filter",
        "desc": "Housing stainless steel 304 tugas berat tersedia dalam ukuran 10 inci dan 20 inci. Kompatibel dengan membran UF, filter sedimen PP, dan filter Carbon Block. Ideal untuk aplikasi aliran tinggi. Pasokan pabrik grosir, dapat disesuaikan untuk OEM/ODM. Bersertifikat NSF/ISO untuk pengolahan air industri dan komersial."
    },
    "it": {
        "name": "Contenitore per filtro Jumbo industriale in acciaio inossidabile 304/316L",
        "category": "Contenitore per filtro",
        "desc": "Robusto contenitore in acciaio inossidabile 304 disponibile nelle dimensioni da 10 e 20 pollici. Compatibile con membrane UF, filtri per sedimenti in PP e filtri Carbon Block. Ideale per applicazioni ad alto flusso. Fornitura all'ingrosso dalla fabbrica, personalizzabile per OEM/ODM. Certificato NSF/ISO per il trattamento dell'acqua industriale e commerciale."
    },
    "ja": {
        "name": "304/316L ステンレス製工業用ジャンボフィルターハウジング",
        "category": "フィルターハウジング",
        "desc": "10インチおよび20インチサイズの頑丈な304ステンレススチール製ハウジング。UF膜、PP沈殿物フィルター、カーボンブロックフィルターに対応。大流量用途に最適。工場卸売供給、OEM/ODM向けにカスタマイズ可能。工業用および商業用水処理のNSF/ISO認証取得済み。"
    },
    "kk": {
        "name": "304/316L Тот баспайтын болаттан жасалған өнеркәсіптік Jumbo сүзгі корпусы",
        "category": "Сүзгі корпусы",
        "desc": "10 дюймдік және 20 дюймдік өлшемдерде қолжетімді ауыр салмақты 304 тот баспайтын болаттан жасалған корпус. UF мембраналарымен, PP шөгінді сүзгілерімен және Carbon Block сүзгілерімен үйлесімді. Жоғары ағынды қолданбалар үшін қолайлы. Зауыттық көтерме жеткізу, OEM/ODM үшін теңшеуге болады. Өнеркәсіптік және коммерциялық суды тазарту үшін NSF/ISO сертификатталған."
    },
    "km": {
        "name": "សំបកចម្រោះ Jumbo ឧស្សាហកម្មធ្វើពីដែកអ៊ីណុក 304/316L",
        "category": "សំបកចម្រោះ",
        "desc": "សំបកដែកអ៊ីណុក 304 កម្លាំងខ្លាំង មានទំហំ 10 អ៊ីង និង 20 អ៊ីង។ អាចប្រើជាមួយភ្នាស UF, តម្រងដីល្បាប់ PP និងតម្រង Carbon Block ។ ល្អបំផុតសម្រាប់កម្មវិធីលំហូរខ្ពស់។ ការផ្គត់ផ្គង់រោងចក្រលក់ដុំ អាចប្ដូរតាមបំណងសម្រាប់ OEM/ODM ។ បញ្ជាក់ដោយ NSF/ISO សម្រាប់ការបន្សុทธิទឹកក្នុងឧស្សាហកម្ម និងពាណិជ្ជកម្ម។"
    },
    "ko": {
        "name": "304/316L 스테인리스 스틸 산업용 점보 필터 하우징",
        "category": "필터 하우징",
        "desc": "10인치 및 20인치 크기로 제공되는 견고한 304 스테인리스 스틸 하우징. UF 멤브레인, PP 침전물 필터 및 카본 블록 필터와 호환됩니다. 대유량 응용 분야에 적합합니다. 공장 도매 공급, OEM/ODM 맞춤화 가능. 산업 및 상업용 수처리를 위한 NSF/ISO 인증 획득."
    },
    "lo": {
        "name": "ຖັງກອງ Jumbo ອຸດສາຫະກຳສະແຕນເລດ 304/316L",
        "category": "ຖັງກອງ",
        "desc": "ຖັງສະແຕນເລດ 304 ທີ່ທົນທານ ມີຂະໜາດ 10 ນິ້ວ ແລະ 20 ນິ້ວ. ເຂົ້າກັນໄດ້ກັບເຍື່ອ UF, ໄສ້ກອງຕະກອນ PP, ແລະໄສ້ກອງ Carbon Block. ເໝາະສຳລັບການນຳໃຊ້ທີ່ມີການໄຫຼສູງ. ການສະໜອງໂຮງງານຂາຍສົ່ງ, ສາມາດປັບແຕ່ງໄດ້ສຳລັບ OEM/ODM. ໄດ້ຮັບການຢັ້ງຢືນ NSF/ISO ສຳລັບການບຳບັດນ້ຳໃນອຸດສາຫະກຳ ແລະ ການຄ້າ."
    },
    "ms": {
        "name": "Perumahan Penapis Jumbo Industri Keluli Tahan Karat 304/316L",
        "category": "Perumahan Penapis",
        "desc": "Perumahan keluli tahan karat 304 tugas berat tersedia dalam saiz 10 inci dan 20 inci. Serasi dengan membran UF, penapis sedimen PP, dan penapis Carbon Block. Ideal untuk aplikasi aliran tinggi. Bekalan kilang borong, boleh disesuaikan untuk OEM/ODM. Diiktiraf NSF/ISO untuk rawatan air industri dan komersial."
    },
    "my": {
        "name": "304/316L စတီးလ်စက်မှုလုပ်ငန်းသုံး Jumbo Filter Housing",
        "category": "Filter Housing",
        "desc": "၁၀ လက်မနှင့် ၂၀ လက်မ အရွယ်အစားရှိ အကြီးစား 304 စတီးလ်အိမ်။ UF မန်ဘရိန်းများ၊ PP အနည်စစ်စစ်များ၊ နှင့် Carbon Block စစ်ထုတ်မှုများနှင့် အသုံးပြုနိုင်သည်။ စီးဆင်းမှုနှုန်းမြင့်မားသောအသုံးပြုမှုများအတွက် အထူးသင့်လျော်သည်။ စက်ရုံလက်ကားရောင်းချမှု၊ OEM/ODM အတွက် စိတ်ကြိုက်ပြင်ဆင်နိုင်သည်။ စက်မှုနှင့် စီးပွားဖြစ် ရေသန့်စင်မှုအတွက် NSF/ISO လက်မှတ်ရထားသည်။"
    },
    "nl": {
        "name": "304/316L roestvrijstalen industriële Jumbo filterbehuizing",
        "category": "Filterbehuizing",
        "desc": "Zware 304 roestvrijstalen behuizing verkrijgbaar in 10-inch en 20-inch maten. Compatibel met UF-membranen, PP-sedimentfilters en Carbon Block-filters. Ideaal voor toepassingen met een hoog debiet. Groothandel af fabriek, aanpasbaar voor OEM/ODM. NSF/ISO gecertificeerd voor industriële en commerciële waterbehandeling."
    },
    "no": {
        "name": "304/316L rustfritt stål industrielt Jumbo filterhus",
        "category": "Filterhus",
        "desc": "Kraftig 304 rustfritt stålhus tilgjengelig i 10-tommers og 20-tommers størrelser. Kompatibel med UF-membraner, PP-sedimentfiltre og Carbon Block-filtre. Ideell for høystrømsapplikasjoner. Engros fabrikkforsyning, kan tilpasses for OEM/ODM. NSF/ISO-sertifisert for industriell og kommersiell vannbehandling."
    },
    "pl": {
        "name": "Obudowa filtra Jumbo przemysłowa ze stali nierdzewnej 304/316L",
        "category": "Obudowa filtra",
        "desc": "Wytrzymała obudowa ze stali nierdzewnej 304 dostępna w rozmiarach 10-calowych i 20-calowych. Kompatybilna z membranami UF, filtrami osadowymi PP i filtrami Carbon Block. Idealna do zastosowań o wysokim natężeniu przepływu. Hurtowa dostawa fabryczna, możliwość dostosowania do potrzeb OEM/ODM. Certyfikat NSF/ISO do przemysłowego i komercyjnego uzdatniania wody."
    },
    "ps": {
        "name": "304/316L د سټینلیس سټیل صنعتي جمبو فلټر کور",
        "category": "د فلټر کور",
        "desc": "دروند 304 سټینلیس سټیل کور په 10 انچ او 20 انچ اندازو کې شتون لري. د UF میمبرانونو، PP سیډیمینټ فلټرونو، او کاربن بلاک فلټرونو سره مطابقت لري. د لوړ جریان غوښتنلیکونو لپاره مثالی. د فابریکې عمده پلور، د OEM/ODM لپاره د دودیز کولو وړ. د صنعتي او سوداګریزې اوبو درملنې لپاره د NSF/ISO تصدیق شوی."
    },
    "pt": {
        "name": "Carcaça de filtro Jumbo industrial de aço inoxidável 304/316L",
        "category": "Carcaça de filtro",
        "desc": "Carcaça de aço inoxidável 304 de alta resistência disponível em tamanhos de 10 e 20 polegadas. Compatível com membranas UF, filtros de sedimentos PP e filtros Carbon Block. Ideal para aplicações de alto fluxo. Fornecimento de fábrica por atacado, personalizável para OEM/ODM. Certificação NSF/ISO para tratamento de água industrial e comercial."
    },
    "ro": {
        "name": "Carcasă filtru Jumbo industrială din oțel inoxidabil 304/316L",
        "category": "Carcasă filtru",
        "desc": "Carcasă robustă din oțel inoxidabil 304 disponibilă în dimensiuni de 10 inchi și 20 inchi. Compatibilă cu membrane UF, filtre de sedimente PP și filtre Carbon Block. Ideală pentru aplicații cu debit mare. Aprovizionare de la fabrică în regim en-gros, personalizabilă pentru OEM/ODM. Certificare NSF/ISO pentru tratarea apei industriale și comerciale."
    },
    "ru": {
        "name": "Промышленный корпус фильтра Jumbo из нержавеющей стали 304/316L",
        "category": "Корпус фильтра",
        "desc": "Прочный корпус из нержавеющей стали 304 доступен в размерах 10 и 20 дюймов. Совместим с мембранами ультрафильтрации (UF), полипропиленовыми осадочными фильтрами (PP) и угольными блочными фильтрами (CTO). Идеально подходит для высокопоточных систем. Оптовые поставки с завода, возможность изготовления по OEM/ODM. Сертифицирован NSF/ISO для промышленной и коммерческой очистки воды."
    },
    "sv": {
        "name": "304/316L rostfritt stål industriellt Jumbo-filterhus",
        "category": "Filterhus",
        "desc": "Kraftigt 304 rostfritt stålhus tillgängligt i 10-tums och 20-tums storlekar. Kompatibel med UF-membran, PP-sedimentfilter och Carbon Block-filter. Idealisk för applikationer med högt flöde. Partihandel med fabriksförsörjning, anpassningsbar för OEM/ODM. NSF/ISO-certifierad for industriell und kommersiell vattenrening."
    },
    "sw": {
        "name": "Nyumba ya chujio cha Jumbo ya viwandani ya chuma cha pua 304/316L",
        "category": "Nyumba ya chujio",
        "desc": "Nyumba ya chuma cha pua ya 304 yenye uwezo mkubwa inayopatikana katika saizi za inchi 10 na inchi 20. Inaoana na utando wa UF, vichungi vya sediment vya PP, na vichungi vya Carbon Block. Inafaa kwa matumizi ya mtiririko wa juu. Ugavi wa kiwanda wa jumla, unaoweza kubinafsishwa kwa OEM/ODM. NSF/ISO iliyoidhinishwa kwa ajili ya matibabu ya maji ya viwandani na kibiashara."
    },
    "ta": {
        "name": "304/316L துருப்பிடிக்காத எஃகு தொழில்துறை ஜம்போ வடிகட்டி வீட்டுவசதி",
        "category": "வடிகட்டி வீட்டுவசதி",
        "desc": "10 அங்குல மற்றும் 20 அங்குல அளவுகளில் கிடைக்கும் ஹெவி-டியூட்டி 304 துருப்பிடிக்காத எஃகு வீட்டுவசதி. UF சவ்வுகள், PP வண்டல் வடிகட்டிகள் மற்றும் கார்பன் பிளாக் வடிகட்டிகளுடன் இணக்கமானது. அதிக ஓட்டம் கொண்ட பயன்பாடுகளுக்கு ஏற்றது. மொத்த தொழிற்சாலை விநியோகம், OEM/ODM க்காக தனிப்பயனாக்கக்கூடியது. தொழில்துறை மற்றும் வணிக நீர் சுத்திகரிப்புக்காக NSF/ISO சான்றிதழ் பெற்றது."
    },
    "th": {
        "name": "กระบอกกรองน้ำบิ๊กบลู (Jumbo) สแตนเลส 304/316L สำหรับอุตสาหกรรม",
        "category": "กระบอกกรองน้ำ",
        "desc": "ตัวเรือนสแตนเลส 304 เกรดหนาพิเศษ มีให้เลือกขนาด 10 นิ้ว และ 20 นิ้ว รองรับเมมเบรน UF, ไส้กรองตะกอน PP และไส้กรองคาร์บอนบล็อก เหมาะสำหรับการใช้งานที่ต้องการอัตราการไหลสูง ราคาส่งจากโรงงานโดยตรง รองรับงาน OEM/ODM ได้รับการรับรองมาตรฐาน NSF/ISO สำหรับการบำบัดน้ำในภาคอุตสาหกรรมและพาณิชย์"
    },
    "tr": {
        "name": "304/316L Paslanmaz Çelik Endüstriyel Jumbo Filtre Muhafazası",
        "category": "Filtre Muhafazası",
        "desc": "10 inç ve 20 inç boyutlarında mevcut olan ağır hizmet tipi 304 paslanmaz çelik muhafaza. UF membranları, PP tortu filtreleri ve Karbon Blok filtrelerle uyumludur. Yüksek debili uygulamalar için idealdir. Toptan fabrika teslimi, OEM/ODM için özelleştirilebilir. Endüstriyel ve ticari su arıtma için NSF/ISO sertifikalıdır."
    },
    "uk": {
        "name": "Промисловий корпус фільтра Jumbo з нержавіючої сталі 304/316L",
        "category": "Корпус фільтра",
        "desc": "Міцний корпус із нержавіючої сталі 304 доступний у розмірах 10 та 20 дюймів. Сумісний з ультрафільтраційними мембранами (UF), поліпропіленовими осадовими фільтрами (PP) та вугільними блок-фільтрами. Ідеально підходить для систем з високою пропускною здатністю. Оптові поставки з заводу, можливість виготовлення за OEM/ODM. Сертифікований за стандартом NSF/ISO для промислової та комерційної очистки води."
    },
    "uz": {
        "name": "304/316L zanglamaydigan po'latdan yasalgan sanoat Jumbo filtri korpusi",
        "category": "Filtr korpusi",
        "desc": "10 dyuymli va 20 dyuymli o'lchamlarda mavjud bo'lgan og'ir yuklarga chidamli 304 zanglamaydigan po'latdan yasalgan korpus. UF membranalari, PP cho'kindi filtrlari va Carbon Block filtrlari bilan mos keladi. Yuqori oqimli ilovalar uchun ideal. Zavoddan ulgurji yetkazib berish, OEM/ODM uchun moslashtirilishi mumkin. Sanoat va tijorat suvlarini tozalash uchun NSF/ISO sertifikatiga ega."
    },
    "vi": {
        "name": "Vỏ lọc Jumbo công nghiệp bằng thép không gỉ 304/316L",
        "category": "Vỏ lọc",
        "desc": "Vỏ thép không gỉ 304 hạng nặng có sẵn ở kích thước 10 inch và 20 inch. Tương thích với màng UF, lõi lọc cặn PP và lõi lọc Carbon Block. Lý tưởng cho các ứng dụng lưu lượng cao. Cung cấp sỉ từ nhà máy, có thể tùy chỉnh cho OEM/ODM. Được chứng nhận NSF/ISO cho xử lý nước công nghiệp và thương mại."
    },
    "zu": {
        "name": "I-304/316L Stainless Steel Industrial Jumbo Filter Housing",
        "category": "Indlu yesihlungi",
        "desc": "Indlu yensimbi engagqwali engu-304 esindayo itholakala ngosayizi abangu-10-intshi no-20-intshi. Ihambisana nemembrani ye-UF, izihlungi ze-PP sediment, nezihlungi ze-Carbon Block. Ilungele izinhlelo zokusebenza zokugeleza okuphezulu. Ukunikezwa kwefekthri ngokuphelele, okwenziwa ngokwezifiso kwe-OEM/ODM. Isitifiketi se-NSF/ISO sokuhlanza amanzi ezimbonini nawokuhweba."
    }
}

base_dir = "assets/i18n"
target_id = "ss-jumbo-housing"

for lang, data in translations.items():
    file_path = os.path.join(base_dir, f"{lang}.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                json_data = json.load(f)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
        
        updated = False
        if "products" in json_data:
            for product in json_data["products"]:
                if product.get("id") == target_id:
                    product["name"] = data["name"]
                    product["category"] = data["category"]
                    product["desc"] = data["desc"]
                    updated = True
                    break
        
        if updated:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)
            print(f"Updated {file_path}")
        else:
            print(f"Product ID {target_id} not found in {file_path}")
    else:
        print(f"File {file_path} not found")
