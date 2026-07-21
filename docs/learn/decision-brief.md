---
title: Plantilla Decision Brief
description: Plantilla de una página para integrar decisión, evidencia, experiencia, control, acción y aprendizaje antes de actuar.
status: candidate
version: 0.7.0-rc.1
artifact_type: practice-template
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains:
  - Decision Intelligence
  - Decision Governance
  - Decision Metrics
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-ARCH-001
claim_ids:
  - CLAIM-PULSE-ROLE-001
last_reviewed: 2026-07-21
---

# Plantilla Decision Brief

El **Decision Brief** condensa el contrato decisional antes de actuar. No sustituye el análisis detallado; permite descubrir rápidamente qué parte sigue implícita, no gobernada o sin evidencia suficiente.

## Criterio de completitud

El brief está listo para revisión cuando otra persona puede responder, sin reconstruir conversaciones privadas:

- qué se decide, por qué y antes de cuándo;
- quién tiene autoridad y quién será afectado;
- qué alternativas se comparan;
- qué evidencia sustenta o debilita cada opción;
- qué acción ocurrirá;
- qué puede hacer la IA y qué permanece bajo control humano;
- qué resultado se espera y qué cambiaría la conclusión.

## Plantilla para copiar

```markdown
Decision Brief — [nombre de la decisión]

## 1. Priority
- Prioridad material:
- Baseline:
- Horizonte:
- Consecuencia de no actuar:

## 2. Decision
- Frase de decisión:
- Owner:
- Fecha límite:
- Personas o grupos afectados:
- Alternativas, incluida no actuar:
- Criterios y pesos si aplican:
- Restricciones:
- Costo de error / demora:
- Reversibilidad:

## 3. Evidence & context
- Hechos observados:
- Cálculos:
- Inferencias:
- Hipótesis:
- Desconocidos materiales:
- Procedencia y calidad:
- Contexto operativo:
- Incertidumbre:
- Contraevidencia:
- Información que cambiaría la elección:

## 4. Decision Experience
- Usuario y momento de uso:
- Señal que requiere atención:
- Explicación y escenarios:
- Forma de comparar opciones:
- Interfaz elegida y por qué:
- Decisión y acción conectadas:
- Feedback previsto:

## 5. Human–AI control
- Papel permitido para la IA:
- Datos y herramientas autorizados:
- Quién propone / decide / aprueba / ejecuta:
- Condición de escalamiento:
- Stop condition y reversión:
- Traza requerida:
- Owner de accountability:

## 6. Action, metric & learning
- Opción elegida:
- Acción concreta, responsable y fecha:
- Expectativa inferior / central / superior:
- Métrica de proceso:
- Outcome:
- Guardrails:
- Comparación o contrafactual:
- Fecha de revisión:
- Regla para mantener / ampliar / detener / revertir:

## 7. Challenge record
- Supuesto más frágil:
- Mejor contraargumento:
- Riesgo de primer orden:
- Riesgo de segundo orden:
- Alternativa potencialmente superior:
- Confianza: alta / media / baja
- Firmas o aprobaciones:
```

## Revisión en diez preguntas

1. ¿Existe una elección real o solo un tema?
2. ¿El owner puede comprometer la acción?
3. ¿Las alternativas incluyen trade-offs materiales?
4. ¿La evidencia está clasificada y tiene límites?
5. ¿La incertidumbre puede cambiar la opción preferida?
6. ¿La experiencia termina en una acción asignada?
7. ¿Los permisos de IA son mínimos y observables?
8. ¿La expectativa se registró antes de conocer el resultado?
9. ¿Resultado y causalidad están diferenciados?
10. ¿Está acordado cuándo y cómo aprender?

## Uso recomendado

Completa primero el brief sin IA para revelar tu modelo mental. Después usa una conversación para cuestionar supuestos, generar alternativas o detectar campos faltantes. No delegues al sistema la autoridad para definir la prioridad, inventar evidencia o aprobar sus propias acciones.

[Volver a la ruta de aprendizaje](index.md){ .md-button }
[Crear el Measurement Record](../07-governance-quality/measurement-record.md){ .md-button }
