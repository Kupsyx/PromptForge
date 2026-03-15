/* ═══════════════════════════════════════════════════════════════
   PromptForge v2.1 — app.js (RU)
   + Ракурс камеры · Грудь (только жен.) · Русский UI · Footer
   ═══════════════════════════════════════════════════════════════ */
"use strict";

/* ══════════════════════════════════════════════
   STATE
══════════════════════════════════════════════ */
const state = {
  style:    null,
  gender:   null,
  age:      null,
  hair:     { hair_color: null, hair_style: null },
  face:     new Set(),
  body:     {},
  clothes:  {},
  action:   null,
  location: null,
  camera:   null,
};

let presets       = null;
let categoryPaths = {};

const modal = { uploadedFilename: null };

/* ══════════════════════════════════════════════
   STARFIELD
══════════════════════════════════════════════ */
function initStarfield() {
  const canvas = document.getElementById("starfield");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const resize = () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; };
  resize();
  window.addEventListener("resize", resize, { passive: true });
  const stars = Array.from({ length: 80 }, () => ({
    x: Math.random() * canvas.width, y: Math.random() * canvas.height,
    r: Math.random() * 1.2 + 0.3,
    vx: (Math.random() - 0.5) * 0.2, vy: (Math.random() - 0.5) * 0.15,
    a: Math.random() * 0.45 + 0.08,
  }));
  const tick = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (const s of stars) {
      s.x += s.vx; s.y += s.vy;
      if (s.x < 0) s.x = canvas.width;  if (s.x > canvas.width)  s.x = 0;
      if (s.y < 0) s.y = canvas.height; if (s.y > canvas.height) s.y = 0;
      ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(167,139,250,${s.a})`; ctx.fill();
    }
    requestAnimationFrame(tick);
  };
  tick();
}

/* ══════════════════════════════════════════════
   FOOTER YEAR
══════════════════════════════════════════════ */
function initFooter() {
  const el = document.getElementById("footer-year");
  if (el) el.textContent = new Date().getFullYear();
}

/* ══════════════════════════════════════════════
   IMAGE HELPERS
══════════════════════════════════════════════ */
function buildCardImg(opt) {
  const wrap = document.createElement("div");
  wrap.className = "card-img-wrap";
  const img = document.createElement("img");
  img.className = "card-img"; img.alt = opt.label;
  const fallback = document.createElement("div");
  fallback.className = "card-fallback";
  fallback.innerHTML = `<span>${opt.icon || opt.label[0] || "✦"}</span><span class="card-fallback-hint">Нет фото</span>`;

  const sources = [];
  if (opt.image) sources.push(`/images/${opt.image}`);
  sources.push(`/images/${opt.id}.jpg`, `/images/${opt.id}.png`, `/images/${opt.id}.webp`);
  const seen = new Set();
  const queue = sources.filter(s => { if (seen.has(s)) return false; seen.add(s); return true; });
  let qi = 0;
  img.onerror = () => {
    if (qi >= queue.length) { wrap.classList.add("img-failed"); return; }
    img.src = queue[qi++];
  };
  img.src = queue[qi++];

  wrap.appendChild(img); wrap.appendChild(fallback);
  return wrap;
}

/* ══════════════════════════════════════════════
   DATA LOADING
══════════════════════════════════════════════ */
async function loadPresets() {
  try {
    const res = await fetch("/api/presets");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    presets       = data;
    categoryPaths = data.category_paths || {};
    initStateKeys();
    renderAll();
    hideLoading();
  } catch (err) {
    console.error("[PromptForge] Ошибка загрузки пресетов:", err);
    showError(`Не удалось подключиться к серверу (${err.message}). Убедитесь, что бэкенд запущен на порту 8000.`);
    hideLoading();
  }
}

function initStateKeys() {
  for (const id of Object.keys(presets.character.body.subcategories))    state.body[id]    ??= null;
  for (const id of Object.keys(presets.character.clothes.subcategories)) state.clothes[id] ??= new Set();
}

function hideLoading() {
  document.getElementById("loading-screen")?.classList.add("gone");
  document.getElementById("main-content")?.removeAttribute("aria-hidden");
}
function showError(msg) {
  const b = document.getElementById("error-banner"), t = document.getElementById("error-message");
  if (b && t) { t.textContent = msg; b.classList.remove("hidden"); }
}

/* ══════════════════════════════════════════════
   RENDER ALL
══════════════════════════════════════════════ */
function renderAll() {
  renderStyleGrid();
  renderFlatGrid("gender",   presets.character.gender.options, "single");
  renderFlatGrid("age",      presets.character.age.options,    "single");
  renderHairSection();
  renderFlatGrid("face",     presets.character.face.options,   "multi-face");
  renderBodySection();
  renderClothesSection();
  renderFlatGrid("action",   presets.actions,   "action");
  renderFlatGrid("location", presets.locations, "location");
  renderFlatGrid("camera",   presets.cameras || [], "camera");
}

/* ── Стиль ──────────────────────────────────── */
function renderStyleGrid() {
  const grid = document.getElementById("style-grid");
  if (!grid) return;
  grid.innerHTML = Object.values(presets.styles).map(s => `
    <div class="style-card" id="sc-${s.id}" role="button" tabindex="0" aria-pressed="false"
         onclick="selectStyle('${s.id}')" onkeydown="if(event.key==='Enter'||event.key===' ')selectStyle('${s.id}')">
      <div class="style-card-preview" style="background:${s.preview_gradient}">${s.icon}</div>
      <div class="style-card-body">
        <div class="style-card-name">${s.name}</div>
        <div class="style-card-desc">${s.description}</div>
      </div>
      <div class="style-card-check" aria-hidden="true">✓</div>
    </div>
  `).join("");
}
function selectStyle(id) {
  state.style = state.style === id ? null : id;
  document.querySelectorAll(".style-card").forEach(el => {
    const a = el.id === `sc-${state.style}`;
    el.classList.toggle("selected", a); el.setAttribute("aria-pressed", String(a));
  });
  refreshDots(); updatePrompt();
}

/* ── Универсальная плоская сетка карточек ─── */
function renderFlatGrid(catId, options, selType) {
  const grid = document.getElementById(`grid-${catId}`);
  if (!grid) return;
  grid.innerHTML = "";
  for (const opt of options) grid.appendChild(buildCard(opt, catId, selType));
}

function buildCard(opt, catId, selType) {
  const card = document.createElement("div");
  card.className = "card";
  card.id = `card-${catId}-${opt.id}`;
  card.setAttribute("role","button"); card.setAttribute("tabindex","0");
  card.setAttribute("aria-pressed","false"); card.setAttribute("aria-label", opt.label);

  const check = document.createElement("div");
  check.className = "card-check"; check.setAttribute("aria-hidden","true"); check.textContent = "✓";
  card.appendChild(check);

  if (opt.custom) {
    const del = document.createElement("button");
    del.className = "card-delete"; del.textContent = "✕"; del.title = "Удалить";
    del.setAttribute("aria-label", `Удалить ${opt.label}`);
    const path = _resolvePathForCat(catId);
    del.onclick = e => { e.stopPropagation(); deleteCustomOption(path, opt.id, opt.image); };
    card.appendChild(del);
  }

  card.appendChild(buildCardImg(opt));

  const body = document.createElement("div"); body.className = "card-body";
  const lbl  = document.createElement("span"); lbl.className = "card-label"; lbl.textContent = opt.label;
  const desc = document.createElement("span"); desc.className = "card-desc"; desc.textContent = opt.description || "";
  body.appendChild(lbl); body.appendChild(desc); card.appendChild(body);

  if (opt.custom) { const b = document.createElement("div"); b.className="card-custom-badge"; card.appendChild(b); }

  const handler = () => handleCardClick(catId, opt.id, selType);
  card.onclick = handler;
  card.onkeydown = e => { if (e.key==="Enter"||e.key===" ") handler(); };
  return card;
}

function handleCardClick(catId, optId, selType) {
  // Camera and location are simple singles stored in state directly
  const stateKey = selType === "action"   ? "action"
                 : selType === "location" ? "location"
                 : selType === "camera"   ? "camera"
                 : catId;

  if (selType === "single" || selType === "action" || selType === "location" || selType === "camera") {
    const prev = state[stateKey];
    if (prev) {
      const p = document.getElementById(`card-${catId}-${prev}`);
      if (p) { p.classList.remove("selected"); p.setAttribute("aria-pressed","false"); }
    }
    state[stateKey] = (prev === optId) ? null : optId;
    if (state[stateKey]) {
      const el = document.getElementById(`card-${catId}-${optId}`);
      if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
    }
    // special: when gender changes, update bust visibility
    if (stateKey === "gender") updateBustVisibility();
  } else if (selType === "multi-face") {
    const el = document.getElementById(`card-${catId}-${optId}`);
    if (state.face.has(optId)) {
      state.face.delete(optId);
      if (el) { el.classList.remove("selected"); el.setAttribute("aria-pressed","false"); }
    } else {
      state.face.add(optId);
      if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
    }
  }
  refreshDots(); updatePrompt();
}

/* ── Волосы ─────────────────────────────────── */
function renderHairSection() {
  const swatchRow = document.getElementById("grid-hair_color");
  if (swatchRow) {
    swatchRow.innerHTML = "";
    for (const opt of presets.character.hair.subcategories.hair_color.options)
      swatchRow.appendChild(buildSwatch(opt));
  }
  renderFlatGrid("hair_style", presets.character.hair.subcategories.hair_style.options, "single");
  document.querySelectorAll("#grid-hair_style .card").forEach(el => {
    const id = el.id.replace("card-hair_style-","");
    el.onclick = () => selectHairPart("hair_style", id);
    el.onkeydown = e => { if(e.key==="Enter"||e.key===" ") selectHairPart("hair_style", id); };
  });
}

function buildSwatch(opt) {
  const sw = document.createElement("div");
  sw.className="swatch"; sw.id=`sw-${opt.id}`;
  sw.setAttribute("role","button"); sw.setAttribute("tabindex","0");
  sw.setAttribute("aria-label",`Цвет волос: ${opt.label}`);
  const dot = document.createElement("div"); dot.className="swatch-dot";
  dot.style.background = opt.color || "#888";
  const name = document.createElement("span"); name.className="swatch-name"; name.textContent=opt.label;
  if (opt.custom) {
    const del = document.createElement("button"); del.className="swatch-delete"; del.textContent="✕";
    del.onclick = e => { e.stopPropagation(); deleteCustomOption("hair.hair_color", opt.id, opt.image); };
    dot.appendChild(del);
  }
  const click = () => selectHairPart("hair_color", opt.id);
  sw.onclick = click; sw.onkeydown = e => { if(e.key==="Enter"||e.key===" ") click(); };
  sw.appendChild(dot); sw.appendChild(name);
  return sw;
}

function selectHairPart(subKey, optId) {
  const prev = state.hair[subKey];
  if (prev) {
    const el = subKey==="hair_color" ? document.getElementById(`sw-${prev}`)
                                     : document.getElementById(`card-hair_style-${prev}`);
    if (el) { el.classList.remove("selected"); el.setAttribute("aria-pressed","false"); }
  }
  state.hair[subKey] = (prev===optId) ? null : optId;
  if (state.hair[subKey]) {
    const el = subKey==="hair_color" ? document.getElementById(`sw-${optId}`)
                                     : document.getElementById(`card-hair_style-${optId}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  refreshDots(); updatePrompt();
}

