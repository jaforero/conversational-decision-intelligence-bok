---
id: ADR-026
title: Promoción estable del portal bilingüe v0.8.1
status: accepted
date: 2026-07-21
decider: Javier Forero
domains: [Decision Governance, Publication Architecture]
---

# ADR-026: Promoción estable del portal bilingüe v0.8.1

## Contexto

`v0.8.1-rc.1` implementó 46 pares ES/EN mediante el PR #12, fusionado como `655e3b80ad1cbd8b443b6339358996f9fe656083`. La revisión pública detectó textos españoles procedentes de configuración y plantillas compartidas; el PR #13 corrigió la causa raíz y se fusionó como `5837657f6bfe0627f5bd0c8ada13640dba9a0a4b`. Los gates post-hotfix y Pages aprobaron, y el portal inglés fue verificado públicamente.

Javier Forero autorizó el 21 de julio de 2026 preparar la promoción estable `v0.8.1`. La decisión estabiliza el sistema bilingüe, no la eficacia o autoridad de todos los conocimientos contenidos.

## Decisión

Promover `v0.8.1-rc.1` a **`v0.8.1` como línea base editorial y técnica estable del portal bilingüe**.

La promoción acepta la equivalencia de rutas, la interfaz localizada, la búsqueda por idioma, la metadata SEO, el registro de pares y sus gates de mantenimiento. El español permanece canónico durante `0.x`; el inglés continúa como traducción gobernada.

## Gate de release

El tag y GitHub Release `v0.8.1` solo pueden crearse desde el SHA de `main` que contenga esta decisión y apruebe:

1. linaje exacto de los PR #12 y #13;
2. inventario y hashes de todos los pares ES/EN;
3. preflight acumulado y build estricto;
4. regresión visual, recorridos Playwright y análisis Axe;
5. manifiesto, notas y versión activa coherentes;
6. ausencia de un tag `v0.8.1` apuntando a otro commit.

## Límites

- Traducir y estabilizar el portal no valida CDI, PULSE o los patrones.
- La autoridad aprobada del núcleo `v0.4.0` no se extiende a artefactos candidatos.
- El caso B2B permanece `instrumented-not-executed`.
- Los checks automatizados no establecen conformidad completa WCAG 2.2 AA.
- Una modificación posterior requiere una nueva versión; el tag estable no se reescribe.
