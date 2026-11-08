# Conversational Decision Intelligence Body of Knowledge

> Referencia bilingüe para convertir evidencia y contexto en decisiones explícitas, acción responsable y aprendizaje medible.

[![Despliegue del portal](https://github.com/jaforero/conversational-decision-intelligence-bok/actions/workflows/deploy-pages.yml/badge.svg?branch=main&event=push)](https://github.com/jaforero/conversational-decision-intelligence-bok/actions/workflows/deploy-pages.yml)
[![Validación editorial y técnica](https://github.com/jaforero/conversational-decision-intelligence-bok/actions/workflows/validate.yml/badge.svg?branch=main&event=push)](https://github.com/jaforero/conversational-decision-intelligence-bok/actions/workflows/validate.yml)
[![Última release estable](https://img.shields.io/github/v/release/jaforero/conversational-decision-intelligence-bok?label=release)](https://github.com/jaforero/conversational-decision-intelligence-bok/releases/latest)
[![Portal en español e inglés](https://img.shields.io/badge/portal-ES%20%7C%20EN-4e00ff)](https://decision.javierforero.co/)

## Accesos rápidos

| Quiero… | Dónde empezar |
| --- | --- |
| Leer el CDI-BoK | [Portal en español](https://decision.javierforero.co/) · [English edition](https://decision.javierforero.co/en/) |
| Entender CDI, CDI-BoK y PULSE | [Empieza aquí](https://decision.javierforero.co/start-here/) · [De los cinco niveles de analítica a PULSE](https://decision.javierforero.co/03-pulse/from-five-levels/) |
| Hacer una pregunta y verificar la cita | [Pregúntale al CDI-BoK](https://decision.javierforero.co/ask-cdi/) |
| Practicar con un caso resuelto | [Decision Brief de SLA](https://decision.javierforero.co/practice-lab/sla-decision-brief/) · [Catálogo del Practice Lab](https://decision.javierforero.co/practice-lab/catalog/) |
| Explorar las relaciones entre documentos | [Laboratorio de grafos](https://decision.javierforero.co/practice-lab/knowledge-graph/) |
| Revisar la evidencia o una versión | [Claims y evidencia](https://decision.javierforero.co/governance/claims-evidence/) · [Releases de GitHub](https://github.com/jaforero/conversational-decision-intelligence-bok/releases) |

## Mapa del conocimiento

**CDI** es el dominio de práctica propuesto. **CDI-BoK** organiza definiciones, fuentes, patrones y casos con autoridad explícita. **PULSE** es el marco de práctica que conecta la evidencia con la decisión, la acción y la revisión del resultado.

| Parte | Contenido | Entrada en el repositorio |
| --- | --- | --- |
| Fundamentos | Constitución, alcance, glosario y dominios | [Fundamentos del CDI-BoK](docs/00-foundation/index.md) |
| PULSE | Especificación y puente desde las capacidades analíticas | [PULSE](docs/03-pulse/index.md) |
| Aprendizaje | Cinco módulos y una plantilla de Decision Brief | [Ruta de aprendizaje](docs/learn/index.md) |
| Calidad y medición | Calidad de la decisión, métricas y registro | [Sistema de medición](docs/07-governance-quality/index.md) |
| Patrones | Lenguaje, catálogo y antipatrones conversacionales | [Patrones](docs/08-patterns/index.md) |
| Practice Lab | Dashboards, grafos y casos de decisión | [Laboratorios y casos](docs/practice-lab/index.md) |
| Investigación | Estado del arte, mapa de evidencia y agenda | [Research](docs/research/index.md) |
| Gobierno editorial | Autoridad, trazabilidad y publicación | [Gobernanza](docs/governance/index.md) |

## Estado y cómo citar

- Release estable del portal: `v0.9.0` · [Evidence Backbone y estado del arte de Decision Intelligence](https://github.com/jaforero/conversational-decision-intelligence-bok/releases/tag/v0.9.0).
- Linaje editorial. El núcleo `v0.4.0` está aprobado. El caso B2B `v0.5.0-rc.1` está instrumentado y pendiente de ejecución. Aprendizaje `v0.6.0-rc.1` y calidad y medición `v0.7.0-rc.1` conservan su estado candidato. El caso de SLA es simulado.

La [arquitectura editorial CDI-GOV-001](governance/00_CDI-BoK_Architecture_and_Editorial_Governance.md) define cómo se asigna autoridad a cada componente.

[Consulta el historial del portal](https://decision.javierforero.co/versions/) y el [changelog](CHANGELOG.md) para distinguir lo etiquetado de los cambios posteriores en `main`. Para citar el libro, usa [CITATION.cff](CITATION.cff) o **Cite this repository**. Para una afirmación concreta, añade la página, el apartado y el tag o SHA consultado.

## Trabajar con el repositorio

- [`docs/`](docs/) contiene las dos ediciones del portal. [`governance/`](governance/) reúne ADR, manifiestos y registros. [`sources/constitutional/`](sources/constitutional/) contiene las fuentes controladas de PULSE.
- [`evidence/`](evidence/) conserva evidencia reproducible de los casos. [`brand/`](brand/), [`overrides/`](overrides/), [`scripts/`](scripts/) y [`tests/`](tests/) sustentan la interfaz, el build y las verificaciones.
- Lee la [guía de contribución](CONTRIBUTING.md) para preparar el entorno, elegir un tipo de issue y abrir un pull request. Consulta el [código de conducta](CODE_OF_CONDUCT.md) y la [política de seguridad](SECURITY.md) para los canales de reporte.
- La [guía de mantenimiento](.github/MAINTAINERS.md) describe los controles de GitHub y el flujo de publicación. El [runbook de Pages](docs/governance/publication-runbook.md) documenta el dominio y el despliegue.

## Derechos y reutilización

Consulta la [decisión de licenciamiento ADR-003](governance/adr/ADR-003-licensing-posture.md). El acceso público permite consultar y auditar el proyecto. Los derechos de reutilización se reservan, incluidos los derechos aplicables a fuentes y activos de terceros.
