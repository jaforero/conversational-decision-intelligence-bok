import { createHash } from "node:crypto";
export const hash = (text) => createHash("sha256").update(text).digest("hex");
function stripped(text) {
  return text
    .replace(/!\[([^\]]*)\]\([^)]+\)/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/<[^>]*>/g, " ")
    .replace(/^[ \t]*[>*+-][ \t]+/gm, "")
    .replace(/[*_~\x60]/g, "")
    .replace(/\s+/g, " ").trim();
}
function splitLong(paragraph, maxChars) {
  const pieces = [], words = paragraph.text.split(/\s+/);
  while (words.length) {
    const group = [];
    let length = 0;
    while (words.length && (length + words[0].length + 1 <= maxChars || !group.length)) {
      const word = words.shift(); group.push(word); length += word.length + 1;
    }
    pieces.push({ ...paragraph, text: group.join(" ") });
  }
  return pieces;
}
export function parseMarkdown(source, path, maxChars = 800) {
  const lines = source.replace(/\r\n/g, "\n").split("\n");
  let start = 0;
  const metadata = {};
  if (lines[0]?.trim() === "---") {
    const end = lines.findIndex((line, i) => i > 0 && line.trim() === "---");
    if (end > 0) {
      for (const line of lines.slice(1, end)) {
        const match = line.match(/^([a-z_]+):\s*(.*)$/i);
        if (match) metadata[match[1]] = match[2].replace(/^["']|["']$/g, "");
      }
      start = end + 1;
    }
  }
  const title = metadata.title || path.split("/").at(-1).replace(/\.en\.md$|\.md$/g, "");
  const stack = [], paragraphs = [];
  let buffer = [], lineStart = 0, fence = false;
  const flush = () => {
    if (!buffer.length) return;
    const text = stripped(buffer.join(" "));
    if (text) paragraphs.push({ text, start: lineStart, end: lineStart + buffer.length - 1,
      section: stack.map((item) => item.title).join(" › ") || title });
    buffer = [];
  };
  for (let i = start; i < lines.length; i++) {
    const raw = lines[i];
    if (/^\s*(\x60{3}|~{3})/.test(raw)) { flush(); fence = !fence; continue; }
    if (fence || /^<!--/.test(raw.trim())) continue;
    const heading = raw.match(/^(#{1,6})\s+(.+?)\s*#*\s*$/);
    if (heading) {
      flush();
      const depth = heading[1].length;
      while (stack.length && stack.at(-1).depth >= depth) stack.pop();
      stack.push({ depth, title: stripped(heading[2]) });
      continue;
    }
    if (!raw.trim()) { flush(); continue; }
    if (!buffer.length) lineStart = i + 1;
    buffer.push(raw);
  }
  flush();
  const chunks = [];
  let current = [], total = 0;
  const commit = () => {
    if (!current.length) return;
    const first = current[0], last = current.at(-1);
    const text = current.map((p) => p.text).join("\n");
    chunks.push({ id: hash(path + "\n" + first.section + "\n" + text).slice(0, 24),
      text, path, page: title, heading: first.section, lineStart: first.start, lineEnd: last.end,
      contentHash: hash(text) });
    current = []; total = 0;
  };
  for (const paragraph of paragraphs.flatMap((p) => p.text.length > maxChars ? splitLong(p, maxChars) : [p])) {
    if (current.length && (total + paragraph.text.length > maxChars || current[0].section !== paragraph.section)) commit();
    current.push(paragraph); total += paragraph.text.length + 1;
  }
  commit();
  return { metadata, chunks };
}
