---
title: Registro del ciclo B2B
description: Estado actual, campos pendientes y ritual mensual para convertir la decisión en aprendizaje trazable.
status: candidate
version: 0.5.0-rc.1
artifact_type: learning-log
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains:
  - Decision Metrics
  - Decision Quality
  - Enterprise Implementation
source_ids:
  - SRC-PRACTICE-B2B-001
claim_ids:
  - CLAIM-PRACTICE-B2B-HYP-001
last_reviewed: 2026-07-21
---

# Registro del ciclo B2B

## Estado actual

| Campo | Valor |
|---|---|
| Decisión | `DEC-2026-07-COMM-PROPUESTA-01` |
| Ciclo | `CYCLE-01` |
| Estado | **No iniciado** |
| Opción elegida | Pendiente |
| Acción ejecutada | No |
| Expectativa bloqueada | No |
| Resultado observado | No |
| Efecto atribuible | No estimable |
| Aprendizaje | Pendiente |

El registro no usa ceros para campos desconocidos: `0` sería un dato; vacío significa que todavía no existe observación.

## Ritual antes de actuar

1. Confirmar owner y decision rights.
2. Elegir opción y registrar por qué se descartan las demás.
3. Definir intervención, comparador y regla de asignación.
4. Aprobar baseline y sensibilidad.
5. Fijar expectativa inferior, central y superior con horizonte.
6. Puntuar calidad de proceso sin mirar el futuro.
7. Bloquear timestamp y obtener sign-off.

## Revisión mensual

1. Verificar que la intervención ocurrió como fue diseñada.
2. Calcular métricas en intervención y comparación con las mismas definiciones.
3. Registrar cambios de mix, personas, pricing, estacionalidad y deals atípicos.
4. Estimar diferencia-en-diferencias cuando el diseño lo permita.
5. Comparar rango esperado y resultado observado.
6. Separar juicio sobre proceso, outcome y atribución.
7. Decidir: continuar, adaptar, detener o escalar.

## Gate para elevar el estado

| Próximo estado | Condición mínima |
|---|---|
| `observed-noncausal` | Acción y resultado registrados, pero comparador insuficiente. |
| `evaluated` | Expectativa preregistrada, comparador defendible, 2–3 ciclos y limitaciones analizadas. |
| `blocked` | Sin owner, datos fitness for purpose o posibilidad de medir. |

[Descargar el log CSV](../../assets/data/b2b-proposal-cycle-log.csv){ .md-button .md-button--primary }
[Descargar el registro YAML](../../assets/data/b2b-proposal-decision-record.yml){ .md-button }

!!! note "La primera evidencia útil"
    Antes de medir conversión, el ciclo ya puede revelar si el contrato es comprensible, si el owner puede formular una expectativa y si el ritual cabe en la operación. Eso es evidencia de usabilidad del método, no de impacto comercial.
