import assert from "node:assert/strict";
import test from "node:test";
import { parseMarkdown } from "./markdown.mjs";
import { buildLexicon, lexical, semantic, rank, shouldAbstain, terms } from "./retrieval.mjs";
test("Markdown extracts frontmatter, headings and 1-based line references", () => {
  const source = "---\ntitle: Demo\nstatus: candidate\n---\n# Title\n\n## Section\n\nHola mundo importante.\n\nOtro párrafo.\n";
  const {metadata,chunks} = parseMarkdown(source, "docs/demo.md");
  assert.equal(metadata.status,"candidate");
  assert.equal(chunks[0].heading, "Title › Section");
  assert.equal(chunks[0].lineStart, 9);
  assert.equal(chunks[0].lineEnd, 11);
  assert.match(chunks[0].text, /Hola mundo/);
});
test("chunk identity changes when text changes; punctuation is normalized", () => {
  const a = parseMarkdown("# Uno\n\nInformación central.", "docs/x.md").chunks[0];
  const b = parseMarkdown("# Uno\n\nInformación revisada.", "docs/x.md").chunks[0];
  assert.notEqual(a.contentHash, b.contentHash);
  assert.deepEqual(terms("¿Información, info?"), ["informacion","info"]);
});
test("BM25 matches exact codes and RRF adds semantic paraphrases", () => {
  const chunks = [{ text:"control humano y evidencia",heading:"Governance",vector:[1,0] },
    { text:"SKU DTC2PT capacidad",heading:"Inventory",vector:[0,1] }];
  const index = {modelKey:"test",chunks,lexicon:buildLexicon(chunks)};
  assert.equal(lexical(index,"DTC2PT")[0].i,1);
  assert.equal(semantic(index,[1,0])[0].i,0);
  const result = rank(index,"control humano",[1,0]);
  assert.equal(result.ranked[0].text,chunks[0].text);
  assert.equal(shouldAbstain(index,result.ranked,{modelKey:"test",minCosine:0.5}),false);
  assert.equal(shouldAbstain(index,result.ranked,{modelKey:"other",minCosine:0.5}),true);
});
test("gibberish should not be considered lexical evidence", () => {
  const chunks=[{heading:"A",text:"Evidence about decisions",vector:[1,0]}];
  const i={chunks,lexicon:buildLexicon(chunks)};
  assert.equal(lexical(i,"zxyznotfound").length, 0); 
});
