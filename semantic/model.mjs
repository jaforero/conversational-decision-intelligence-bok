export const MODEL = "Xenova/multilingual-e5-small";
export const REVISION = "761b726";
export const DTYPE = "q8";
export const DIM = 384;
export const MODEL_KEY = MODEL + "@" + REVISION + ":" + DTYPE + ":mean-l2:v1";
export const ASSETS = "assets/semantic/";
export function normalizedVector(data) {
  const result = Array.from(data);
  if (result.length !== DIM || !result.every(Number.isFinite)) {
    throw new Error("Invalid 384-dimensional embedding");
  }
  const length = Math.hypot(...result);
  if (!length || !Number.isFinite(length)) throw new Error("Zero embedding");
  return result.map((v) => v / length);
}
export function embedText(value, mode) {
  if (mode !== "query" && mode !== "passage") throw new Error("Invalid E5 prefix");
  return mode + ": " + value.replace(/\s+/g, " ").trim().slice(0, 1100);
}
