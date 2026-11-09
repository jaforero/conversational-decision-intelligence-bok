export const STOP = new Set(("a al algo algunas algunos ante bajo como con contra cual cuales cuando de del desde donde el ella ellos en entre era eran es esa ese eso esta estas este estos " +
 "hay la las le les lo los mas me mi mis muy no nos o para pero por porque que quien se sea ser si sin sobre son su sus un una unas unos y ya " +
 "a an and are as at be by can do does for from how in into is it of on or our the their there these this those to was were what when where which who why with would").split(/\s+/));
export function terms(text) {
  return text.normalize("NFD").replace(/\p{M}/gu, "").toLowerCase()
    .match(/[\p{L}\p{N}][\p{L}\p{N}_-]*/gu)?.filter((w) => w.length > 1 && !STOP.has(w)) || [];
}
export function buildLexicon(chunks) {
  const posting = {}, lengths = [];
  for (let i = 0; i < chunks.length; i++) {
    const words = terms(chunks[i].heading + " " + chunks[i].text);
    lengths.push(words.length);
    const tf = new Map();
    for (const word of words) tf.set(word, (tf.get(word) || 0) + 1);
    for (const [word, frequency] of tf) (posting[word] ||= []).push([i, frequency]);
  }
  return { posting, lengths, average: lengths.reduce((a,b) => a + b, 0) / Math.max(1,lengths.length) };
}
export function lexical(index, query) {
  const N = index.chunks.length, score = new Float64Array(N);
  for (const word of new Set(terms(query))) {
    const matches = index.lexicon.posting[word] || [];
    const idf = Math.log(1 + (N - matches.length + 0.5) / (matches.length + 0.5));
    for (const [i, tf] of matches) {
      const norm = tf + 1.2 * (0.25 + 0.75 * index.lexicon.lengths[i] / (index.lexicon.average || 1));
      score[i] += idf * tf * 2.2 / norm;
    }
  }
  return [...score].map((value, i) => ({ i, score: value })).filter((x) => x.score > 0).sort((a,b) => b.score - a.score);
}
export function dot(a, b) {
  if (a.length !== b.length) throw new Error("Embedding dimension mismatch");
  let result = 0;
  for (let i = 0; i < a.length; i++) result += a[i] * b[i];
  return result;
}
export function semantic(index, vector) {
  return index.chunks.map((chunk, i) => ({ i, score: dot(chunk.vector, vector) }))
    .sort((a, b) => b.score - a.score);
}
export function rank(index, query, vector, options = {}) {
  const topN = options.topN || 40, k = options.k || 60;
  const sem = semantic(index, vector), lex = lexical(index, query), fused = new Map();
  for (const [list, weight] of [[sem, options.semanticWeight ?? 1], [lex, options.lexicalWeight ?? 1]]) {
    list.slice(0, topN).forEach(({ i }, pos) => fused.set(i, (fused.get(i) || 0) + weight / (k + pos + 1)));
  }
  const bySem = new Map(sem.map((x) => [x.i, x.score]));
  const byLex = new Map(lex.map((x) => [x.i, x.score]));
  const ranked = [...fused].map(([i, score]) => ({...index.chunks[i], fusion: score,
    cosine: bySem.get(i), bm25: byLex.get(i) || 0}))
    .sort((a,b) => b.fusion - a.fusion).slice(0, options.limit || 5);
  return { ranked, sem, lex };
}
export function shouldAbstain(index, ranked, calibration) {
  if (!ranked.length || !calibration || calibration.modelKey !== index.modelKey) return true;
  return ranked[0].cosine < calibration.minCosine;
}
