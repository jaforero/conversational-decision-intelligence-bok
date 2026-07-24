---
id: ADR-029
title: Promoción estable del Evidence Backbone y Research v0.9.0
status: accepted
date: 2026-07-24
decider: Javier Forero
domains: [Decision Governance, Evidence Governance, Research, Publication Architecture]
---

# ADR-029: Promoción estable del Evidence Backbone y Research v0.9.0

## Contexto

El candidato `v0.9.0-rc.1` incorporó un Evidence Backbone ejecutable, auditó
fuentes adicionales, publicó un estado del arte bilingüe y estableció límites
contra claims sobredimensionados. El PR #18 se fusionó mediante
`3e9ad9937f35d85d737a23813e6ac55a0d74ee64`; el cierre ratificado quedó en
`main` mediante el PR #19 y
`a2965f352664bbfa05b94b91f358e261aaa2bc54`. Los gates estructurales,
Playwright, regresión visual, Axe, Pages y las rutas Research ES/EN fueron verificados.

## Decisión

Publicar **`v0.9.0` como línea base estable de publicación y gobierno de
evidencia**. La promoción congela el bundle reproducible del candidato y su
linaje. No homogeneiza la autoridad de los componentes incluidos: cada claim,
hipótesis, patrón, recomendación y fuente conserva su clasificación, alcance y limitaciones.

La estabilidad de la release es una propiedad editorial y técnica. No constituye
validación científica de CDI o PULSE, consenso académico sobre el estado del
campo, prueba de eficacia ni evidencia de impacto organizacional.

## Gate de release

El tag y GitHub Release `v0.9.0` solo pueden crearse desde el SHA de `main`
que contenga esta decisión y apruebe:

1. linaje exacto del candidato, PR #18 y cierre PR #19;
2. manifiesto estable y registro de promoción coherentes;
3. perfiles de evidencia, derechos y compatibilidad claim–fuente;
4. paridad ES/EN, hashes y búsqueda separada por idioma;
5. preflight acumulado y build estricto;
6. Playwright, regresión visual y Axe;
7. ausencia de un tag `v0.9.0` apuntando a otro commit.

## Límites y consecuencias

- La tesis de DI como campo integrador emergente sigue siendo provisional.
- PULSE permanece como síntesis del proyecto y no como sistema científicamente validado.
- Las fuentes asistidas sirven para descubrimiento, no para elevar claims.
- Los documentos incompletos y las señales prospectivas conservan sus restricciones.
- Los checks automatizados no establecen conformidad completa WCAG 2.2 AA.
- El tag estable es inmutable; cualquier cambio posterior exige otra versión.
