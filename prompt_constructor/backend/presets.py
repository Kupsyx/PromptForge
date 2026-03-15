STYLE_PRESETS = {
    "anime": {
        "id": "anime",
        "name": "Anime",
        "icon": "✦",
        "description": "Vibrant 2D anime illustration with sharp linework and cel-shading",
        "preview_gradient": "linear-gradient(135deg, #ec4899, #8b5cf6, #3b82f6)",
        "prompt": "ultra high quality anime illustration style, modern high-end anime rendering, clean lineart with variable line weight, crisp outlines, soft gradient cel-shading, subtle painterly highlights, vibrant yet balanced color palette, cinematic lighting, volumetric glow, soft bloom, atmospheric depth, delicate color transitions, smooth shading layers, studio-level digital painting quality, sharp focus, extremely detailed brushwork, stylized lighting reflections, high dynamic range lighting, polished composition, professional anime production look, high resolution, ultra-detailed, smooth textures, subtle film grain, depth of field, dramatic contrast, trending anime illustration style, masterpiece quality"
    },
    "realistic": {
        "id": "realistic",
        "name": "Realistic",
        "icon": "◈",
        "description": "Cinematic photorealism with professional lighting and 8K detail",
        "preview_gradient": "linear-gradient(135deg, #f59e0b, #ef4444, #1d4ed8)",
        "prompt": "ultra photorealistic rendering, extreme realism, cinematic photography style, physically accurate lighting, global illumination, ray-traced reflections, natural color grading, realistic materials and textures, micro surface detail, high dynamic range, film-quality lighting, professional DSLR photography aesthetic, shallow depth of field, realistic shadows, volumetric light scattering, ultra high resolution, hyper-detailed textures, natural imperfections, subtle film grain, optical realism, true-to-life contrast, studio photography quality, ultra sharp focus, physically based rendering, photogrammetry-level detail, 8k realism"
    }
}
CHARACTER_OPTIONS = {
    "gender": {
        "id": "gender",
        "label": "Пол",
        "icon": "⊹",
        "type": "single",
        "options": [
            {"id": "male",        "label": "Мужской",    "icon": "♂", "description": "Мужской персонаж",          "prompt": "male, man"},
            {"id": "female",      "label": "Женский",    "icon": "♀", "description": "Женский персонаж",           "prompt": "female, woman"},
            {"id": "androgynous", "label": "Андрогин",   "icon": "⚥", "description": "Нейтральные черты",          "prompt": "androgynous character, gender-neutral appearance"},
        ]
    },
    "age": {
        "id": "age",
        "label": "Возраст",
        "icon": "◷",
        "type": "single",
        "options": [
            {"id": "teen",        "label": "Подросток",  "icon": "○", "description": "16–17 лет",       "prompt": "teenager, 17 years old"},
            {"id": "young_adult", "label": "Молодой",    "icon": "○", "description": "Ранние 20-е",     "prompt": "young adult, early 20s"},
            {"id": "adult",       "label": "Взрослый",   "icon": "○", "description": "Поздние 20–30-е", "prompt": "adult, late 20s"},
            {"id": "mature",      "label": "Зрелый",     "icon": "○", "description": "40–50 лет",       "prompt": "mature adult, 45 years old"},
        ]
    },
    "hair": {
        "id": "hair",
        "label": "Волосы",
        "icon": "✿",
        "type": "subcategory",
        "subcategories": {
            "hair_color": {
                "id": "hair_color",
                "label": "Цвет волос",
                "type": "single",
                "options": [
                    {"id": "black",      "label": "Чёрный",      "color": "#111111", "description": "Глубокий чёрный",    "prompt": "black hair"},
                    {"id": "dark_brown", "label": "Тёмно-кор.",  "color": "#3b1f0e", "description": "Тёмный каштан",      "prompt": "dark brown hair"},
                    {"id": "brown",      "label": "Каштан",      "color": "#7c4a2d", "description": "Классический каштан","prompt": "brown hair"},
                    {"id": "blonde",     "label": "Блонд",       "color": "#e8c97a", "description": "Золотой блонд",       "prompt": "blonde hair, golden hair"},
                    {"id": "red",        "label": "Рыжий",       "color": "#c0392b", "description": "Огненно-рыжий",       "prompt": "red hair, ginger"},
                    {"id": "pink",       "label": "Розовый",     "color": "#f472b6", "description": "Яркий розовый",       "prompt": "pink hair"},
                    {"id": "purple",     "label": "Фиолет.",     "color": "#9333ea", "description": "Глубокий фиолетовый", "prompt": "purple hair"},
                    {"id": "blue",       "label": "Синий",       "color": "#3b82f6", "description": "Яркий синий",         "prompt": "blue hair"},
                    {"id": "silver",     "label": "Серебро",     "color": "#b0b8c8", "description": "Металлическое серебро","prompt": "silver hair"},
                    {"id": "white",      "label": "Белый",       "color": "#f0f0f5", "description": "Чисто белый",         "prompt": "white hair"},
                    {"id": "green",      "label": "Зелёный",     "color": "#22c55e", "description": "Яркий зелёный",       "prompt": "green hair"},
                    {"id": "orange",     "label": "Оранжевый",   "color": "#f97316", "description": "Насыщенный оранжевый","prompt": "orange hair"},
                ]
            },
            "hair_style": {
                "id": "hair_style",
                "label": "Стиль волос",
                "type": "single",
                "options": [
                    {"id": "short",      "label": "Короткие",    "icon": "⌇", "description": "Короткая стрижка",      "prompt": "short hair"},
                    {"id": "medium",     "label": "Средние",     "icon": "⌇", "description": "До плеч",               "prompt": "medium length hair"},
                    {"id": "long",       "label": "Длинные",     "icon": "⌇", "description": "Длинные волосы",        "prompt": "long hair"},
                    {"id": "very_long",  "label": "Очень дл.",   "icon": "⌇", "description": "До пояса",              "prompt": "very long hair, waist length"},
                    {"id": "curly",      "label": "Кудрявые",    "icon": "∿", "description": "Кудряшки",              "prompt": "curly hair"},
                    {"id": "wavy",       "label": "Волнистые",   "icon": "∿", "description": "Лёгкие волны",          "prompt": "wavy hair"},
                    {"id": "straight",   "label": "Прямые",      "icon": "⌇", "description": "Гладкие прямые",        "prompt": "straight hair"},
                    {"id": "braided",    "label": "Косы",        "icon": "≋", "description": "Заплетённые косы",      "prompt": "braided hair"},
                    {"id": "ponytail",   "label": "Хвост",       "icon": "⌇", "description": "Хвостик",               "prompt": "ponytail"},
                    {"id": "twin_tails", "label": "Два хвоста",  "icon": "⌇", "description": "Двойной хвостик",       "prompt": "twin tails, pigtails"},
                    {"id": "bun",        "label": "Пучок",       "icon": "○", "description": "Пучок на голове",       "prompt": "hair bun"},
                    {"id": "messy",      "label": "Растрёпан.",  "icon": "※", "description": "Небрежный стиль",       "prompt": "messy hair, disheveled"},
                    {"id": "spiky",      "label": "Острые",      "icon": "✦", "description": "Торчащие пряди",        "prompt": "spiky hair"},
                    {"id": "undercut",   "label": "Андеркат",    "icon": "⌇", "description": "Стиль андеркат",        "prompt": "undercut hairstyle"},
                ]
            }
        }
    },
    "face": {
        "id": "face",
        "label": "Лицо",
        "icon": "◯",
        "type": "multi",
        "options": [
            {"id": "cute",          "label": "Милое",       "icon": "✿", "description": "Мило и трогательно",      "prompt": "cute face, adorable features"},
            {"id": "pretty",        "label": "Красивое",    "icon": "✦", "description": "Элегантно красивое",      "prompt": "pretty face, beautiful features"},
            {"id": "handsome",      "label": "Мужеств.",    "icon": "◈", "description": "Классически мужественное","prompt": "handsome face, chiseled features"},
            {"id": "sharp",         "label": "Острые",      "icon": "◇", "description": "Выраженные черты",        "prompt": "sharp facial features, defined jawline"},
            {"id": "soft",          "label": "Мягкое",      "icon": "○", "description": "Нежные мягкие черты",     "prompt": "soft facial features"},
            {"id": "round_face",    "label": "Круглое",     "icon": "○", "description": "Круглая форма лица",      "prompt": "round face"},
            {"id": "oval_face",     "label": "Овальное",    "icon": "◎", "description": "Овальная форма лица",     "prompt": "oval face"},
            {"id": "freckles",      "label": "Веснушки",    "icon": "·", "description": "Милые веснушки",          "prompt": "freckles on face"},
            {"id": "blue_eyes",     "label": "Синие гл.",   "icon": "◉", "description": "Синий цвет глаз",         "prompt": "blue eyes"},
            {"id": "green_eyes",    "label": "Зелёные гл.", "icon": "◉", "description": "Зелёный цвет глаз",       "prompt": "green eyes"},
            {"id": "brown_eyes",    "label": "Карие гл.",   "icon": "◉", "description": "Карий цвет глаз",         "prompt": "brown eyes"},
            {"id": "purple_eyes",   "label": "Фиол. гл.",   "icon": "◉", "description": "Редкий фиолетовый",       "prompt": "purple eyes, amethyst eyes"},
            {"id": "red_eyes",      "label": "Красные гл.", "icon": "◉", "description": "Выразительные красные",   "prompt": "red eyes, ruby eyes"},
            {"id": "heterochromia", "label": "Гетерохр.",   "icon": "◉", "description": "Разный цвет глаз",        "prompt": "heterochromia, different colored eyes"},
        ]
    },
    "body": {
        "id": "body",
        "label": "Тело",
        "icon": "⟡",
        "type": "subcategory",
        "subcategories": {
            "build": {
                "id": "build",
                "label": "Телосложение",
                "type": "single",
                "options": [
                    {"id": "slim",      "label": "Стройное",   "icon": "▏", "description": "Тонкое, стройное",         "prompt": "slim build, slender body"},
                    {"id": "athletic",  "label": "Спортивное", "icon": "▎", "description": "Подтянутое, атлетичное",   "prompt": "athletic build, toned body"},
                    {"id": "muscular",  "label": "Мускулист.", "icon": "▍", "description": "Мощное мускулистое",        "prompt": "muscular build, strong physique"},
                    {"id": "curvy",     "label": "Изгибистое", "icon": "◌", "description": "Женственные изгибы",        "prompt": "curvy body, hourglass figure"},
                    {"id": "petite",    "label": "Миниатюрн.", "icon": "▏", "description": "Маленькое, миниатюрное",    "prompt": "petite figure, small frame"},
                    {"id": "tall",      "label": "Высокое",    "icon": "▌", "description": "Высокого роста",            "prompt": "tall figure, long legs"},
                    {"id": "average",   "label": "Среднее",    "icon": "▎", "description": "Среднее телосложение",      "prompt": "average build"},
                    {"id": "chubby",    "label": "Пухлое",     "icon": "◌", "description": "Мягкое, пухлое",           "prompt": "chubby, soft body"},
                ]
            },
            "bust": {
                "id": "bust",
                "label": "Грудь (только для женских персонажей)",
                "female_only": True,
                "type": "single",
                "options": [
                    {"id": "bust_flat",    "label": "Плоская",    "icon": "▔", "description": "Плоская грудь",      "prompt": "flat chest"},
                    {"id": "bust_small",   "label": "Малая",      "icon": "▕", "description": "Маленькая грудь",    "prompt": "small breasts"},
                    {"id": "bust_medium",  "label": "Средняя",    "icon": "▐", "description": "Средняя грудь",      "prompt": "medium breasts"},
                    {"id": "bust_large",   "label": "Большая",    "icon": "█", "description": "Большая грудь",      "prompt": "large breasts"},
                    {"id": "bust_huge",    "label": "Очень бол.", "icon": "█", "description": "Очень большая",      "prompt": "huge breasts, very large chest"},
                ]
            },
            "chest": {
                "id": "chest",
                "label": "Плечи / Торс",
                "type": "single",
                "options": [
                    {"id": "broad_shoulders",  "label": "Широкие пл.",  "icon": "━", "description": "Широкие плечи",        "prompt": "broad shoulders, wide chest"},
                    {"id": "narrow_shoulders", "label": "Узкие пл.",    "icon": "╌", "description": "Узкие плечи",          "prompt": "narrow shoulders, slim upper body"},
                    {"id": "flat_chest",       "label": "Плоский торс", "icon": "▔", "description": "Плоский торс",         "prompt": "flat chest, flat torso"},
                    {"id": "toned_torso",      "label": "Рельефный",    "icon": "▐", "description": "Рельефный пресс",      "prompt": "toned torso, visible abs"},
                ]
            },
            "legs": {
                "id": "legs",
                "label": "Ноги",
                "type": "single",
                "options": [
                    {"id": "long_legs",   "label": "Длинные",   "icon": "▌", "description": "Длинные стройные ноги","prompt": "long legs, slender legs"},
                    {"id": "short_legs",  "label": "Короткие",  "icon": "▏", "description": "Короткие ноги",        "prompt": "short legs"},
                    {"id": "thick_legs",  "label": "Толстые",   "icon": "█", "description": "Мощные, полные ноги",  "prompt": "thick thighs, strong legs"},
                    {"id": "toned_legs",  "label": "Подтянут.", "icon": "▐", "description": "Подтянутые ноги",      "prompt": "toned legs, defined calves"},
                ]
            },
            "arms": {
                "id": "arms",
                "label": "Руки",
                "type": "single",
                "options": [
                    {"id": "slender_arms",  "label": "Изящные",   "icon": "⌒", "description": "Тонкие изящные руки", "prompt": "slender arms, delicate hands"},
                    {"id": "muscular_arms", "label": "Мускулист.","icon": "⌒", "description": "Мускулистые руки",    "prompt": "muscular arms, strong arms"},
                    {"id": "toned_arms",    "label": "Подтянут.", "icon": "⌒", "description": "Подтянутые руки",     "prompt": "toned arms"},
                    {"id": "soft_arms",     "label": "Мягкие",    "icon": "⌒", "description": "Мягкие, округлые",    "prompt": "soft arms"},
                ]
            }
        }
    },
    "clothes": {
        "id": "clothes",
        "label": "Одежда",
        "icon": "✤",
        "type": "subcategory",
        "subcategories": {
            "outerwear": {
                "id": "outerwear",
                "label": "Верхняя одежда",
                "type": "multi",
                "options": [
                    {"id": "business_suit",  "label": "Костюм",        "icon": "▣", "description": "Деловой костюм",         "prompt": "business suit, formal attire"},
                    {"id": "casual_tshirt",  "label": "Футболка",      "icon": "▢", "description": "Повседневная футболка",   "prompt": "casual t-shirt"},
                    {"id": "hoodie",         "label": "Худи",          "icon": "▢", "description": "Уютное худи",             "prompt": "hoodie"},
                    {"id": "leather_jacket", "label": "Кожанка",       "icon": "▣", "description": "Кожаная куртка",          "prompt": "leather jacket"},
                    {"id": "school_uniform", "label": "Школьная",      "icon": "▢", "description": "Школьная форма",          "prompt": "school uniform"},
                    {"id": "dress",          "label": "Платье",        "icon": "◇", "description": "Элегантное платье",       "prompt": "dress"},
                    {"id": "kimono",         "label": "Кимоно",        "icon": "✿", "description": "Японское кимоно",         "prompt": "kimono, traditional Japanese clothing"},
                    {"id": "military",       "label": "Военная",       "icon": "▣", "description": "Военная форма",           "prompt": "military uniform, combat gear"},
                    {"id": "sportswear",     "label": "Спортивная",    "icon": "⌒", "description": "Спортивная одежда",       "prompt": "sportswear, athletic clothing"},
                    {"id": "trench_coat",    "label": "Тренч",         "icon": "▌", "description": "Классический тренч",      "prompt": "trench coat"},
                    {"id": "maid_outfit",    "label": "Горничная",     "icon": "✿", "description": "Костюм горничной",        "prompt": "maid outfit, maid costume"},
                    {"id": "fantasy_armor",  "label": "Броня",         "icon": "◆", "description": "Фэнтезийная броня",       "prompt": "fantasy armor, knight armor"},
                    {"id": "streetwear",     "label": "Стритвир",      "icon": "▢", "description": "Уличная мода",            "prompt": "streetwear, urban fashion"},
                    {"id": "swimwear",       "label": "Купальник",     "icon": "〰", "description": "Пляжный купальник",       "prompt": "swimwear, swimsuit"},
                    {"id": "gothic",         "label": "Готика",        "icon": "✦", "description": "Тёмная готика",           "prompt": "gothic outfit, dark fashion"},
                    {"id": "ninja",          "label": "Ниндзя",        "icon": "◆", "description": "Костюм ниндзя",           "prompt": "ninja outfit, dark stealth suit"},
                ]
            },
            "underwear": {
                "id": "underwear",
                "label": "Нижний слой / Нижнее бельё",
                "type": "multi",
                "options": [
                    {"id": "white_shirt", "label": "Белая рубашка","icon": "□", "description": "Классическая рубашка", "prompt": "white shirt"},
                    {"id": "turtleneck",  "label": "Водолазка",    "icon": "○", "description": "Водолазка",            "prompt": "turtleneck"},
                    {"id": "crop_top",    "label": "Кроп-топ",     "icon": "▭", "description": "Укороченный топ",      "prompt": "crop top"},
                    {"id": "tank_top",    "label": "Майка",        "icon": "▭", "description": "Майка без рукавов",    "prompt": "tank top"},
                    {"id": "lingerie",    "label": "Бельё",        "icon": "♡", "description": "Нижнее бельё",        "prompt": "lingerie"},
                    {"id": "boxer",       "label": "Боксёры",      "icon": "□", "description": "Боксёрские шорты",    "prompt": "boxer shorts"},
                    {"id": "shorts",      "label": "Шорты",        "icon": "▭", "description": "Повседневные шорты",  "prompt": "shorts"},
                ]
            },
            "accessories": {
                "id": "accessories",
                "label": "Аксессуары",
                "type": "multi",
                "options": [
                    {"id": "glasses",    "label": "Очки",         "icon": "◎", "description": "Очки",               "prompt": "wearing glasses"},
                    {"id": "sunglasses", "label": "Солнечные",    "icon": "◎", "description": "Солнцезащитные очки","prompt": "wearing sunglasses"},
                    {"id": "hat",        "label": "Шапка/Кепка",  "icon": "▲", "description": "Головной убор",      "prompt": "wearing a hat"},
                    {"id": "scarf",      "label": "Шарф",         "icon": "≋", "description": "Тёплый шарф",        "prompt": "wearing a scarf"},
                    {"id": "earrings",   "label": "Серьги",       "icon": "◇", "description": "Серьги",             "prompt": "earrings"},
                    {"id": "necklace",   "label": "Ожерелье",     "icon": "○", "description": "Ожерелье",           "prompt": "necklace"},
                    {"id": "gloves",     "label": "Перчатки",     "icon": "⌒", "description": "Перчатки",           "prompt": "wearing gloves"},
                    {"id": "boots",      "label": "Ботинки",      "icon": "▼", "description": "Ботинки",            "prompt": "wearing boots"},
                    {"id": "sneakers",   "label": "Кроссовки",    "icon": "▼", "description": "Кроссовки",          "prompt": "wearing sneakers"},
                    {"id": "heels",      "label": "Каблуки",      "icon": "▼", "description": "Туфли на каблуке",   "prompt": "wearing high heels"},
                    {"id": "stockings",  "label": "Чулки",        "icon": "▌", "description": "Чулки до бедра",     "prompt": "thigh-high stockings"},
                    {"id": "cat_ears",   "label": "Ушки",         "icon": "∧", "description": "Кошачьи ушки",      "prompt": "cat ears"},
                    {"id": "tail",       "label": "Хвост",        "icon": "〜", "description": "Пушистый хвост",    "prompt": "animal tail"},
                    {"id": "wings",      "label": "Крылья",       "icon": "✦", "description": "Фэнтезийные крылья","prompt": "wings, fantasy wings"},
                    {"id": "tattoo",     "label": "Тату",         "icon": "∼", "description": "Татуировки",         "prompt": "tattoos on body"},
                    {"id": "choker",     "label": "Чокер",        "icon": "○", "description": "Чокер на шею",       "prompt": "choker necklace"},
                ]
            }
        }
    }
}

