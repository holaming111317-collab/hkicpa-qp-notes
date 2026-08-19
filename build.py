#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HKICPA Notes 靜態網站生成器
用法: python3 build.py
掃描上層目錄 (/mnt/agents/output/) 嘅 .md 筆記，生成零外部依賴嘅靜態網站。
可重複執行（idempotent）：每次會清空 pages/ 同 notes/ 再重新生成。
"""
import datetime
import html
import json
import re
import shutil
import sys
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent
SRC_DIR = SITE_DIR.parent
EXCLUDE_FILES = {"SPEC.md", "plan.md"}

CATEGORY_ORDER = [
    "計劃與追蹤",
    "M7 Financial Management",
    "M9 Principles of Taxation",
    "工具表",
    "其他",
]


def categorize(filename: str) -> str:
    """按檔名自動判斷分類（規則見 SPEC.md）。"""
    if "詞彙" in filename:
        return "工具表"
    if re.search(r"Plan|Roadmap|Tracker", filename):
        return "計劃與追蹤"
    if "M7" in filename:
        return "M7 Financial Management"
    if "M9" in filename:
        return "M9 Principles of Taxation"
    return "其他"


def slugify(stem: str) -> str:
    """檔名轉 kebab-case slug（保留中文字元）。"""
    s = stem.lower()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"[^0-9a-z\-一-鿿]", "", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "note"


def collect_notes():
    """掃描來源目錄，回傳 note dict 列表。"""
    notes = []
    for path in sorted(SRC_DIR.rglob("*.md")):
        if not path.is_file():
            continue
        # 排除網站目錄本身（避免 re-run 時掃到 notes/ 副本）
        if SITE_DIR in path.parents or path.parent == SITE_DIR:
            continue
        if any(part.startswith(".") for part in path.relative_to(SRC_DIR).parts):
            continue
        if path.name in EXCLUDE_FILES:
            continue
        rel = path.relative_to(SRC_DIR)  # e.g. Week1/M7_....md
        stem = path.stem
        notes.append(
            {
                "src": path,
                "rel": rel.as_posix(),
                "stem": stem,
                "slug": slugify(stem),
                "category": categorize(path.name),
                "mtime": datetime.datetime.fromtimestamp(path.stat().st_mtime),
            }
        )
    # 確保 slug 唯一
    seen = {}
    for n in notes:
        s = n["slug"]
        if s in seen:
            seen[s] += 1
            n["slug"] = f"{s}-{seen[s]}"
        else:
            seen[s] = 1
    return notes


def extract_title(md_text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", md_text, flags=re.M)
    if m:
        return re.sub(r"\s*#+\s*$", "", m.group(1)).strip()
    return fallback


def extract_headings(md_text: str):
    heads = []
    for m in re.finditer(r"^(#{1,4})\s+(.+)$", md_text, flags=re.M):
        text = re.sub(r"\s*#+\s*$", "", m.group(2)).strip()
        heads.append(text)
    return heads


def plain_text(md_text: str) -> str:
    """粗略剝走 markdown 符號，用嚟做搜尋索引。"""
    t = re.sub(r"```.*?```", " ", md_text, flags=re.S)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[#>*`|\-]{1,}", " ", t)
    t = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


# 筆記入面有大量「[中文白話解釋]: ……」呢類行首標籤，
# 會被標準 markdown 誤當 reference link definition 而吞咗啲內容。
# 若「目標」唔係真正 URL/路徑，就將 [ escape 做字面文字。
_REF_DEF = re.compile(
    r"^(\s*(?:[-*+]\s+|\d+\.\s+|>\s+)?)\[([^\]]+)\]:(\s*\S.*)$", flags=re.M
)
_REAL_TARGET = re.compile(
    r"\s*(https?://|mailto:|ftp://|/|#|\.\.?/|\S+\.(?:md|html?|png|jpe?g|gif|pdf)\b)",
    flags=re.I,
)


def _protect_fake_ref_defs(md_text: str) -> str:
    def repl(m: re.Match) -> str:
        if _REAL_TARGET.match(m.group(3)):
            return m.group(0)
        return f"{m.group(1)}\\[{m.group(2)}]:{m.group(3)}"

    return _REF_DEF.sub(repl, md_text)


def render_markdown(md_text: str) -> str:
    """build-time 渲染 markdown → HTML，表格包上可橫向捲動 container。"""
    try:
        import markdown
    except ImportError:
        sys.exit(
            "缺少 markdown 模組，請先執行: pip install markdown"
        )
    md_text = _protect_fake_ref_defs(md_text)
    body = markdown.markdown(
        md_text, extensions=["tables", "fenced_code", "sane_lists"]
    )
    body = re.sub(
        r"(<table>.*?</table>)",
        r'<div class="table-wrap">\1</div>',
        body,
        flags=re.S,
    )
    return body


def esc(s: str) -> str:
    return html.escape(s, quote=True)


CSS = r"""
:root {
  --bg: #faf7f1;
  --surface: #fffdf8;
  --ink: #3c372f;
  --ink-soft: #6f675c;
  --accent: #a4713f;
  --accent-soft: #f3e9dc;
  --line: #e9e1d4;
  --badge-m7: #7a8ba0;
  --badge-m9: #8a9a7b;
  --badge-plan: #b08d6a;
  --badge-tool: #9a8ba8;
  --radius: 10px;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "PingFang TC",
    "Microsoft JhengHei", "Noto Sans TC", "Segoe UI", sans-serif;
  line-height: 1.75;
  font-size: 16px;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

/* ---------- 版面骨架 ---------- */
.layout { display: flex; min-height: 100vh; }
.sidebar {
  width: 264px;
  flex: 0 0 264px;
  background: var(--surface);
  border-right: 1px solid var(--line);
  padding: 28px 20px 48px;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
}
.sidebar .brand {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--ink);
  display: block;
  margin-bottom: 4px;
}
.sidebar .brand:hover { text-decoration: none; color: var(--accent); }
.sidebar .tagline { font-size: .8rem; color: var(--ink-soft); margin: 0 0 20px; }
.nav-cat { margin-bottom: 18px; }
.nav-cat-title {
  font-size: .78rem;
  letter-spacing: .06em;
  color: var(--ink-soft);
  text-transform: uppercase;
  margin: 0 0 6px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 4px;
}
.nav-cat ul { list-style: none; margin: 0; padding: 0; }
.nav-cat li { margin: 2px 0; }
.nav-cat a {
  display: block;
  padding: 5px 10px;
  border-radius: 6px;
  color: var(--ink);
  font-size: .9rem;
  line-height: 1.45;
}
.nav-cat a:hover { background: var(--accent-soft); text-decoration: none; }
.nav-cat a.active { background: var(--accent-soft); color: var(--accent); font-weight: 600; }