/* ── Тело ───────────────────────────────────── */
function renderBodySection() {
  const container = document.getElementById("acc-body");
  if (!container) return;
  container.innerHTML = "";

  for (const [subcatId, subcat] of Object.entries(presets.character.body.subcategories)) {
    const isBust = !!subcat.female_only;

    const wrap = document.createElement("div");
    wrap.className = "subcat bust-block";
    if (isBust) wrap.id = "bust-subcat";

    const hdr = document.createElement("div"); hdr.className="subcat-header";
    const lbl = document.createElement("span"); lbl.className="subcat-label"; lbl.textContent=subcat.label;
    const btn = document.createElement("button"); btn.className="add-custom-btn add-custom-sm";
    btn.textContent="＋ Добавить"; btn.onclick=()=>openModal(`body.${subcatId}`);
    hdr.appendChild(lbl); hdr.appendChild(btn); wrap.appendChild(hdr);

    const grid = document.createElement("div"); grid.className="cards-grid compact"; grid.id=`grid-body-${subcatId}`;
    for (const opt of subcat.options) {
      const card = buildCard(opt, `body-${subcatId}`, "single");
      card.onclick = () => selectBodyPart(subcatId, opt.id);
      card.onkeydown = e => { if(e.key==="Enter"||e.key===" ") selectBodyPart(subcatId, opt.id); };
      grid.appendChild(card);
    }
    wrap.appendChild(grid); container.appendChild(wrap);
  }
  updateBustVisibility();
}

