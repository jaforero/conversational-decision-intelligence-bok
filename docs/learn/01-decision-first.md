---
title: 1. Enfocar la decisión
description: Convierte una prioridad o pregunta amplia en una decisión explícita mediante PDAMR y un contrato mínimo.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains:
  - Decision Intelligence
  - PULSE
  - Decision Governance
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-PULSE-IDENTITY-002
  - SRC-JF-005
  - SRC-ARCH-001
claim_ids:
  - CLAIM-PULSE-001
  - CLAIM-PULSE-ROLE-001
last_reviewed: 2026-07-21
---

# 1. Enfocar la decisión

**Resultado del módulo:** una frase de decisión y una brújula PDAMR suficientemente completas para saber qué evidencia buscar y qué acción podría cambiar.

## La pregunta que precede a la tecnología

PULSE comienza con: **¿qué decisión queremos mejorar?** Una prioridad no es una decisión; un problema tampoco; un insight y una recomendación todavía no comprometen una elección.

| Expresión | Qué es | Qué falta |
|---|---|---|
| “Las ventas están cayendo” | Señal o problema | Quién debe elegir qué hacer y cuándo. |
| “¿Por qué cae la conversión?” | Pregunta diagnóstica | La elección que usará la respuesta. |
| “Debemos capacitar al equipo” | Recomendación | Alternativas, criterios y autoridad para comprometer recursos. |
| “La directora comercial elegirá antes del viernes entre rediseñar la propuesta, cambiar el seguimiento o no intervenir” | Decisión encuadrada | Evidencia, criterios, restricciones, acción y aprendizaje. |

## La frase de decisión

Completa esta estructura:

> **Antes de [fecha], [owner] debe elegir [una opción] entre [alternativas] para mover [prioridad], usando [criterios], bajo [restricciones]. La elección cambiará [acción].**

Una buena frase hace visibles siete componentes:

1. **momento** en que la decisión debe cerrarse;
2. **owner** con autoridad real;
3. **alternativas**, incluida la opción de no actuar cuando sea legítima;
4. **prioridad** que justifica decidir;
5. **criterios** para comparar opciones;
6. **restricciones** de recursos, regulación, capacidad o riesgo;
7. **acción** que ocurrirá después de elegir.

## La brújula PDAMR

| Componente | Pregunta | Evidencia de una respuesta útil |
|---|---|---|
| **Priority** | ¿Qué prioridad material debe moverse? | Tiene baseline, horizonte y consecuencia. |
| **Decision** | ¿Qué elección debe mejorar? | Tiene owner, opciones y fecha. |
| **Action** | ¿Qué se hará diferente? | Describe un cambio observable de conducta, proceso o asignación. |
| **Metric** | ¿Cómo sabremos si funcionó? | Incluye resultado, proceso y guardrails. |
| **Risk** | ¿Qué puede salir mal y quién lo controla? | Incluye daño, permisos, escalamiento y stop conditions. |

PDAMR no es una prueba de calidad; es una prueba de **integridad mínima**. Puede estar completo y contener malas premisas. Por eso los módulos siguientes examinan evidencia, diseño, control y aprendizaje.

## Costos que suelen quedar ocultos

No basta con preguntar por el costo del error.

- **Costo de actuar mal:** recursos desperdiciados, daño, inequidad o pérdida de confianza.
- **Costo de esperar:** oportunidad perdida, deterioro acumulado o decisión tomada de facto por inacción.
- **Costo de reversión:** qué tan difícil es deshacer la opción.
- **Costo de información:** tiempo y recursos para reducir incertidumbre.

La alternativa “investigar más” solo es superior si el valor esperado de esa información supera su costo y llega antes de que la decisión pierda utilidad.

## Prueba de estrés

Antes de continuar, responde:

- ¿El owner puede realmente comprometer la acción?
- ¿Las alternativas son materialmente distintas o variaciones cosméticas?
- ¿Qué opción preferiríamos si no apareciera ningún dato nuevo?
- ¿Qué información podría cambiar esa preferencia?
- ¿Quién soporta las consecuencias pero no participa en la elección?
- ¿Es reversible la decisión? Si no lo es, ¿qué evidencia adicional exige?

## Entregable

Registra:

```text
Decisión:
Owner:
Fecha límite:
Alternativas:
Prioridad y baseline:
Acción posterior:
Criterios:
Restricciones:
Costo de error:
Costo de demora:
Reversibilidad:
```

**Siguiente:** [sustentar la decisión con evidencia y contexto →](02-evidence-context.md)
