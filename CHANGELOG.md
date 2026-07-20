# Changelog

Todos los cambios relevantes del CDI-BoK se documentan en este archivo.

## [0.3.0-rc.1] - 2026-07-20

### Añadido

- Portal MkDocs Material con navegación pública progresiva de nueve rutas.
- Páginas iniciales para orientación, CDI-BoK, PULSE, Practice Lab, Research, gobernanza, versiones y autoría.
- Sincronización ejecutable de design tokens y de la norma editorial publicada.
- Modos claro y oscuro, diseño adaptable y personalización coherente con la marca Javier Forero.
- GitHub Actions separados para validación, regresión visual/accesibilidad y despliegue a Pages.
- Dependencias Python con hashes y dependencias Node bloqueadas.
- Baselines visuales de cuatro rutas representativas en escritorio, móvil, modo claro y modo oscuro.
- Runbook para activar GitHub Pages, `decision.javierforero.co`, DNS y HTTPS.
- ADR-012 y ADR-013 para gobernar publicación y navegación.

### Validado localmente

- Build estricto de MkDocs y auditoría semántica de 14 páginas HTML generadas.
- 127 controles de integridad heredados del Sprint 0.
- 20 pruebas de navegador aprobadas; cuatro duplicados de Axe en móvil se omiten deliberadamente porque el mismo conjunto automatizado se ejecuta en escritorio.

### Pendiente antes de promover la release

- Ejecución satisfactoria de los workflows en el primer pull request.
- Merge explícito a `main`.
- Activación de Pages, configuración del dominio, propagación DNS y HTTPS.
- Auditoría humana de accesibilidad de la release desplegada; no se declara todavía conformidad WCAG 2.2 AA.

## [0.2.0] - 2026-07-19

### Ratificado

- CDI-GOV-001 como norma fundacional, aprobada y normativa.
- Ocho áreas de conocimiento y 29 dominios.
- MkDocs y GitHub Pages como arquitectura objetivo del portal.
- Javier Forero como masterbrand respaldante.
- `dashboards.javierforero.co` como Practice Lab externo.

### Añadido

- Registros iniciales de conceptos, claims, fuentes, activos y demos.
- Documentos constitucionales vigentes de PULSE.
- `brand-source.yml`, design tokens en JSON/CSS y manifiesto de activos.
- ADR-001 a ADR-011, incluidos los cierres de marca, IgraSans y accesibilidad.
- Validador reproducible del Sprint 0.
- Publicación del repositorio oficial en GitHub y establecimiento de `main` como rama canónica.

### Limitaciones explícitas

- No se declara conformidad WCAG 2.2 AA hasta auditar una release completa del portal.
- IgraSans no se redistribuye dentro del repositorio hasta verificar derechos y licencia.
- No se otorga licencia de reutilización en `v0.2.0`.