.main { flex: 1; min-width: 0; padding: 40px 24px 80px; }
.content { max-width: 760px; margin: 0 auto; }

/* ---------- 手機頂欄 / 漢堡 ---------- */
.topbar {
  display: none;
  position: sticky;
  top: 0;
  z-index: 30;
  background: var(--surface);
  border-bottom: 1px solid var(--line);
  padding: 10px 14px;
  align-items: center;
  gap: 12px;
}
.topbar .brand { font-weight: 700; font-size: 1rem; color: var(--ink); }
.hamburger {
  background: none;
  border: 1px solid var(--line);
  border-radius: 8px;
  width: 40px;
  height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--ink);
}
.drawer-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(60, 55, 47, .35);
  z-index: 40;
}
@media (max-width: 860px) {
  .layout { display: block; }
  .topbar { display: flex; }
  .sidebar {
    position: fixed;
    z-index: 50;
    top: 0;
    left: 0;
    height: 100vh;
    transform: translateX(-105%);
    transition: transform .22s ease;
    box-shadow: 2px 0 18px rgba(60, 55, 47, .12);
  }
  body.drawer-open .sidebar { transform: translateX(0); }
  body.drawer-open .drawer-overlay { display: block; }
  .main { padding: 20px 16px 64px; }
}

/* ---------- 首頁 ---------- */
.hero { margin-bottom: 32px; }
.hero h1 { font-size: 1.7rem; margin: 0 0 8px; }
.hero p { color: var(--ink-soft); margin: 0; }
.search-box { margin: 22px 0 8px; position: relative; }
.search-box input {
  width: 100%;
  padding: 12px 16px 12px 42px;
  font-size: 1rem;
  font-family: inherit;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--surface);
  color: var(--ink);
}
.search-box input:focus { outline: 2px solid var(--accent-soft); border-color: var(--accent); }
.search-box .search-icon {
  position: absolute;
  left: 13px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--ink-soft);
  pointer-events: none;
}
.search-results { margin: 0 0 24px; }
.search-results .result {
  display: block;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 12px 16px;
  margin-bottom: 10px;
  color: var(--ink);
}
.search-results .result:hover { border-color: var(--accent); text-decoration: none; }
.search-results .result h3 { margin: 0 0 4px; font-size: 1rem; }
.search-results .result .excerpt {
  margin: 6px 0 0;
  font-size: .85rem;
  color: var(--ink-soft);
}
.search-empty { color: var(--ink-soft); font-size: .9rem; padding: 8px 2px; }

