---
title: Catálogo del Practice Lab
description: Encuentra un laboratorio por decisión y distingue datos públicos, demos simuladas y casos instrumentados.
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
  - SRC-PRACTICE-FX-001
  - SRC-PRACTICE-POP-001
  - SRC-PRACTICE-GRAPH-001
claim_ids: []
last_reviewed: 2026-11-08
---

# Catálogo del Practice Lab

Elige según la decisión que quieras practicar. Los laboratorios guían el ejercicio dentro del CDI-BoK y enlazan las herramientas del [portafolio de Javier Forero](https://dashboards.javierforero.co/).

| Empieza por | Qué produces |
|---|---|
| [Dashboards de decisión](dashboards.md) | Un brief con indicador verificable, criterio para actuar y fecha de revisión. |
| [Grafos de conocimiento](knowledge-graph.md) | Un hallazgo de trazabilidad reproducible y una propuesta de mejora para el CDI-BoK. |
| [Evaluar un asistente con evidencia](conversational-evidence.md) | Un registro de pruebas y una decisión sobre ampliar, mantener o pausar un piloto de consulta. |
| [Caso B2B · Propuesta](b2b-proposal/index.md) | Un protocolo para evaluar una intervención comercial con datos simulados. |

## Recursos con fuentes públicas

Rutas contrastadas con el portafolio el **8 de noviembre de 2026**.

| Recurso | Qué puedes practicar | Naturaleza de los datos |
|---|---|---|
| [Tasas de cambio](https://dashboards.javierforero.co/tasas-cambio/) | Interpretar base 100 y separar publicación oficial de arrastre | Series de siete bancos centrales y cruces calculados |
| [Población de América Latina](https://dashboards.javierforero.co/poblacion-latam/) | Comparar estructura, territorios y horizontes | Series oficiales y proyecciones de 20 países |
| [Costo de vida por ciudad](https://dashboards.javierforero.co/claude/costo-vida-colombia/) | Interpretar una referencia relativa al promedio | Indicadores públicos para Colombia, con metodología en la pieza |
| [Cómputo de entrenamiento en IA](https://dashboards.javierforero.co/ia-compute/) | Contrastar una tendencia con los niveles de evidencia | Compilación pública de modelos con valores reportados o estimados |
| [Explorador de grafos](https://dashboards.javierforero.co/claude/grafo-conocimiento/) | Seguir enlaces y revisar su contexto | Corpus que el usuario selecciona. El laboratorio carga el CDI-BoK público |

## Demos de consultoría

| Decisión de práctica | Claude | ChatGPT Work | Datos |
|---|---|---|---|
| Priorizar una intervención operativa | [SLA B2B](https://dashboards.javierforero.co/claude/sla-operaciones/) | [SLA B2B](https://javier-dashboards.jforero.chatgpt.site/dashboards/sla) | Simulados; Claude admite carga local. |
| Evaluar una alerta presupuestaria | [Pulso financiero](https://dashboards.javierforero.co/claude/pulso-financiero/) | [Predicción financiera](https://javier-dashboards.jforero.chatgpt.site/dashboards/finanzas) | Simulados; Claude admite carga local. |
| Elegir una intervención en el funnel | [Desempeño comercial](https://dashboards.javierforero.co/claude/desempeno-comercial/) | [Comercial y ventas](https://javier-dashboards.jforero.chatgpt.site/dashboards/comercial) | Ventas, funnel y CRM simulados. |

La [colección ChatGPT Work](https://javier-dashboards.jforero.chatgpt.site/) también enlaza piezas externas de predicción deportiva e inflación. El [registro de demos](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/governance/registries/external-demos.yml) conserva la observación de julio y los recursos incorporados después.

## Caso instrumentado

El CDI-BoK seleccionó **Comercial B2B · Propuesta** por su decisión recurrente, tres fuentes simuladas, un baseline disponible y una intervención reversible. Su ejecución requiere un responsable confirmado y un comparador viable. El estado [instrumentado, no ejecutado](b2b-proposal/index.md) separa el protocolo de los resultados de un piloto real.
