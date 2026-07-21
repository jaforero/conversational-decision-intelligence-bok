---
title: Catálogo del Practice Lab
description: Inventario verificado de demos y evaluación de su capacidad para convertirse en casos instrumentados.
status: candidate
version: 0.5.0-rc.1
artifact_type: practice-catalog
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains:
  - Case Studies
  - Decision Patterns
  - Decision Metrics
source_ids:
  - SRC-PRACTICE-DASH-ROOT-001
  - SRC-PRACTICE-GPT-ROOT-001
claim_ids: []
last_reviewed: 2026-07-21
---

# Catálogo del Practice Lab

Este inventario registra lo que estaba públicamente disponible el **21 de julio de 2026**. Cataloga interfaces; no atribuye impacto. La disponibilidad puede cambiar fuera del ciclo de publicación del CDI-BoK.

## Dos portafolios, una frontera de evidencia

| Portafolio | Casos observados | Capacidades visibles | Límite |
|---|---:|---|---|
| [Claude](https://dashboards.javierforero.co/claude/) | 3 demos interactivas | Carga local de datos en SLA y Finanzas; Q&A determinista; gobernanza | Las páginas específicas declaran datos de demo simulados o sintéticos. |
| [ChatGPT Work](https://javier-dashboards.jforero.chatgpt.site/) | 5 casos disponibles y 1 anunciado | Tres dashboards, un proyecto predictivo y un benchmark Tableau | Una colección y una interfaz no demuestran mejora decisional. |

!!! warning "La declaración específica prevalece"
    La portada principal usa la expresión “datos reales embebidos”, mientras las páginas específicas revisadas de SLA, Finanzas y Comercial declaran datos simulados, sintéticos o de demostración. Para evaluar evidencia, este catálogo adopta la declaración más específica y conservadora.

## Inventario verificado

| ID | Caso | Portafolio | Estado público | Naturaleza de datos observada | Readiness para caso |
|---|---|---|---|---|---|
| `JF-CLAUDE-SLA` | Cumplimiento de SLA · Operaciones B2B | Claude | Disponible | Sintéticos; acepta CSV/XLSX local | Media: decisión y umbrales visibles; falta resultado organizacional. |
| `JF-CLAUDE-FINANCE` | Pulso Financiero · Finanzas Corporativas | Claude | Disponible | Demo simulada; acepta CSV/XLSX local | Media: backtest visible; atribución de acción más lenta. |
| `JF-CLAUDE-COMMERCIAL` | Desempeño Comercial · Dirección B2B | Claude | Disponible | Ventas, funnel y CRM simulados | **Alta para instrumentación:** tres fuentes, decisión recurrente y acción reversible. |
| `JF-GPT-FINANCE` | Predicción financiera 2025 | ChatGPT Work | Disponible | Dataset financiero simulado | Media: evidencia predictiva; aprendizaje de decisión aún no registrado. |
| `JF-GPT-SLA` | Cumplimiento SLA B2B | ChatGPT Work | Disponible | 570 registros simulados | Media-Alta: señal y acción; falta vínculo con churn o retención. |
| `JF-GPT-COMMERCIAL` | Desempeño comercial y ventas | ChatGPT Work | Disponible | Tres datasets simulados | Alta para instrumentación; representa la misma familia decisional del caso seleccionado. |
| `JF-GPT-WORLDCUP` | Predicción Mundial 2026 | ChatGPT Work | Disponible, externo | Datos y modelos de predicción | Alta para calibración predictiva; baja para acción organizacional B2B. |
| `JF-GPT-TABLEAU` | Inflación en América Latina | ChatGPT Work | Disponible, externo | No evaluada en este sprint | Baja: benchmark descriptivo, no ciclo decisional instrumentado. |
| `JF-GPT-PULSE` | PULSE Decision Intelligence | ChatGPT Work | Próximamente | Sin caso observable | No evaluable. |

## Por qué se seleccionó Comercial B2B

| Criterio | Comercial B2B | Implicación |
|---|---|---|
| Decisión material y recurrente | Sí, intervención mensual sobre el funnel | Permite más de un ciclo. |
| Fuentes heterogéneas | Ventas, conversiones y pipeline CRM | Prueba integración sin construir plataforma. |
| Baseline disponible | Sí, dentro del demo | Permite instrumentar; no sustituye datos reales. |
| Acción reversible | Sí, comenzar por calidad/velocidad de Propuesta | Reduce costo de error frente a reasignar presupuesto. |
| Resultado observado | No | Bloquea cualquier claim de eficacia. |
| Owner real confirmado | No | Bloquea ejecución como piloto organizacional. |
| Contrafactual | Diseñado, no asignado | Bloquea atribución causal. |

[Abrir el caso B2B Propuesta](b2b-proposal/index.md){ .md-button .md-button--primary }

## Qué haría cambiar la selección

- Datos SLA–churn a nivel cliente convertirían el caso de retención en un candidato transversal más fuerte.
- Imposibilidad de confirmar un owner comercial convertiría B2B Propuesta en prueba pedagógica, no en piloto de impacto.
- Una muestra mayor y evidencia robusta por canal podría elevar la reasignación de demanda como opción.
- Un caso con acción ya ejecutada y comparación válida podría producir aprendizaje observable antes.
