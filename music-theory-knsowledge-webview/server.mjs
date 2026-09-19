import { createServer } from 'node:http';
import { readFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CONTENT_ROOT = path.resolve(__dirname, '..', 'music-theory-knsowledge');
const PUBLIC_DIR = path.join(__dirname, 'public');
const MARKED_FILE = path.join(__dirname, 'node_modules', 'marked', 'lib', 'marked.esm.js');
const PORT = Number(process.env.PORT) || 5174;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.json': 'application/json; charset=utf-8',
  '.wasm': 'application/wasm',
  '.sf3': 'audio/soundfont',
  '.mp3': 'audio/mpeg',
};

const isWithin = (base, target) =>
  target === base || target.startsWith(base + path.sep);

async function walk(dir, rel = '') {
  const entries = await readdir(dir, { withFileTypes: true });
  entries.sort((a, b) => a.name.localeCompare(b.name, 'id'));
  const out = [];
  for (const e of entries) {
    const abs = path.join(dir, e.name);
    const relPath = rel ? path.join(rel, e.name) : e.name;
    if (e.isDirectory()) {
      const children = await walk(abs, relPath);
      if (children.length) out.push({ type: 'dir', name: e.name, path: relPath, children });
    } else if (e.name.toLowerCase().endsWith('.md')) {
      out.push({ type: 'file', name: e.name, path: relPath.replaceAll('\\', '/') });
    }
  }
  return out;
}

async function searchFiles(q) {
  const needle = q.toLowerCase();
  const results = [];
  const rootMd = [];
  const scan = async (dir, rel = '') => {
    const entries = await readdir(dir, { withFileTypes: true });
    for (const e of entries) {
      const abs = path.join(dir, e.name);
      const relPath = rel ? path.join(rel, e.name) : e.name;
      if (e.isDirectory()) { await scan(abs, relPath); continue; }
      if (!e.name.toLowerCase().endsWith('.md')) continue;
      const text = await readFile(abs, 'utf8');
      let idx = text.toLowerCase().indexOf(needle);
      let hit = 0;
      while (idx !== -1 && hit < 20) {
        const lineStart = text.lastIndexOf('\n', idx) + 1;
        const lineEnd = text.indexOf('\n', idx);
        const line = text.slice(lineStart, lineEnd === -1 ? text.length : lineEnd).trim();
        const lineNo = text.slice(0, idx).split('\n').length;
        results.push({ path: relPath.replaceAll('\\', '/'), line: lineNo, snippet: line.slice(0, 180) });
        idx = text.toLowerCase().indexOf(needle, idx + 1);
        hit++;
      }
    }
  };
  await scan(CONTENT_ROOT);
  results.sort((a, b) => a.path.localeCompare(b.path) || a.line - b.line);
  return results.slice(0, 300);
}

const server = createServer(async (req, res) => {
  try {
    const url = new URL(req.url, `http://localhost:${PORT}`);
    const p = decodeURIComponent(url.pathname);

    if (p === '/api/tree') {
      const tree = await walk(CONTENT_ROOT);
      const rootFiles = [];
      const tiers = [];
      for (const node of tree) {
        if (node.type === 'dir') tiers.push(node);
        else rootFiles.push(node);
      }
      res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
      res.end(JSON.stringify({ root: CONTENT_ROOT, rootFiles, tiers }));
      return;
    }

    if (p === '/api/file') {
      const rel = url.searchParams.get('path') || '';
      const target = path.resolve(CONTENT_ROOT, rel);
      if (!isWithin(CONTENT_ROOT, target)) {
        res.writeHead(403, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ error: 'Forbidden' }));
        return;
      }
      const content = await readFile(target, 'utf8');
      res.writeHead(200, { 'Content-Type': 'text/markdown; charset=utf-8', 'Cache-Control': 'no-store' });
      res.end(content);
      return;
    }

    if (p === '/api/search') {
      const q = (url.searchParams.get('q') || '').trim();
      if (!q) { res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' }); res.end('[]'); return; }
      const results = await searchFiles(q);
      res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
      res.end(JSON.stringify(results));
      return;
    }

    if (p === '/vendor/marked.js' || p === '/marked.js') {
      const content = await readFile(MARKED_FILE, 'utf8');
      res.writeHead(200, { 'Content-Type': 'text/javascript; charset=utf-8' });
      res.end(content);
      return;
    }

    // Serve OSMD vendor file
    if (p === '/vendor/opensheetmusicdisplay.min.js') {
      const osmdFile = path.join(__dirname, 'node_modules', 'opensheetmusicdisplay', 'build', 'opensheetmusicdisplay.min.js');
      const content = await readFile(osmdFile);
      res.writeHead(200, { 'Content-Type': 'text/javascript; charset=utf-8', 'Cache-Control': 'public, max-age=3600' });
      res.end(content);
      return;
    }

    let filePath;
    if (p === '/' || p === '') filePath = path.join(PUBLIC_DIR, 'index.html');
    else filePath = path.join(PUBLIC_DIR, p);

    if (!isWithin(PUBLIC_DIR, filePath)) {
      res.writeHead(403); res.end('Forbidden'); return;
    }
    const ext = path.extname(filePath).toLowerCase();
    if (!MIME[ext]) { res.writeHead(404); res.end('Not found'); return; }
    const content = await readFile(filePath);
    res.writeHead(200, { 'Content-Type': MIME[ext] });
    res.end(content);
  } catch (err) {
    res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Server error: ' + err.message);
  }
});

server.listen(PORT, () => {
  console.log('');
  console.log('  MaestroPro MD Viewer');
  console.log('  --------------------');
  console.log(`  Content : ${CONTENT_ROOT}`);
  console.log(`  Buka    : http://localhost:${PORT}`);
  console.log('');
});