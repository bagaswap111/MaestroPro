/* ── MaestroPro Music Theory Knowledge Base Viewer ──── */
import { marked } from '/vendor/marked.js';

const $ = (s, p = document) => p.querySelector(s);
const $$ = (s, p = document) => [...p.querySelectorAll(s)];

/* ── State ─────────────────────────────────────────── */
let tree = null;
let flatFiles = [];
let currentPath = null;
let searchTimer = null;

/* ── DOM refs ──────────────────────────────────────── */
const sidebar       = $('#sidebar');
const treeEl        = $('#tree');
const searchInput   = $('#search-input');
const searchResults = $('#search-results');
const content       = $('#content');
const breadcrumb    = $('#breadcrumb');
const prevBtn       = $('#prev-btn');
const nextBtn       = $('#next-btn');
const menuToggle    = $('#menu-toggle');
const tocFloat      = $('#toc-float');
const tocList       = $('#toc-list');

/* ── Helpers ───────────────────────────────────────── */
function stripFrontmatter(md) {
  return md.replace(/^---[\s\S]*?---\s*/, '');
}

function extractTitle(md) {
  const fm = md.match(/^---[\s\S]*?---/);
  if (fm) {
    const m = fm[0].match(/title:\s*["']?(.+?)["']?\s*$/m);
    if (m) return m[1].trim();
  }
  const h1 = md.match(/^#\s+(.+)$/m);
  return h1 ? h1[1].trim() : null;
}

function shortenName(name) {
  return name
    .replace(/^\d+-[\w-]+\/?/g, '')
    .replace(/\.md$/, '')
    .replace(/-/g, ' ');
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/* ── Build flat file list (for pager) ──────────────── */
function flattenFiles() {
  flatFiles = [];
  for (const tier of tree.tiers) {
    for (const subj of (tier.children || [])) {
      for (const f of (subj.children || [])) {
        if (f.type === 'file') flatFiles.push(f);
      }
    }
  }
  for (const f of (tree.rootFiles || [])) {
    flatFiles.push(f);
  }
}

/* ── Render sidebar tree ───────────────────────────── */
function renderTree() {
  treeEl.innerHTML = '';

  if (tree.rootFiles && tree.rootFiles.length) {
    for (const f of tree.rootFiles) {
      const a = document.createElement('a');
      a.className = 'tree-file';
      a.dataset.path = f.path;
      a.innerHTML = `<span class="tree-file-name">${shortenName(f.name)}</span>`;
      a.addEventListener('click', (e) => { e.preventDefault(); loadFile(f.path); });
      treeEl.appendChild(a);
    }
  }

  for (const tier of tree.tiers) {
    const tierDiv = document.createElement('div');
    tierDiv.className = 'tree-tier open';

    const label = document.createElement('div');
    label.className = 'tree-tier-label';
    label.innerHTML = `<span class="arrow">▸</span>${tier.name}`;
    label.addEventListener('click', () => tierDiv.classList.toggle('open'));
    tierDiv.appendChild(label);

    const subjContainer = document.createElement('div');
    subjContainer.className = 'tree-subjects';

    for (const subj of (tier.children || [])) {
      if (subj.type === 'dir' && subj.children && subj.children.length) {
        const fileLinks = subj.children.filter(c => c.type === 'file');
        if (!fileLinks.length) continue;
        for (const f of fileLinks) {
          const a = document.createElement('a');
          a.className = 'tree-file';
          a.dataset.path = f.path;
          a.innerHTML = `<span class="tree-file-name">${shortenName(f.name)}</span>`;
          a.addEventListener('click', (e) => { e.preventDefault(); loadFile(f.path); });
          subjContainer.appendChild(a);
        }
      }
    }

    tierDiv.appendChild(subjContainer);
    treeEl.appendChild(tierDiv);
  }
}

/* ── Load & render markdown ────────────────────────── */
async function loadFile(relPath) {
  if (!relPath) return;
  currentPath = relPath;

  window.location.hash = relPath;
  if (window.innerWidth <= 768) sidebar.classList.add('collapsed');

  content.innerHTML = '<div class="loading">Memuat…</div>';
  content.scrollTop = 0;

  $$('.tree-file.active', treeEl).forEach(el => el.classList.remove('active'));
  const activeLink = $(`.tree-file[data-path="${CSS.escape(relPath)}"]`, treeEl);
  if (activeLink) {
    activeLink.classList.add('active');
    const tier = activeLink.closest('.tree-tier');
    if (tier && !tier.classList.contains('open')) tier.classList.add('open');
    activeLink.scrollIntoView({ block: 'nearest' });
  }

  try {
    const res = await fetch(`/api/file?path=${encodeURIComponent(relPath)}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const md = await res.text();
    renderMarkdown(md, relPath);
    updatePager(relPath);
    updateBreadcrumb(relPath, md);
    buildTOC();
  } catch (err) {
    content.innerHTML = `<div class="loading" style="color:#e06c75">Gagal memuat: ${err.message}</div>`;
  }
}

function renderMarkdown(md, relPath) {
  const clean = stripFrontmatter(md);
  const html = marked.parse(clean);

  const wrapped = html.replace(
    /<pre><code class="language-(\w+)">/g,
    '<pre data-lang="$1"><code class="language-$1">'
  );

  content.innerHTML = `<div class="md-body">${wrapped}</div>`;

  $$('a[href]', content).forEach(a => {
    const href = a.getAttribute('href');
    if (href && href.endsWith('.md')) {
      a.addEventListener('click', (e) => {
        e.preventDefault();
        const baseDir = relPath.includes('/') ? relPath.substring(0, relPath.lastIndexOf('/')) : '';
        const target = baseDir ? baseDir + '/' + href : href;
        loadFile(target);
      });
    }
  });

  initMusicXmlBlocks();
}

/* ── MusicXML: syntax highlight + sheet preview ──── */
let osmdLib = null;

async function loadOSMD() {
  if (osmdLib) return osmdLib;
  await new Promise((resolve, reject) => {
    if (window.opensheetmusicdisplay) { resolve(); return; }
    const s = document.createElement('script');
    s.src = '/vendor/opensheetmusicdisplay.min.js';
    s.onload = resolve;
    s.onerror = reject;
    document.head.appendChild(s);
  });
  osmdLib = window.opensheetmusicdisplay;
  return osmdLib;
}

function isCompleteMusicXml(text) {
  return text.includes('<score-partwise') || text.includes('<score-timewise');
}

function highlightXml(xml) {
  const safe = escapeHtml(xml);
  return safe
    .replace(/(&lt;\/?)([\w:-]+)/g, '$1<span class="xml-tag">$2</span>')
    .replace(/\s([\w:-]+)(=)(&quot;[^&]*?&quot;)/g, ' <span class="xml-attr">$1</span>$2<span class="xml-val">$3</span>')
    .replace(/(&lt;!--[\s\S]*?--&gt;)/g, '<span class="xml-comment">$1</span>');
}

async function initMusicXmlBlocks() {
  const pres = $$('pre[data-lang="xml"], pre[data-lang="musicxml"]', content);
  for (const pre of pres) {
    if (pre.dataset.xmlDone) continue;
    pre.dataset.xmlDone = 'true';

    const code = $('code', pre);
    if (!code) continue;
    const rawXml = code.textContent;
    const complete = isCompleteMusicXml(rawXml);

    // Syntax highlight
    code.innerHTML = highlightXml(rawXml);

    // Toggle bar
    const bar = document.createElement('div');
    bar.className = 'xml-toggle-bar';
    bar.innerHTML = complete
      ? `<button class="xml-toggle-btn active" data-view="code">Code</button>
         <button class="xml-toggle-btn" data-view="preview">Preview</button>`
      : `<span class="xml-label">XML Fragment</span>`;
    pre.parentNode.insertBefore(bar, pre);

    if (!complete) continue;

    // Preview container
    const box = document.createElement('div');
    box.className = 'xml-preview-container';
    box.style.display = 'none';
    const sheet = document.createElement('div');
    sheet.className = 'musicxml-sheet';
    box.appendChild(sheet);
    pre.parentNode.insertBefore(box, pre.nextSibling);

    // Toggle logic
    $$('.xml-toggle-btn', bar).forEach(btn => {
      btn.addEventListener('click', async () => {
        $$('.xml-toggle-btn', bar).forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        if (btn.dataset.view === 'code') {
          pre.style.display = '';
          box.style.display = 'none';
        } else {
          pre.style.display = 'none';
          box.style.display = '';
          if (!sheet.dataset.rendered) {
            sheet.dataset.rendered = 'true';
            await renderSheet(rawXml, sheet);
          }
        }
      });
    });
  }
}

async function renderSheet(xml, sheet) {
  try {
    const lib = await loadOSMD();
    const osmd = new lib.OpenSheetMusicDisplay(sheet, {
      autoResize: false,
      backend: 'svg',
      drawTitle: false,
      drawComposer: false,
      drawCredits: false,
      drawPartNames: true,
      drawPartAbbreviations: true,
      drawingParameters: 'compact',
    });
    await osmd.load(xml);
    osmd.render();
  } catch (err) {
    console.error('OSMD error:', err);
    sheet.innerHTML = `<div class="mxl-error">Gagal merender partitur.<br><small>${escapeHtml(err.message)}</small></div>`;
  }
}

/* ── Pager ─────────────────────────────────────────── */
function updatePager(relPath) {
  const idx = flatFiles.findIndex(f => f.path === relPath);
  prevBtn.disabled = idx <= 0;
  nextBtn.disabled = idx < 0 || idx >= flatFiles.length - 1;
  prevBtn.onclick = () => { if (idx > 0) loadFile(flatFiles[idx - 1].path); };
  nextBtn.onclick = () => { if (idx < flatFiles.length - 1) loadFile(flatFiles[idx + 1].path); };
}

/* ── Breadcrumb ────────────────────────────────────── */
function updateBreadcrumb(relPath, md) {
  const parts = relPath.split('/');
  const crumbs = parts.map((p, i) => `<span>${shortenName(p)}</span>`);
  breadcrumb.innerHTML = crumbs.join('<span class="sep">›</span>');
}

/* ── Table of Contents ─────────────────────────────── */
function buildTOC() {
  const headings = $$('.md-body h2, .md-body h3, .md-body h4', content);
  if (headings.length < 2) { tocFloat.hidden = true; return; }

  tocFloat.hidden = false;
  tocList.innerHTML = '';

  headings.forEach((h, i) => {
    if (!h.id) {
      h.id = 'toc-' + i + '-' + h.textContent.toLowerCase()
        .replace(/[^\w]+/g, '-').replace(/^-|-$/g, '');
    }
    const a = document.createElement('a');
    a.className = `toc-link toc-${h.tagName.toLowerCase()}`;
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    a.addEventListener('click', (e) => {
      e.preventDefault();
      h.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    tocList.appendChild(a);
  });

  const onScroll = () => {
    let activeId = null;
    for (const h of headings) {
      if (h.offsetTop - 80 <= content.scrollTop) activeId = h.id;
    }
    $$('.toc-link.active', tocList).forEach(l => l.classList.remove('active'));
    if (activeId) {
      const link = $(`.toc-link[href="#${activeId}"]`, tocList);
      if (link) link.classList.add('active');
    }
  };
  content.removeEventListener('scroll', content._tocScroll);
  content._tocScroll = onScroll;
  content.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ── Search ────────────────────────────────────────── */
searchInput.addEventListener('input', () => {
  clearTimeout(searchTimer);
  const q = searchInput.value.trim();
  if (!q) { searchResults.hidden = true; return; }
  searchTimer = setTimeout(() => doSearch(q), 300);
});

searchInput.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') { searchInput.value = ''; searchResults.hidden = true; }
  if (e.key === 'ArrowDown') { const f = $('.search-item', searchResults); if (f) f.focus(); }
});

document.addEventListener('click', (e) => {
  if (!e.target.closest('.searchbox')) searchResults.hidden = true;
});

async function doSearch(q) {
  try {
    const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
    const results = await res.json();
    if (!results.length) {
      searchResults.innerHTML = '<div class="search-item"><span class="search-item-snippet">Tidak ditemukan</span></div>';
      searchResults.hidden = false;
      return;
    }
    searchResults.innerHTML = results.map(r => `
      <div class="search-item" tabindex="0" data-path="${r.path}">
        <div class="search-item-path">${r.path} : ${r.line}</div>
        <div class="search-item-snippet">${highlightMatch(r.snippet, q)}</div>
      </div>
    `).join('');
    $$('.search-item', searchResults).forEach(item => {
      item.addEventListener('click', () => { loadFile(item.dataset.path); searchInput.value = ''; searchResults.hidden = true; });
      item.addEventListener('keydown', (e) => { if (e.key === 'Enter') { loadFile(item.dataset.path); searchInput.value = ''; searchResults.hidden = true; } });
    });
    searchResults.hidden = false;
  } catch { searchResults.hidden = true; }
}

function highlightMatch(text, q) {
  const escaped = q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return text.replace(new RegExp(`(${escaped})`, 'gi'), '<mark>$1</mark>');
}

/* ── Sidebar toggle ────────────────────────────────── */
menuToggle.addEventListener('click', () => sidebar.classList.toggle('collapsed'));

/* ── Keyboard shortcuts ────────────────────────────── */
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey && e.key === 'k') || (e.key === '/' && document.activeElement !== searchInput)) {
    e.preventDefault(); searchInput.focus();
  }
  if (e.altKey && e.key === 'ArrowLeft' && !prevBtn.disabled) prevBtn.click();
  if (e.altKey && e.key === 'ArrowRight' && !nextBtn.disabled) nextBtn.click();
});

/* ── Hash routing ──────────────────────────────────── */
function handleHash() {
  const hash = window.location.hash.replace(/^#\/?/, '');
  if (hash && hash.endsWith('.md')) loadFile(hash);
}
window.addEventListener('hashchange', handleHash);

/* ── Init ──────────────────────────────────────────── */
async function init() {
  try {
    const res = await fetch('/api/tree');
    tree = await res.json();
    renderTree();
    flattenFiles();
    if (window.location.hash) handleHash();
    else if (flatFiles.length) loadFile(flatFiles[0].path);
  } catch (err) {
    content.innerHTML = `<div class="loading" style="color:#e06c75">Gagal memuat pustaka: ${err.message}</div>`;
  }
}

init();
