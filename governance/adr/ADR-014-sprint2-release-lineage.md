---
id: ADR-014
title: Linaje de versión del núcleo fundacional
status: accepted
date: 2026-07-21
decider: Javier Forero
domains:
  - Foundations
  - Decision Governance
---

# ADR-014: Linaje de versión del núcleo fundacional

## Contexto

La secuencia inicial ya publicó gobernanza `v0.2.0` y portal técnico `v0.3.0-rc.1`. La arquitectura ratificada describía la salida de Sprint 2 como `v0.1.0`, lo que produciría una regresión de versión y ambigüedad histórica.

## Decisión

El núcleo fundacional de Sprint 2 se publicará como candidato `v0.4.0-rc.1`. Esta decisión corrige únicamente la etiqueta prevista de salida y no cambia la autoridad de CDI-GOV-001 `v0.2.0`.

Las versiones se interpretan así:

- `v0.2.0`: gobernanza fundacional ratificada;
- `v0.3.0-rc.1`: infraestructura y portal desplegados;
- `v0.4.0-rc.1`: Constitución, fronteras, glosario, dominios y especificación PULSE candidatos.

## Consecuencias

- no se reescribe ni oculta la historia;
- una versión de portal no eleva automáticamente la madurez científica;
- `v0.4.0-rc.1` solo podrá convertirse en release aprobada tras ratificación del núcleo y checks en verde.

