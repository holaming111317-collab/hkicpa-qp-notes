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
