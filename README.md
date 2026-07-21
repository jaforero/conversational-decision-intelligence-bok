# Conversational Decision Intelligence Body of Knowledge

Repositorio fundacional y versionado del **CDI-BoK**, el sistema de conocimiento de Conversational Decision Intelligence. Este repositorio gobierna conceptos, claims, fuentes, decisiones editoriales, PULSE y la relación entre conocimiento y práctica.

## Estado

- Release de gobernanza: `v0.2.0`
- Release estable del portal y núcleo fundacional: `v0.4.0`
- Candidato actual: `v0.7.0-rc.1`
- Fase activa: cierre ratificado de Sprint 5 — Decision Quality & Measurement
- Idioma canónico durante `0.x`: español
- Norma fundacional: `governance/00_CDI-BoK_Architecture_and_Editorial_Governance.md`
- Portal objetivo: `https://decision.javierforero.co`
- Practice Lab externo: `https://dashboards.javierforero.co`
- Repositorio oficial: `https://github.com/jaforero/conversational-decision-intelligence-bok`

La release `v0.4.0` ratifica el núcleo fundacional con autoridad diferenciada. `v0.5.0-rc.1` conserva el primer caso instrumentado sobre datos simulados. `v0.6.0-rc.1` aporta la experiencia de aprendizaje ratificada. El candidato `v0.7.0-rc.1` está ratificado, fusionado y desplegado con calidad y medición de decisiones; **no** afirma que CDI, PULSE o la instrumentación hayan producido impacto organizacional, ni constituye una promoción estable.

## Fuentes de autoridad

1. CDI-GOV-001 aprobado.
2. Documentos constitucionales vigentes de PULSE.
3. Registros controlados de conceptos, claims, fuentes y activos.
4. ADR aceptados.
5. Guías, casos y evidencia con alcance explícito.

## Estructura del sistema

- `governance/`: norma fundacional, ADR, registros y contratos editoriales.
- `brand/`: fuente de marca, tokens y manifiesto de activos.
- `docs/`: proyección pública controlada del CDI-BoK.
- `overrides/`: componentes de interfaz de MkDocs Material.
- `sources/constitutional/`: copias controladas de las fuentes constitucionales de PULSE.
- `scripts/`: sincronizadores y validadores de integridad.
- `tests/`: regresión visual y reglas de accesibilidad automatizables.
- `evidence/`: agregados reproducibles y no sensibles para auditar casos.
- `.github/workflows/`: validación, pruebas de navegador y despliegue a Pages.

## Uso local

Requiere Python 3.12 y Node.js 24.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --require-hashes -r requirements.lock
npm ci
python scripts/preflight_release.py
python -m mkdocs serve
```

Las pruebas de navegador se ejecutan con `npm test` después de instalar Chromium mediante `npx playwright install chromium`.

## Publicación

- Todo pull request ejecuta los controles editoriales, de build, visuales y de accesibilidad automatizada.
- Solo un merge a `main` puede desplegar el portal.
- El dominio y DNS se activan siguiendo `docs/governance/publication-runbook.md`.
- Un resultado automatizado sin violaciones no constituye por sí solo una declaración de conformidad WCAG 2.2 AA.

## Licenciamiento

No se concede licencia de reutilización en esta release. ADR-003 preserva todos los derechos mientras se realiza una revisión legal independiente para contenido, código, marca, tipografía y activos de terceros.
