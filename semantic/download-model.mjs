import { mkdir, rename, stat, rm, cp } from "node:fs/promises";
import { createHash } from "node:crypto";
import { createReadStream } from "node:fs";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import path from "node:path";
import { MODEL, REVISION } from "./model.mjs";

const exec = promisify(execFile);
const destination = path.resolve(".semantic-cache/model", MODEL);
const files = ["config.json", "tokenizer.json", "tokenizer_config.json",
  "special_tokens_map.json", "onnx/model_quantized.onnx"];
const expected = { "onnx/model_quantized.onnx":
  "f80102d3f2a1229f387d3c81909990d8945513e347b0eab049f7de3c6f98c193" };
async function digest(file) {
  const sha = createHash("sha256");
  for await (const part of createReadStream(file)) sha.update(part);
  return sha.digest("hex");
}
for (const name of files) {
  const target = path.join(destination, name);
  await mkdir(path.dirname(target), { recursive: true });
  let present = false;
  try { present = (await stat(target)).size > 100 && (!expected[name] || await digest(target) === expected[name]); }
  catch { /* cache miss */ }
  if (present) continue;
  const temporary = target + ".partial";
  await rm(temporary, { force: true });
  const source = "https://huggingface.co/" + MODEL + "/resolve/" + REVISION + "/" + name;
  await exec("curl", ["-fsSL", "--retry", "4", "--retry-all-errors", "--connect-timeout",
    "30", "--max-time", "600", "-o", temporary, source], { maxBuffer: 1024 * 1024 });
  if ((await stat(temporary)).size < 100 || (expected[name] && await digest(temporary) !== expected[name])) {
    await rm(temporary, { force: true });
    throw new Error("Invalid or truncated model asset: " + name);
  }
  await rename(temporary, target);
  console.log("Fetched model asset " + name);
}
await cp(path.resolve(".semantic-cache/model"), path.resolve("site/assets/semantic/models"), { recursive: true });
