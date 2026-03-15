"""AI Prompt Constructor — FastAPI Backend v2.1 (RU)"""
import sys, os, uuid, copy, configparser, webbrowser

_REQUIRED = {
    "fastapi":   "fastapi>=0.104.0",
    "uvicorn":   "uvicorn[standard]>=0.24.0",
    "pydantic":  "pydantic>=2.0.0",
    "multipart": "python-multipart>=0.0.6",
}
_missing = []
for _m, _p in _REQUIRED.items():
    try: __import__(_m)
    except ImportError:
        _missing.append(_p)
        print(f"[ERROR] Отсутствует пакет '{_m}'  →  pip install {_p}", file=sys.stderr)
if _missing:
    print(f"\n[FATAL] Установите зависимости:\n  pip install {' '.join(_missing)}", file=sys.stderr)
    sys.exit(1)

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any

from presets import STYLE_PRESETS, CHARACTER_OPTIONS, ACTIONS, LOCATIONS, CAMERA_ANGLES
from prompt_builder import build_prompt
from custom_manager import CATEGORY_PATHS, add_option, delete_option, get_all as get_all_custom, merge_into_presets

# ── Пути ──────────────────────────────────────────────────────────
_BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_BASE_DIR)
_FRONTEND_DIR = os.path.join(_PROJECT_ROOT, "frontend")
_IMAGES_DIR   = os.path.join(_PROJECT_ROOT, "static", "images")
_CONFIG_FILE  = os.path.join(_BASE_DIR, "config.ini")

os.makedirs(_IMAGES_DIR, exist_ok=True)

# ── Читаем config.ini ─────────────────────────────────────────────
_cfg = configparser.ConfigParser()
_cfg.read(_CONFIG_FILE, encoding="utf-8")

def _cfg_get(key: str, fallback: str) -> str:
    try:    return _cfg.get("server", key).strip() or fallback
    except: return fallback

SERVER_HOST    = _cfg_get("host",         "0.0.0.0")
SERVER_PORT    = int(_cfg_get("port",     "8888"))
OPEN_BROWSER   = _cfg_get("open_browser", "true").lower() == "true"
_browser_host  = _cfg_get("browser_host", "")
BROWSER_URL    = f"http://{_browser_host or 'localhost'}:{SERVER_PORT}"

_ALLOWED_EXTS    = {".jpg",".jpeg",".png",".webp",".gif",".avif"}
_MAX_IMAGE_BYTES = 8 * 1024 * 1024

# ── FastAPI ───────────────────────────────────────────────────────
app = FastAPI(title="AI Prompt Constructor", version="2.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

if os.path.isdir(_FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=_FRONTEND_DIR), name="static")
else:
    print("[WARN] Директория frontend/ не найдена.", file=sys.stderr)

app.mount("/images", StaticFiles(directory=_IMAGES_DIR), name="images")

def _merged_presets() -> Dict[str, Any]:
    data = {
        "styles":    copy.deepcopy(STYLE_PRESETS),
        "character": copy.deepcopy(CHARACTER_OPTIONS),
        "actions":   copy.deepcopy(ACTIONS),
        "locations": copy.deepcopy(LOCATIONS),
        "cameras":   copy.deepcopy(CAMERA_ANGLES),
    }
    return merge_into_presets(data)

# ── Роуты ─────────────────────────────────────────────────────────

@app.get("/", include_in_schema=False)
async def root():
    p = os.path.join(_FRONTEND_DIR, "index.html")
    return FileResponse(p, media_type="text/html") if os.path.isfile(p) else {"docs": "/docs"}

@app.get("/api/health")
async def health():
    return {"status": "ok", "version": "2.1.0", "host": SERVER_HOST, "port": SERVER_PORT}

@app.get("/api/presets")
async def get_presets():
    data = _merged_presets()
    data["category_paths"] = CATEGORY_PATHS
    return data

