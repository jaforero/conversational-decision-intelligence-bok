---
id: ADR-021
title: Arquitectura de calidad y medición de decisiones
status: accepted
date: 2026-07-21
decision_owner: Javier Forero
scope: Sprint 5 decision quality and measurement candidate
---

# ADR-021: Arquitectura de calidad y medición de decisiones

## Contexto

El mapa estable `v0.4.0` declara Decision Quality como parcialmente establecido y Decision Metrics como sistema CDI por desarrollar. Sprint 4 enseña a fijar expectativa, outcome y aprendizaje, pero no proporciona todavía una arquitectura suficientemente precisa para seleccionar, calcular y gobernar métricas.

No hay una muestra longitudinal de decisiones organizacionales reales que permita validar un instrumento universal. Crear un índice sintético en esta etapa produciría comunicabilidad a costa de validez, comparabilidad y resistencia al gaming.

## Decisión

Crear `v0.7.0-rc.1` como candidato de **Decision Quality & Measurement** con estas reglas:

1. La unidad mínima será un ciclo de decisión identificado, no una herramienta, equipo o proyecto de IA.
2. La medición separará calidad ex ante, ejecución, latencia, outcome, guardrails y aprendizaje.
3. La calidad se representará como perfil por dimensiones, evidencia y bloqueadores; no como puntuación universal.
4. Baseline, expectativa, horizonte y regla de respuesta se fijarán antes de la acción.
5. La calibración probabilística se aplicará solo a eventos repetidos, comparables y definidos ex ante.
6. Overrides, acuerdo y adopción humano–IA se interpretarán junto con exactitud, contexto, riesgo y outcome; ninguna tasa aislada equivaldrá a calidad.
7. El Measurement Record mantendrá un snapshot de decisión y una revisión posterior sin sobrescritura retrospectiva.
8. La carga de medición será proporcional a stakes, incertidumbre, reversibilidad y daño potencial.

## Autoridad

- La separación entre expectativa, resultado y aprendizaje deriva del PULSE DNA.
- La cadena de Decision Quality se atribuye a la Society of Decision Professionals.
- Outcome bias y reglas de puntuación propias se presentan con fuentes académicas explícitas.
- El sistema de seis lentes es una síntesis candidata del CDI-BoK, no un estándar externo ni un instrumento validado.

## Consecuencias

- Decision Metrics pasa de dominio declarado a guía pública candidata.
- Aumentan los campos que una implementación puede instrumentar, pero no todos son obligatorios.
- El BoK puede evaluar trazabilidad antes de disponer de impacto organizacional.
- No se altera la autoridad del núcleo estable `v0.4.0` ni el estado del caso B2B.

## Contraargumento

Un índice único facilitaría benchmarking, venta ejecutiva y seguimiento. Sin embargo, permitiría compensar un bloqueador crítico con fortalezas irrelevantes y mezclaría decisiones de stakes y horizontes incompatibles. El perfil multidimensional es menos atractivo, pero más honesto para la evidencia disponible.

## Alternativa potencialmente superior

Después de observar suficientes ciclos reales, diseñar y validar un instrumento con acuerdo entre revisores, sensibilidad, estabilidad, resistencia al gaming y utilidad predictiva. Esa evidencia podría justificar pesos, retirar dimensiones o crear benchmarks por clase de decisión.

