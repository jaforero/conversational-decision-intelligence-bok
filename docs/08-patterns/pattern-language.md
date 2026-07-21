---
title: Lenguaje y plantilla de patrones
description: Anatomía, estados de madurez, criterios de selección y plantilla controlada para patrones y anti-patrones de decisión conversacional.
status: candidate
version: 0.8.0-rc.1
artifact_type: candidate-standard
authority_level: candidate-synthesis-and-guidance
normative: false
owner: Javier Forero
domains:
  - Decision Patterns
  - Decision Anti-patterns
  - Decision Governance
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-PULSE-MAP-001
  - SRC-ARCH-001
claim_ids:
  - CLAIM-CDP-CATALOG-001
  - CLAIM-CDP-SELECTION-001
last_reviewed: 2026-07-21
---

# Lenguaje y plantilla de patrones

## Definiciones candidatas

> Un **patrón de decisión conversacional** es una estructura reusable de movimientos, roles, evidencias, controles y salidas para abordar un problema recurrente dentro de una conversación orientada a una decisión.

> Un **anti-patrón de decisión conversacional** es un comportamiento recurrente y reconocible que parece útil en el corto plazo, pero tiende a debilitar la decisión, la acción, el control o el aprendizaje bajo condiciones especificadas.

Son definiciones institucionales candidatas. No sustituyen los documentos futuros `06_PULSE_Decision_Patterns.md` y `05_PULSE_Pattern_Library.md` identificados en el PULSE Documentation Map. Si esos activos se aprueban, este lenguaje deberá alinearse con sus fronteras de propiedad conceptual.

## Qué cuenta como patrón

Una buena práctica aislada —“cite la fuente”— no basta. Una entrada debe contener:

1. **contexto recurrente** y decisión a la que sirve;
2. **problema observable**, no una etiqueta de moda;
3. **fuerzas y trade-offs** que explican por qué el problema no es trivial;
4. **movimientos conversacionales** independientes de proveedor o interfaz;
5. **roles y decision rights**;
6. **evidencia requerida**, incertidumbre y condiciones de abstención;
7. **salida auditable** conectada con acción o aprendizaje;
8. **consecuencias, riesgos y contraindicaciones**;
9. **métricas de proceso y outcome** sin confundirlas;
10. **procedencia y madurez**.

Un patrón es reusable cuando conserva su lógica entre contextos, no cuando copia exactamente el mismo prompt.

## Anatomía controlada

| Campo | Pregunta que debe responder |
|---|---|
| ID y nombre | ¿Cómo se identifica sin depender del título? |
| Tipo y estado | ¿Es patrón o anti-patrón? ¿Candidato, probado en contexto, aprobado o retirado? |
| Momento decisional | ¿Enmarcar, fundamentar, deliberar, comprometer o aprender? |
| Contexto y problema | ¿Cuándo aparece y qué fricción observable resuelve? |
| Fuerzas | ¿Qué tensiones impiden una respuesta obvia? |
| Precondiciones | ¿Qué debe existir antes de usarlo? |
| Movimientos | ¿Qué turnos o verificaciones ejecutan personas y sistemas? |
| Derechos | ¿Quién pregunta, recomienda, decide, aprueba, ejecuta y escala? |
| Evidencia | ¿Qué fuentes, definiciones y límites sostienen la salida? |
| Stop conditions | ¿Cuándo abstenerse, escalar o cambiar de interfaz? |
| Consecuencias | ¿Qué mejora y qué carga o riesgo introduce? |
| Medición | ¿Cómo se evalúan proceso, outcome y guardrails por separado? |
| Alternativas | ¿Qué mecanismo más simple o más seguro puede ser superior? |
| Procedencia | ¿Qué es fundamento, síntesis, hipótesis o experiencia contextual? |

## Contrato de movimientos

Cada patrón usa cuatro tipos de movimiento:

- **Entrada:** hace visible la decisión o el estado desde el que comienza la conversación.
- **Desafío:** busca omisiones, contraevidencia, alternativas o conflictos de definición.
- **Compromiso:** registra una elección, una abstención o un escalamiento bajo derechos explícitos.
- **Salida:** produce un artefacto o estado verificable que otra persona pueda revisar.

No todos los patrones deben llegar al compromiso. **Frontera de evidencia**, por ejemplo, termina correctamente cuando declara que los datos no son aptos para el uso propuesto.

## Estados de madurez

| Estado | Evidencia mínima | Uso permitido |
|---|---|---|
| `candidate-synthesis` | Coherencia con fuentes autorizadas y revisión editorial | Aprendizaje, diseño y prueba controlada |
| `tested-in-context` | Ejecución documentada con resultado y límites en un contexto | Reutilización condicionada; no generalización |
| `approved-guidance` | Ratificación del owner y evidencia acumulada suficiente | Guía institucional dentro de alcance |
| `deprecated` | Alternativa superior o riesgo no aceptable | Solo historia y migración |

El número de usos o la satisfacción del usuario no eleva por sí solo la madurez. Se necesita evidencia sobre el problema decisional, no únicamente sobre la interfaz.

## Regla de selección

El patrón preferible es el **mínimo suficiente** que:

1. resuelve el bloqueo actual;
2. mantiene control humano proporcional al riesgo;
3. conserva evidencia, derechos y trazabilidad;
4. genera una salida que cambia decisión, acción o aprendizaje;
5. cuesta menos que el error o la demora que busca evitar.

### Contraargumento

Formalizar conversaciones puede crear burocracia, inhibir conocimiento tácito y ralentizar decisiones expertas. Esta objeción es fuerte: un catálogo aplicado mecánicamente puede ser peor que una conversación competente. Por eso el sistema permite omitir movimientos ya satisfechos, usar registros mínimos para decisiones reversibles y cambiar a reglas, reportes o revisión experta cuando la conversación no sea la interfaz adecuada.

## Plantilla machine-readable

La plantilla comienza con campos vacíos; no inventa contexto, roles, métricas ni evidencia. Un nuevo patrón no debe publicarse hasta declarar sus contraindicaciones, stop conditions y procedencia.

[Descargar plantilla YAML](../assets/data/conversational-decision-pattern.yml){ .md-button .md-button--primary }

El registro controlado de las entradas publicadas se mantiene en [`governance/registries/patterns.yml`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/governance/registries/patterns.yml).
