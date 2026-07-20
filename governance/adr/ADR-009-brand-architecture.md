---
id: ADR-009
title: Arquitectura de marca del ecosistema CDI
status: accepted
date: 2026-07-19
decider: Javier Forero
domains:
  - Foundations
  - Decision Governance
  - Enterprise Implementation
---

# ADR-009: Arquitectura de marca del ecosistema CDI

## Contexto

El CDI-BoK necesita autoridad institucional y continuidad con `javierforero.co` y `dashboards.javierforero.co`, sin convertir un estándar de conocimiento en un portafolio personal ni fragmentar la identidad en marcas competidoras.

## Decisión

Se adopta una arquitectura de **marca endosada**:

`Javier Forero → CDI-BoK → PULSE / Dashboards Practice Lab`

- **Javier Forero** es el masterbrand respaldante, owner y firma editorial.
- **CDI-BoK** es la identidad institucional del sistema de conocimiento.
- **PULSE** es el framework oficial de práctica; no sustituye al CDI-BoK.
- **Dashboards** es una extensión práctica externa, gobernada por ADR-006.

El respaldo se expresa de forma compacta en encabezado, metadatos de autoría y sello de pie. Las páginas normativas no usarán llamados comerciales. No se creará un logotipo provisional: hasta que exista un activo aprobado, la identidad CDI-BoK será tipográfica.

## Contrato visual

La fuente técnica es `brand/brand-source.yml`; los valores ejecutables viven en `brand/tokens.json`. El morado funciona como acento, el azul profundo sostiene autoridad y se permite un solo gradiente dominante por composición.

## Consecuencias

- El portal y el Practice Lab comparten familia visual, no navegación ni autoridad de contenido.
- Una nueva submarca, logo, sello o cambio de jerarquía exige ADR.
- La marca personal aporta procedencia; la evidencia y el estado editorial aportan credibilidad epistémica.

## Alternativas descartadas

- **Marca CDI-BoK completamente independiente:** pierde continuidad y duplica el esfuerzo de reconocimiento en fase fundacional.
- **Marca personal dominante en todas las páginas:** confunde autoría con autoridad normativa y degrada la lectura de estándar.
- **Unificar CDI-BoK y dashboards en un solo sitio:** mezcla conocimiento gobernado con demostraciones de distinta madurez.

