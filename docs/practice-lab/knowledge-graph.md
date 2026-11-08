---
title: Laboratorio de grafos de conocimiento
description: Explora el CDI-BoK como red documental y convierte un hallazgo verificable en una mejora editorial.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: experimental
normative: false
owner: Javier Forero
domains: [Knowledge Graphs, Semantic Layers, Decision Governance]
source_ids: [SRC-PRACTICE-GRAPH-001, SRC-JF-BLOG-3248]
claim_ids: []
last_reviewed: 2026-11-08
---

# Laboratorio de grafos de conocimiento

**Pregunta de práctica.** ¿Qué enlace, referencia o ruta de lectura debería corregir primero el mantenedor del CDI-BoK? Prioriza los cambios que permitan reconstruir evidencia o llegar desde una guía a su aplicación.

[Abrir el CDI-BoK en el explorador](https://dashboards.javierforero.co/claude/grafo-conocimiento/?repo=jaforero%2Fconversational-decision-intelligence-bok&ref=main&path=docs&lang=es){ .md-button .md-button--primary }

## Carga el libro y recorre una relación

1. El enlace carga el CDI-BoK directamente. Para cargarlo de forma manual o fijar otra versión, elige **Cargar otra bóveda → GitHub**. Introduce `jaforero/conversational-decision-intelligence-bok` y, en Opciones, la subcarpeta `docs`. Usa `main` para el corpus vigente o una etiqueta para reproducir una revisión histórica. El repositorio es público y se puede cargar sin token, sujeto al límite de la API de GitHub.
2. Abre `learn/02-evidence-context.md` y sigue el enlace al módulo de diseño de experiencias. En el destino, revisa el backlink y su contexto. Repite con `research/research-agenda.md` y busca el protocolo candidato de GraphRAG.
3. Clasifica un hallazgo. Un **enlace roto** apunta a un destino que no se resuelve. Una **página sin enlaces entrantes desde el contenido** puede seguir siendo accesible por navegación. Una **relación implícita** requiere comprobar ambos documentos antes de añadir un enlace editorial.
4. Valida en el portal y en GitHub. Las convenciones de MkDocs y las traducciones `.en.md` pueden producir diferencias con un explorador genérico de Markdown. Registra origen, destino esperado, edición, evidencia, responsable y corrección propuesta. Verifica ambas ediciones después del cambio.

**Entregable.** Prepara un hallazgo reproducible y una corrección pequeña. Si una relación ya existe, úsala como control y documenta qué comprobaste.

## Inspecciona el grafo editorial del CDI-BoK { #editorial-graph }

El sitio genera un inventario JSON en cada compilación desde las páginas canónicas registradas, sus enlaces renderizados y los registros de fuentes y afirmaciones. Distingue cuatro relaciones: página que enlaza otra página, página que declara una fuente, página que declara una afirmación y afirmación que declara una fuente. Cada etiqueta describe lo que consta en el repositorio.

<a href="/assets/data/cdi-knowledge-graph.json" download>Descargar el grafo editorial en JSON</a>

El campo `pages_without_inbound_content_links` enumera candidatos a revisión, excluyendo la portada. Los enlaces del menú se omiten y cada página cuenta una sola vez, en su edición canónica en español. Una referencia declarada permite rastrear procedencia. Su relevancia o fuerza exige [revisar la evidencia](../governance/claims-evidence.md).

**Criterio de aceptación.** Encuentra la ruta de una página a una fuente o afirmación, contrástala con el archivo original y documenta qué acción editorial cambiaría. El [protocolo de GraphRAG](../research/research-agenda.md#graphrag-evaluation) describe la prueba adicional necesaria para evaluar recuperación basada en relaciones.
