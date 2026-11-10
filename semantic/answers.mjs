// Pure, browser-safe answer selection. No text generation or external calls.
export function dotVectors(a, b) {
  if (!a || !b || a.length !== b.length) throw new Error("Incompatible answer embeddings");
  let sum = 0;
  for (let i = 0; i < a.length; i++) sum += a[i] * b[i];
  return sum;
}
export function curatedCandidates(index, vector) {
  return (index.curated || [])
    .map((item) => ({
      item,
      similarity: Math.max(...(item.vectors || [item.vector]).map((candidate) =>
        dotVectors(candidate, vector))),
    }))
    .sort((a,b) => b.similarity - a.similarity);
}
// Reject a generic editorial answer when the question names a more specific
// title-cased concept absent from its evidence (e.g. "Decision Circle" vs PULSE).
// This is a narrow guard; ordinary semantic paraphrases remain supported.
export function matchesNamedConcept(question, item) {
  const named = String(question).match(/\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,})+\b/g) || [];
  if (!named.length) return true;
  const plain = (value) => String(value).normalize("NFD").replace(/\p{M}/gu, "")
    .toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
  const corpus = plain([item.question, ...(item.aliases || []), item.answer || "",
    ...(item.bullets || []), item.excerpt || ""].join(" "));
  return named.every((phrase) => corpus.includes(plain(phrase)));
}
export function matchCurated(index, vector, calibration, question = "") {
  if (!calibration || index.modelKey !== calibration.modelKey ||
      !Number.isFinite(calibration.curatedMinCosine)) return null;
  const first = curatedCandidates(index, vector)[0];
  return first && first.similarity >= calibration.curatedMinCosine &&
    matchesNamedConcept(question, first.item) ? first.item : null;
}
// A fallback is a literal, unmodified source quotation, never a synthesized answer.
// Keep only one substantive paragraph; the reader can expand full evidence below.
export function extractPassage(ranked) {
  const item = (ranked || []).find((x) => x.text && x.text.trim().length >= 35);
  if (!item) return null;
  const paragraphs = item.text.split(/\n+/).map((x) => x.trim()).filter(Boolean);
  const value = paragraphs.find((x) => x.length >= 35 && !x.startsWith("|")) || paragraphs[0];
  const excerpt = value.length <= 480 ? value :
    value.slice(0, 480).replace(/\s+\S*$/, "") + "…";
  return { excerpt, item };
}
