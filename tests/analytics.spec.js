const { test, expect } = require("@playwright/test");

const site = "https://decision.javierforero.co";
const measurementId = "G-MQ3K8EVKV0";
const tagUrl = `https://www.googletagmanager.com/gtag/js?id=${measurementId}`;

test("GA4 follows consent across languages and omits URL queries", async ({ page, baseURL }) => {
  await page.route(`${site}/**`, async (route) => {
    const url = new URL(route.request().url());
    const response = await route.fetch({ url: baseURL + url.pathname + url.search });
    await route.fulfill({ response });
  });
  await page.route(tagUrl, (route) => route.fulfill({
    contentType: "application/javascript",
    body: "/* Analytics stub. No requests leave the browser test. */",
  }));

  const consent = page.locator("form[name=consent]");
  const tag = page.locator("#cdi-ga4-tag");
  const reject = consent.locator("button[type=reset]");
  const accept = consent.locator("button:not([type=reset])");

  await page.goto(`${site}/en/about/?example=omit-me`);
  await expect(consent).toBeVisible();
  await expect(consent).toContainText("Optional analytics");
  await expect(tag).toHaveCount(0);

  await reject.click();
  await expect(consent).toBeHidden();
  await expect(tag).toHaveCount(0);

  await page.getByRole("link", { name: "Change analytics preferences" }).click();
  await expect(consent).toBeVisible();
  await consent.locator('label[for="__settings"]').click();
  await consent.locator('input[name="analytics"]').check();
  await Promise.all([page.waitForRequest(tagUrl), accept.click()]);
  await expect(tag).toHaveAttribute("src", tagUrl);

  const commands = await page.evaluate(() => window.dataLayer.map((entry) => Array.from(entry)));
  expect(commands.filter(([command]) => command === "event")).toEqual([["event", "page_view"]]);
  expect(commands.find(([command]) => command === "config")).toEqual([
    "config",
    measurementId,
    expect.objectContaining({
      send_page_view: false,
      page_location: `${site}/en/about/`,
      page_referrer: expect.not.stringContaining("?"),
    }),
  ]);

  await page.goto(`${site}/about/`);
  await expect(tag).toHaveCount(1);
  await expect(consent).toBeHidden();

  await page.getByRole("link", { name: "Cambiar preferencias de medición" }).click();
  await expect(consent).toContainText("Medición opcional");
  await reject.click();
  await expect(consent).toBeHidden();
  await expect(tag).toHaveCount(0);
});

test("GA4 does not load on a local preview even with saved consent", async ({ page }) => {
  await page.addInitScript(() => localStorage.setItem("/.__consent", '{"analytics":true}'));
  await page.goto("/");
  await expect(page.locator("#cdi-ga4-tag")).toHaveCount(0);
});
