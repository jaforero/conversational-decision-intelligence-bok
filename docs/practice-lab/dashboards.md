---
title: Laboratorio de dashboards de decisión
description: Practica la lectura de un indicador, verifica su fuente y registra una decisión con sus límites.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: experimental
normative: false
owner: Javier Forero
domains: [Conversational Analytics, Semantic Layers, Decision Patterns]
source_ids: [SRC-PRACTICE-FX-001, SRC-PRACTICE-POP-001, SRC-PRACTICE-DASH-B2B-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# Laboratorio de dashboards de decisión

**Pregunta de práctica.** ¿Qué señal justificaría revisar una exposición presupuestaria en moneda extranjera? En este ejercicio, planeación decide si abre una revisión o conserva el supuesto vigente. La decisión final requiere conocer los flujos de la organización, la moneda del presupuesto y el horizonte de la exposición.

[Abrir tasas de cambio oficiales](https://dashboards.javierforero.co/tasas-cambio/){ .md-button .md-button--primary }

## Recorrido guiado · Tasas de cambio { #fx }

1. Elige dos monedas, una fecha inicial y un horizonte. Registra la unidad de cotización, el valor y la fecha oficial de cada serie. Consulta [los datos y su metodología](https://github.com/jaforero/fx-bancos-centrales).
2. En **Comparación base 100**, identifica el primer dato oficial desde la fecha elegida para cada moneda. En cotizaciones de moneda local por USD, por encima de 100 indica depreciación frente al dólar y por debajo indica apreciación frente a esa base. Repite con otra fecha de partida y observa si cambia la lectura.
3. Contrasta con la tabla de datos. Distingue una observación oficial de un valor repetido por un día sin publicación. Para comparar monedas, revisa si los puntos de partida y las fechas de observación coinciden.
4. Define un umbral de revisión antes de evaluar la señal. Si se activa, solicita al responsable del presupuesto contrastarla con la exposición efectiva y registra cuándo revisarás el supuesto.

**Entregable.** Completa un [Decision Brief](../learn/decision-brief.md) con las dos alternativas, el umbral, la evidencia con fechas, el responsable y la condición de revisión. Repite la lectura desde una segunda fecha de partida. Si cambia la decisión, registra por qué.

**Criterio de aceptación.** Otra persona puede reconstruir tu lectura con el mismo par, periodo y fuente. El brief explica qué cambiaría la acción y distingue las tasas oficiales de referencia de una tasa que la organización podría negociar.

## Otras rutas de práctica

| Decisión que quieres practicar | Demo | Qué debes registrar |
|---|---|---|
| Revisar capacidad de un servicio por edad y territorio | [Población de América Latina](https://dashboards.javierforero.co/poblacion-latam/) | Grupo etario, edición y serie seleccionada, años estimados o proyectados y efecto de una revisión de la fuente. Sigue el [ejercicio demográfico](../learn/02-evidence-context.md#demographic-planning). |
| Priorizar una intervención ante una caída de servicio | [SLA B2B](https://dashboards.javierforero.co/claude/sla-operaciones/) | Periodo del quiebre, denominador, regla de escalamiento y evidencia que podría cambiar la prioridad. Usa el escenario simulado de la demo. |
| Revisar una alerta financiera antes de comprometer presupuesto | [Pulso financiero](https://dashboards.javierforero.co/claude/pulso-financiero/) | Horizonte, referencia del pronóstico, error observado en el backtest y responsable de la acción. La demo usa datos simulados. |
| Elegir una intervención comercial reversible | [Desempeño comercial](https://dashboards.javierforero.co/claude/desempeno-comercial/) | Alternativas, baseline simulado y criterio para observar el resultado. Continúa con el [caso B2B instrumentado](b2b-proposal/index.md). |

Para pilotear preguntas conversacionales, añade las [pruebas de referencia y acceso](../learn/03-decision-experience.md#conversational-dashboard-pilot). Consulta el [catálogo del Practice Lab](catalog.md) para identificar los datos que usa cada recurso.
