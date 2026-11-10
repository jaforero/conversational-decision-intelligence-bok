import { mkdir, cp, readdir, stat } from "node:fs/promises";
import path from "node:path";
import { build } from "esbuild";
const root = process.cwd(), dest = path.join(root, "site/assets/semantic");
await mkdir(dest, { recursive: true });
await build({ entryPoints: ["semantic/browser-model.mjs"], platform: "browser",
  format: "esm", target: ["es2022"], bundle: true, minify: true,
  outfile: path.join(dest, "embed.mjs"), logLevel: "warning" });
await cp("semantic/retrieval.mjs", path.join(dest, "retrieval.mjs"));
await cp("semantic/answers.mjs", path.join(dest, "answers.mjs"));
const wasmRoot = path.join(root, "semantic/node_modules/onnxruntime-web/dist");
const ortDest = path.join(dest, "ort");
await mkdir(ortDest, { recursive: true });
const wasmFiles = (await readdir(wasmRoot)).filter((name) =>
  /^ort-wasm.*\.(wasm|mjs)$/.test(name));
if (!wasmFiles.some((name) => name.endsWith(".wasm"))) throw new Error("Missing ONNX Runtime WASM");
for (const file of wasmFiles) await cp(path.join(wasmRoot, file), path.join(ortDest, file));
const walk = async (dir) => (await Promise.all((await readdir(dir, { withFileTypes: true }))
  .map(async (entry) => entry.isDirectory() ? walk(path.join(dir, entry.name)) :
    (await stat(path.join(dir, entry.name))).size))).flat();
const total = (await walk("site")).reduce((a,b) => a+b,0);
console.log("Static Pages size: " + (total/1048576).toFixed(1) + " MiB");
if (total > 900*1048576) throw new Error("Pages size too close to 1 GB limit");
