import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { env, pipeline } from "@huggingface/transformers";
import { MODEL, MODEL_KEY, DTYPE, embedText, normalizedVector } from "./model.mjs";
import { rank, lexical } from "./retrieval.mjs";
import { curatedCandidates } from "./answers.mjs";

const base = path.resolve("site/assets/semantic");
const fixtures = JSON.parse(await readFile("semantic/evaluation-questions.json", "utf8"));
const indexes = {};
for (const lang of ["es", "en"]) {
  indexes[lang] = JSON.parse(await readFile(path.join(base, "index-" + lang + ".json"), "utf8"));
  if (indexes[lang].modelKey !== MODEL_KEY) throw new Error("Evaluation/index model mismatch");
}
env.allowRemoteModels = false;
env.allowLocalModels = true;
env.localModelPath = path.join(base, "models") + path.sep;
const extractor = await pipeline("feature-extraction", MODEL, { dtype: DTYPE, device: "cpu" });
const observations = [];
for (const fixture of fixtures) {
  const started = performance.now();
  const output = await extractor(embedText(fixture.question, "query"), { pooling: "mean", normalize: true });
  const vector = normalizedVector(output.data);
  const index = indexes[fixture.lang];
  const fused = rank(index, fixture.question, vector);
  const lex = lexical(index, fixture.question);
    const curated = curatedCandidates(index, vector)[0];
  observations.push({ ...fixture,
    curatedScore: curated?.similarity ?? -1, curatedSource: curated?.item.source ?? null,
    durationMs: performance.now() - started,
    score: fused.ranked[0]?.cosine ?? -1,
    bm25Hit: fixture.path ? lex.slice(0, 5).some((x) => index.chunks[x.i].path === fixture.path) : null,
    hybridHit: fixture.path ? fused.ranked.some((x) => x.path === fixture.path) : null,
    bestPath: fused.ranked[0]?.path || null });
}
const train = observations.filter((x) => x.split === "train");
if (train.filter((x) => !x.path).length < 2 || train.filter((x) => x.path).length < 2)
  throw new Error("Calibration needs positive and unsupported questions");
const scores = [...new Set(train.map((x) => x.score))].sort((a,b) => a-b);
const candidates = [scores[0] - 0.000001, ...scores.slice(1).map((v,i) => (v+scores[i])/2),
  scores.at(-1) + 0.000001];
const balanced = (threshold) => {
  const positives = train.filter((x) => x.path), negatives = train.filter((x) => !x.path);
  const tpr = positives.filter((x) => x.score >= threshold).length / positives.length;
  const tnr = negatives.filter((x) => x.score < threshold).length / negatives.length;
  return { value: (tpr + tnr)/2, tpr, tnr };
};
const choice = candidates.map((threshold) => ({ threshold, ...balanced(threshold) }))
  .sort((a,b) => b.value-a.value || b.tnr-a.tnr || b.threshold-a.threshold)[0];
// Calibrate answer-card routing separately from passage abstention.
const curatedScores = [...new Set(train.map((x) => x.curatedScore))].sort((a,b) => a-b);
const curatedCandidatesThresholds = [curatedScores[0] - 0.000001,
  ...curatedScores.slice(1).map((v,i) => (v+curatedScores[i])/2), curatedScores.at(-1)+0.000001];
const curatedPositives = train.filter((x) => x.curatedExpected);
const curatedNegatives = train.filter((x) => !x.curatedExpected);
if (curatedPositives.length < 2 || curatedNegatives.length < 2) {
  throw new Error("Curated answer calibration requires positive and negative questions");
}
const curatedChoice = curatedCandidatesThresholds.map((threshold) => ({
  threshold,
  tpr: curatedPositives.filter((x) => x.curatedScore >= threshold &&
    x.curatedSource === x.curatedExpected).length / curatedPositives.length,
  tnr: curatedNegatives.filter((x) => x.curatedScore < threshold).length / curatedNegatives.length
})).map((x) => ({...x, value:(x.tpr+x.tnr)/2}))
  .sort((a,b) => b.value-a.value || b.tnr-a.tnr || b.threshold-a.threshold)[0];
const calibration = { format: 2, modelKey: MODEL_KEY, minCosine: choice.threshold,
  curatedMinCosine: curatedChoice.threshold,
  method: "Maximize balanced accuracy on declared training examples; ties prefer specificity",
  trainCount: train.length, testCount: observations.length - train.length };
await writeFile(path.join(base, "calibration.json"), JSON.stringify(calibration));
const summarize = (part) => {
  const positive = part.filter((x) => x.path), negative = part.filter((x) => !x.path);
  const rate = (n, d) => d ? n/d : null;
  return { questions: part.length, answerable: positive.length, unsupported: negative.length,
    recall5BM25: rate(positive.filter((x) => x.bm25Hit).length, positive.length),
    recall5Hybrid: rate(positive.filter((x) => x.hybridHit).length, positive.length),
    abstentionAccuracy: rate(negative.filter((x) => x.score < choice.threshold).length, negative.length),
    answerableCoverage: rate(positive.filter((x) => x.score >= choice.threshold).length, positive.length),
    meanEmbeddingMs: rate(part.reduce((s,x) => s + x.durationMs,0),part.length),
    curatedAnswerAccuracy: rate(part.filter((x) =>
      (x.curatedScore >= curatedChoice.threshold ? x.curatedSource : null) ===
      (x.curatedExpected || null)).length, part.length) };
};
const result = { note: "Small, hand-authored evaluation set. Not a population estimate; review the held-out split.",
  modelKey: MODEL_KEY, calibration, train: summarize(train),
  heldOut: summarize(observations.filter((x) => x.split === "test")),
  samples: observations.map((x) => ({ question: x.question, expectedPath: x.path,
    split: x.split, bestPath: x.bestPath, cosine: Number(x.score.toFixed(5)),
    bm25Hit: x.bm25Hit, hybridHit: x.hybridHit,
    curatedExpected: x.curatedExpected || null, curatedSource: x.curatedSource,
    curatedScore: Number(x.curatedScore.toFixed(5)) })) };
await writeFile(path.join(base, "evaluation.json"), JSON.stringify(result, null, 2));
console.log("Held-out evaluation: " + JSON.stringify(result.heldOut));
if (extractor.dispose) await extractor.dispose();