.cat-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 12px;
  margin: 20px 0 36px;
}
.cat-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 14px 16px;
  color: var(--ink);
}
.cat-card:hover { border-color: var(--accent); text-decoration: none; }
.cat-card .cat-name { font-weight: 600; font-size: .95rem; }
.cat-card .cat-count { font-size: .8rem; color: var(--ink-soft); }

.note-section { margin-bottom: 36px; }
.note-section h2 {
  font-size: 1.15rem;
  border-bottom: 1px solid var(--line);
  padding-bottom: 8px;
  margin: 0 0 12px;
}
.note-list { list-style: none; margin: 0; padding: 0; }
.note-list li { margin-bottom: 8px; }
.note-list a.note-link {
  display: flex;
  align-items: baseline;
  gap: 10px;
  flex-wrap: wrap;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 12px 16px;
  color: var(--ink);
}
.note-list a.note-link:hover { border-color: var(--accent); text-decoration: none; }
.note-list .note-title { font-weight: 600; font-size: .95rem; }
.note-list .note-date { font-size: .78rem; color: var(--ink-soft); margin-left: auto; }
.memo-dot {
  display: none;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  flex: 0 0 8px;
  align-self: center;
}
.memo-dot.on { display: inline-block; }

.badge {
  display: inline-block;
  font-size: .72rem;
  padding: 2px 9px;
  border-radius: 999px;
  color: #fff;
  background: var(--ink-soft);
  white-space: nowrap;
}
.badge.m7 { background: var(--badge-m7); }
.badge.m9 { background: var(--badge-m9); }
.badge.plan { background: var(--badge-plan); }
.badge.tool { background: var(--badge-tool); }

/* ---------- 筆記頁 ---------- */
.breadcrumb {
  font-size: .85rem;
  color: var(--ink-soft);
  margin-bottom: 20px;
}
.breadcrumb a { color: var(--ink-soft); }
.breadcrumb a:hover { color: var(--accent); }
.breadcrumb .sep { margin: 0 6px; }
.page-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}
.back-home { font-size: .85rem; color: var(--ink-soft); }
.edit-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: .8rem;
  color: var(--ink-soft);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 5px 14px;
  background: var(--surface);
}
.edit-btn:hover { color: var(--accent); border-color: var(--accent); text-decoration: none; }
.pair-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 24px;
  padding: 10px 18px;
  border-radius: var(--radius);
  border: 1px solid var(--accent);
  color: var(--accent);
  background: var(--accent-soft);
  font-weight: 600;
  font-size: .9rem;
}
.pair-btn:hover { text-decoration: none; background: var(--accent); color: #fff; }

article.note-body {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 32px 36px;
}
article.note-body h1 { font-size: 1.55rem; line-height: 1.4; margin: 0 0 18px; }
article.note-body h2 {
  font-size: 1.25rem;
  margin: 2em 0 .6em;
  padding-bottom: .3em;
  border-bottom: 1px solid var(--line);
}
article.note-body h3 { font-size: 1.08rem; margin: 1.8em 0 .5em; }
article.note-body h4 { font-size: 1rem; margin: 1.6em 0 .4em; }
article.note-body p { margin: .9em 0; }
article.note-body ul, article.note-body ol { padding-left: 1.5em; margin: .9em 0; }
article.note-body li { margin: .3em 0; }
article.note-body blockquote {
  margin: 1.2em 0;
  padding: 10px 18px;
  border-left: 3px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 0 8px 8px 0;
  color: var(--ink-soft);
}
article.note-body code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: .88em;
  background: var(--accent-soft);
  padding: 2px 6px;
  border-radius: 5px;
}
article.note-body pre {
  background: #f4efe6;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px 16px;
  overflow-x: auto;
}
article.note-body pre code { background: none; padding: 0; }
article.note-body hr { border: none; border-top: 1px solid var(--line); margin: 2em 0; }
article.note-body img { max-width: 100%; }
.table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 1.2em 0; }
.table-wrap table {
  border-collapse: collapse;
  min-width: 100%;
  font-size: .9rem;
  background: var(--surface);
}
.table-wrap th, .table-wrap td {
  border: 1px solid var(--line);
  padding: 8px 12px;
  text-align: left;
  vertical-align: top;
}
.table-wrap th { background: var(--accent-soft); font-weight: 600; white-space: nowrap; }