ACTIONS = [
    {"id": "standing",     "label": "Стоит",           "icon": "▌", "description": "Стоячая поза",            "prompt": "standing pose"},
    {"id": "sitting",      "label": "Сидит",           "icon": "⌐", "description": "Сидящая поза",            "prompt": "sitting"},
    {"id": "lying_down",   "label": "Лежит",           "icon": "─", "description": "Лежит на поверхности",    "prompt": "lying down"},
    {"id": "walking",      "label": "Идёт",            "icon": "↗", "description": "Идёт вперёд",             "prompt": "walking"},
    {"id": "running",      "label": "Бежит",           "icon": "⇒", "description": "Бег",                    "prompt": "running, dynamic movement"},
    {"id": "jumping",      "label": "Прыжок",          "icon": "↑", "description": "В прыжке",                "prompt": "jumping in the air"},
    {"id": "fighting",     "label": "Боевая поза",     "icon": "◆", "description": "Боевая стойка",           "prompt": "fighting pose, combat stance"},
    {"id": "reading",      "label": "Читает",          "icon": "▭", "description": "Читает книгу",            "prompt": "reading a book"},
    {"id": "looking_back", "label": "Смотрит назад",   "icon": "↩", "description": "Взгляд через плечо",      "prompt": "looking back over shoulder"},
    {"id": "arms_crossed", "label": "Руки скрещены",   "icon": "✕", "description": "Скрещённые руки",         "prompt": "arms crossed"},
    {"id": "waving",       "label": "Машет рукой",     "icon": "∧", "description": "Приветственный жест",     "prompt": "waving hand, cheerful"},
    {"id": "thinking",     "label": "Задумался",       "icon": "?", "description": "Задумчивая поза",          "prompt": "thinking pose, hand on chin"},
    {"id": "smiling",      "label": "Улыбается",       "icon": "◡", "description": "Радостная улыбка",        "prompt": "smiling, happy expression"},
    {"id": "dancing",      "label": "Танцует",         "icon": "♪", "description": "Динамичный танец",        "prompt": "dancing, dynamic pose"},
    {"id": "magic",        "label": "Колдует",         "icon": "✦", "description": "Заклинание магии",        "prompt": "casting magic spell, glowing magical energy around hands"},
    {"id": "cooking",      "label": "Готовит",         "icon": "○", "description": "Готовит еду",             "prompt": "cooking, holding cooking utensils"},
    {"id": "portrait",     "label": "Портрет",         "icon": "◈", "description": "Крупный план, лицо",      "prompt": "portrait shot, close-up face, upper body"},
    {"id": "full_body",    "label": "Полный рост",     "icon": "▌", "description": "Фигура в полный рост",    "prompt": "full body shot, full figure visible"},
    {"id": "action_pose",  "label": "Экшн-поза",       "icon": "⚡", "description": "Динамичная поза героя",   "prompt": "dynamic action pose, hero stance"},
    {"id": "leaning",      "label": "Опирается",       "icon": "⌇", "description": "Облокотился на стену",    "prompt": "leaning against wall, relaxed pose"},
]

