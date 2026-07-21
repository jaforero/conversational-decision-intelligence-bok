---
id: ADR-017
title: Ratificación y promoción estable del núcleo fundacional v0.4.0
status: accepted
date: 2026-07-21
decider: Javier Forero
domains:
  - Foundations
  - Decision Governance
---

# ADR-017: Ratificación y promoción estable del núcleo fundacional v0.4.0

## Contexto

El núcleo fundacional se publicó inicialmente como `v0.4.0-rc.1` para separar su revisión humana de su disponibilidad técnica. El candidato incluye la Constitución del CDI-BoK, la definición y fronteras de CDI, el glosario controlado, el mapa de dominios y la especificación pública derivada de PULSE.

Javier Forero ratificó explícitamente el portal y su núcleo fundacional el 21 de julio de 2026. Los controles editoriales, técnicos, visuales y de accesibilidad automatizada del candidato terminaron en verde antes de la ratificación.

## Decisión

Promover `v0.4.0-rc.1` a la release estable `v0.4.0` con la siguiente autoridad:

| Activo | Estado | Autoridad | Normativo dentro del proyecto |
|---|---|---|---:|
| Constitución del CDI-BoK | `approved` | `foundational-approved` | Sí |
| Alcance y fronteras de CDI | `approved` | `institutional-approved` | Sí |
| Glosario controlado | `approved` | `approved-controlled` | Sí |
| Mapa de dominios | `approved` | `approved-controlled` | Sí |
| Especificación nuclear de PULSE | `approved` | `constitutional-derived-approved` | No |

El estado editorial continúa usando el vocabulario de ADR-004. Los calificadores `approved-controlled` y `constitutional-derived-approved` son niveles de autoridad, no estados adicionales.

La definición de CDI es oficial para el proyecto, pero continúa presentando CDI como un dominio de práctica interdisciplinar propuesto. La especificación pública de PULSE conserva autoridad derivada y no sustituye sus fuentes constitucionales.

## Gate de release

El tag y GitHub Release `v0.4.0` solo se crean desde `main` después de:

1. validar la ratificación, los estados y los registros;
2. ejecutar el preflight editorial y el build estricto;
3. aprobar las comparaciones visuales canónicas;
4. aprobar las reglas automatizadas Axe;
5. confirmar que el tag no apunta a otro commit.

## Consecuencias

- `decision.javierforero.co` puede presentar `v0.4.0` como release estable del proyecto;
- las páginas candidatas de Research, Practice Lab y otros activos no ratificados permanecen candidatas;
- estabilidad editorial no equivale a reconocimiento académico, estandarización externa o eficacia generalizable;
- la evidencia empírica y la revisión externa siguen siendo trabajo futuro;
- cualquier cambio posterior a los activos normativos debe seguir control de versión y revisión explícita.