.page-meta {
  font-size: .82rem;
  color: var(--ink-soft);
  margin: 0 0 18px;
  display: flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
}

/* ---------- 速記面板 ---------- */
.memo {
  margin-top: 36px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--surface);
}
.memo summary {
  cursor: pointer;
  padding: 14px 18px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  list-style: none;
  color: var(--ink);
}
.memo summary::-webkit-details-marker { display: none; }
.memo summary .chev { transition: transform .2s; color: var(--ink-soft); }
.memo[open] summary .chev { transform: rotate(90deg); }
.memo .memo-inner { padding: 0 18px 18px; }
.memo textarea {
  width: 100%;
  min-height: 140px;
  resize: vertical;
  font-family: inherit;
  font-size: .95rem;
  line-height: 1.6;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--bg);
  color: var(--ink);
}
.memo textarea:focus { outline: 2px solid var(--accent-soft); border-color: var(--accent); }
.memo .memo-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 10px;
}
.memo .memo-status { font-size: .78rem; color: var(--ink-soft); margin-right: auto; }
.memo .btn {
  font-family: inherit;
  font-size: .82rem;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  border-radius: 8px;
  padding: 6px 14px;
  cursor: pointer;
}
.memo .btn:hover { border-color: var(--accent); color: var(--accent); }
.memo .btn.danger:hover { border-color: #b05a4a; color: #b05a4a; }

/* ---------- prev / next ---------- */
.pager {
  display: flex;
  gap: 12px;
  margin-top: 36px;
}
.pager a {
  flex: 1;
  border: 1px solid var(--line);
  background: var(--surface);
  border-radius: var(--radius);
  padding: 12px 16px;
  color: var(--ink);
  font-size: .88rem;
  min-width: 0;
}
.pager a:hover { border-color: var(--accent); text-decoration: none; }
.pager .dir { display: block; font-size: .75rem; color: var(--ink-soft); margin-bottom: 2px; }
.pager .next { text-align: right; }
.pager .spacer { flex: 1; }

footer.site-footer {
  margin-top: 56px;
  padding-top: 18px;
  border-top: 1px solid var(--line);
  font-size: .8rem;
  color: var(--ink-soft);
  text-align: center;
}

@media (max-width: 480px) {
  article.note-body { padding: 22px 18px; }
  .hero h1 { font-size: 1.4rem; }
  .note-list .note-date { margin-left: 0; width: 100%; }
  .pager { flex-direction: column; }
  .pager .next { text-align: left; }
}
"""

APP_JS = r"""
(function () {
  "use strict";

  /* ---------- 漢堡抽屜 ---------- */
  var burger = document.querySelector(".hamburger");
  var overlay = document.querySelector(".drawer-overlay");
  function closeDrawer() { document.body.classList.remove("drawer-open"); }
  if (burger) {
    burger.addEventListener("click", function () {
      document.body.classList.toggle("drawer-open");
    });
  }
  if (overlay) overlay.addEventListener("click", closeDrawer);

  /* ---------- Edit on GitHub ---------- */
  var GITHUB_USER =
    typeof window.HKICPA_GITHUB_USER === "string"
      ? window.HKICPA_GITHUB_USER
      : "__GITHUB_USER__";
  document.querySelectorAll(".edit-btn[data-note-path]").forEach(function (btn) {
    var p = btn.getAttribute("data-note-path");
    btn.href =
      "https://github.com/" +
      GITHUB_USER +
      "/hkicpa-qp-notes/edit/main/notes/" +
      p.split("/").map(encodeURIComponent).join("/");
    btn.target = "_blank";
    btn.rel = "noopener";
  });

  /* ---------- 速記面板 ---------- */
  var MEMO_PREFIX = "hkicpa-memo:";
  function memoKey(slug) { return MEMO_PREFIX + slug; }
  function loadMemo(slug) {
    try { return localStorage.getItem(memoKey(slug)) || ""; }
    catch (e) { return ""; }
  }
  function saveMemo(slug, text) {
    try { localStorage.setItem(memoKey(slug), text); return true; }
    catch (e) { return false; }
  }
  function fmtTime(d) {
    var h = String(d.getHours()).padStart(2, "0");
    var m = String(d.getMinutes()).padStart(2, "0");
    return h + ":" + m;
  }

  var memoBox = document.querySelector(".memo[data-slug]");
  if (memoBox) {
    var slug = memoBox.getAttribute("data-slug");
    var ta = memoBox.querySelector("textarea");
    var status = memoBox.querySelector(".memo-status");
    ta.value = loadMemo(slug);
    var timer = null;
    ta.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(function () {
        saveMemo(slug, ta.value);
        status.textContent = "已自動儲存 · " + fmtTime(new Date());
      }, 250);
    });
    memoBox.querySelector(".btn-copy").addEventListener("click", function () {
      var done = function () { status.textContent = "已複製到剪貼簿"; };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(ta.value).then(done, function () {
          ta.select(); document.execCommand("copy"); done();
        });
      } else {
        ta.select(); document.execCommand("copy"); done();
      }
    });
    memoBox.querySelector(".btn-download").addEventListener("click", function () {
      var blob = new Blob([ta.value], { type: "text/markdown;charset=utf-8" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = slug + "-速記.md";
      document.body.appendChild(a);
      a.click();
      setTimeout(function () {
        URL.revokeObjectURL(a.href);
        a.remove();
      }, 100);
      status.textContent = "已下載 .md";
    });
    memoBox.querySelector(".btn-clear").addEventListener("click", function () {
      if (window.confirm("確定要清除呢頁嘅速記？呢個動作唔可以復原。")) {
        ta.value = "";
        saveMemo(slug, "");
        status.textContent = "已清除";
      }
    });
  }

  /* ---------- 首頁速記小圓點 ---------- */
  document.querySelectorAll("[data-memo-dot]").forEach(function (dot) {
    var s = dot.getAttribute("data-memo-dot");
    if (loadMemo(s).trim() !== "") dot.classList.add("on");
  });

  /* ---------- 即打即搜 ---------- */
  var input = document.querySelector(".search-box input");
  if (input) {
    var resultsBox = document.querySelector(".search-results");
    var sections = document.querySelectorAll("[data-searchable-section]");
    var index = [];
    function renderResults(q) {
      var query = q.trim().toLowerCase();
      if (!query) {
        resultsBox.innerHTML = "";
        sections.forEach(function (s) { s.style.display = ""; });
        return;
      }
      var hits = index.filter(function (item) {
        return (
          item.title.toLowerCase().indexOf(query) !== -1 ||
          item.category.toLowerCase().indexOf(query) !== -1 ||
          (item.headings || []).join(" ").toLowerCase().indexOf(query) !== -1 ||
          (item.text || "").toLowerCase().indexOf(query) !== -1
        );
      });
      sections.forEach(function (s) { s.style.display = "none"; });
      if (!hits.length) {
        resultsBox.innerHTML =
          '<p class="search-empty">搵唔到「' +
          q.replace(/[<>&]/g, "") +
          "」相關嘅筆記。</p>";
        return;
      }
      resultsBox.innerHTML = hits
        .map(function (h) {
          return (
            '<a class="result" href="' + h.url + '">' +
            "<h3>" + h.title + "</h3>" +
            '<span class="badge ' + h.badgeClass + '">' + h.category + "</span>" +
            '<p class="excerpt">' + h.excerpt + "</p>" +
            "</a>"
          );
        })
        .join("");
    }
    function boot(data) {
      index = data;
      input.addEventListener("input", function () {
        renderResults(input.value);
      });
    }
    if (window.HKICPA_SEARCH_INDEX) {
      boot(window.HKICPA_SEARCH_INDEX);
    } else {
      fetch("assets/search.json")
        .then(function (r) { return r.json(); })
        .then(boot)
        .catch(function () {
          resultsBox.innerHTML =
            '<p class="search-empty">搜尋索引載入失敗。</p>';
        });
    }
  }
})();
"""

CONFIG_JS = 'window.HKICPA_GITHUB_USER = "__GITHUB_USER__";\n'


BADGE_CLASS = {
    "M7 Financial Management": "m7",
    "M9 Principles of Taxation": "m9",
    "計劃與追蹤": "plan",
    "工具表": "tool",
    "其他": "tool",
}

SVG_MENU = (
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round">'
    '<line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/>'
    '<line x1="4" y1="17" x2="20" y2="17"/></svg>'
)
SVG_SEARCH = (
    '<svg class="search-icon" width="17" height="17" viewBox="0 0 24 24" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
    '<circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>'
)
SVG_EDIT = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round"><path d="M17 3a2.8 2.8 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5z"/></svg>'
)
SVG_MEMO = (
    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round"><path d="M12 20h9"/>'
    '<path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>'
)
SVG_CHEV = (
    '<svg class="chev" width="13" height="13" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>'
)
SVG_SWAP = (
    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round"><polyline points="17 1 21 5 17 9"/>'
    '<path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/>'
    '<path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>'
)


def group_by_category(notes):
    groups = {}
    for n in notes:
        groups.setdefault(n["category"], []).append(n)
    for g in groups.values():
        g.sort(key=lambda n: n["rel"])
    ordered = []
    for cat in CATEGORY_ORDER:
        if cat in groups:
            ordered.append((cat, groups[cat]))
    for cat in sorted(groups):
        if cat not in CATEGORY_ORDER:
            ordered.append((cat, groups[cat]))
    return ordered


def sidebar_html(groups, prefix, current_slug=None):
    parts = [
        '<aside class="sidebar">',
        f'<a class="brand" href="{prefix}index.html">HKICPA QP 筆記</a>',
        '<p class="tagline">M7 Financial Management · M9 Principles of Taxation</p>',
        "<nav>",
    ]
    for cat, items in groups:
        parts.append(f'<div class="nav-cat"><p class="nav-cat-title">{esc(cat)}</p><ul>')
        for n in items:
            active = ' class="active"' if n["slug"] == current_slug else ""
            parts.append(
                f'<li><a{active} href="{prefix}pages/{n["slug"]}.html">'
                f'{esc(n["title"])}</a></li>'
            )
        parts.append("</ul></div>")
    parts.append("</nav></aside>")
    return "\n".join(parts)


def page_shell(title, body_inner, prefix, groups, current_slug=None, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · HKICPA QP 筆記</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
{extra_head}</head>
<body>
<div class="topbar">
<button class="hamburger" aria-label="開關目錄">{SVG_MENU}</button>
<a class="brand" href="{prefix}index.html">HKICPA QP 筆記</a>
</div>
<div class="drawer-overlay"></div>
<div class="layout">
{sidebar_html(groups, prefix, current_slug)}
<main class="main"><div class="content">
{body_inner}
<footer class="site-footer">HKICPA QP 備考筆記 · 由 build.py 自動生成</footer>
</div></main>
</div>
<script src="{prefix}assets/config.js"></script>
<script src="{prefix}assets/app.js"></script>
</body>
</html>
"""


