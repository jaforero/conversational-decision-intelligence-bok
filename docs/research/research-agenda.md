---
title: Agenda de investigación
description: Preguntas falsables, diseños mínimos y criterios de actualización para fortalecer Decision Intelligence, CDI y PULSE.
status: candidate
version: 0.9.0-rc.1
artifact_type: research-agenda
authority_level: candidate-research-guidance
normative: false
owner: Javier Forero
domains: [Research, Evidence Quality, Decision Measurement]
claim_ids: [CLAIM-DI-MATURITY-001, CLAIM-HUMAN-AI-EVIDENCE-001, CLAIM-PULSE-SYNTHESIS-001, CLAIM-PULSE-BIOLOGICAL-LENSES-001]
source_ids: [SRC-ACADEMIC-HAI-001, SRC-ACADEMIC-AIEVAL-001, SRC-ACADEMIC-RUDIN-001, SRC-ACADEMIC-OUTCOME-BIAS-001, SRC-ACADEMIC-SCORING-RULES-001, SRC-PRACTICE-B2B-001]
last_reviewed: 2026-07-24
---

# Agenda de investigación

La agenda convierte vacíos en decisiones de investigación. Prioriza preguntas
que podrían **reducir** un claim, no solo confirmarlo.

## Prioridades

| Prioridad | Pregunta falsable | Diseño mínimo | Señal de avance | Riesgo |
|---|---|---|---|---|
| P1 · Campo DI | ¿El corpus DI tiene comunidad, métodos y evidencia acumulativa propios? | revisión sistemática preregistrada y mapa bibliométrico | criterios y búsqueda reproducibles | confundir ausencia en la muestra con ausencia real |
| P1 · Humano–IA | ¿Cuándo humano+IA supera a humano e IA sola? | comparación por tarea con asignación y outcomes definidos | efecto, heterogeneidad, daño y costo | automatización complaciente o deskilling |
| P1 · Control | ¿Qué controles cambian conducta cuando un agente puede actuar? | pruebas de override, stop y reversión | tasa de intervención y recuperación | control ceremonial |
| P2 · PULSE | ¿PDAMR reduce omisiones relevantes frente al proceso actual? | piloto preregistrado con comparador | completitud, latencia, carga y calidad ex ante | burocracia y gaming |
| P2 · Aprendizaje | ¿El registro longitudinal mejora calibración o solo documentación? | decisiones repetidas y feedback comparable | calibración, revisión y cambio observable | outcome bias |
| P2 · Decision Experience | ¿Qué combinación de conversación, visualización y workflow funciona por tarea? | estudio factorial o secuencial | exactitud, comprensión, tiempo y accesibilidad | fluidez confundida con calidad |
| P3 · Metáforas | ¿Las lentes biológicas generan predicciones útiles y diferenciables? | hipótesis observables sin lenguaje metafórico | predicción que pueda fallar | antropomorfismo |

## Contratos mínimos

Todo estudio del programa debe declarar:

- decisión y unidad de análisis;
- población, contexto y exclusiones;
- comparador pertinente;
- outcomes y guardrails separados de adopción;
- tiempo de medición y datos faltantes;
- autoridad humana y protocolo de incidentes;
- análisis de heterogeneidad y resultados adversos;
- materiales, versión del sistema y desviaciones;
- criterio para elevar, mantener o reducir cada claim.

## Primer piloto recomendado

El caso B2B puede servir como prueba de instrumentación, pero no debe pasar
directamente de datos simulados a un claim de eficacia. La siguiente decisión es
si existe un owner, una operación autorizada y un comparador viable. Si no
existen, el caso permanece detenido.

Una prueba inicial más segura mediría si PDAMR y el Decision Brief reducen
omisiones de proceso en decisiones históricas o simuladas, sin permitir que la
IA ejecute acciones. Ese resultado informaría usabilidad y cobertura, no impacto
causal en ventas.

## Cadencia de revisión

- trimestral: estándares, marcos y señales futuras;
- por release candidata: fuentes, claims y traducciones;
- después de cada estudio: resultados nulos, adversos y desviaciones;
- anual: búsqueda reproducible del estado del arte;
- extraordinaria: cambio regulatorio, incidente material o nueva evidencia
  contradictoria.

## Criterio de éxito

El programa avanza cuando un claim se vuelve más preciso, aunque su fuerza
disminuya. Producir más páginas o más uso del portal no demuestra mejores
decisiones.
