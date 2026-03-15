"""prompt_builder.py — сборка финального промпта из выборов пользователя"""
from typing import Optional, Dict, Any
from presets import STYLE_PRESETS, CHARACTER_OPTIONS, ACTIONS, LOCATIONS, CAMERA_ANGLES

def _find_prompt(options: list, option_id: str) -> Optional[str]:
    for opt in options:
        if opt["id"] == option_id:
            return opt.get("prompt")
    return None

def build_prompt(
    style:       Optional[str]  = None,
    selections:  Dict[str, Any] = {},
    action:      Optional[str]  = None,
    location:    Optional[str]  = None,
    camera:      Optional[str]  = None,
    custom_text: Optional[str]  = None,
) -> str:
    parts: list[str] = []

    if style and style in STYLE_PRESETS:
        parts.append(STYLE_PRESETS[style]["prompt"])

    gender_id = selections.get("gender")
    if gender_id:
        p = _find_prompt(CHARACTER_OPTIONS["gender"]["options"], gender_id)
        if p: parts.append(p)

    age_id = selections.get("age")
    if age_id:
        p = _find_prompt(CHARACTER_OPTIONS["age"]["options"], age_id)
        if p: parts.append(p)

    hair_sels = selections.get("hair", {})
    if isinstance(hair_sels, dict):
        sc = CHARACTER_OPTIONS["hair"]["subcategories"]
        for key in ("hair_color", "hair_style"):
            vid = hair_sels.get(key)
            if vid:
                p = _find_prompt(sc[key]["options"], vid)
                if p: parts.append(p)

    face_sels = selections.get("face", [])
    if face_sels:
        face_opts = CHARACTER_OPTIONS["face"]["options"]
        ids = face_sels if isinstance(face_sels, list) else [face_sels]
        for opt in face_opts:
            if opt["id"] in ids and opt.get("prompt"):
                parts.append(opt["prompt"])

    body_sels = selections.get("body", {})
    if isinstance(body_sels, dict):
        for sid, subcat in CHARACTER_OPTIONS["body"]["subcategories"].items():
            chosen = body_sels.get(sid)
            if chosen:
                p = _find_prompt(subcat["options"], chosen)
                if p: parts.append(p)

    clothes_sels = selections.get("clothes", {})
    if isinstance(clothes_sels, dict):
        for sid, subcat in CHARACTER_OPTIONS["clothes"]["subcategories"].items():
            chosen_list = clothes_sels.get(sid, [])
            if isinstance(chosen_list, str): chosen_list = [chosen_list]
            for item_id in chosen_list:
                p = _find_prompt(subcat["options"], item_id)
                if p: parts.append(p)

    if action:
        p = _find_prompt(ACTIONS, action)
        if p: parts.append(p)

    if location:
        p = _find_prompt(LOCATIONS, location)
        if p: parts.append(p)

    if camera:
        p = _find_prompt(CAMERA_ANGLES, camera)
        if p: parts.append(p)

    if custom_text and custom_text.strip():
        parts.append(custom_text.strip())

    return ", ".join(p for p in parts if p)