def build_index(notes, groups, search_index):
    cards = []
    for cat, items in groups:
        cards.append(
            f'<a class="cat-card" href="#cat-{BADGE_CLASS.get(cat, "tool")}">'
            f'<div class="cat-name">{esc(cat)}</div>'
            f'<div class="cat-count">{len(items)} 份筆記</div></a>'
        )
    sections = []
    for cat, items in groups:
        badge = BADGE_CLASS.get(cat, "tool")
        lis = []
        for n in items:
            lis.append(
                f'<li><a class="note-link" href="pages/{n["slug"]}.html">'
                f'<span class="memo-dot" data-memo-dot="{n["slug"]}" '
                f'title="有速記"></span>'
                f'<span class="note-title">{esc(n["title"])}</span>'
                f'<span class="badge {badge}">{esc(cat)}</span>'
                f'<span class="note-date">更新於 {n["mtime"]:%Y-%m-%d}</span>'
                f"</a></li>"
            )
        sections.append(
            f'<section class="note-section" id="cat-{badge}" data-searchable-section>'
            f"<h2>{esc(cat)}</h2>"
            f'<ul class="note-list">{"".join(lis)}</ul></section>'
        )
    inline_index = json.dumps(search_index, ensure_ascii=False)
    body = f"""
<div class="hero">
<h1>HKICPA QP 備考筆記</h1>
<p>Module 7 Financial Management · Module 9 Principles of Taxation — 溫習筆記、速查表、Quiz 與答案。</p>
</div>
<div class="search-box">
{SVG_SEARCH}
<input type="search" placeholder="即打即搜：輸入關鍵字搵筆記…" aria-label="搜尋筆記" autocomplete="off">
</div>
<div class="search-results"></div>
<div data-searchable-section>
<div class="cat-cards">{"".join(cards)}</div>
{"".join(sections)}
</div>
"""
    extra = (
        "<script>window.HKICPA_SEARCH_INDEX = "
        + inline_index.replace("</", "<\\/")
        + ";</script>"
    )
    return page_shell("首頁", body, "", groups, extra_head=extra)


