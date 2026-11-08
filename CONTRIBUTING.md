# Contribuir al CDI-BoK

## Elige un punto de entrada

- **Error del portal, enlaces o accesibilidad.** Registra el idioma, la URL, el resultado observado y los pasos mínimos para reproducirlo.
- **Mejora de contenido o evidencia.** Identifica el apartado, el claim o la decisión afectada. Enlaza la fuente original e indica qué sostiene, con qué alcance y qué queda incierto.
- **Cambio pequeño y verificable.** Abre un pull request con un solo propósito. Si cambia autoridad, arquitectura, alcance o licenciamiento, abre primero un issue y consulta la [arquitectura editorial](governance/00_CDI-BoK_Architecture_and_Editorial_Governance.md).
- **Vulnerabilidad o información sensible.** Usa el [canal privado de seguridad](SECURITY.md).

[Abre un issue](https://github.com/jaforero/conversational-decision-intelligence-bok/issues/new/choose) · [Código de conducta](CODE_OF_CONDUCT.md)

## Prepara el entorno

Desde la raíz del repositorio, con Python 3.12 y Node.js 24:

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install --require-hashes -r requirements.lock
npm ci
python scripts/preflight_release.py
```

En Windows, crea el entorno con `py -3.12 -m venv .venv` y activa con `.venv\Scripts\Activate.ps1` en PowerShell. La vista local se abre con `python -m mkdocs serve`.

Para verificar un cambio de interfaz, instala Chromium con `npx playwright install chromium` y ejecuta `npm test` después del preflight. Cierra la vista local antes de probar para que Playwright use el build auditado. Las capturas canónicas se toman en GitHub Actions.

## Prepara el pull request

1. Crea una rama desde `main`. Describe el problema, el cambio y cómo comprobarlo.
2. Para contenido, consulta el [mapa del corpus](governance/content-map.yml), los [registros](governance/registries/) y el front matter. Identifica el concepto, claim, fuente, activo o ADR afectado cuando aplique.
3. Usa el hogar canónico de cada definición. Distingue evidencia, hipótesis y síntesis. Reserva `Original Contribution` para aportes con comparación documentada con antecedentes. Usa `Original Contribution Proposal` mientras se evalúa la originalidad.
4. Enlaza cada página desde el contenido y verifica la ruta en ambos idiomas. En inglés, apunta al archivo `.en.md` si existe. Registra cambios relevantes en [Unreleased](CHANGELOG.md#unreleased).
5. Adjunta al PR los resultados de la verificación. Para cambios visuales, incluye la evidencia del antes y después, y revisa cualquier cambio de captura en el informe de GitHub Actions.

El estado editorial de cada aporte lo determina su revisión explícita y su registro. Consulta la [guía de mantenimiento](.github/MAINTAINERS.md) para publicar y verificar el despliegue.
