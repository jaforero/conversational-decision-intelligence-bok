---
title: Patrones de decisión conversacional
description: Sistema candidato para elegir y aplicar estructuras conversacionales que llevan evidencia hacia decisión, acción y aprendizaje sin convertirlas en recetas universales.
status: candidate
version: 0.8.0-rc.1
artifact_type: knowledge-area-landing
authority_level: candidate-synthesis-and-guidance
normative: false
owner: Javier Forero
domains:
  - Decision Patterns
  - Decision Anti-patterns
  - Conversational Decision Intelligence
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-PULSE-MAP-001
  - SRC-ARCH-001
claim_ids:
  - CLAIM-CDP-CATALOG-001
  - CLAIM-CDP-SELECTION-001
last_reviewed: 2026-07-21
---

# Patrones de decisión conversacional

<div class="cdi-insight" markdown>

**Un patrón no decide por ti.** Organiza una conversación recurrente para que una decisión, su evidencia, sus derechos, su acción y su aprendizaje dejen de permanecer implícitos.

</div>

Esta área activa **Decision Patterns** y **Decision Anti-patterns** como una taxonomía candidata del CDI-BoK. No afirma que cinco patrones cubran todas las decisiones ni que seguirlos produzca mejores resultados. Su función es hacer observable el razonamiento mínimo y permitir que un equipo elija la estructura menos compleja que resuelva su bloqueo actual.

## Qué problema resuelve

Una conversación puede ser fluida y aun así no producir una decisión. Puede responder cifras sin definiciones, generar opciones sin trade-offs, recomendar sin autoridad o celebrar un outcome sin conservar la expectativa original.

Los patrones conectan cinco momentos:

| Momento | Pregunta de control | Patrón candidato |
|---|---|---|
| Enmarcar | ¿Qué decisión concreta y qué prioridad están en juego? | **Contrato de decisión** |
| Fundamentar | ¿Qué sabemos, de dónde viene y qué permanece incierto? | **Frontera de evidencia** |
| Deliberar | ¿Qué alternativas materiales sobreviven al desafío? | **Desafío de opciones** |
| Comprometer | ¿Quién decide y qué acción gobernada ocurre después? | **Handoff decisión–acción** |
| Aprender | ¿Qué cambió entre expectativa y resultado? | **Revisión expectativa–resultado** |

No es una secuencia obligatoria. Si la decisión ya está bien enmarcada, no debe repetirse el contrato. Si falta evidencia material o autoridad, el patrón correcto puede terminar en **abstención o escalamiento**, no en una recomendación.

## Selección rápida

Empieza por el bloqueo, no por el catálogo completo.

| Señal observable | Usa primero | Detente si |
|---|---|---|
| La pregunta pide “analizar” un tema, pero no existe elección | Contrato de decisión | No aparece owner, alternativa o fecha límite |
| Dos personas usan la misma métrica con significados distintos | Frontera de evidencia | No puede resolverse la definición o el permiso |
| Solo existe una opción preferida | Desafío de opciones | Las alternativas serían artificiales o el tiempo exige una regla preacordada |
| Hay recomendación, pero nadie ejecuta | Handoff decisión–acción | Quien conversa no tiene derecho para comprometer recursos |
| El horizonte terminó y todos recuerdan una expectativa distinta | Revisión expectativa–resultado | No existe snapshot previo; solo puede hacerse una revisión exploratoria |

### Ajusta el rigor al riesgo

- **Bajo riesgo y alta reversibilidad:** usa el movimiento mínimo, registra owner, acción y revisión.
- **Riesgo medio:** añade fuentes, alternativas, guardrails y aprobación explícita.
- **Alto riesgo, baja reversibilidad o impacto sobre derechos:** exige revisión experta, evidencia reforzada, permisos, trazabilidad y una vía no automatizada. El catálogo no sustituye obligaciones legales, éticas o profesionales.

## Dos catálogos, una misma disciplina

- El [catálogo de patrones](catalog.md) describe estructuras que pueden ayudar a avanzar una decisión.
- El [catálogo de anti-patrones](anti-patterns.md) describe comportamientos recurrentes que degradan trazabilidad, control o aprendizaje.

La [anatomía y plantilla](pattern-language.md) permite documentar nuevas entradas sin confundir experiencia práctica con evidencia generalizable. La [aplicación B2B](b2b-proposal-walkthrough.md) muestra una consecuencia importante: el protocolo debe detenerse antes de inventar un owner o simular un outcome.

## Fronteras de autoridad

Este candidato:

- deriva de PULSE, PDAMR, Decision Circle y Human-in-Control sin redefinirlos;
- implementa una taxonomía institucional, no un estándar académico reconocido;
- conserva separadas **reutilización**, **conformidad** y **eficacia**;
- no convierte una interfaz conversacional en requisito de PULSE o CDI;
- no autoriza a un sistema de IA a decidir, aprobar o ejecutar fuera de derechos explícitos.

<div class="cdi-actions" markdown>
[Elegir un patrón](catalog.md){ .md-button .md-button--primary }
[Reconocer anti-patrones](anti-patterns.md){ .md-button }
[Usar la plantilla](pattern-language.md){ .md-button }
</div>
