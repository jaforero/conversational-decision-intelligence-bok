# Local hybrid search for Ask the CDI-BoK

Status: **candidate engineering feature**. This does not modify the normative PULSE DNA, definitions, approved releases or editorial authority.

## What it actually does

The public CDI-BoK uses MkDocs Material with Spanish/English Markdown under docs/. The existing curated "Ask the CDI-BoK" answers remain in place. Questions outside the curated answers use **two local retrieval channels**:

1. multilingual-e5-small, 384-dimensional cosine nearest neighbors over Markdown chunks;
2. a published BM25 posting index for technical terms, codes, and names.

The top 40 results from each channel are combined by reciprocal rank fusion (RRF, k=60); default weights 1:1. No LLM is loaded and the extracts are **not synthesized answers**. Citations link to the exact committed Markdown file and line range. Editorial status and simulated cases remain labeled.

This index deliberately covers the *publicly published* bilingual docs/ corpus (approved/candidate pages). Sources under sources/constitutional/, private drafts and governance registries are not silently promoted to reader-facing evidence. No authoring Markdown is modified by indexing. To include those other repositories of text, first make an explicit editorial scope decision.

## Model and licensing

- Base: intfloat/multilingual-e5-small (MIT), ONNX conversion: Xenova/multilingual-e5-small.
- Pinned conversion revision: 761b726; quantization: q8/model_quantized.onnx (118 MB; SHA256 enforced).
- Transformers.js 3.8.1 in both Node and browser. The same E5 query: / passage: prefixes, mean pooling, L2 normalization and 384 dimensions are used on both sides.
- Runtime files (ONNX, tokenizer, config, WASM, compiled JS) are copied into the GitHub Pages artifact by Actions. They are **not served from Hugging Face during a user's query**. Build-time downloads use Hugging Face and npm and therefore require outbound network *during CI only*.
- License provenance should be rechecked whenever upgrading model or conversion. Do not replace revision or dtype without invalidating the cache and repeating the browser parity test.

## Build and update

GitHub Actions on main runs the existing MkDocs release preflight, then:

    npm install --prefix semantic --no-package-lock --no-audit --no-fund
    node --test semantic/tests.mjs
    node semantic/download-model.mjs
    node semantic/index.mjs
    node semantic/evaluate.mjs
    node semantic/build.mjs
    node semantic/validate.mjs

Indexing uses Markdown structure, SHA256 hashes of chunks and a model-versioned incremental cache (.semantic-cache/). Cached vectors are reused if and only if their text and model signature agree. Deleted documents disappear from the newly generated manifest. Corrupted/missing cache entries are recomputed; the index is only uploaded to Pages after all validation gates pass. No cache is a correctness dependency.

To reconstruct completely: run **Deploy CDI-BoK to GitHub Pages → Run workflow** on main; remove the saved Actions cache beforehand to force embeddings regeneration. Workflow dispatch also works after a cache miss.

The deployed assets are under /assets/semantic/ in the custom domain and under <repo-prefix>/assets/semantic/ on project Pages. The UI resolves these URLs using the configured site URL path and the current browser origin. All inference and scoring run on the visitor's device.

## Evaluation and abstention

The file evaluation-questions.json supplies 20 documented bilingual prompts, both answerable and unsupported, labeled train/test. evaluate.mjs chooses the cosine abstention threshold by maximizing balanced accuracy on the train portion (with tie-breaks favoring specificity), then publishes observed BM25 Recall@5, hybrid Recall@5, correct abstentions and query-embedding latency for the held-out portion in evaluation.json. The small hand-picked sample and reused domains **are insufficient to claim population-level accuracy**. Errors must be inspected and the evaluation expanded with independent questions before calling the search reliable.

The abstention does not establish lack of information in the world; only lack of sufficiently supported evidence in this corpus. RRF score itself cannot be read as a calibrated probability. If calibration is missing or incompatible, the system abstains instead of inventing a relevance cutoff.

## Production limits and costs

At 2026-11-09 GitHub Pages imposes a 1 GB published site limit, a soft 100 GB/month bandwidth limit and a 10-minute deployment timeout. GitHub Actions' standard hosted runners are free for public repositories; larger runners and some storage uses are not free. The q8 model alone is approximately 118 MB, tokenizer approximately 17 MB, plus WASM and site files. First-visit download costs user bandwidth, storage and latency, especially on iOS. Model and file caching reduce repeated requests but do not guarantee zero transfer on every visit. Site build fails if artifact grows beyond 900 MiB.

Operating monetary cost is USD 0 **under current free public-repository rules and within practical service limits**, not unlimited capacity. A public educational docs site is the intended workload; review GitHub Pages' restrictions on commercial SaaS hosting.

The site currently offers optional Google Analytics subject to consent. That pre-existing integration is outside the retrieval engine; to guarantee absolutely no third-party requests on an entire browser session, disable analytics for the Ask page too and audit the surrounding MkDocs theme and external media. The search code does not send or store queries.

## Main risks and recovery

- First semantic query is a large download: show on-demand status and cache the model, keep curated answers immediate.
- Older phones may run out of memory: disclose local model initialization failure and do not secretly fall back to lexical-only search.
- Quantization differs between browser/Node: compare reference embeddings in a browser against the index, and block release on mismatch.
- Semantic matches can be topically plausible but fail to answer: every excerpt is labeled and linked to the exact source; abstain if empirical gate rejects.
- Operational failures: last published Pages artifact is not replaced unless Actions succeeds. On a failed release, inspect CI logs, resolve, and re-run.