def find_pair(note, by_stem):
    """Quiz ↔ Answers 配對。"""
    stem = note["stem"]
    if stem.endswith("_Quiz") or "_Quiz" in stem:
        partner = stem.replace("Quiz", "Answers")
        label = "睇答案"
    elif stem.endswith("_Answers") or "_Answers" in stem:
        partner = stem.replace("Answers", "Quiz")
        label = "返去題目"
    else:
        return None
    hit = by_stem.get(partner)
    if hit:
        return (hit, label)
    return None


def build_note_page(note, notes, groups, by_stem):
    prefix = "../"
    crumb = (
        '<nav class="breadcrumb">'
        f'<a href="{prefix}index.html">首頁</a><span class="sep">/</span>'
        f'<span>{esc(note["category"])}</span><span class="sep">/</span>'
        f'<span>{esc(note["title"])}</span></nav>'
    )
    toolbar = (
        '<div class="page-toolbar">'
        f'<a class="back-home" href="{prefix}index.html">← 返回首頁</a>'
        f'<a class="edit-btn" data-note-path="{esc(note["rel"])}" href="#">{SVG_EDIT}在 GitHub 編輯</a>'
        "</div>"
    )
    pair = find_pair(note, by_stem)
    pair_html = ""
    if pair:
        hit, label = pair
        pair_html = (
            f'<a class="pair-btn" href="{hit["slug"]}.html">{SVG_SWAP}{label}：'
            f"{esc(hit['title'])}</a>"
        )
    badge = BADGE_CLASS.get(note["category"], "tool")
    meta = (
        '<p class="page-meta">'
        f'<span class="badge {badge}">{esc(note["category"])}</span>'
        f"<span>最後更新：{note['mtime']:%Y-%m-%d}</span>"
        "</p>"
    )
    memo = f"""
<details class="memo" data-slug="{note['slug']}">
<summary>{SVG_MEMO}速記{SVG_CHEV}</summary>
<div class="memo-inner">
<textarea placeholder="喺度寫低你嘅速記，會即打即存喺瀏覽器…" aria-label="速記"></textarea>
<div class="memo-bar">
<span class="memo-status">未開始編輯</span>
<button type="button" class="btn btn-copy">複製內容</button>
<button type="button" class="btn btn-download">下載為 .md</button>
<button type="button" class="btn btn-clear danger">清除</button>
</div>
</div>
</details>
"""
    # prev / next（按分類內順序）
    cat_items = [n for n in notes if n["category"] == note["category"]]
    cat_items.sort(key=lambda n: n["rel"])
    idx = next(i for i, n in enumerate(cat_items) if n["slug"] == note["slug"])
    prev_n = cat_items[idx - 1] if idx > 0 else None
    next_n = cat_items[idx + 1] if idx < len(cat_items) - 1 else None
    pager_parts = ['<nav class="pager">']
    if prev_n:
        pager_parts.append(
            f'<a class="prev" href="{prev_n["slug"]}.html">'
            f'<span class="dir">上一份</span>{esc(prev_n["title"])}</a>'
        )
    else:
        pager_parts.append('<span class="spacer"></span>')
    if next_n:
        pager_parts.append(
            f'<a class="next" href="{next_n["slug"]}.html">'
            f'<span class="dir">下一份</span>{esc(next_n["title"])}</a>'
        )
    else:
        pager_parts.append('<span class="spacer"></span>')
    pager_parts.append("</nav>")

    body = f"""
{crumb}
{toolbar}
{pair_html}
{meta}
<article class="note-body">
{note["html"]}
</article>
{memo}
{"".join(pager_parts)}
"""
    return page_shell(note["title"], body, prefix, groups, current_slug=note["slug"])


