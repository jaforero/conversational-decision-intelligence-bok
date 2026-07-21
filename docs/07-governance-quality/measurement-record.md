---
title: Decision Measurement Record
description: Plantilla versionada para congelar el plan de medición antes de actuar y añadir el resultado después sin reescribir la decisión original.
status: candidate
version: 0.7.0-rc.1
artifact_type: practice-template
authority_level: candidate-guidance
normative: false
owner: Javier Forero
domains:
  - Decision Metrics
  - Decision Quality
  - PULSE
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-ARCH-001
  - SRC-PRACTICE-B2B-001
claim_ids:
  - CLAIM-DM-SYSTEM-001
  - CLAIM-DQ-PROFILE-001
last_reviewed: 2026-07-21
---

# Decision Measurement Record

Este registro complementa el [Decision Brief](../learn/decision-brief.md). El brief estructura la elección; el Measurement Record conserva el plan de observación y la revisión posterior.

## Dos snapshots, una historia

| Snapshot | Cuándo se cierra | Puede cambiarse después |
|---|---|---|
| **Decision snapshot** | Antes de la primera acción | No. Las correcciones se agregan como enmiendas con fecha y razón. |
| **Outcome review** | Al cerrar el horizonte definido | Sí, como revisiones versionadas; nunca sobrescribiendo el snapshot original. |

Esta separación reduce la posibilidad de adaptar retrospectivamente baseline, expectativa o criterio de éxito al resultado observado y conserva una historia sin sobrescritura.

## Antes de actuar

Completa como mínimo:

- ID, decisión, owner, fecha y opción elegida;
- baseline con fuente y fecha de corte;
- outcome esperado con rango e incertidumbre;
- métrica de fidelidad y denominador;
- guardrails, umbrales y respuesta;
- horizonte, comparación y límites de atribución;
- perfil ex ante con evidencia y bloqueadores;
- aprobaciones y timestamp de congelamiento.

Un campo desconocido debe permanecer `null` con un blocker explícito. No lo completes con una estimación inventada para que el registro parezca listo.

## Después del horizonte

Añade:

- acción realmente ejecutada y excepciones;
- outcome y guardrails observados;
- desviación frente al rango;
- cambios concurrentes y explicaciones alternativas;
- fuerza del claim permitida por el diseño;
- decisión de mantener, ampliar, detener, revertir o investigar;
- cambio concreto al siguiente ciclo.

## Plantilla reutilizable

[Descargar plantilla YAML](../assets/data/decision-measurement-record.yml){ .md-button .md-button--primary }

La plantilla conserva valores desconocidos en `null` y resultados en estado `not-observed`. Antes de usarla en producción, define permisos, retención, información sensible y trazabilidad compatibles con el contexto.

## Ritual de revisión

1. Verificar que el snapshot fue congelado antes de la acción.
2. Revisar calidad de proceso sin mirar primero el outcome.
3. Abrir el outcome y los guardrails por segmento pertinente.
4. Comparar con expectativa, no solo con el periodo anterior.
5. Examinar fidelidad, shocks y explicaciones alternativas.
6. Calibrar la fuerza del claim.
7. Registrar qué cambiará en el siguiente ciclo y quién lo hará.

## Regla de publicación

Un registro completo demuestra **trazabilidad**, no eficacia. Para afirmar que una intervención causó un resultado se necesita un diseño de identificación defendible, datos adecuados y límites explícitos. Para afirmar que CDI o PULSE mejoran decisiones se requieren múltiples casos y evaluación externa; esta plantilla no proporciona esa evidencia.

[Volver al sistema de medición](decision-measurement-system.md){ .md-button }
