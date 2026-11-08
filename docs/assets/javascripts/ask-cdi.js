(() => {
  "use strict";

  const normalize = (value) => value.normalize("NFD")
    .replace(/\p{M}/gu, "").toLowerCase().replace(/[^\p{L}\p{N}]+/gu, " ").trim();

  const stop = new Set(("a al algo algun como con cual cuales cuando de del donde el en es esta estan " +
    "esto hay la las lo los mas me mi para por porque puede puedo que quien se si sin sobre su un una unos " +
    "y and are as at be by can could do does for from had has have how i in is it me of on or our should " +
    "so than that the their there these this to was were what when where which who why will with would you").split(" "));
  const tokens = (value) => new Set(normalize(value).split(" ")
    .filter((word) => word.length >= 3 && !stop.has(word))
    .map((word) => word.length > 5 ? word.replace(/s$/, "") : word));

  function createSearch(index) {
    const editorial = new Map();
    for (const item of index.editorial) {
      for (const text of [item.question, ...item.aliases]) editorial.set(normalize(text), item);
    }

    const passages = index.sections.flatMap((section) =>
      section.passages.map((excerpt) => ({ section, excerpt, words: tokens(excerpt) }))
    );
    const sectionCount = new Map();
    for (const section of index.sections) {
      for (const word of tokens(section.passages.join(" "))) {
        sectionCount.set(word, (sectionCount.get(word) || 0) + 1);
      }
    }

    return (question) => {
      if (question.length > 240) return { kind: "insufficient", items: [] };
      const match = editorial.get(normalize(question));
      if (match) return { kind: "editorial", items: [match] };

      const query = [...tokens(question)];
      if (query.length < 2) return { kind: "insufficient", items: [] };
      const minimum = Math.ceil(0.8 * query.length);
      const ranked = new Map();
      for (const { section, excerpt, words } of passages) {
        const overlap = query.filter((word) => words.has(word));
        if (overlap.length < minimum) continue;
        // An uncommon term is more informative than one repeated throughout the book.
        const relevance = overlap.reduce((score, word) =>
          score + Math.log1p(index.sections.length / sectionCount.get(word)), 0);
        const score = relevance / Math.log2(words.size + 2);
        if (score > (ranked.get(section.source)?.score || 0)) {
          ranked.set(section.source, { ...section, excerpt, score });
        }
      }
      const items = [...ranked.values()].sort((a, b) => b.score - a.score).slice(0, 3);
      return { kind: items.length ? "related" : "insufficient", items };
    };
  }

  function suggestions(index, path, anchor = "") {
    const relevance = (item) => item.source === path + anchor ? 2 : item.source.split("#")[0] === path ? 1 : 0;
    return [...index.editorial].sort((a, b) => relevance(b) - relevance(a)).slice(0, 3);
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { createSearch, suggestions };
    return;
  }

  const messages = {
    es: {
      loading: "Cargando el índice de apartados publicados…",
      unavailable: "El índice no pudo cargarse. Vuelve a abrir el panel o recarga la página para reintentar.",
      editorial: "Respuesta editorial · extracto de la fuente",
      related: "Pasajes relacionados · comprueba si responden tu pregunta.",
      insufficient: "No encontré evidencia suficiente en esta edición. Reformula con términos más concretos o elige una pregunta sugerida.",
      candidate: "Estado editorial de la fuente: candidato",
      approved: "Estado editorial de la fuente: aprobado",
      simulated: "Caso simulado.",
      context: "Leyendo:",
    },
    en: {
      loading: "Loading the published section index…",
      unavailable: "The index could not be loaded. Reopen the panel or reload the page to retry.",
      editorial: "Editorial answer · source excerpt",
      related: "Related passages · check whether they answer your question.",
      insufficient: "I found insufficient evidence in this edition. Try more specific terms or select a suggested question.",
      candidate: "Source editorial status: candidate",
      approved: "Source editorial status: approved",
      simulated: "Simulated case.",
      context: "Reading:",
    },
  };

  function append(parent, tag, text) {
    const element = document.createElement(tag);
    element.textContent = text;
    parent.append(element);
    return element;
  }

  function sourceUrl(source, language) {
    const url = new URL(source, location.origin);
    if (url.origin !== location.origin || !url.hash || url.search ||
        url.pathname.startsWith("/en/") !== (language === "en")) {
      throw new Error("Invalid evidence link");
    }
    return url;
  }

  function excerptText(text) {
    return text.length <= 600 ? text : text.slice(0, 600).replace(/\s+\S*$/, "") + "…";
  }

  const indexes = new Map();
  function loadIndex(language) {
    if (!indexes.has(language)) {
      indexes.set(language, fetch(`/assets/data/ask-cdi-${language}.json`, { mode: "same-origin" })
        .then((response) => {
          if (!response.ok) throw new Error("Evidence index unavailable");
          return response.json();
        })
        .catch((error) => {
          indexes.delete(language);
          throw error;
        }));
    }
    return indexes.get(language);
  }

  function init(widget) {
    const language = widget.dataset.language === "en" ? "en" : "es";
    const copy = messages[language];
    const form = widget.querySelector("form");
    const input = form.querySelector("input");
    const submit = form.querySelector('button[type="submit"]');
    const status = widget.querySelector("[data-ask-status]");
    const results = widget.querySelector("[data-ask-results]");
    const prompts = widget.querySelector("[data-ask-suggestions]");
    const context = widget.querySelector("[data-ask-context]");
    const dialog = widget.closest("dialog");
    let index;
    let search;

    function ask() {
      if (!search || input.value.trim().length < 3) return;
      results.replaceChildren();
      const result = search(input.value.trim());
      status.textContent = copy[result.kind];
      for (const item of result.items) {
        const url = sourceUrl(item.source, language);
        const article = append(results, "article", "");
        article.className = "cdi-ask-evidence";
        append(article, "blockquote", excerptText(item.excerpt));
        if (item.note || item.simulated) append(article, "p", item.note || copy.simulated);
        const link = append(article, "a", `${item.page} · ${item.title}`);
        link.href = url.href;
        append(article, "small", copy[item.status]);
      }
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      ask();
    });

    async function activate() {
      if (!index) {
        status.textContent = copy.loading;
        try {
          index = await loadIndex(language);
          search = createSearch(index);
        } catch {
          status.textContent = copy.unavailable;
          return;
        }
        status.textContent = "";
        input.disabled = false;
        submit.disabled = false;
      }

      if (dialog) {
        const title = document.querySelector("main h1")?.textContent.replace(/¶\s*$/, "").trim();
        context.hidden = !title;
        if (title) context.textContent = `${copy.context} ${title}`;
      }

      prompts.replaceChildren();
      for (const item of suggestions(index, location.pathname, location.hash)) {
        const prompt = append(prompts, "button", item.question);
        prompt.type = "button";
        prompt.addEventListener("click", () => {
          input.value = item.question;
          ask();
        });
      }
      if (dialog?.open) input.focus();
    }

    if (dialog) {
      const launcher = document.querySelector("[data-ask-launcher]");
      launcher.hidden = false;
      launcher.addEventListener("click", () => {
        dialog.showModal();
        activate();
      });
    } else {
      activate();
    }
  }

  document.querySelectorAll("[data-ask-cdi]").forEach(init);
})();
