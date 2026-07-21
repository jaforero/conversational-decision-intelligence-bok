---
id: ADR-020
title: Arquitectura de aprendizaje orientada a resultados
status: accepted
date: 2026-07-21
decision_owner: Javier Forero
scope: Sprint 4 learning experience and public home
---

# ADR-020: Arquitectura de aprendizaje orientada a resultados

## Contexto

El portal ya dispone de un núcleo fundacional, gobernanza y un caso instrumentado. Sin embargo, la portada prioriza definiciones, cautelas y estructura institucional antes de expresar el valor para el lector. El mapa de 29 dominios organiza conocimiento, pero no constituye por sí solo una secuencia pedagógica.

No existe todavía una organización piloto con datos reales, owner operativo e intervención. Ampliar el caso simulado produciría profundidad aparente sin nueva evidencia de impacto.

## Decisión

Crear `v0.6.0-rc.1` como candidato independiente de aprendizaje y experiencia:

1. La portada comenzará con la transformación buscada: formular, evaluar, diseñar, gobernar y aprender.
2. La entrada principal será una ruta de cinco módulos desde Decision First hasta Learning First.
3. Cada módulo declarará un resultado, un modelo, una checklist, una prueba de estrés y un entregable.
4. Un Decision Brief integrará las salidas sin adquirir autoridad normativa.
5. Los límites epistemológicos seguirán visibles, pero después de que el lector comprenda el propósito y no como propuesta de valor principal.
6. El caso B2B conservará su versión y estado histórico; no se ampliará hasta disponer de evidencia real o un objetivo explícito de usabilidad.

## Consecuencias

- La taxonomía y la ruta pedagógica coexistirán: una organiza el campo; la otra guía una aplicación.
- Aumenta el contenido que debe mantenerse y validarse.
- La ruta puede evaluarse con pruebas de comprensión y usabilidad, pero no demuestra impacto organizacional.
- El núcleo estable `v0.4.0` no cambia.

## Contraargumento

Una portada más institucional podría proteger mejor la precisión conceptual. Sin embargo, obliga al lector nuevo a inferir el beneficio antes de decidir si continúa. La arquitectura adoptada conserva precisión en metadatos, módulos y gobernanza, mientras adelanta una promesa concreta y verificable de aprendizaje.

## Alternativa potencialmente superior

Cuando existan usuarios suficientes, probar dos variantes de entrada —por rol y por problema— con tareas de comprensión y finalización. Esa evidencia podría cambiar la navegación adoptada en este sprint.
