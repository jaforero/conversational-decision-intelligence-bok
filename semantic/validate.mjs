import assert from "node:assert/strict";
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { MODEL_KEY, DIM } from "./model.mjs";
import { buildLexicon } from "./retrieval.mjs";
const base = "site/assets/semantic";
const sha = execFileSync("git", ["rev-parse","HEAD"],{encoding:"utf8"}).trim();
const calibration = JSON.parse(await readFile(path.join(base,"calibration.json"),"utf8"));
assert.equal(calibration.modelKey,MODEL_KEY);
assert.ok(Number.isFinite(calibration.minCosine));
assert.ok(Number.isFinite(calibration.curatedMinCosine));
for(const lang of ["es","en"]) {
  const index=JSON.parse(await readFile(path.join(base,"index-"+lang+".json"),"utf8"));
  assert.equal(index.sourceSha,sha);
  assert.equal(index.modelKey,MODEL_KEY);
  assert.equal(index.language,lang);
  assert.equal(index.dimension,DIM);
  assert.equal(index.reference.length,DIM);
  assert.ok(index.chunks.length>20);
  assert.deepEqual(index.lexicon,buildLexicon(index.chunks));
  assert.ok(index.curated.length>=7);
  for (const answer of index.curated) {
    assert.ok(Array.isArray(answer.vectors) && answer.vectors.length >= 2);
    for (const vector of answer.vectors) {
      assert.equal(vector.length,DIM);
      assert.ok(vector.every(Number.isFinite));
    }
    assert.equal(answer.sourceSha,sha);
    assert.ok(answer.sourceUrl.includes("/blob/"+sha+"/"));
    assert.ok(answer.sourcePath.startsWith("docs/"));
    if (answer.answer) {
      assert.ok(index.chunks.some((chunk) => chunk.path===answer.sourcePath &&
        chunk.text.includes(answer.excerpt)));
    }
  }
  const architecture=index.curated.find((x)=>x.source.includes("/learn/data-architecture-fable/#architecture-map"));
  assert.ok(architecture?.answer && architecture?.bullets.length===5);
  assert.ok(architecture.sourceUrl.includes("#L"));
  for(const item of index.chunks) {
    assert.equal(item.vector.length,DIM);
    assert.ok(item.vector.every(Number.isFinite));
    assert.ok(item.lineStart>0 && item.lineEnd>=item.lineStart);
    assert.ok(item.url.includes("/blob/"+sha+"/"+item.path+"#L"+item.lineStart+"-L"+item.lineEnd));
    const source=(await readFile(item.path,"utf8")).split(/\r?\n/);
    assert.ok(item.lineEnd<=source.length);
  }
  console.log(lang+": "+index.chunks.length+" valid cited chunks");
}
const file="site/assets/semantic/models/Xenova/multilingual-e5-small/onnx/model_quantized.onnx";
assert.ok((await stat(file)).size>100000000);
assert.ok((await stat(path.join(base,"embed.mjs"))).size>100000);
assert.ok((await stat(path.join(base,"answers.mjs"))).size>500);
console.log("PASS: index consistency, citations and local model distribution");
