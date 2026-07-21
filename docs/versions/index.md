---
title: Versiones
description: Releases normativas, candidatos del portal y política de historia del CDI-BoK.
status: candidate
version: 0.6.0-rc.1
artifact_type: version-index
authority_level: guidance
normative: false
owner: Javier Forero
domains:
  - Decision Governance
last_reviewed: 2026-07-21
---

# Versiones

## Estado actual

| Componente | Versión | Estado | Alcance |
|---|---|---|---|
| Gobernanza CDI-BoK | `v0.2.0` | Aprobada y normativa | Arquitectura, autoridad, claims, marca y Sprint 0 |
| Portal técnico | `v0.3.0-rc.1` | Integrado | MkDocs, navegación, CI/CD, checks y dominio personalizado |
| Núcleo fundacional | [`v0.4.0`](v0.4.0.md) | Estable | Constitución, fronteras CDI, glosario, dominios y especificación PULSE |
| Práctica y evidencia | [`v0.5.0-rc.1`](v0.5.0-rc.1.md) | Candidato | Catálogo y primer caso B2B instrumentado, sin outcome observado |
| Aprendizaje y experiencia | [`v0.6.0-rc.1`](v0.6.0-rc.1.md) | Candidato actual | Portada orientada a resultados, cinco módulos y Decision Brief |

La versión del portal no eleva automáticamente la madurez doctrinal del contenido. Infraestructura, conocimiento y evidencia pueden evolucionar a ritmos distintos, pero siempre deben conservar trazabilidad.

## Política inicial

- Git tags y GitHub Releases preservan versiones fuente.
- `decision.javierforero.co` muestra la última release pública aprobada.
- Borradores no aparecen en navegación estable.
- El selector de versiones web se incorporará cuando existan al menos dos releases históricas útiles para el lector.

!!! note "Por qué no existe un v0.1.0 posterior"
    La hoja de ruta inicial nombró la salida de Sprint 2 como `v0.1.0`, pero la secuencia ya había publicado `v0.2.0` y `v0.3.0-rc.1`. ADR-014 asignó `v0.4.0-rc.1` al candidato; ADR-017 registra su ratificación y promoción estable a `v0.4.0`.

## Historial

Consulte el [`CHANGELOG.md`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/CHANGELOG.md) y las [releases del repositorio](https://github.com/jaforero/conversational-decision-intelligence-bok/releases).
