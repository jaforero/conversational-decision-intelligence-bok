---
id: ADR-005
title: Modelo de versiones
status: superseded
date: 2026-07-19
decider: Javier Forero
superseded_by: ADR-022
---

# ADR-005: Modelo de versiones

> **Estado:** sustituido por ADR-022 el 21 de julio de 2026. Se conserva como registro de la decisión inicial; la política vigente distingue releases estables, hitos aprobados y candidatos desplegados.

## Decisión

El CDI-BoK usa SemVer en el nivel de release y versiones independientes en el front matter de cada activo. `0.x` indica desarrollo fundacional; no implica estabilidad de `1.0`.

## Consecuencias

Cada release tendrá tag y changelog. Un cambio incompatible de definición normativa incrementa la versión mayor del activo y deberá reflejarse en el release cuando afecte el contrato público.

La obligación indiscriminada de tag fue reemplazada porque no distinguía entre una release estable y un release candidate desplegado para evaluación.
