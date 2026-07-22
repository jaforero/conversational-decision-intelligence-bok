---
id: ADR-027
title: Promoción estable del parche de localización y búsqueda v0.8.2
status: accepted
date: 2026-07-22
decider: Javier Forero
domains: [Decision Governance, Publication Architecture, Localization]
---

# ADR-027: Promoción estable del parche de localización y búsqueda v0.8.2

## Contexto

Después de publicar `v0.8.1`, la revisión del portal encontró etiquetas inglesas visibles en la edición española, un tooltip sin localizar, una propuesta de valor demasiado técnica y un índice de búsqueda compartido entre idiomas. El PR #15 corrigió estas brechas y se fusionó en `main` como `1f81e2ad26b42da4959744733ad8261dfd188f81`, después de aprobar validación estructural, Playwright, regresión visual y Axe.

## Decisión

Publicar **`v0.8.2` como parche estable del portal bilingüe**. La versión estabiliza la localización española, la claridad de la portada para usuarios de negocio y la separación física y funcional de los índices ES/EN.

La promoción no cambia definiciones, claims, autoridad doctrinal ni madurez de evidencia. Los nombres ingleses controlados permanecen como referencia entre paréntesis en su primera aparición española.

## Gate de release

El tag y GitHub Release `v0.8.2` solo pueden crearse desde el SHA de `main` que contenga esta decisión y apruebe:

1. linaje exacto del PR #15 y su merge;
2. dos índices de búsqueda sin rutas cruzadas;
3. paridad de las notas ES/EN y hashes vigentes;
4. preflight acumulado y build estricto;
5. recorridos Playwright, regresión visual y Axe;
6. manifiesto, notas y versión activa coherentes;
7. ausencia de un tag `v0.8.2` apuntando a otro commit.

## Límites

- La localización no crea doctrina independiente en inglés o español.
- La claridad editorial no demuestra comprensión, adopción o impacto en decisiones reales.
- La separación de índices evita mezcla de corpus, pero no garantiza relevancia perfecta de resultados.
- Los checks automatizados no establecen conformidad completa WCAG 2.2 AA.
- El tag estable no se reescribe; cualquier cambio posterior exige otra versión.
