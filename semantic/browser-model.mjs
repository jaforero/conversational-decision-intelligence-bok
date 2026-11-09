import { env, pipeline } from "@huggingface/transformers";
import { MODEL, DTYPE, DIM, embedText, normalizedVector } from "./model.mjs";
let pipePromise;
export function loadEmbedder(base) {
  if (!pipePromise) {
    env.allowRemoteModels = false;
    env.allowLocalModels = true;
    env.useBrowserCache = true;
    env.localModelPath = new URL("assets/semantic/models/", base).href;
    env.backends.onnx.wasm.wasmPaths = new URL("assets/semantic/ort/", base).href;
    env.backends.onnx.wasm.numThreads = 1;
    pipePromise = pipeline("feature-extraction", MODEL, { device: "wasm", dtype: DTYPE })
      .catch((error) => { pipePromise = null; throw error; });
  }
  return pipePromise;
}
export async function embedQuestion(question, base) {
  const pipe = await loadEmbedder(base);
  const output = await pipe(embedText(question, "query"), { pooling: "mean", normalize: true });
  if (output.data.length !== DIM) throw new Error("Unexpected query dimension");
  return normalizedVector(output.data);
}
