<div align="center">

# ✦ PromptForge

**Визуальный конструктор промптов для генерации ИИ-изображений**

![Python](https://img.shields.io/badge/Python-3.10%2B-8b5cf6?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-8b5cf6?style=flat-square&logo=fastapi&logoColor=white)
![Vanilla JS](https://img.shields.io/badge/Frontend-Vanilla%20JS-8b5cf6?style=flat-square&logo=javascript&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-8b5cf6?style=flat-square)

*Собирайте детальные промпты через удобный тёмный UI — без ручного ввода текста*

</div>

---

## 📋 Содержание

- [О проекте](#-о-проекте)
- [Скриншоты](#-скриншоты)
- [Возможности](#-возможности)
- [Быстрый старт](#-быстрый-старт)
- [Структура проекта](#-структура-проекта)
- [Конфигурация](#-конфигурация)
- [Добавление изображений](#-добавление-изображений-в-карточки)
- [Кастомные опции](#-кастомные-опции)
- [API](#-api)
- [Стек технологий](#-стек-технологий)

---

## 🎯 О проекте

**PromptForge** — веб-приложение для пошагового составления промптов для ИИ-генераторов изображений (Stable Diffusion, Midjourney, DALL·E и др.).

Вместо ручного набора текста вы собираете персонажа через карточки: выбираете стиль, пол, возраст, причёску, черты лица, телосложение, одежду, действие, локацию и ракурс. Промпт формируется **в реальном времени** и копируется одной кнопкой.

---

## ✨ Возможности

### Конструктор персонажа — **167 встроенных опций**

| Категория | Параметры | Опций |
|-----------|-----------|-------|
| 🎨 **Стиль** | Аниме, Реализм | 2 |
| ⊹ **Пол** | Мужской, Женский, Андрогин | 3 |
| ◷ **Возраст** | Подросток → Зрелый | 4 |
| ✿ **Цвет волос** | 12 цветов со свотчами | 12 |
| ✿ **Стиль волос** | Короткие → Андеркат | 14 |
| ◯ **Лицо** | Черты, форма, цвет глаз (мульти) | 14 |
| ⟡ **Телосложение** | Стройное → Пухлое | 8 |
| ⟡ **Грудь** | Только для жен. персонажей | 5 |
| ⟡ **Плечи/Торс** | Широкие → Рельефный | 4 |
| ⟡ **Ноги** | Длинные → Подтянутые | 4 |
| ⟡ **Руки** | Изящные → Мягкие | 4 |
| ✤ **Верхняя одежда** | Костюм, Кимоно, Броня… | 16 |
| ✤ **Нижний слой** | Рубашка, Кроп-топ… | 7 |
| ✤ **Аксессуары** | Очки, Крылья, Тату… (мульти) | 16 |
| ▌ **Действие** | Стоит, Колдует, Танцует… | 20 |
| ⬡ **Локация** | Лес, Киберпанк, Космос… | 20 |
| ◈ **Ракурс камеры** | Сверху, Снизу, Рыбий глаз… | 16 |

### UX-функции

- ⚡ **Live-превью** — промпт обновляется при каждом клике
- ⎘ **Копировать** одной кнопкой (`Ctrl+Enter`)
- ↺ **Сброс** всех параметров
- 🔢 **Счётчик слов** промпта
- ● **Прогресс-точки** в шапке — видно что уже заполнено
- 👙 **Умная блокировка** — размер груди активен только для женских персонажей
- ＋ **Добавить своё** — кастомные опции в любую категорию
- 🗑 **Удаление** кастомных опций прямо с карточки
- 🖼 **Изображения на карточках** — кладите PNG/WebP в `static/images/`

---

## 🚀 Быстрый старт

### Требования

- **Python 3.10+** → [скачать](https://www.python.org/downloads/)
- При установке Python включить **"Add Python to PATH"**

### Windows — одним кликом

```
Дважды кликните start.bat
```

Скрипт сам установит зависимости и откроет браузер.

### Вручную (Windows / macOS / Linux)

```bash
# 1. Клонировать репозиторий
git clone https://github.com/YOUR_USERNAME/promptforge.git
cd promptforge

# 2. Установить зависимости
pip install -r backend/requirements.txt

# 3. Запустить
cd backend
python main.py
```

Открыть в браузере: **http://localhost:8888**

---

## 📁 Структура проекта

```
promptforge/
│
├── start.bat                   ← Запуск одним кликом (Windows)
│
├── backend/
│   ├── main.py                 ← FastAPI-сервер, API-роуты
│   ├── presets.py              ← Все встроенные опции (167 шт.)
│   ├── prompt_builder.py       ← Сборка финального промпта
│   ├── custom_manager.py       ← CRUD кастомных опций + JSON
│   ├── config.ini              ← Настройки хоста и порта
│   ├── requirements.txt        ← Python-зависимости
│   └── custom_options.json     ← Создаётся автоматически при добавлении своих опций
│
├── frontend/
│   ├── index.html              ← Разметка UI
│   ├── style.css               ← Dark-тема, glassmorphism
│   └── app.js                  ← Логика, стейт, рендеринг
│
├── static/
│   └── images/
│       ├── _placeholder.svg    ← Заглушка при отсутствии фото
│       ├── female.png          ← Изображения карточек (добавляете сами)
│       └── ...
│
└── README.md
```

---

## ⚙️ Конфигурация

Файл **`backend/config.ini`** — откройте в любом текстовом редакторе:

```ini
[server]
host = 0.0.0.0       # 0.0.0.0 = доступно по локальной сети
                     # 127.0.0.1 = только этот компьютер
port = 8888          # порт (измените если конфликт с ComfyUI / A1111)

open_browser = true  # автоматически открывать браузер при старте

browser_host =       # если пусто — откроет localhost
                     # укажите LAN IP для доступа с других устройств
```

### Примеры настройки

| Сценарий | `host` | `port` | `browser_host` |
|----------|--------|--------|----------------|
| Только локально | `127.0.0.1` | `8888` | *(пусто)* |
| Рядом с ComfyUI (7860) | `0.0.0.0` | `8888` | *(пусто)* |
| Доступ по локальной сети | `0.0.0.0` | `8888` | `192.168.1.100` |

---

## 🖼 Добавление изображений в карточки

Положите изображение в папку `static/images/` с именем **равным ID опции**.

### Правило именования

```
static/images/{option_id}.png   (или .jpg / .webp)
```

### Примеры

```
static/images/female.png
static/images/pink.webp
static/images/leather_jacket.jpg
static/images/cyberpunk_city.webp
```

### Порядок поиска изображения

Для каждой карточки приложение ищет файл в такой последовательности:

```
1. /images/{opt.image}        ← если задано вручную через "Add Custom"
2. /images/{opt.id}.jpg
3. /images/{opt.id}.png
4. /images/{opt.id}.webp
5. Заглушка с иконкой         ← если ничего не найдено
```

### Рекомендуемые параметры

| Параметр | Значение |
|----------|----------|
| Разрешение | 768 × 512 px |
| Соотношение сторон | 3:2 |
| Формат | WebP (лучшее сжатие) или PNG |
| Макс. размер | до 2 МБ на файл |

### Полный список ID для изображений

<details>
<summary>Показать все 148 ID</summary>

**Пол:** `male` `female` `androgynous`

**Возраст:** `teen` `young_adult` `adult` `mature`

**Цвет волос:** `black` `dark_brown` `brown` `blonde` `red` `pink` `purple` `blue` `silver` `white` `green` `orange`

**Стиль волос:** `short` `medium` `long` `very_long` `curly` `wavy` `straight` `braided` `ponytail` `twin_tails` `bun` `messy` `spiky` `undercut`

**Лицо:** `cute` `pretty` `handsome` `sharp` `soft` `round_face` `oval_face` `freckles` `blue_eyes` `green_eyes` `brown_eyes` `purple_eyes` `red_eyes` `heterochromia`

**Телосложение:** `slim` `athletic` `muscular` `curvy` `petite` `tall` `average` `chubby`

**Грудь:** `bust_flat` `bust_small` `bust_medium` `bust_large` `bust_huge`

**Торс:** `broad_shoulders` `narrow_shoulders` `flat_chest` `toned_torso`

**Ноги:** `long_legs` `short_legs` `thick_legs` `toned_legs`

**Руки:** `slender_arms` `muscular_arms` `toned_arms` `soft_arms`

**Верхняя одежда:** `business_suit` `casual_tshirt` `hoodie` `leather_jacket` `school_uniform` `dress` `kimono` `military` `sportswear` `trench_coat` `maid_outfit` `fantasy_armor` `streetwear` `swimwear` `gothic` `ninja`

**Нижний слой:** `white_shirt` `turtleneck` `crop_top` `tank_top` `lingerie` `boxer` `shorts`

**Аксессуары:** `glasses` `sunglasses` `hat` `scarf` `earrings` `necklace` `gloves` `boots` `sneakers` `heels` `stockings` `cat_ears` `tail` `wings` `tattoo` `choker`

**Действие:** `standing` `sitting` `lying_down` `walking` `running` `jumping` `fighting` `reading` `looking_back` `arms_crossed` `waving` `thinking` `smiling` `dancing` `magic` `cooking` `portrait` `full_body` `action_pose` `leaning`

**Локация:** `city_street` `forest` `beach` `school` `cafe` `rooftop` `bedroom` `fantasy_world` `space` `japanese_street` `library` `mountains` `dungeon` `cyberpunk_city` `white_studio` `garden` `rainy_street` `sunset_field` `underwater` `ancient_ruins`

**Ракурс:** `cam_eye_level` `cam_low_angle` `cam_high_angle` `cam_birds_eye` `cam_dutch` `cam_closeup` `cam_extreme_close` `cam_medium` `cam_cowboy` `cam_full_body` `cam_over_shoulder` `cam_from_behind` `cam_side` `cam_three_quarter` `cam_fisheye` `cam_pov`

</details>

---

## ➕ Кастомные опции

В каждой категории есть кнопка **＋ Добавить**. В открывшемся окне:

| Поле | Описание |
|------|----------|
| **Категория** | Куда добавить опцию |
| **Название** | Текст на карточке |
| **Описание** | Подпись под названием |
| **Текст промпта** | Фрагмент, добавляемый к итогу |
| **Иконка** | Эмодзи/символ если нет картинки |
| **Цвет свотча** | Только для категории «Цвет волос» |
| **Изображение** | Drag & drop, до 8 МБ |

Все кастомные опции сохраняются в `backend/custom_options.json` и **переживают перезапуск** сервера.

Удалить опцию — навести мышь на карточку и нажать **✕**.

---

## 🔌 API

Swagger-документация: **`http://localhost:8888/docs`**

### Эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| `GET` | `/` | Frontend UI |
| `GET` | `/api/health` | Статус сервера |
| `GET` | `/api/presets` | Все пресеты + кастомные опции |
| `POST` | `/api/build-prompt` | Сборка промпта на сервере |
| `GET` | `/api/custom-options` | Список кастомных опций |
| `POST` | `/api/custom-options` | Добавить опцию |
| `DELETE` | `/api/custom-options/{path}/{id}` | Удалить опцию |
| `POST` | `/api/upload-image` | Загрузить изображение |
| `DELETE` | `/api/images/{filename}` | Удалить изображение |

### Пример запроса `POST /api/build-prompt`

```json
{
  "style": "anime",
  "selections": {
    "gender": "female",
    "age": "young_adult",
    "hair": { "hair_color": "pink", "hair_style": "long" },
    "face": ["cute", "blue_eyes", "freckles"],
    "body": { "build": "slim", "bust": "bust_medium" },
    "clothes": {
      "outerwear": ["school_uniform"],
      "accessories": ["cat_ears", "stockings"]
    }
  },
  "action": "smiling",
  "location": "japanese_street",
  "camera": "cam_medium",
  "custom_text": "sakura petals, soft bokeh, golden hour"
}
```

```json
{
  "prompt": "anime style, high quality 2D illustration, ..., pink hair, long hair, cute face, ...",
  "word_count": 54,
  "success": true
}
```

---

## 🛠 Стек технологий

| Слой | Технология |
|------|-----------|
| **Backend** | Python 3.10+, FastAPI, Uvicorn, Pydantic v2 |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript (ES2022) |
| **Хранение данных** | JSON-файл (custom_options.json) |
| **Шрифты** | Syne, DM Sans (Google Fonts) |
| **UI-стиль** | Dark theme, Glassmorphism, CSS Variables |

---

## 📦 Зависимости

```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.5.0
python-multipart>=0.0.6
```

---

## 🔧 Устранение неполадок

**`python` не найден**
→ Установите Python 3.10+ и включите «Add Python to PATH»

**Порт занят**
→ Откройте `backend/config.ini` и измените `port = 8888` на любой свободный

**Конфликт с ComfyUI (7860) или A1111 (7861)**
→ Используйте порт `8888`, `9000`, `9999` или любой другой выше 8000

**Frontend не загружается**
→ Убедитесь что запускаете `python main.py` из папки `backend/`

**Изображения не показываются**
→ Проверьте имя файла: должно совпадать с ID опции (`female.png`, а не `Female.PNG`)

---

<div align="center">

© 2025 **MyroSoft** · PromptForge v2.1

</div>
