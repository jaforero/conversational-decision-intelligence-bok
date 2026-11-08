# Mantenimiento del repositorio

## Integrar un cambio

1. Revisa el alcance del PR, la evidencia y los resultados de **Governance, content and build** y **Browser quality**. Conserva las capturas de GitHub Actions como referencia para regresiones.
2. Fusiona a `main` cuando los controles estén en verde. Verifica el job **Publish** del workflow de Pages y abre las rutas afectadas en ES/EN.
3. Para una release, sigue la [política de identificación y tags](../governance/adr/ADR-022-release-identification-and-tag-policy.md). La versión, el manifiesto, las notas, el changelog y [CITATION.cff](../CITATION.cff) deben corresponder al corte ratificado. Verifica en [Releases](https://github.com/jaforero/conversational-decision-intelligence-bok/releases) el tag y su commit.

Los PR de Dependabot cubren Actions y npm. Revisa la procedencia de cada SHA y prueba el cambio antes de fusionar. Las dependencias Python siguen `requirements.in` y `requirements.lock`; actualízalas juntas y verifica la instalación con `--require-hashes`.

## Configuración de GitHub que debe revisar el mantenedor

| Área | Configuración objetivo |
| --- | --- |
| About | Descripción «Base de conocimiento bilingüe sobre inteligencia de decisiones conversacional. Fundamentos, PULSE, evidencia y laboratorios prácticos.» Sitio `https://decision.javierforero.co/`. Topics `decision-intelligence`, `conversational-ai`, `decision-governance`, `conversational-analytics`, `business-intelligence`, `knowledge-base`, `knowledge-graph`, `data-visualization`. |
| Ruleset de `main` | Exigir PR y los checks **Governance, content and build** y **Browser quality**. Bloquear force-push y eliminación de la rama. Usar cero aprobaciones obligatorias mientras el proyecto tenga un solo mantenedor y conservar la revisión editorial explícita. Seleccionar los checks de GitHub Actions tras una ejecución correcta. |
| Seguridad | Habilitar el reporte privado de vulnerabilidades y revisar alertas de Dependabot y protección de secretos en **Settings → Advanced Security** según las opciones disponibles. |
| Pages | Usar GitHub Actions, el entorno `github-pages` limitado a `main` y HTTPS. Consultar el [runbook de publicación](../docs/governance/publication-runbook.md) para verificar dominio y despliegue. |

Los archivos de la rama principal definen los workflows y las plantillas. La configuración de la tabla se administra en GitHub y se verifica en su interfaz.