LOCATIONS = [
    {"id": "city_street",     "label": "Улица города",    "icon": "⬡", "description": "Городская улица",           "prompt": "city street background, urban environment"},
    {"id": "forest",          "label": "Лес",             "icon": "✦", "description": "Мистический густой лес",    "prompt": "forest background, trees, dappled light, nature"},
    {"id": "beach",           "label": "Пляж",            "icon": "〰", "description": "Тропический пляж",          "prompt": "beach background, ocean waves, sand, sunlight"},
    {"id": "school",          "label": "Школа",           "icon": "▣", "description": "Школьный класс",            "prompt": "school classroom background, school hallway"},
    {"id": "cafe",            "label": "Кафе",            "icon": "○", "description": "Уютное кафе",               "prompt": "café background, coffee shop interior, warm lighting"},
    {"id": "rooftop",         "label": "Крыша",           "icon": "⬡", "description": "Крыша на закате",           "prompt": "rooftop background, city skyline, golden sunset"},
    {"id": "bedroom",         "label": "Спальня",         "icon": "□", "description": "Уютная спальня",            "prompt": "bedroom background, cozy interior, soft lighting"},
    {"id": "fantasy_world",   "label": "Фэнтези мир",     "icon": "✦", "description": "Магический фэнтезийный мир","prompt": "fantasy world background, magical landscape, mystical glowing environment"},
    {"id": "space",           "label": "Космос",          "icon": "○", "description": "Открытый космос",           "prompt": "space background, stars and nebula, cosmos, galaxy"},
    {"id": "japanese_street", "label": "Япония",          "icon": "⛩", "description": "Японская улица",            "prompt": "Japanese street background, cherry blossoms, traditional Japan"},
    {"id": "library",         "label": "Библиотека",      "icon": "▭", "description": "Большая библиотека",        "prompt": "grand library background, towering bookshelves, warm study lights"},
    {"id": "mountains",       "label": "Горы",            "icon": "▲", "description": "Горный пейзаж",             "prompt": "mountain background, dramatic mountain peaks, misty atmosphere"},
    {"id": "dungeon",         "label": "Подземелье",      "icon": "◆", "description": "Тёмное подземелье",         "prompt": "dungeon background, dark cave, stone walls, torchlight"},
    {"id": "cyberpunk_city",  "label": "Киберпанк",       "icon": "⚡", "description": "Неоновый кибергород",       "prompt": "cyberpunk city background, neon lights, rain-slicked streets, futuristic"},
    {"id": "white_studio",    "label": "Студия",          "icon": "□", "description": "Белый фотофон",             "prompt": "white studio background, clean minimalist background"},
    {"id": "garden",          "label": "Сад",             "icon": "✿", "description": "Цветущий сад",              "prompt": "garden background, flowers blooming, peaceful nature"},
    {"id": "rainy_street",    "label": "Дождливая улица", "icon": "〰", "description": "Ночь под дождём",           "prompt": "rainy street background, rain drops, wet pavement reflections, moody night"},
    {"id": "sunset_field",    "label": "Закат в поле",    "icon": "○", "description": "Золотой закат в поле",      "prompt": "sunset field background, golden hour light, warm sky, meadow"},
    {"id": "underwater",      "label": "Под водой",       "icon": "〰", "description": "Подводный мир",             "prompt": "underwater background, ocean depths, rays of light, bubbles, sea life"},
    {"id": "ancient_ruins",   "label": "Руины",           "icon": "▣", "description": "Древние руины",             "prompt": "ancient ruins background, crumbling stone architecture, overgrown vines"},
]

