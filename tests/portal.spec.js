const { test, expect } = require("@playwright/test");
const AxeBuilder = require("@axe-core/playwright").default;

const representativePages = [
  { name: "home", path: "/" },
  {
    name: "governance",
    path: "/governance/architecture/",
    accessibilityPath: "/governance/",
    fullPage: false,
  },
  { name: "research", path: "/research/" },
  { name: "practice-lab", path: "/practice-lab/" },
];

const foundationalPages = [
  { name: "constitution", path: "/00-foundation/constitution/" },
  { name: "cdi-scope", path: "/00-foundation/cdi-scope-boundaries/" },
  { name: "glossary", path: "/00-foundation/glossary/" },
  { name: "domain-map", path: "/00-foundation/domain-map/" },
  { name: "pulse-spec", path: "/03-pulse/specification/" },
];

async function stabilizeExternalAssets(page) {
  await page.route("**/IgraSans.woff2", (route) => route.abort());
}

for (const theme of ["light", "dark"]) {
  for (const pageCase of representativePages) {
    test(`${pageCase.name} · ${theme}`, async ({ page }) => {
      await stabilizeExternalAssets(page);
      await page.emulateMedia({ colorScheme: theme, reducedMotion: "reduce" });
      await page.goto(pageCase.path, { waitUntil: "domcontentloaded" });
      await expect(page.locator("main h1")).toBeVisible();
      await expect(page).toHaveScreenshot(`${pageCase.name}-${theme}.png`, {
        fullPage: pageCase.fullPage !== false,
      });
    });
  }
}

for (const pageCase of representativePages) {
  test(`${pageCase.name} · WCAG 2.2 AA automated rules`, async ({ page }, testInfo) => {
    test.skip(testInfo.project.name !== "desktop-chromium", "One viewport is sufficient for the automated rule set.");
    await stabilizeExternalAssets(page);
    await page.emulateMedia({ colorScheme: "light", reducedMotion: "reduce" });
    await page.goto(pageCase.accessibilityPath || pageCase.path, { waitUntil: "domcontentloaded" });
    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"])
      .analyze();
    expect(results.violations).toEqual([]);
  });
}

for (const pageCase of foundationalPages) {
  test(`${pageCase.name} · foundational semantics`, async ({ page }, testInfo) => {
    test.skip(testInfo.project.name !== "desktop-chromium", "One viewport is sufficient for semantic and automated accessibility checks.");
    await stabilizeExternalAssets(page);
    await page.emulateMedia({ colorScheme: "light", reducedMotion: "reduce" });
    await page.goto(pageCase.path, { waitUntil: "domcontentloaded" });
    await expect(page.locator("main h1")).toBeVisible();
    await expect(page.locator("main article")).toContainText(/CDI|PULSE|decisi/i);
    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"])
      .analyze();
    expect(results.violations).toEqual([]);
  });
}
