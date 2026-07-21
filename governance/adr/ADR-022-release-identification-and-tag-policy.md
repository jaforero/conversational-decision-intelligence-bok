---
id: ADR-022
title: Identificación de releases, candidatos y política de tags
status: accepted
date: 2026-07-21
decider: Javier Forero
supersedes: ADR-005
scope: Release lineage and immutable Git identification
---

# ADR-022: Identificación de releases, candidatos y política de tags

## Contexto

ADR-005 estableció que cada release tendría tag y changelog. La regla no distinguía entre una release estable, un hito de gobernanza aprobado y un release candidate desplegado para revisión. El repositorio materializó `v0.5.0-rc.1`, `v0.6.0-rc.1` y `v0.7.0-rc.1` mediante notas, manifiestos, PR, commits y despliegues, pero no creó tags para esos candidatos.

Crear tags retrospectivos ahora exigiría seleccionar después del hecho qué commit representa cada RC. Esa elección podría confundir el primer merge funcional, el cierre documental y el estado actualmente servido por el portal. La ausencia de tag es una brecha de política, no evidencia de que los candidatos no sean trazables.

## Decisión

El CDI-BoK conserva SemVer para identificar versiones del portal y de sus releases, con las siguientes clases:

1. **Release estable:** requiere tag inmutable `vX.Y.Z`, changelog, nota pública, manifiesto, ratificación, gates y GitHub Release.
2. **Hito de gobernanza aprobado:** puede usar tag inmutable cuando el ADR o manifiesto que lo aprueba así lo declare. El tag no convierte automáticamente el portal o todo su contenido en estable.
3. **Release candidate:** usa identificador SemVer de pre-release, changelog, nota pública, manifiesto, PR, commit de merge y evidencia de validación y despliegue. El tag es opcional y solo se crea si el owner autoriza explícitamente congelar ese candidato como artefacto distribuible inmutable.
4. **Draft o review:** no recibe tag ni se presenta como release pública.

La ratificación, el despliegue y la estabilidad son dimensiones diferentes. Un candidato puede estar ratificado y desplegado sin convertirse en release estable. La versión visible del portal identifica el build público actual; no eleva por sí sola la autoridad doctrinal o la madurez de evidencia de todos sus activos.

## Regla de no retroactividad

No se crearán tags retrospectivos para candidatos históricos únicamente para uniformar la apariencia del historial. Solo podrán crearse si:

- el commit exacto que fue aprobado puede reconstruirse sin ambigüedad;
- existe una razón de distribución o auditoría que requiera congelarlo;
- el owner autoriza explícitamente el tag; y
- la nota de release explica que se creó con posterioridad.

Mientras esas condiciones no se cumplan, el registro `governance/releases/index.yml`, los manifiestos, los PR y los SHA de merge preservan la línea de procedencia.

## Gate mínimo por clase

| Evidencia | Candidato desplegado | Release estable |
|---|---:|---:|
| Changelog y nota pública | Obligatoria | Obligatoria |
| Manifiesto y estado de autoridad | Obligatorio | Obligatorio |
| PR y SHA de merge | Obligatorios | Obligatorios |
| Validación y despliegue reproducibles | Obligatorios | Obligatorios |
| Ratificación del owner | Para declarar “ratificado” | Obligatoria |
| Tag Git inmutable | Opcional con autorización | Obligatorio |
| GitHub Release | Opcional y marcada pre-release | Obligatoria |
| Evidencia de impacto | Según el claim; nunca implícita | Según el claim; nunca implícita |

## Consecuencias

- ADR-005 queda `superseded`; se preserva como registro histórico.
- `v0.5.0-rc.1`, `v0.6.0-rc.1` y `v0.7.0-rc.1` permanecen sin tag por decisión explícita, no por omisión silenciosa.
- `v0.7.0-rc.1` puede registrarse como candidato ratificado, fusionado y desplegado sin promover `v0.7.0`.
- El tag y GitHub Release `v0.4.0` continúan identificando el núcleo fundacional estable.
- Cada cierre futuro debe actualizar el registro de releases y verificar que el lenguaje público no confunda versión del portal, autoridad del contenido o fuerza de evidencia.
