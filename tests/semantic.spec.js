const { test, expect } = require("@playwright/test");

test("Node and browser produce equivalent local q8 E5 embeddings, without remote requests", async ({ page }, testInfo) => {
  test.skip(testInfo.project.name.includes("mobile"), "Mobile first-load and accessibility are covered by the Ask widget tests.");
  test.setTimeout(240000);
  await page.addInitScript(() => localStorage.setItem("/.__consent", "{}"));
  const external = [];
  page.on("request", (request) => {
    if (new URL(request.url()).origin !== "http://127.0.0.1:8000") external.push(request.url());
  });
  await page.goto("/ask-cdi/");
  await page.waitForLoadState("networkidle");
  // Existing theme assets may load during navigation; audit only the actual query.
  external.length = 0;
  const parity = await page.evaluate(async () => {
    const index = await (await fetch("/assets/semantic/index-es.json")).json();
    const { embedQuestion } = await import("/assets/semantic/embed.mjs");
    const { dot } = await import("/assets/semantic/retrieval.mjs");
    const vector = await embedQuestion("What is PULSE?", new URL("/", location.origin));
    return { cosine: dot(vector, index.reference), dimension: vector.length,
      revision: index.modelKey, sha: index.sourceSha };
  });
  expect(parity.dimension).toBe(384);
  expect(parity.cosine).toBeGreaterThan(0.995);
  expect(parity.revision).toContain("multilingual-e5-small");
  expect(parity.sha).toMatch(/^[0-9a-f]{40}$/);
  expect(external).toEqual([]);
});

test("project Pages paths resolve model and index under prefix, not origin root", () => {
  const origin = "https://example.github.io";
  const base = new URL("/conversational-decision-intelligence-bok/", origin);
  expect(new URL("assets/semantic/index-es.json", base).pathname)
    .toBe("/conversational-decision-intelligence-bok/assets/semantic/index-es.json");
});
