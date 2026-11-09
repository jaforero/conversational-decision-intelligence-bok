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
      preparing: "Preparando búsqueda híbrida local. La primera consulta descarga aproximadamente 140 MB del modelo y tokenizer…",
      searching: "Buscando en los documentos con embeddings y BM25, sin enviar tu pregunta…",
      modelUnavailable: "La búsqueda semántica no está disponible en este navegador. Las respuestas editoriales siguen accesibles; no se ha sustituido silenciosamente por búsqueda textual.",
      semanticRelated: "Fragmentos recuperados por búsqueda híbrida · verifica las citas en GitHub.",
      semanticInsufficient: "No encontré información suficiente en los documentos para responder esta pregunta.",
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
      preparing: "Preparing local hybrid retrieval. The first query downloads approximately 140 MB of model assets…",
      searching: "Searching locally using embeddings and BM25. Your question is not transmitted…",
      modelUnavailable: "Semantic retrieval could not run in this browser. Editorial answers remain available; text search has not silently replaced semantics.",
      semanticRelated: "Hybrid search passages · verify the GitHub citations.",
      semanticInsufficient: "I could not find sufficient information in the documents to answer this question.",
    },
  };

  function append(parent, tag, text) {
    const element = document.createElement(tag);
    element.textContent = text;
    parent.append(element);
    return element;
  }

  function sourceUrl(source, language, base) {
    const url = new URL(source.replace(/^\//, ""), base);
    const relative = url.pathname.slice(base.pathname.length);
    if (url.origin !== location.origin || !url.hash || url.search ||
        !url.pathname.startsWith(base.pathname) ||
        relative.startsWith("en/") !== (language === "en")) {
      throw new Error("Invalid evidence link");
    }
    return url;
  }

  function excerptText(text) {
    return text.length <= 600 ? text : text.slice(0, 600).replace(/\s+\S*$/, "") + "…";
  }

  const indexes = new Map();
  function loadIndex(language, base) {
    const key = base.href + language;
    if (!indexes.has(key)) {
      indexes.set(key, fetch(new URL("assets/data/ask-cdi-" + language + ".json", base), { mode: "same-origin" })
        .then((response) => {
          if (!response.ok) throw new Error("Evidence index unavailable");
          return response.json();
        })
        .catch((error) => {
          indexes.delete(key);
          throw error;
        }));
    }
    return indexes.get(key);
  }

  const hybridCache = new Map();
  function loadHybrid(language, base) {
    const key = base.href + language;
    if (!hybridCache.has(key)) {
      const root = new URL("assets/semantic/", base);
      const loadJson = (filename) => fetch(new URL(filename, root), { mode: "same-origin" }).then((response) => {
        if (!response.ok) throw new Error("Missing static semantic index: " + filename);
        return response.json();
      });
      hybridCache.set(key, Promise.all([
        loadJson("index-" + language + ".json"),
        loadJson("calibration.json"),
        import(new URL("retrieval.mjs", root).href),
        import(new URL("embed.mjs", root).href),
      ]).then(([index, calibration, retrieval, embedding]) => {
        if (index.modelKey !== calibration.modelKey || index.dimension !== 384) {
          throw new Error("Model/index/calibration mismatch");
        }
        return { index, calibration, retrieval, embedding };
      }).catch((error) => {
        hybridCache.delete(key);
        throw error;
      }));
    }
    return hybridCache.get(key);
  }

  function highlight(parent, value, question) {
    const needles = [...new Set(normalize(question).split(" ").filter((v) => v.length > 3))]
      .filter((word) => /^[a-z0-9]+$/.test(word));
    if (!needles.length) { parent.textContent = value; return; }
    const regex = new RegExp("(" + needles.sort((a, b) => b.length - a.length).join("|") + ")", "gi");
    for (const piece of value.split(regex)) {
      if (needles.includes(piece.toLowerCase())) append(parent, "mark", piece);
      else parent.append(document.createTextNode(piece));
    }
  }

  function init(widget) {
    const language = widget.dataset.language === "en" ? "en" : "es";
    const configured = new URL(widget.dataset.siteUrl || location.origin + "/");
    const base = new URL(configured.pathname, location.origin);
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
    let requestId = 0;

    async function ask() {
      if (!search || input.value.trim().length < 3) return;
      const question = input.value.trim();
      const current = ++requestId;
      results.replaceChildren();
      const result = search(question);
      if (result.kind === "editorial") {
        status.textContent = copy.editorial;
        for (const item of result.items) {
          const url = sourceUrl(item.source, language, base);
          const article = append(results, "article", "");
          article.className = "cdi-ask-evidence";
          append(article, "blockquote", excerptText(item.excerpt));
          if (item.note || item.simulated) append(article, "p", item.note || copy.simulated);
          const link = append(article, "a", item.page + " · " + item.title);
          link.href = url.href;
          if (item.github_url && item.source_sha) {
            const original = append(article, "a", language === "en" ? " · Original Markdown at this commit" : " · Markdown original en este commit");
            original.href = item.github_url;
            original.target = "_blank";
            original.rel = "noopener noreferrer";
            append(article, "small", item.source_path + " · Commit SHA: " + item.source_sha);
          }
          append(article, "small", copy[item.status]);
        }
        return;
      }

      status.textContent = copy.preparing;
      submit.disabled = true;
      try {
        const local = await loadHybrid(language, base);
        status.textContent = copy.searching;
        const vector = await local.embedding.embedQuestion(question, base);
        if (current !== requestId) return;
        // Exact same E5 preprocessing, q8 weights, mean pooling and L2 normalization.
        if (local.retrieval.dot(vector, local.index.reference) > 1.01) {
          throw new Error("Inconsistent embedding dimensions");
        }
        const found = local.retrieval.rank(local.index, question, vector);
        const abstain = local.retrieval.shouldAbstain(local.index, found.ranked, local.calibration);
        status.textContent = abstain ? copy.semanticInsufficient : copy.semanticRelated;
        if (abstain) return;
        const usedPaths = new Set();
        for (const item of found.ranked) {
          if (usedPaths.has(item.path)) continue;
          usedPaths.add(item.path);
          const article = append(results, "article", "");
          article.className = "cdi-ask-evidence";
          const caption = append(article, "strong", item.page + " · " + item.heading);
          caption.className = "cdi-ask-section-title";
          const quote = append(article, "blockquote", "");
          highlight(quote, excerptText(item.text), question);
          if (item.simulated) append(article, "p", copy.simulated);
          const source = append(article, "a", language === "en" ? "Verify original Markdown" : "Verificar Markdown original");
          source.href = item.url;
          source.target = "_blank";
          source.rel = "noopener noreferrer";
          append(article, "small", item.path + " · L" + item.lineStart + "–L" + item.lineEnd);
          append(article, "small", "Commit SHA: " + local.index.sourceSha);
          append(article, "small", copy[item.status] || item.status);
        }
      } catch (error) {
        console.error("Local semantic retrieval failed:", error);
        if (current === requestId) status.textContent = copy.modelUnavailable;
      } finally {
        if (current === requestId) submit.disabled = false;
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
          index = await loadIndex(language, base);
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
