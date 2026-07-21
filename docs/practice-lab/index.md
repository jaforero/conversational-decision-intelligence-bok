---
title: Practice Lab
description: Extensión práctica del CDI-BoK con catálogo verificable y primer caso instrumentado.
status: candidate
version: 0.5.0-rc.1
artifact_type: practice-landing
authority_level: experimental
normative: false
owner: Javier Forero
domains:
  - Case Studies
  - Decision Patterns
  - Enterprise Implementation
source_ids:
  - SRC-PRACTICE-DASH-ROOT-001
  - SRC-PRACTICE-GPT-ROOT-001
claim_ids: []
last_reviewed: 2026-07-21
---

# Practice Lab

El Practice Lab conecta el Body of Knowledge con experiencias observables. Su propiedad externa es la galería [Dashboards con IA](https://dashboards.javierforero.co), que reúne dos portafolios creados bajo la dirección analítica de Javier Forero.

<div class="cdi-practice-card" markdown>
<span class="cdi-eyebrow">EXTENSIÓN PRÁCTICA</span>

## Dashboard and Decision Experience Gallery

Explora interfaces analíticas construidas con IA y observa la transición desde visualización hacia experiencias de decisión.

[Abrir el catálogo verificado](catalog.md){ .md-button .md-button--primary }
[Visitar dashboards.javierforero.co](https://dashboards.javierforero.co){ .md-button }
</div>

## Primer caso instrumentado

<div class="cdi-practice-card" markdown>
<span class="cdi-eyebrow">SPRINT 3 · v0.5.0-rc.1</span>

### Comercial B2B · intervención sobre Propuesta

El caso convierte tres fuentes simuladas —ventas, funnel y pipeline CRM— en un contrato falsable con alternativas, baseline, expectativa previa, contrafactual y registro de aprendizaje.

**Estado:** instrumentado, no ejecutado. No existe todavía evidencia de impacto comercial.

[Examinar el caso](b2b-proposal/index.md){ .md-button .md-button--primary }
</div>

## Una demo no es todavía un caso

Para ingresar al CDI-BoK como caso, una demostración debe registrar al menos:

1. decisión y contexto;
2. usuarios y responsabilidad;
3. datos disponibles y limitaciones;
4. baseline anterior;
5. intervención o experiencia diseñada;
6. acción tomada;
7. resultado observado;
8. aprendizaje y relación con PULSE.

ADR-018 añade una secuencia explícita: `catalogued → selected → instrumented-not-executed → observed-noncausal → evaluated`. Publicar una demo no permite saltar etapas.

!!! warning "Límite de evidencia"
    Una interfaz convincente demuestra capacidad de diseño. No prueba por sí sola que una organización decidió mejor, actuó con mayor calidad o produjo mejores resultados.
