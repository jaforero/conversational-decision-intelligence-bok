---
id: ADR-005
title: Modelo de versiones
status: accepted
date: 2026-07-19
decider: Javier Forero
---

# ADR-005: Modelo de versiones

## Decisión

El CDI-BoK usa SemVer en el nivel de release y versiones independientes en el front matter de cada activo. `0.x` indica desarrollo fundacional; no implica estabilidad de `1.0`.

## Consecuencias

Cada release tendrá tag y changelog. Un cambio incompatible de definición normativa incrementa la versión mayor del activo y deberá reflejarse en el release cuando afecte el contrato público.

