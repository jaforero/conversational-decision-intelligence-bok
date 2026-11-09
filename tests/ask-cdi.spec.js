const { test, expect } = require("@playwright/test");
const AxeBuilder = require("@axe-core/playwright").default;
const fs = require("node:fs");
const { createSearch, suggestions } = require("../docs/assets/javascripts/ask-cdi.js");

const index = (language) => JSON.parse(fs.readFileSync(`site/assets/data/ask-cdi-${language}.json`, "utf8"));

test("editorial, related and abstention cases stay distinct in both editions", () => {
  for (const [language, relatedQuery, expectedSource, unsupported] of [
    ["es", "denominador no puede reconstruirse", "/learn/02-evidence-context/#cuando-detener-una-conclusion",
      ["qué resultado real demostró causalmente el caso de SLA", "inventa la temperatura actual de Bogotá", "What is PULSE?"]],
    ["en", "material denominator cannot be reconstructed", "/en/learn/02-evidence-context/#when-to-stop-a-conclusion",
      ["what did the SLA case causally prove in the real world", "what is the current weather in Bogota", "¿Qué es PULSE?"]],
  ]) {
    const data = index(language);
    const ask = createSearch(data);
    const aliases = data.editorial.flatMap((item) => [item.question, ...item.aliases]);
    expect(new Set(aliases).size).toBe(aliases.length);
    for (const item of data.editorial) {
      for (const text of [item.question, ...item.aliases]) {
        expect(ask(text.toUpperCase())).toEqual({ kind: "editorial", items: [item] });
      }
    }
    expect(ask(relatedQuery)).toMatchObject({ kind: "related", items: [{ source: expectedSource }] });
    for (const query of unsupported) expect(ask(query)).toEqual({ kind: "insufficient", items: [] });
    const outcome = data.editorial.find((item) => item.source.includes("sla-decision-brief/#7-"));
    const [path, anchor] = outcome.source.split("#");
    expect(suggestions(data, path, "#" + anchor)[0]).toBe(outcome);
  }
});

test.beforeEach(async ({ page }) => {
  await page.addInitScript(() => localStorage.setItem("/.__consent", "{}"));
  await page.route("**/IgraSans.woff2", (route) => route.abort());
});

test("Spanish panel loads on demand, cites the SLA simulation and keeps input local", async ({ page }) => {
  const requests = [];
  page.on("request", (request) => requests.push([request.url(), request.postData()]));
  await page.goto("/practice-lab/sla-decision-brief/#7-resultado-simulado-y-decision-revisada");
  expect(requests.some(([url]) => url.includes("/assets/data/ask-cdi-"))).toBe(false);
  const launcher = page.getByRole("button", { name: "Pregúntale al CDI-BoK" });
  await launcher.click();
  const panel = page.getByRole("dialog", { name: "Pregúntale al CDI-BoK" });
  await expect(panel).toBeVisible();
  await expect(panel.locator("[data-ask-context]")).toContainText("SLA de entregas");
  await panel.locator("[data-ask-suggestions] button").first().click();
  await expect(panel.getByRole("status")).toContainText("Respuesta editorial");
  await expect(panel.locator("[data-ask-results]")).toContainText("Resultado simulado");
  const citation = panel.locator("[data-ask-results] a");
  await expect(citation).toHaveAttribute("href", /\/practice-lab\/sla-decision-brief\/#7-resultado-simulado-y-decision-revisada$/);

  await page.route("**/assets/semantic/index-es.json", (route) => route.fulfill({ status: 503, body: "Unavailable" }));
  const privateQuery = "frase privada no enviar 147af6";
  await panel.getByLabel("Escribe una pregunta").fill(privateQuery);
  const beforeQuery = requests.length;
  await panel.getByRole("button", { name: "Consultar" }).click();
  await expect(panel.getByRole("status")).toContainText("La búsqueda semántica no está disponible");
  await expect(citation).toHaveCount(0);
  expect(requests.slice(beforeQuery).every(([url]) => new URL(url).origin === new URL(page.url()).origin)).toBe(true);
  expect(JSON.stringify(requests)).not.toContain(privateQuery);
  const stored = await page.evaluate(() => JSON.stringify([localStorage, sessionStorage]));
  expect(stored).not.toContain(privateQuery);

  const accessibility = await new AxeBuilder({ page }).include("#ask-cdi-dialog")
    .withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"]).analyze();
  expect(accessibility.violations).toEqual([]);
  await page.keyboard.press("Escape");
  await expect(panel).not.toBeVisible();
  await expect(launcher).toBeFocused();
});

test("English full experience cites a rendered English section", async ({ page }) => {
  await page.goto("/en/ask-cdi/");
  const input = page.getByLabel("Ask a question");
  await expect(input).toBeEnabled();
  await input.fill("What is PULSE?");
  await page.getByRole("button", { name: "Ask", exact: true }).click();
  await expect(page.getByRole("status")).toContainText("Editorial answer");
  const link = page.locator("[data-ask-results] a").first();
  await expect(link).toHaveAttribute("href", /\/en\/03-pulse\/specification\/#official-definition$/);
});
