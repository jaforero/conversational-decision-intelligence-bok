---
id: ADR-024
title: Promoción estable del portal integrado v0.8.0
status: accepted
date: 2026-07-21
decider: Javier Forero
domains:
  - Decision Governance
  - Publication Architecture
---

# ADR-024: Promoción estable del portal integrado v0.8.0

## Contexto

`v0.8.0-rc.1` completó Sprint 6 con cinco patrones, seis anti-patrones, plantilla, registro y demostración B2B detenida. El PR #10 fue fusionado en `main` mediante `bbc5c0583b28bbc3d4d2b6a2aedf28f8df336347`; la validación post-merge `29871891960`, el despliegue `29871892015` y la verificación pública HTTP 200 terminaron correctamente.

Javier Forero autorizó explícitamente el 21 de julio de 2026 preparar el PR #11 para promover `v0.8.0` como release estable. La decisión requiere evitar una equivalencia engañosa entre estabilidad del portal, autoridad editorial de cada activo y evidencia de eficacia.

## Decisión

Promover `v0.8.0-rc.1` a **`v0.8.0` como línea base editorial y técnica estable del portal integrado**.

La promoción acepta:

- el build reproducible y la arquitectura pública del portal;
- la navegación y los contratos de calidad automatizada;
- la integridad del linaje, los registros, las fuentes y los límites de claims;
- la coexistencia explícita de componentes con distintas autoridades y madureces.

La promoción no cambia en bloque el estado editorial de los activos incluidos.

| Componente | Autoridad o madurez preservada |
|---|---|
| Gobernanza `v0.2.0` | Aprobada y normativa dentro del proyecto |
| Núcleo `v0.4.0` | Aprobado con autoridad diferenciada |
| Caso `v0.5.0-rc.1` | Candidato, instrumentado y no ejecutado |
| Aprendizaje `v0.6.0-rc.1` | Guía candidata ratificada |
| Medición `v0.7.0-rc.1` | Síntesis candidata ratificada |
| Patrones `v0.8.0-rc.1` | Taxonomía candidata ratificada |

## Gate de release

El tag y GitHub Release `v0.8.0` solo se crean desde el SHA de `main` que contiene esta decisión, después de:

1. validar el cierre ratificado, fusionado y desplegado de Sprint 6;
2. verificar el manifiesto estable, la nota pública y el registro de linaje;
3. ejecutar el preflight acumulado y el build estricto;
4. aprobar la regresión visual y los análisis Axe en el runner canónico;
5. comprobar que el tag no existe sobre otro commit;
6. resolver versión, título y notas desde el manifiesto estable, sin valores codificados para una release histórica.

El workflow `.github/workflows/release.yml` crea el tag sobre `GITHUB_SHA`; por ello el registro usa `refs/tags/v0.8.0` como referencia resoluble y conserva por separado el SHA de merge del candidato.

## Límites de interpretación

- Estabilidad técnica no es validación científica de CDI o PULSE.
- Ratificación editorial no demuestra que los patrones mejoren decisiones u outcomes.
- La presencia de un caso instrumentado no prueba ejecución ni impacto.
- Los controles automatizados no establecen conformidad completa con WCAG 2.2 AA.
- La release `0.x` continúa siendo una etapa fundacional y no equivale a madurez `1.0`.

## Consecuencias

- `decision.javierforero.co` puede identificar su build integrado como `v0.8.0` estable;
- `v0.8.0-rc.1` queda cerrado como candidato ratificado, fusionado, desplegado y promovido, pero permanece sin tag;
- el tag `v0.8.0` y su GitHub Release serán la referencia inmutable del bundle estable;
- los estados candidatos siguen visibles para impedir que la estabilidad del contenedor eleve artificialmente la evidencia del contenido;
- una modificación futura del bundle requiere una nueva versión, no reescribir el tag estable.
