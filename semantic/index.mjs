import { readFile, writeFile, readdir, mkdir, rename } from "node:fs/promises";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { pipeline, env } from "@huggingface/transformers";
import { MODEL, MODEL_KEY, DTYPE, DIM, embedText, normalizedVector } from "./model.mjs";
import { hash, parseMarkdown } from "./markdown.mjs";
import { buildLexicon } from "./retrieval.mjs";

const root = process.cwd();
const dest = path.join(root, "site/assets/semantic");
const cacheDir = path.join(root, ".semantic-cache");
const cacheFile = path.join(cacheDir, "embeddings.json");
const sha = execFileSync("git", ["rev-parse", "HEAD"], { encoding: "utf8" }).trim();
async function documents(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const nested = await Promise.all(entries.map(async (entry) => {
    const current = path.join(dir, entry.name);
    if (entry.isDirectory()) return documents(current);
    if (entry.isFile() && entry.name.endsWith(".md")) return [current];
    return [];
  }));
  return nested.flat().sort();
}
await mkdir(dest, { recursive: true });
await mkdir(cacheDir, { recursive: true });
let cache = { modelKey: MODEL_KEY, vectors: {} };
try {
  const existing = JSON.parse(await readFile(cacheFile, "utf8"));
  if (existing.modelKey === MODEL_KEY && existing.vectors &&
      typeof existing.vectors === "object") cache = existing;
} catch { console.log("No compatible incremental cache; rebuilding embeddings"); }
const files = await documents(path.join(root, "docs"));
const data = { es: [], en: [] };
const sourceDigest = [];
for (const file of files) {
  const relative = path.relative(root, file).replaceAll(path.sep, "/");
  if (/^docs\/(ask-cdi|index)(\.en)?\.md$/.test(relative)) continue;
  const source = await readFile(file, "utf8");
  const lang = relative.endsWith(".en.md") ? "en" : "es";
  const { metadata, chunks } = parseMarkdown(source, relative);
  if (metadata.status && !["approved", "candidate"].includes(metadata.status)) continue;
  sourceDigest.push(relative + ":" + hash(source));
  for (const chunk of chunks) data[lang].push({ ...chunk, language: lang,
    status: metadata.status || "unclassified",
    simulated: /practice-lab\/(sla-decision-brief|b2b-proposal)\//.test(relative) ||
      relative.includes("/sla-decision-brief."),
    url: "https://github.com/jaforero/conversational-decision-intelligence-bok/blob/" +
      sha + "/" + encodeURI(relative) + "#L" + chunk.lineStart + "-L" + chunk.lineEnd });
}
const all = [...data.es, ...data.en], missing = [];
for (const chunk of all) {
  const key = hash(MODEL_KEY + "\n" + chunk.text);
  chunk.vectorKey = key;
  if (!Array.isArray(cache.vectors[key]) || cache.vectors[key].length !== DIM ||
      !cache.vectors[key].every(Number.isFinite)) missing.push(chunk);
  else chunk.vector = cache.vectors[key];
}
console.log("Documents: " + files.length + ", chunks: " + all.length + ", new embeddings: " + missing.length);
let extractor;
async function getExtractor() {
  if (!extractor) {
    env.allowRemoteModels = false;
    env.allowLocalModels = true;
    env.localModelPath = path.join(dest, "models") + path.sep;
    extractor = await pipeline("feature-extraction", MODEL, { device: "cpu", dtype: DTYPE });
  }
  return extractor;
}
async function embed(value, mode) {
  const pipe = await getExtractor();
  const tensor = await pipe(embedText(value, mode), { pooling: "mean", normalize: true });
  return normalizedVector(tensor.data).map((v) => Number(v.toFixed(7)));
}
for (let i = 0; i < missing.length; i++) {
  const chunk = missing[i];
  chunk.vector = await embed(chunk.heading + ": " + chunk.text, "passage");
  cache.vectors[chunk.vectorKey] = chunk.vector;
  if ((i + 1) % 25 === 0) console.log("Embedded " + (i + 1) + "/" + missing.length);
}
for (const chunk of all) {
  if (!chunk.vector) chunk.vector = cache.vectors[chunk.vectorKey];
  if (chunk.vector.length !== DIM) throw new Error("Invalid vector: " + chunk.path);
  delete chunk.vectorKey;
}
const digest = hash(sourceDigest.sort().join("\n"));
const oldManifest = await readFile(path.join(cacheDir, "manifest.json"), "utf8").then(JSON.parse).catch(() => null);
let reference = oldManifest?.sourceDigest === digest && oldManifest?.modelKey === MODEL_KEY
  ? oldManifest.reference : null;
if (!reference) reference = await embed("What is PULSE?", "query");
for (const lang of ["es", "en"]) {
  const chunks = data[lang], lexicon = buildLexicon(chunks);
  const payload = { format: 1, modelKey: MODEL_KEY, dimension: DIM, sourceSha: sha,
    sourceDigest: digest, language: lang, reference, documents: new Set(chunks.map((c) => c.path)).size,
    chunks, lexicon };
  if (!chunks.length) throw new Error("Empty " + lang + " corpus");
  await writeFile(path.join(dest, "index-" + lang + ".json"), JSON.stringify(payload));
}
const validKeys = new Set(all.map((chunk) => hash(MODEL_KEY + "\n" + chunk.text)));
cache.vectors = Object.fromEntries(Object.entries(cache.vectors).filter(([key]) => validKeys.has(key)));
const temp = cacheFile + ".partial";
await writeFile(temp, JSON.stringify(cache));
await rename(temp, cacheFile);
await writeFile(path.join(cacheDir, "manifest.json"), JSON.stringify({ sourceDigest: digest,
  modelKey: MODEL_KEY, reference }));
await writeFile(path.join(dest, "manifest.json"), JSON.stringify({ sourceSha: sha, sourceDigest: digest,
  modelKey: MODEL_KEY, dimension: DIM, documents: files.length, chunks: all.length,
  build: "GitHub Actions; all queries run locally" }));
console.log("Index built: commit " + sha + ", corpus digest " + digest);
if (extractor?.dispose) await extractor.dispose();