function selectBodyPart(subcatId, optId) {
  const prev = state.body[subcatId];
  if (prev) {
    const p = document.getElementById(`card-body-${subcatId}-${prev}`);
    if (p) { p.classList.remove("selected"); p.setAttribute("aria-pressed","false"); }
  }
  state.body[subcatId] = (prev===optId) ? null : optId;
  if (state.body[subcatId]) {
    const el = document.getElementById(`card-body-${subcatId}-${optId}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  refreshDots(); updatePrompt();
}

/* Грудь — показывать только если выбран женский пол */
function updateBustVisibility() {
  const bustEl = document.getElementById("bust-subcat");
  if (!bustEl) return;
  const isFemale = state.gender === "female";
  bustEl.classList.toggle("hidden-bust", !isFemale);
  // Сбросить выбор если пол сменился на не-женский
  if (!isFemale && state.body["bust"]) {
    const prev = document.getElementById(`card-body-bust-${state.body["bust"]}`);
    if (prev) { prev.classList.remove("selected"); prev.setAttribute("aria-pressed","false"); }
    state.body["bust"] = null;
    updatePrompt();
  }
}

/* ── Одежда ─────────────────────────────────── */
function renderClothesSection() {
  const container = document.getElementById("acc-clothes");
  if (!container) return;
  container.innerHTML = "";

  for (const [subcatId, subcat] of Object.entries(presets.character.clothes.subcategories)) {
    const wrap = document.createElement("div"); wrap.className="subcat";
    const hdr  = document.createElement("div"); hdr.className="subcat-header";
    const left = document.createElement("div"); left.style.cssText="display:flex;align-items:center;gap:8px";
    const lbl  = document.createElement("span"); lbl.className="subcat-label"; lbl.textContent=subcat.label;
    const badge= document.createElement("span"); badge.className="multi-badge"; badge.textContent="Мульти";
    left.appendChild(lbl); left.appendChild(badge);
    const btn = document.createElement("button"); btn.className="add-custom-btn add-custom-sm";
    btn.textContent="＋ Добавить"; btn.onclick=()=>openModal(`clothes.${subcatId}`);
    hdr.appendChild(left); hdr.appendChild(btn); wrap.appendChild(hdr);

    const grid = document.createElement("div"); grid.className="cards-grid"; grid.id=`grid-clothes-${subcatId}`;
    for (const opt of subcat.options) {
      const card = buildCard(opt, `clothes-${subcatId}`, "single");
      card.onclick = () => selectClothes(subcatId, opt.id);
      card.onkeydown = e => { if(e.key==="Enter"||e.key===" ") selectClothes(subcatId, opt.id); };
      grid.appendChild(card);
    }
    wrap.appendChild(grid); container.appendChild(wrap);
  }
}

function selectClothes(subcatId, optId) {
  if (!state.clothes[subcatId]) state.clothes[subcatId] = new Set();
  const set = state.clothes[subcatId];
  const el  = document.getElementById(`card-clothes-${subcatId}-${optId}`);
  if (set.has(optId)) {
    set.delete(optId);
    if (el) { el.classList.remove("selected"); el.setAttribute("aria-pressed","false"); }
  } else {
    set.add(optId);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  refreshDots(); updatePrompt();
}

/* ── Аккордеон ──────────────────────────────── */
function toggleAccordion(id) {
  const body = document.getElementById(`acc-${id}`);
  const chev = document.getElementById(`chev-${id}`);
  if (!body) return;
  const open = body.classList.toggle("open");
  if (chev) chev.classList.toggle("open", open);
}

/* ── Resolve category path ──────────────────── */
function _resolvePathForCat(catId) {
  if (catId.startsWith("body-"))    return `body.${catId.slice(5)}`;
  if (catId.startsWith("clothes-")) return `clothes.${catId.slice(8)}`;
  if (catId === "hair_color")       return "hair.hair_color";
  if (catId === "hair_style")       return "hair.hair_style";
  return catId;
}

/* ══════════════════════════════════════════════
   ПРОМПТ
══════════════════════════════════════════════ */
function buildPromptLocal() {
  if (!presets) return "";
  const parts = [];
  const find  = (opts, id) => opts?.find(o => o.id === id)?.prompt ?? null;

  if (state.style) { const s = presets.styles[state.style]; if (s) parts.push(s.prompt); }
  if (state.gender)  { const p = find(presets.character.gender.options, state.gender);  if (p) parts.push(p); }
  if (state.age)     { const p = find(presets.character.age.options,    state.age);     if (p) parts.push(p); }
  if (state.hair.hair_color) { const p = find(presets.character.hair.subcategories.hair_color.options, state.hair.hair_color); if (p) parts.push(p); }
  if (state.hair.hair_style) { const p = find(presets.character.hair.subcategories.hair_style.options, state.hair.hair_style); if (p) parts.push(p); }
  for (const fid of state.face) { const p = find(presets.character.face.options, fid); if (p) parts.push(p); }
  for (const [sid, subcat] of Object.entries(presets.character.body.subcategories)) {
    // Skip bust if not female
    if (subcat.female_only && state.gender !== "female") continue;
    if (state.body[sid]) { const p = find(subcat.options, state.body[sid]); if (p) parts.push(p); }
  }
  for (const [sid, subcat] of Object.entries(presets.character.clothes.subcategories)) {
    const set = state.clothes[sid];
    if (set?.size) for (const cid of set) { const p = find(subcat.options, cid); if (p) parts.push(p); }
  }
  if (state.action)   { const p = find(presets.actions,             state.action);   if (p) parts.push(p); }
  if (state.location) { const p = find(presets.locations,           state.location); if (p) parts.push(p); }
  if (state.camera)   { const p = find(presets.cameras || [],       state.camera);   if (p) parts.push(p); }
  const extra = document.getElementById("custom-text")?.value?.trim();
  if (extra) parts.push(extra);
  return parts.filter(Boolean).join(", ");
}

function updatePrompt() {
  const prompt = buildPromptLocal();
  const out = document.getElementById("prompt-output");
  if (out) out.value = prompt;
  const words = prompt ? prompt.split(/[\s,]+/).filter(Boolean).length : 0;
  const wc = document.getElementById("word-count");
  if (wc) wc.textContent = `~${words} слов`;
}

/* ══════════════════════════════════════════════
   ПРОГРЕСС-ТОЧКИ
══════════════════════════════════════════════ */
function refreshDots() {
  setDot("dot-style",    !!state.style);
  setDot("dot-gender",   !!state.gender);
  setDot("dot-hair",     !!(state.hair.hair_color || state.hair.hair_style));
  setDot("dot-face",     state.face.size > 0);
  setDot("dot-body",     Object.values(state.body).some(Boolean));
  setDot("dot-clothes",  Object.values(state.clothes).some(s => s instanceof Set && s.size > 0));
  setDot("dot-action",   !!state.action);
  setDot("dot-location", !!state.location);
  setDot("dot-camera",   !!state.camera);
}
function setDot(id, active) {
  document.getElementById(id)?.classList.toggle("active", active);
}

/* ══════════════════════════════════════════════
   МОДАЛКА
══════════════════════════════════════════════ */
function openModal(preselectedPath) {
  if (!categoryPaths) return;
  const select = document.getElementById("modal-category");
  select.innerHTML = Object.entries(categoryPaths)
    .map(([p, l]) => `<option value="${p}" ${p===preselectedPath?"selected":""}>${l}</option>`)
    .join("");
  ["modal-label","modal-desc","modal-prompt"].forEach(id => { const el=document.getElementById(id); if(el) el.value=""; });
  const ic = document.getElementById("modal-icon"); if(ic) ic.value="✦";
  modal.uploadedFilename = null;
  resetUploadArea();
  onCategoryChange();
  document.getElementById("modal-overlay")?.classList.remove("hidden");
  document.body.style.overflow = "hidden";
  setTimeout(() => document.getElementById("modal-label")?.focus(), 50);
}

function closeModal() {
  document.getElementById("modal-overlay")?.classList.add("hidden");
  document.body.style.overflow = "";
  modal.uploadedFilename = null;
  resetUploadArea();
}
function handleOverlayClick(e) {
  if (e.target === document.getElementById("modal-overlay")) closeModal();
}
function onCategoryChange() {
  const path = document.getElementById("modal-category")?.value || "";
  const cf = document.getElementById("field-color");
  if (cf) cf.style.display = path==="hair.hair_color" ? "flex" : "none";
}

async function submitCustomOption() {
  const path   = document.getElementById("modal-category")?.value;
  const label  = document.getElementById("modal-label")?.value?.trim();
  const desc   = document.getElementById("modal-desc")?.value?.trim();
  const prompt = document.getElementById("modal-prompt")?.value?.trim();
  const icon   = document.getElementById("modal-icon")?.value?.trim() || "✦";
  const color  = document.getElementById("modal-color")?.value;

  if (!label)  { showToast("⚠ Укажите название"); document.getElementById("modal-label")?.focus(); return; }
  if (!prompt) { showToast("⚠ Укажите текст промпта"); document.getElementById("modal-prompt")?.focus(); return; }

  const spinner = document.getElementById("modal-save-spinner");
  const btn     = document.getElementById("modal-save-btn");
  if (spinner) spinner.classList.remove("hidden");
  if (btn) btn.disabled = true;

  try {
    const res = await fetch("/api/custom-options", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ category_path:path, label, description:desc, prompt, icon,
        image: modal.uploadedFilename || null,
        color: path==="hair.hair_color" ? color : null }),
    });
    if (!res.ok) { const e = await res.json(); throw new Error(e.detail || "Ошибка сохранения"); }
    await refreshPresets();
    closeModal();
    showToast(`✓ «${label}» добавлено в «${categoryPaths[path] || path}»`);
  } catch (err) {
    console.error("[PromptForge] Ошибка сохранения:", err);
    showToast(`⚠ ${err.message}`);
  } finally {
    if (spinner) spinner.classList.add("hidden");
    if (btn) btn.disabled = false;
  }
}

async function deleteCustomOption(categoryPath, optionId, imageFilename) {
  if (!confirm("Удалить эту опцию?")) return;
  try {
    const res = await fetch(`/api/custom-options/${categoryPath}/${optionId}`, { method:"DELETE" });
    if (!res.ok) { const e = await res.json(); throw new Error(e.detail || "Ошибка удаления"); }
    if (imageFilename) fetch(`/api/images/${imageFilename}`, { method:"DELETE" }).catch(()=>{});
    await refreshPresets();
    showToast("↺ Пользовательская опция удалена");
  } catch (err) {
    console.error("[PromptForge] Ошибка удаления:", err);
    showToast(`⚠ ${err.message}`);
  }
}

async function refreshPresets() {
  const res = await fetch("/api/presets");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const data = await res.json();
  presets = data; categoryPaths = data.category_paths || {};
  initStateKeys(); renderAll(); restoreSelections();
}

function restoreSelections() {
  if (state.style) {
    const el = document.getElementById(`sc-${state.style}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  for (const cat of ["gender","age","action","location","camera"]) {
    const val = state[cat]; if (!val) continue;
    const el = document.getElementById(`card-${cat}-${val}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  if (state.hair.hair_color) {
    const el = document.getElementById(`sw-${state.hair.hair_color}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  if (state.hair.hair_style) {
    const el = document.getElementById(`card-hair_style-${state.hair.hair_style}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  for (const fid of state.face) {
    const el = document.getElementById(`card-face-${fid}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  for (const [sid, val] of Object.entries(state.body)) {
    if (!val) continue;
    const el = document.getElementById(`card-body-${sid}-${val}`);
    if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
  }
  for (const [sid, set] of Object.entries(state.clothes)) {
    if (!(set instanceof Set)) continue;
    for (const cid of set) {
      const el = document.getElementById(`card-clothes-${sid}-${cid}`);
      if (el) { el.classList.add("selected"); el.setAttribute("aria-pressed","true"); }
    }
  }
  updateBustVisibility();
  refreshDots();
}

/* ══════════════════════════════════════════════
   ЗАГРУЗКА ИЗОБРАЖЕНИЙ
══════════════════════════════════════════════ */
function handleDragOver(e) { e.preventDefault(); document.getElementById("upload-area")?.classList.add("drag-over"); }
function handleDragLeave()  { document.getElementById("upload-area")?.classList.remove("drag-over"); }
function handleDrop(e) { e.preventDefault(); handleDragLeave(); const f=e.dataTransfer?.files?.[0]; if(f) uploadFile(f); }
function handleFileSelect(e) { const f=e.target.files?.[0]; if(f) uploadFile(f); }

async function uploadFile(file) {
  const idle=document.getElementById("upload-idle"), prev=document.getElementById("upload-preview"),
        upl=document.getElementById("upload-uploading");
  idle?.classList.add("hidden"); upl?.classList.remove("hidden"); prev?.classList.add("hidden");
  try {
    const fd = new FormData(); fd.append("file", file);
    const res = await fetch("/api/upload-image", { method:"POST", body:fd });
    if (!res.ok) { const e=await res.json(); throw new Error(e.detail||"Ошибка загрузки"); }
    const data = await res.json();
    modal.uploadedFilename = data.filename;
    upl?.classList.add("hidden"); prev?.classList.remove("hidden");
    const img = document.getElementById("upload-preview-img"); if(img) img.src=data.url;
  } catch (err) {
    upl?.classList.add("hidden"); idle?.classList.remove("hidden");
    showToast(`⚠ Загрузка не удалась: ${err.message}`);
    modal.uploadedFilename = null;
  }
}

function removeUploadedImage(e) {
  e?.stopPropagation();
  if (modal.uploadedFilename) {
    fetch(`/api/images/${modal.uploadedFilename}`, { method:"DELETE" }).catch(()=>{});
    modal.uploadedFilename = null;
  }
  resetUploadArea();
}
function resetUploadArea() {
  document.getElementById("upload-idle")?.classList.remove("hidden");
  document.getElementById("upload-preview")?.classList.add("hidden");
  document.getElementById("upload-uploading")?.classList.add("hidden");
  const inp = document.getElementById("modal-file-input"); if(inp) inp.value="";
  const img = document.getElementById("upload-preview-img"); if(img) img.src="";
}

/* ══════════════════════════════════════════════
   КОПИРОВАТЬ
══════════════════════════════════════════════ */
async function copyPrompt() {
  const prompt = document.getElementById("prompt-output")?.value ?? "";
  if (!prompt) { showToast("⚠ Выберите хотя бы один параметр!"); return; }
  try { await navigator.clipboard.writeText(prompt); }
  catch { const ta=document.getElementById("prompt-output"); if(ta){ta.select();document.execCommand("copy");} }
  const icon=document.getElementById("copy-icon"), lbl=document.getElementById("copy-label");
  if(icon) icon.textContent="✓"; if(lbl) lbl.textContent="Скопировано!";
  setTimeout(()=>{ if(icon) icon.textContent="⎘"; if(lbl) lbl.textContent="Копировать"; }, 2200);
  showToast("✓ Промпт скопирован в буфер обмена!");
}

/* ══════════════════════════════════════════════
   СБРОС
══════════════════════════════════════════════ */
function resetAll() {
  state.style=null; state.gender=null; state.age=null;
  state.hair.hair_color=null; state.hair.hair_style=null;
  state.face.clear(); state.action=null; state.location=null; state.camera=null;
  if (presets) {
    for (const id of Object.keys(presets.character.body.subcategories))    state.body[id]=null;
    for (const id of Object.keys(presets.character.clothes.subcategories)) state.clothes[id]?.clear();
  }
  document.querySelectorAll(".card.selected,.style-card.selected,.swatch.selected").forEach(el => {
    el.classList.remove("selected"); el.setAttribute("aria-pressed","false");
  });
  const ct=document.getElementById("custom-text"); if(ct) ct.value="";
  updateBustVisibility();
  refreshDots(); updatePrompt();
  showToast("↺ Все параметры сброшены");
}

/* ══════════════════════════════════════════════
   ТОСТ
══════════════════════════════════════════════ */
function showToast(message) {
  const wrap=document.getElementById("toast-wrap"); if(!wrap) return;
  const t=document.createElement("div"); t.className="toast"; t.textContent=message;
  wrap.appendChild(t);
  setTimeout(()=>{ t.classList.add("leaving"); t.addEventListener("animationend",()=>t.remove(),{once:true}); }, 2800);
}

/* ══════════════════════════════════════════════
   ИНИЦИАЛИЗАЦИЯ
══════════════════════════════════════════════ */
document.addEventListener("DOMContentLoaded", () => {
  initStarfield();
  initFooter();
  loadPresets();

  // Цветовой превью в модалке
  document.getElementById("modal-color")?.addEventListener("input", e => {
    const t=document.getElementById("color-preview-text"); if(t) t.textContent=e.target.value;
  });
  // Ctrl+Enter — копировать промпт
  document.addEventListener("keydown", e => {
    if ((e.ctrlKey||e.metaKey) && e.key==="Enter") { e.preventDefault(); copyPrompt(); }
    if (e.key==="Escape") closeModal();
  });
});
