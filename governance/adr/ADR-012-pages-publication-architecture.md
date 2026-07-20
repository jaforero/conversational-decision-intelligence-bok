---
id: ADR-012
title: Arquitectura de publicación con GitHub Actions y Pages
status: accepted
date: 2026-07-20
decider: Javier Forero
domains:
  - Decision Governance
  - Enterprise Implementation
---

# ADR-012: Arquitectura de publicación con GitHub Actions y Pages

## Decisión

El portal se construye con MkDocs Material y se despliega mediante un workflow personalizado de GitHub Actions. `main` es la única rama desplegable; los pull requests construyen y validan, pero no publican producción. No se mantiene una rama `gh-pages` como doctrina técnica paralela.

El artefacto estático se publica con las acciones oficiales `configure-pages`, `upload-pages-artifact` y `deploy-pages`, separando los jobs de build y deploy y limitando permisos a `contents: read`, `pages: write` e `id-token: write` según corresponda.

`docs/CNAME` conserva el dominio objetivo dentro del repositorio y del artefacto, pero el dominio también debe configurarse en GitHub Pages. Con workflows personalizados, GitHub no deriva automáticamente esa configuración del archivo.

El versionado web con `mike` se difiere hasta que existan al menos dos releases históricas que aporten valor real al lector. Git tags y Releases conservan entretanto la historia fuente.

## Consecuencias

- Un merge a `main` puede activar un despliegue de producción.
- Pages debe habilitarse manualmente una vez con fuente GitHub Actions.
- El DNS de `decision.javierforero.co` es una dependencia externa y no puede resolverse desde el repositorio.
- El build es reproducible localmente con `requirements.lock` y `mkdocs build --strict`.