def main():
    notes = collect_notes()
    if not notes:
        sys.exit("搵唔到任何 .md 筆記。")

    # 讀取內容、渲染
    for n in notes:
        md_text = n["src"].read_text(encoding="utf-8")
        n["title"] = extract_title(md_text, n["stem"])
        n["headings"] = extract_headings(md_text)
        n["text"] = plain_text(md_text)
        n["html"] = render_markdown(md_text)
        n["excerpt"] = n["text"][:160] + ("…" if len(n["text"]) > 160 else "")

    groups = group_by_category(notes)
    by_stem = {n["stem"]: n for n in notes}

    # 清空可重建目錄（idempotent）
    for d in ("pages", "notes", "assets"):
        target = SITE_DIR / d
        if target.exists():
            shutil.rmtree(target)
    (SITE_DIR / "pages").mkdir(parents=True)
    (SITE_DIR / "assets").mkdir(parents=True)

    # 複製原始 .md 到 notes/（保持子目錄結構）
    for n in notes:
        dest = SITE_DIR / "notes" / n["rel"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(n["src"], dest)

    # 搜尋索引
    search_index = [
        {
            "title": n["title"],
            "category": n["category"],
            "badgeClass": BADGE_CLASS.get(n["category"], "tool"),
            "headings": n["headings"],
            "excerpt": n["excerpt"],
            "text": n["text"],
            "url": f"pages/{n['slug']}.html",
        }
        for n in notes
    ]
    (SITE_DIR / "assets" / "search.json").write_text(
        json.dumps(search_index, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    # 靜態資源
    (SITE_DIR / "assets" / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (SITE_DIR / "assets" / "app.js").write_text(APP_JS.strip() + "\n", encoding="utf-8")
    (SITE_DIR / "assets" / "config.js").write_text(CONFIG_JS, encoding="utf-8")

    # 頁面
    (SITE_DIR / "index.html").write_text(
        build_index(notes, groups, search_index), encoding="utf-8"
    )
    for n in notes:
        (SITE_DIR / "pages" / f"{n['slug']}.html").write_text(
            build_note_page(n, notes, groups, by_stem), encoding="utf-8"
        )

    print(f"完成：{len(notes)} 份筆記 → {SITE_DIR}")
    for cat, items in groups:
        print(f"  [{cat}] {len(items)} 份")


if __name__ == "__main__":
    main()
