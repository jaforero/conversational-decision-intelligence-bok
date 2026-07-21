---
title: 5. Actuar, medir y aprender
description: Prerregistra expectativas, separa calidad de decisión y resultado, y convierte la desviación en el siguiente ciclo.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains:
  - Decision Quality
  - Decision Metrics
  - PULSE
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-PRACTICE-B2B-001
claim_ids:
  - CLAIM-PULSE-001
last_reviewed: 2026-07-21
---

# 5. Actuar, medir y aprender

**Resultado del módulo:** un contrato de aprendizaje que fija expectativa, horizonte, métricas, guardrails, comparación y fecha de revisión antes de ejecutar.

## Una decisión no termina cuando se elige

El ciclo se completa cuando la organización compara lo esperado con lo observado, interpreta la desviación y modifica la siguiente decisión. Sin ese registro, el resultado se reescribe retrospectivamente y la organización aprende poco.

## Fijar la expectativa antes de actuar

Registra:

- resultado esperado con rango inferior, central y superior;
- horizonte en que debería aparecer;
- mecanismo por el cual la acción produciría el resultado;
- métricas de proceso que muestran si la acción ocurrió;
- outcomes y guardrails;
- supuestos decisivos;
- condiciones de detener, mantener, ampliar o revertir;
- comparación o contrafactual disponible.

La precisión debe corresponder a la evidencia. Un rango defendible es superior a un decimal inventado.

## Calidad de decisión y resultado no son lo mismo

|  | Resultado favorable | Resultado desfavorable |
|---|---|---|
| **Proceso de decisión sólido** | Buena decisión con resultado favorable; documentar qué fue replicable. | Buena decisión con mala fortuna o supuesto fallido; revisar mecanismo y calibración. |
| **Proceso de decisión débil** | Resultado favorable por suerte; no institucionalizar sin entenderlo. | Mala decisión y mal resultado; corregir proceso, gobierno y acción. |

Evaluar solo outcomes premia la suerte. Evaluar solo el proceso puede proteger decisiones que nunca producen valor. Se necesitan ambas dimensiones.

## Cinco familias de métricas

| Familia | Ejemplos | Pregunta |
|---|---|---|
| **Latencia** | Tiempo desde señal hasta decisión o acción | ¿Decidimos a tiempo? |
| **Proceso** | Adopción, cumplimiento, override, escalamiento | ¿La intervención ocurrió como se diseñó? |
| **Resultado** | Ingreso, costo, retención, error, servicio | ¿Se movió la prioridad? |
| **Guardrail** | Equidad, calidad, riesgo, carga, quejas | ¿Qué deterioramos mientras mejorábamos otra cosa? |
| **Aprendizaje** | Calibración, hipótesis revisadas, tiempo a corrección | ¿El siguiente ciclo es mejor informado? |

## Atribución prudente

Un cambio posterior no prueba que la decisión lo causó. La fuerza del claim depende del diseño: comparación histórica, grupo comparable, experimento, diferencia-en-diferencias, discontinuidad u otro enfoque apropiado.

Cuando no exista un contrafactual defendible:

- informa el resultado como **observación posterior**;
- enumera cambios concurrentes;
- limita el lenguaje causal;
- usa múltiples ciclos si el contexto lo permite;
- conserva la posibilidad de no atribuir.

## El registro del ciclo

```text
Decisión y fecha:
Opción elegida:
Expectativa inferior / central / superior:
Acción ejecutada:
Fidelidad de ejecución:
Resultado observado:
Guardrails:
Comparación o contrafactual:
Desviación frente a expectativa:
Explicaciones alternativas:
Aprendizaje:
Cambio para el siguiente ciclo:
Owner y fecha de revisión:
```

## Prueba de estrés

- ¿La métrica puede mejorar sin que mejore la prioridad real?
- ¿El equipo que ejecuta tiene capacidad para cumplir la intervención?
- ¿Qué shock externo podría explicar el resultado?
- ¿La ventana elegida favorece la narrativa deseada?
- ¿Qué resultado nos haría abandonar la opción?
- ¿Quién revisará el aprendizaje cuando el resultado sea incómodo?

## Una frontera importante

Puedes aprender el método con un ejemplo o una demo. Para afirmar impacto organizacional necesitas una decisión real, un owner, una acción observada y evidencia suficiente. El CDI-BoK mantiene separadas esas dos clases de aprendizaje.

**Siguiente:** [integrar los cinco módulos en un Decision Brief →](decision-brief.md)
