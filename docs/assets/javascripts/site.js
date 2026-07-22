(function () {
  "use strict";

  const themeMeta = document.querySelector('meta[name="theme-color"]');

  function updateThemeColor() {
    if (!themeMeta) return;
    const scheme = document.body.getAttribute("data-md-color-scheme");
    themeMeta.setAttribute("content", scheme === "slate" ? "#041c59" : "#4e00ff");
  }

  updateThemeColor();

  const observer = new MutationObserver(updateThemeColor);
  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"]
  });

  const searchInput = document.querySelector(".md-search__input");
  if (searchInput) {
    const isEnglish = document.documentElement.lang.toLowerCase().startsWith("en");
    const label = isEnglish ? "Search in English" : "Buscar en español";
    searchInput.setAttribute("aria-label", label);
    searchInput.setAttribute("placeholder", label);
  }
})();
