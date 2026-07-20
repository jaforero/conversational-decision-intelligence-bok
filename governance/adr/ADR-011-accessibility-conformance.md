---
id: ADR-011
title: Objetivo y declaración de accesibilidad
status: accepted
date: 2026-07-19
decider: Javier Forero
domains:
  - Responsible AI
  - Decision Governance
  - Enterprise Implementation
---

# ADR-011: Objetivo y declaración de accesibilidad

## Contexto

La accesibilidad es parte de la calidad de decisión: si la evidencia no puede percibirse, navegarse o comprenderse por usuarios diversos, la experiencia decisional falla. A la vez, adoptar una meta no autoriza a declarar conformidad antes de evaluar el producto completo.

## Decisión

El CDI-BoK adopta **WCAG 2.2 nivel AA** como objetivo de release para `decision.javierforero.co`.

La verificación combinará:

- validación automática de HTML, roles, nombres accesibles y contrastes;
- navegación completa por teclado y foco visible;
- pruebas a 320, 360, 768 y 1024+ px;
- revisión de zoom, reflow, motion y modo oscuro;
- estructura semántica, orden de encabezados y enlaces comprensibles;
- revisión manual con tecnologías de asistencia en flujos críticos;
- texto alternativo y equivalente textual para diagramas y datos.

El estándar interno conserva objetivos de interacción de `44 × 44 px` y separación de `8 px` definidos por la marca. No se publicará la frase “conforme con WCAG 2.2 AA” hasta completar una auditoría sobre la release desplegada, registrar alcance, excepciones y fecha.

## Estados permitidos

- `targeted`: objetivo adoptado; todavía no auditado.
- `tested`: controles parciales ejecutados; sin declaración pública de conformidad.
- `conformant`: auditoría completa de la release y alcance registrados.
- `conformant-with-known-exceptions`: solo si las excepciones están publicadas con plan y fecha.

El estado inicial de `v0.2.0` es `targeted` porque Sprint 0 define contratos, no despliega el portal.

## Consecuencias

- Los tokens de modo oscuro quedan pendientes hasta una auditoría de contraste; no se inventan en Sprint 0.
- Un build automático aprobado es necesario, pero no suficiente para la declaración.
- Demos externas no heredan conformidad del CDI-BoK; deben declarar su propio alcance.

## Alternativas descartadas

- **Declarar AA por adoptar colores de marca:** la conformidad depende de páginas, estados y flujos completos.
- **Usar solo pruebas automáticas:** no cubren comprensión, orden de lectura ni todas las interacciones.
- **Aplazar accesibilidad al final:** hace más costosa la corrección y puede bloquear patrones editoriales ya publicados.

