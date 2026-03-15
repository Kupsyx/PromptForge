"""
custom_manager.py — хранение пользовательских опций в custom_options.json
"""
import json, os, uuid, sys, copy
from typing import Any, Dict, List, Optional

_CUSTOM_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "custom_options.json")

CATEGORY_PATHS: Dict[str, str] = {
    "gender":              "Пол",
    "age":                 "Возраст",
    "hair.hair_color":     "Волосы → Цвет",
    "hair.hair_style":     "Волосы → Стиль",
    "face":                "Лицо",
    "body.build":          "Тело → Телосложение",
    "body.bust":           "Тело → Грудь (жен.)",
    "body.chest":          "Тело → Плечи / Торс",
    "body.legs":           "Тело → Ноги",
    "body.arms":           "Тело → Руки",
    "clothes.outerwear":   "Одежда → Верхняя",
    "clothes.underwear":   "Одежда → Нижний слой",
    "clothes.accessories": "Одежда → Аксессуары",
    "action":              "Действие",
    "location":            "Локация",
    "camera":              "Ракурс",
}

def load_custom() -> Dict[str, List[Dict]]:
    if not os.path.exists(_CUSTOM_FILE):
        return {}
    try:
        with open(_CUSTOM_FILE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except Exception as exc:
        print(f"[WARN] custom_manager: cannot load {_CUSTOM_FILE}: {exc}", file=sys.stderr)
        return {}

def _save_custom(data: Dict) -> None:
    try:
        with open(_CUSTOM_FILE, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
    except Exception as exc:
        print(f"[ERROR] custom_manager: cannot save: {exc}", file=sys.stderr)

def add_option(category_path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    if category_path not in CATEGORY_PATHS:
        raise ValueError(f"Неизвестный путь категории: '{category_path}'")
    data = load_custom()
    if category_path not in data:
        data[category_path] = []
    option: Dict[str, Any] = {
        "id":          f"custom_{uuid.uuid4().hex[:10]}",
        "label":       payload.get("label", "Custom").strip(),
        "description": payload.get("description", "").strip(),
        "prompt":      payload.get("prompt", "").strip(),
        "icon":        payload.get("icon", "✦").strip() or "✦",
        "custom":      True,
    }
    if payload.get("image"):  option["image"] = payload["image"]
    if payload.get("color"):  option["color"] = payload["color"]
    data[category_path].append(option)
    _save_custom(data)
    return option

def delete_option(category_path: str, option_id: str) -> bool:
    if category_path not in CATEGORY_PATHS:
        raise ValueError(f"Неизвестный путь: '{category_path}'")
    data = load_custom()
    before = len(data.get(category_path, []))
    data[category_path] = [o for o in data.get(category_path, []) if o.get("id") != option_id]
    if len(data.get(category_path, [])) < before:
        _save_custom(data)
        return True
    return False

def get_all() -> Dict[str, List[Dict]]:
    return load_custom()

def merge_into_presets(presets: Dict[str, Any]) -> Dict[str, Any]:
    custom = load_custom()
    if not custom:
        return presets
    char = presets.get("character", {})
    _PATH_MAP = {
        "gender": lambda _: char.get("gender", {}).get("options", []),
        "age":    lambda _: char.get("age",    {}).get("options", []),
        "face":   lambda _: char.get("face",   {}).get("options", []),
        "hair.hair_color": lambda _: char.get("hair",{}).get("subcategories",{}).get("hair_color",{}).get("options",[]),
        "hair.hair_style": lambda _: char.get("hair",{}).get("subcategories",{}).get("hair_style",{}).get("options",[]),
        "body.build":  lambda _: char.get("body",{}).get("subcategories",{}).get("build",{}).get("options",[]),
        "body.bust":   lambda _: char.get("body",{}).get("subcategories",{}).get("bust",{}).get("options",[]),
        "body.chest":  lambda _: char.get("body",{}).get("subcategories",{}).get("chest",{}).get("options",[]),
        "body.legs":   lambda _: char.get("body",{}).get("subcategories",{}).get("legs",{}).get("options",[]),
        "body.arms":   lambda _: char.get("body",{}).get("subcategories",{}).get("arms",{}).get("options",[]),
        "clothes.outerwear":   lambda _: char.get("clothes",{}).get("subcategories",{}).get("outerwear",{}).get("options",[]),
        "clothes.underwear":   lambda _: char.get("clothes",{}).get("subcategories",{}).get("underwear",{}).get("options",[]),
        "clothes.accessories": lambda _: char.get("clothes",{}).get("subcategories",{}).get("accessories",{}).get("options",[]),
        "action":   lambda _: presets.get("actions",   []),
        "location": lambda _: presets.get("locations", []),
        "camera":   lambda _: presets.get("cameras",   []),
    }
    for path, entries in custom.items():
        if not entries: continue
        resolver = _PATH_MAP.get(path)
        if not resolver:
            print(f"[WARN] custom_manager: неизвестный путь '{path}' — пропущен", file=sys.stderr)
            continue
        target = resolver(path)
        if target is None: continue
        existing = {o.get("id") for o in target}
        for entry in entries:
            if entry.get("id") not in existing:
                target.append(entry)
    return presets
