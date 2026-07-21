---
title: Decision Quality
description: Cómo evaluar una decisión ex ante, separar proceso de outcome y usar un perfil multidimensional sin fabricar una puntuación universal.
status: candidate
version: 0.7.0-rc.1
artifact_type: domain-guide
authority_level: established-foundations-with-candidate-synthesis
normative: false
owner: Javier Forero
domains:
  - Decision Quality
  - Decision Science
  - Decision Governance
source_ids:
  - SRC-DQ-SDP-001
  - SRC-ACADEMIC-OUTCOME-BIAS-001
  - SRC-PULSE-DNA-001
claim_ids:
  - CLAIM-DQ-OUTCOME-001
  - CLAIM-DQ-PROFILE-001
last_reviewed: 2026-07-21
---

# Decision Quality

La calidad de una decisión se evalúa con la información disponible **al momento de decidir**, no con el beneficio de conocer el desenlace. El outcome importa, pero responde otra pregunta: qué ocurrió después de actuar.

## Fundamento establecido y síntesis candidata

La Society of Decision Professionals describe seis elementos conectados: encuadre, alternativas, información, valores y trade-offs, razonamiento y compromiso con la acción. Su metáfora de cadena advierte que el eslabón más débil limita el proceso completo.

El CDI-BoK usa ese marco como referencia profesional establecida. La contribución candidata de esta release no es una teoría alternativa: es una **superficie de medición** que añade trazabilidad para conversación humano–IA, ejecución, riesgo y aprendizaje PULSE.

## Por qué evaluar antes del outcome

Baron y Hershey mostraron experimentalmente que conocer un resultado puede alterar la valoración retrospectiva de la decisión que lo produjo. Es evidencia primaria de **outcome bias**, no una estimación universal de su magnitud en todas las organizaciones.

La defensa operacional es conservar dos snapshots:

- **snapshot de decisión:** lo conocido, esperado y autorizado antes de actuar;
- **snapshot de revisión:** outcome, desviación, explicaciones y ajuste, añadido después sin sobrescribir el primero.

## Perfil ex ante

Evalúa siete dimensiones con evidencia breve. No promedies automáticamente.

| Dimensión | Pregunta de revisión | Bloqueador material |
|---|---|---|
| **Encuadre y autoridad** | ¿La elección, el owner, el plazo y las personas afectadas están claros? | No existe una elección o nadie puede comprometer la acción. |
| **Alternativas** | ¿Hay opciones materialmente distintas, incluida no actuar cuando sea viable? | La opción preferida es la única analizada. |
| **Evidencia e incertidumbre** | ¿La información es fitness for purpose y muestra desconocidos, rangos y contraevidencia? | Una premisa decisiva carece de procedencia o se presenta con certeza falsa. |
| **Valores y trade-offs** | ¿Los criterios, pesos o prioridades y las consecuencias distributivas son explícitos? | El criterio real permanece implícito o excluye a quien soporta el daño. |
| **Razonamiento y challenge** | ¿La opción se conecta con consecuencias esperadas y sobrevivió a un contraargumento fuerte? | Recomendación sin mecanismo, comparación o prueba de estrés. |
| **Gobierno y compromiso** | ¿Derechos, permisos, escalamiento, stop conditions y acción tienen owner? | La IA o el equipo puede ejecutar fuera de límites o sin accountability. |
| **Expectativa y aprendizaje** | ¿Baseline, rango esperado, horizonte, guardrails y fecha de revisión quedaron fijados? | La expectativa se definirá después de ver el resultado. |

## Escala de revisión

Usa una escala ordinal con evidencia, no decimales:

- **Desconocido:** no hay información suficiente para evaluar.
- **Débil:** existe contenido, pero no soporta la decisión o deja un bloqueador abierto.
- **Adecuado:** suficiente para stakes y reversibilidad actuales, con límites declarados.
- **Fuerte:** triangulado, cuestionado y listo para la decisión específica.

Un perfil `fuerte` no garantiza un buen outcome. `Adecuado` tampoco significa mediocre: una decisión reversible y de bajo costo puede no justificar investigación adicional.

## Regla de proporcionalidad

La carga de revisión debe aumentar con:

- daño potencial y alcance sobre terceros;
- irreversibilidad y costo de corrección;
- incertidumbre material;
- delegación o automatización de la acción;
- dificultad de observar efectos tardíos o distribuidos.

Para decisiones frecuentes y reversibles, el registro mínimo puede ser suficiente. Para decisiones críticas, se requiere revisión independiente, análisis de sensibilidad y evidencia de actores afectados.

## Qué no debe hacer el perfil

- comparar equipos con una media que oculta bloqueadores;
- premiar documentación abundante sin mejor razonamiento;
- convertir el cumplimiento del proceso en sustituto del outcome;
- evaluar una decisión después del resultado como si esa información hubiera estado disponible antes;
- confundir acuerdo del comité con calidad de la decisión.

## Mejor contraargumento

Una rúbrica cualitativa puede volverse burocrática y sus categorías siguen dependiendo de juicio. Es correcto. Por eso esta versión conserva evidencia por dimensión, bloqueadores y proporcionalidad, y no presenta el perfil como instrumento psicométrico validado.

**Qué cambiaría esta arquitectura:** evidencia de campo que muestre que ciertas dimensiones son redundantes, que la escala no logra acuerdo entre revisores o que una métrica alternativa predice mejor fallas de proceso sin aumentar gaming.

[Construir el sistema de medición →](decision-measurement-system.md){ .md-button .md-button--primary }