@app.get("/api/custom-options")
async def list_custom(): return get_all_custom()

class CustomOptionPayload(BaseModel):
    category_path: str
    label:         str
    description:   Optional[str] = ""
    prompt:        str
    icon:          Optional[str] = "✦"
    image:         Optional[str] = None
    color:         Optional[str] = None

@app.post("/api/custom-options", status_code=201)
async def create_custom(payload: CustomOptionPayload):
    try:
        saved = add_option(payload.category_path, payload.model_dump())
        return {"success": True, "option": saved}
    except ValueError as e: raise HTTPException(400, str(e))
    except Exception as e:  raise HTTPException(500, f"Ошибка сохранения: {e}")

@app.delete("/api/custom-options/{category_path:path}/{option_id}")
async def remove_custom(category_path: str, option_id: str):
    try:
        ok = delete_option(category_path, option_id)
        if not ok: raise HTTPException(404, "Опция не найдена")
        return {"success": True, "deleted": option_id}
    except ValueError as e: raise HTTPException(400, str(e))

@app.post("/api/upload-image")
async def upload_image(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in _ALLOWED_EXTS:
        raise HTTPException(400, f"Неподдерживаемый тип '{ext}'. Допустимо: {', '.join(_ALLOWED_EXTS)}")
    data = await file.read()
    if len(data) > _MAX_IMAGE_BYTES: raise HTTPException(400, "Файл слишком большой (макс. 8 МБ)")
    fname = f"{uuid.uuid4().hex}{ext}"
    fpath = os.path.join(_IMAGES_DIR, fname)
    try:
        with open(fpath, "wb") as fh: fh.write(data)
    except OSError as e: raise HTTPException(500, f"Не удалось сохранить: {e}")
    return {"success": True, "filename": fname, "url": f"/images/{fname}"}

@app.delete("/api/images/{filename}")
async def delete_image(filename: str):
    if ".." in filename or "/" in filename or "\\" in filename:
        raise HTTPException(400, "Недопустимое имя файла")
    p = os.path.join(_IMAGES_DIR, filename)
    if not os.path.isfile(p): raise HTTPException(404, "Файл не найден")
    try: os.remove(p); return {"success": True}
    except OSError as e: raise HTTPException(500, str(e))

class PromptRequest(BaseModel):
    style:       Optional[str]  = None
    selections:  Dict[str, Any] = {}
    action:      Optional[str]  = None
    location:    Optional[str]  = None
    camera:      Optional[str]  = None
    custom_text: Optional[str]  = None

@app.post("/api/build-prompt")
async def api_build_prompt(req: PromptRequest):
    try:
        prompt = build_prompt(
            style=req.style, selections=req.selections,
            action=req.action, location=req.location,
            camera=req.camera, custom_text=req.custom_text,
        )
        return {"prompt": prompt, "word_count": len(prompt.split()) if prompt else 0, "success": True}
    except Exception as e: raise HTTPException(400, str(e))

# ── Запуск ────────────────────────────────────────────────────────

if __name__ == "__main__":
    try: import uvicorn
    except ImportError:
        print("[FATAL] uvicorn не установлен", file=sys.stderr); sys.exit(1)

    print("=" * 46)
    print("  AI Prompt Constructor  v2.1  (RU)")
    print("  by MyroSoft")
    print("=" * 46)
    print(f"  UI      ->  {BROWSER_URL}")
    print(f"  Docs    ->  {BROWSER_URL}/docs")
    print(f"  Bind    ->  {SERVER_HOST}:{SERVER_PORT}")
    print(f"  Config  ->  config.ini")
    print("=" * 46)

    if OPEN_BROWSER:
        import threading
        def _open(): 
            import time; time.sleep(1.5)
            webbrowser.open(BROWSER_URL)
        threading.Thread(target=_open, daemon=True).start()

    uvicorn.run(
        "main:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=True,
        log_level="info",
    )
