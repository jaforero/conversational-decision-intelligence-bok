---
title: Research
description: Ruta trazable para distinguir fundamentos, evidencia emergente, síntesis PULSE, hipótesis y señales futuras.
status: candidate
version: 0.9.0-rc.1
artifact_type: research-landing
authority_level: evidence-map
normative: false
owner: Javier Forero
domains:
  - Research
  - Future Directions
claim_ids: [CLAIM-DI-MATURITY-001, CLAIM-DI-LAYERS-001, CLAIM-FUTURE-SIGNALS-001]
source_ids: [SRC-ACADEMIC-DECISION-ANALYSIS-001, SRC-OMG-DMN-001, SRC-NIST-AIRMF-001, SRC-ACADEMIC-HAI-001, SRC-ACADEMIC-AIEVAL-001]
last_reviewed: 2026-07-24
---

# Research

<span class="cdi-release">Evidence Backbone · Candidato v0.9.0-rc.1</span>

El CDI-BoK no utiliza “Deep Research” como sinónimo de evidencia validada. Las
síntesis asistidas por IA sirven para localizar conceptos, tensiones y
referencias candidatas; cada fuente material debe verificarse contra su original
y evaluarse según el claim que pretende sostener.

## Empieza por tu pregunta

| Si necesitas… | Ruta | Resultado |
|---|---|---|
| entender qué es DI y qué tan maduro es el campo | [Estado del arte de DI](decision-intelligence-state-of-the-art.md) | fundamentos, fronteras, disputas y límites |
| saber qué partes de PULSE tienen qué autoridad | [Mapa de evidencia de PULSE](pulse-evidence-map.md) | constitucional, derivado, candidato, hipótesis o no evaluado |
| usar tendencias sin tratarlas como hechos | [Señales futuras](future-signals.md) | escenarios, horizontes y condiciones de revisión |
| decidir qué estudiar después | [Agenda de investigación](research-agenda.md) | preguntas falsables y diseños mínimos |

## Cómo está organizado el conocimiento

| Capa | Ejemplos | Regla |
|---|---|---|
| Fundamentos establecidos | Decision Analysis, DSS, calidad de información, outcome bias | fuente primaria u oficial y límites de aplicación |
| Prácticas maduras en evolución | DMN, EDM, gobernanza de datos y riesgo de IA | versión y fecha `as_of` |
| Campos emergentes | deliberación humano–IA, analítica conversacional y agentes | evidencia dependiente del contexto |
| Síntesis PULSE | PDAMR, Decision Circle, cinco verbos y Human-in-Control | autoridad del proyecto, no eficacia independiente |
| Hipótesis y metáforas | alostasis, interocepción y organismo decisional | predicción observable y posibilidad de abandono |
| Señales futuras | cambios esperados en interfaces, agentes y gobernanza | escenario, no hecho ni readiness |

## Backbone verificable

El registro `governance/registries/evidence-profiles.yml` conserva hash,
procedencia, completitud, derechos, uso permitido y ocho dimensiones sin
convertirlas en una nota total. `ADR-028` bloquea fuentes incompletas, síntesis
asistidas como soporte directo y pronósticos usados como hechos.

<div class="cdi-risk" markdown>
**Riesgo central:** confundir novedad de lenguaje con novedad teórica, y novedad
teórica con eficacia demostrada.
</div>
