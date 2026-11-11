import assert from "node:assert/strict";
import test from "node:test";
import { parseMarkdown } from "./markdown.mjs";
import { curatedCandidates, matchCurated, matchesNamedConcept, extractPassage, extractEvidence } from "./answers.mjs";
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
test("abstention applies calibrated cosine to the RRF top hit, not the semantic best hit", () => {
  const chunks = [
    {heading:"Alpha",text:"generic background",vector:[0.8,0.6]},
    {heading:"Beta",text:"DTC2PT specific exact code",vector:[0.6,0.8]},
  ];
  const index = {modelKey:"test",chunks,lexicon:buildLexicon(chunks)};
  const found = rank(index,"DTC2PT",[1,0]);
  assert.equal(found.ranked[0].heading,"Beta");
  assert.ok(semantic(index,[1,0])[0].score > found.ranked[0].cosine);
  assert.equal(shouldAbstain(index,found.ranked,{modelKey:"test",minCosine:0.7}),true);
  assert.equal(shouldAbstain(index,[{cosine:NaN}],{modelKey:"test",minCosine:0.7}),true);
});
test("gibberish should not be considered lexical evidence", () => {
  const chunks=[{heading:"A",text:"Evidence about decisions",vector:[1,0]}];
  const i={chunks,lexicon:buildLexicon(chunks)};
  assert.equal(lexical(i,"zxyznotfound").length, 0); 
});

test("semantic editorial routing matches a paraphrase, never unsupported low-score queries", () => {
  const index = {modelKey:"test",curated:[
    {question:"Choose data architecture",source:"/learn/data-architecture-fable/#architecture-map",vectors:[[1,0],[0.8,0.6]]},
    {question:"Human governance",source:"/03-pulse/specification/#human-in-control",vectors:[[0,1],[0.1,0.9]]},
  ]};
  const candidates = curatedCandidates(index,[0.98,0.2]);
  assert.equal(candidates[0].item.source,"/learn/data-architecture-fable/#architecture-map");
  const calibration = {modelKey:"test",curatedMinCosine:0.9};
  assert.equal(matchCurated(index,[0.98,0.2],calibration)?.source,
    "/learn/data-architecture-fable/#architecture-map");
  assert.equal(matchCurated(index,[0.55,0.55],calibration),null);
  assert.equal(matchCurated(index,[1,0],{modelKey:"wrong",curatedMinCosine:0.5}),null);
});
test("fallback answer is a literal paragraph rather than generated prose", () => {
  const passage = "A same-platform design can cover more than one responsibility.\nSecond paragraph with further evidence.";
  const result = extractPassage([{text:passage,path:"docs/example.md"}]);
  assert.equal(result.excerpt, "A same-platform design can cover more than one responsibility.");
  assert.equal(result.item.path,"docs/example.md");
  assert.equal(extractPassage([]),null);
});

test("named technical concepts cannot be answered with an unrelated generic editorial card", () => {
  const pulse = {
    question:"What is PULSE?", aliases:["Definition of PULSE"],
    answer:"PULSE is a decision intelligence methodology.", bullets:[],
    excerpt:"PULSE links context to action.", vectors:[[1,0]]
  };
  const architecture = {
    question:"How do I choose data architecture?", aliases:["Choosing Data Lake"],
    answer:"Data Lake and Data Warehouse support different decisions.",
    bullets:["Data Mesh assigns domain ownership."],
    excerpt:"Choose what you need.",vectors:[[0,1]]
  };
  assert.equal(matchesNamedConcept("What is the Decision Circle in PULSE?", pulse),false);
  assert.equal(matchesNamedConcept("How to choose Data Lake architecture?", architecture),true);
  assert.equal(matchesNamedConcept("How do I choose architecture?", architecture),true);
  assert.equal(matchCurated({modelKey:"test",curated:[pulse]},[1,0],
    {modelKey:"test",curatedMinCosine:0.7},"What is the Decision Circle in PULSE?"),null);
});

test("extractive evidence is literal, brief and linked to its source", () => {
  const ranked = [
    {path:"docs/learn/example.md", heading:"Usar datos", url:"https://github.com/example#L20-L24",
      cosine:0.85, text:"Para seleccionar una arquitectura, identifica la decisión que cambia y sus restricciones.\\nLa calidad de los datos se comprueba mediante el origen documentado y su definición."},
    {path:"docs/governance/example.md",heading:"Plataforma",cosine:0.42,
      text:"El repositorio utiliza GitHub Actions para publicar la plataforma de documentación."}
  ];
  const result = extractEvidence(ranked,"¿Cómo seleccionar una arquitectura de datos?",3);
  assert.ok(result.length >= 2);
  assert.equal(result[0].item.path,"docs/learn/example.md");
  for (const part of result) {
    assert.ok(part.item.text.includes(part.excerpt));
    assert.ok(part.excerpt.length <= 420);
  }
});
