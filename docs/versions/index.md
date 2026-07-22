---
title: Versiones
description: Releases normativas, candidatos del portal y política de historia del CDI-BoK.
status: candidate
version: 0.8.2
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
| Portal bilingüe | [`v0.8.2`](v0.8.2.md) | Estable editorial y técnicamente | Localización española, claridad para negocio y búsqueda independiente ES/EN |
| Línea base bilingüe anterior | [`v0.8.1`](v0.8.1.md) | Estable e histórica | Rutas ES/EN completas, interfaz localizada y gates contra deriva de traducción |
| Candidato bilingüe fuente | [`v0.8.1-rc.1`](v0.8.1-rc.1.md) | Ratificado, fusionado, desplegado y promovido | Fuente trazable de la release estable `v0.8.1` |
| Portal integrado | [`v0.8.0`](v0.8.0.md) | Estable editorial y técnicamente | Build reproducible, navegación, trazabilidad, gates y límites de autoridad |
| Gobernanza CDI-BoK | `v0.2.0` | Aprobada y normativa | Arquitectura, autoridad, claims, marca y Sprint 0 |
| Portal técnico | `v0.3.0-rc.1` | Integrado y desplegado | MkDocs, navegación, CI/CD, checks y dominio personalizado |
| Núcleo fundacional | [`v0.4.0`](v0.4.0.md) | Estable | Constitución, fronteras CDI, glosario, dominios y especificación PULSE |
| Práctica y evidencia | [`v0.5.0-rc.1`](v0.5.0-rc.1.md) | Candidato desplegado, no ratificado | Catálogo y primer caso B2B instrumentado, sin outcome observado |
| Aprendizaje y experiencia | [`v0.6.0-rc.1`](v0.6.0-rc.1.md) | Candidato ratificado y desplegado | Portada orientada a resultados, cinco módulos y Decision Brief |
| Calidad y medición | [`v0.7.0-rc.1`](v0.7.0-rc.1.md) | Candidato ratificado y desplegado | Decision Quality, seis lentes, anti-métricas y Measurement Record |
| Patrones conversacionales | [`v0.8.0-rc.1`](v0.8.0-rc.1.md) | Candidato ratificado, fusionado y desplegado | Cinco patrones, seis anti-patrones, lenguaje, plantilla y demostración B2B detenida |

La versión del portal no eleva automáticamente la madurez doctrinal del contenido. Infraestructura, conocimiento y evidencia pueden evolucionar a ritmos distintos, pero siempre deben conservar trazabilidad.

## Política vigente

- Las releases estables requieren tag inmutable y GitHub Release.
- Los candidatos se trazan mediante nota, changelog, manifiesto, PR, SHA de merge, validación y despliegue. Solo reciben tag cuando el owner autoriza explícitamente congelarlos como pre-release inmutable.
- Ratificación, despliegue y estabilidad son estados diferentes: un candidato ratificado y desplegado no se vuelve estable automáticamente.
- `decision.javierforero.co` muestra el último build público fusionado; la versión del portal no eleva la autoridad ni la fuerza de evidencia de todos sus contenidos.
- Borradores no aparecen en navegación estable.
- El español permanece canónico durante `0.x`; cada página inglesa se vincula a su fuente, versión y hash en un registro controlado.
- El selector de versiones web se incorporará cuando existan al menos dos releases históricas útiles para el lector.

ADR-022 sustituye la regla inicial de ADR-005 y evita crear tags retrospectivos ambiguos. El registro controlado `governance/releases/index.yml` conserva la línea completa. Los RC históricos permanecen intencionalmente sin tag; `v0.8.0`, `v0.8.1` y `v0.8.2` reciben sus referencias inmutables únicamente desde gates posteriores al merge gobernados por ADR-024, ADR-026 y ADR-027.

!!! note "Por qué no existe un v0.1.0 posterior"
    La hoja de ruta inicial nombró la salida de Sprint 2 como `v0.1.0`, pero la secuencia ya había publicado `v0.2.0` y `v0.3.0-rc.1`. ADR-014 asignó `v0.4.0-rc.1` al candidato; ADR-017 registra su ratificación y promoción estable a `v0.4.0`.

## Historial

Consulte el [`CHANGELOG.md`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/CHANGELOG.md) y las [releases del repositorio](https://github.com/jaforero/conversational-decision-intelligence-bok/releases).
