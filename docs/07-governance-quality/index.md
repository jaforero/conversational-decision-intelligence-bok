---
title: Calidad y medición de decisiones
description: Sistema candidato para evaluar el proceso antes de decidir, observar la ejecución y aprender de resultados sin confundir outcome con calidad.
status: candidate
version: 0.7.0-rc.1
artifact_type: knowledge-area-landing
authority_level: candidate-synthesis
normative: false
owner: Javier Forero
domains:
  - Decision Quality
  - Decision Metrics
  - Decision Governance
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-DQ-SDP-001
  - SRC-ACADEMIC-OUTCOME-BIAS-001
  - SRC-ACADEMIC-SCORING-RULES-001
claim_ids:
  - CLAIM-DQ-OUTCOME-001
  - CLAIM-DQ-PROFILE-001
  - CLAIM-DM-SYSTEM-001
last_reviewed: 2026-07-21
---

# Calidad y medición de decisiones

Medir una decisión no consiste en preguntar si “salió bien”. Una decisión material debe poder examinarse en tres momentos distintos:

1. **antes de decidir:** calidad del encuadre, alternativas, evidencia, valores, razonamiento y compromiso;
2. **durante la ejecución:** latencia, fidelidad de la acción, escalamiento, overrides y guardrails;
3. **después del horizonte:** resultado, desviación frente a expectativa, atribución prudente y cambio del siguiente ciclo.

El sistema candidato de Sprint 5 conecta esos momentos sin colapsarlos en una nota universal.

<div class="cdi-grid cdi-grid--3">

<a class="cdi-card" href="decision-quality/" aria-label="Examinar la calidad de una decisión antes de conocer el resultado">
<span class="cdi-card__index">ANTES</span>
<h3>Calidad de la decisión</h3>
<p>Revisa si la decisión es defendible antes de que el resultado introduzca sesgo retrospectivo.</p>
</a>

<a class="cdi-card" href="decision-measurement-system/" aria-label="Diseñar métricas para un ciclo de decisión">
<span class="cdi-card__index">CICLO</span>
<h3>Sistema de medición de decisiones</h3>
<p>Selecciona una cartera mínima de métricas para prioridad, calidad, acción, tiempo, riesgo y aprendizaje.</p>
</a>

<a class="cdi-card" href="measurement-record/" aria-label="Crear un registro de medición para una decisión">
<span class="cdi-card__index">ARTEFACTO</span>
<h3>Registro de medición de decisiones</h3>
<p>Prerregistra expectativa y medición; después agrega el outcome sin reescribir lo que se sabía al decidir.</p>
</a>

</div>

## Qué problema resuelve

Un dashboard puede mostrar resultados y una reunión puede producir una decisión, pero ninguno conserva necesariamente:

- qué se esperaba antes de actuar;
- qué parte del proceso estaba débil;
- si la acción ocurrió como fue autorizada;
- qué riesgo o grupo absorbió el costo;
- si el outcome fue compatible con la expectativa;
- qué cambió en la siguiente decisión.

Sin esa separación, un buen outcome puede legitimar un proceso deficiente y un mal outcome puede castigar una decisión razonable bajo incertidumbre.

## La unidad de medición

La unidad mínima es un **ciclo de decisión identificado**, no una herramienta, una persona ni una iniciativa de IA. El ciclo debe declarar owner, fecha, opciones, acción, expectativa, horizonte y revisión. Solo después de disponer de ciclos comparables tiene sentido agregar métricas de portafolio.

!!! warning "No existe una métrica universal"
    La calidad depende de stakes, reversibilidad, frecuencia, incertidumbre y personas afectadas. El sistema propone una arquitectura y contratos de medición; no un benchmark universal ni una prueba validada de madurez organizacional.

## Relación con PULSE

PULSE exige que el valor sea observable y que el aprendizaje compare expectativa con resultado. Esta sección **operacionaliza** esas exigencias para el CDI-BoK; no redefine PULSE ni demuestra que la instrumentación produzca mejores outcomes.

[Diseñar la medición de una decisión →](decision-measurement-system.md){ .md-button .md-button--primary }
[Volver al módulo de acción y aprendizaje](../learn/05-action-learning.md){ .md-button }