CAMERA_ANGLES = [
    {"id": "cam_eye_level",    "label": "На уровне глаз",  "icon": "◈", "description": "Нейтральный ракурс",         "prompt": "eye level shot, neutral angle"},
    {"id": "cam_low_angle",    "label": "Снизу",           "icon": "↑", "description": "Съёмка снизу",               "prompt": "low angle shot, shot from below, worm's eye view"},
    {"id": "cam_high_angle",   "label": "Сверху",          "icon": "↓", "description": "Съёмка сверху",              "prompt": "high angle shot, shot from above"},
    {"id": "cam_birds_eye",    "label": "Вид птицы",       "icon": "⬡", "description": "Вид прямо сверху",           "prompt": "bird's eye view, top down angle"},
    {"id": "cam_dutch",        "label": "Наклон",          "icon": "⌇", "description": "Наклонный ракурс",           "prompt": "dutch angle, tilted camera"},
    {"id": "cam_closeup",      "label": "Крупный план",    "icon": "◎", "description": "Лицо и плечи",               "prompt": "close-up shot, face and shoulders"},
    {"id": "cam_extreme_close","label": "Сверхкрупный",    "icon": "◉", "description": "Только лицо",                "prompt": "extreme close-up, face only"},
    {"id": "cam_medium",       "label": "Средний план",    "icon": "▐", "description": "Пояс и выше",                "prompt": "medium shot, waist up"},
    {"id": "cam_cowboy",       "label": "Ковбойский",      "icon": "▌", "description": "Колени и выше",              "prompt": "cowboy shot, thighs up"},
    {"id": "cam_full_body",    "label": "Полный рост",     "icon": "█", "description": "Вся фигура",                 "prompt": "full body shot, full figure"},
    {"id": "cam_over_shoulder","label": "Через плечо",     "icon": "↩", "description": "Взгляд через плечо",         "prompt": "over the shoulder shot"},
    {"id": "cam_from_behind",  "label": "Сзади",           "icon": "↗", "description": "Вид со спины",               "prompt": "shot from behind, back view"},
    {"id": "cam_side",         "label": "Сбоку",           "icon": "▷", "description": "Вид сбоку (профиль)",        "prompt": "side view, profile shot"},
    {"id": "cam_three_quarter","label": "¾ ракурс",        "icon": "◈", "description": "Три четверти",               "prompt": "three quarter view, 3/4 angle"},
    {"id": "cam_fisheye",      "label": "«Рыбий глаз»",   "icon": "○", "description": "Широкоугольный объектив",    "prompt": "fisheye lens, wide angle distortion"},
    {"id": "cam_pov",          "label": "Вид от первого",  "icon": "◆", "description": "Перспектива первого лица",   "prompt": "point of view shot, first person perspective"},
]
