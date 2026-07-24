---
title: Mapa de evidencia de PULSE
description: Qué partes de PULSE son constitucionales, derivadas, candidatas, hipotéticas o todavía no evaluadas.
status: candidate
version: 0.9.0-rc.1
artifact_type: evidence-map
authority_level: bounded-project-evidence-map
normative: false
owner: Javier Forero
domains: [Research, PULSE, Decision Governance]
claim_ids: [CLAIM-PULSE-001, CLAIM-PULSE-ROLE-001, CLAIM-PULSE-SYNTHESIS-001, CLAIM-PULSE-BIOLOGICAL-LENSES-001]
source_ids: [SRC-PULSE-DNA-001, SRC-PULSE-MAP-001, SRC-PULSE-IDENTITY-002, SRC-JF-001, SRC-JF-003, SRC-JF-005, SRC-JF-006, SRC-ARCH-001, SRC-PRACTICE-B2B-001]
last_reviewed: 2026-07-24
---

# Mapa de evidencia de PULSE

Este mapa responde una pregunta concreta: **¿qué autoridad tiene hoy cada pieza
de PULSE y qué no permite afirmar?** No asigna una nota total ni convierte
documentación abundante en validación.

| Componente | Estado | Soporte admisible | Límite decisivo |
|---|---|---|---|
| Identidad y definición PULSE | Constitucional | PULSE DNA e Identity | Autoridad del owner, no eficacia empírica |
| Decision First y PDAMR | Constitucional y de práctica | DNA, Identity y POV completo del autor | No existe comparación externa de desempeño |
| Decision Circle | Constitucional | DNA e Identity | El ciclo organiza la práctica; no prueba aprendizaje |
| Cinco verbos | Síntesis de práctica | POV del autor y fuentes constitucionales | No son una secuencia universal |
| Human-in-Control | Principio constitucional | DNA, Identity y controles del BoK | Su presencia documental no garantiza control efectivo |
| Decision Experience | Contrato candidato | Arquitectura y especificación derivada | Requiere evaluación con usuarios y tareas reales |
| Arquitectura L0–L7 | Arquitectura derivada candidata | `SRC-ARCH-001` | No es doctrina aprobada ni arquitectura validada |
| Cinco niveles de analítica | Framework pedagógico del autor | `SRC-JF-006` | No es una escala universal de madurez |
| Interocepción, alostasis y organismo decisional | Metáforas e hipótesis | Arquitectura derivada | No son mecanismos causales ni equivalencias biológicas |
| Registro longitudinal | Hipótesis de aprendizaje | DNA, arquitectura y Measurement Record | Registrar no demuestra cambio de conducta o outcome |
| Caso B2B | Diseño instrumentado, no ejecutado | diseño MVP y datos simulados | No hay acción real, outcome observado ni atribución |

## Compatibilidad con claims

- Las fuentes constitucionales pueden gobernar definiciones de PULSE.
- Un POV del autor puede explicar linaje o propósito.
- Una arquitectura derivada puede soportar una hipótesis de diseño candidata.
- Ninguna de esas clases puede demostrar por sí sola superioridad o eficacia.
- Las copias `SRC-JF-001` y `SRC-JF-003` permanecen bloqueadas porque están
  truncadas.
- Una síntesis asistida por IA no reemplaza la fuente original ni valida la
  arquitectura.

## Tensiones abiertas

### Framework práctico frente a escalera tecnológica

El framework de cinco niveles puede ayudar a enseñar capacidades analíticas,
pero se vuelve incompatible con Decision First si se interpreta como “subir de
nivel” antes de definir la decisión. Se conserva como taxonomía pedagógica, no
como madurez obligatoria.

### Metáfora biológica frente a explicación causal

Interocepción y alostasis pueden generar preguntas útiles sobre señales,
feedback y adaptación. El riesgo es convertir semejanza verbal en mecanismo.
Toda predicción derivada debe formularse de manera observable sin depender de
que la metáfora sea literalmente cierta.

### Integración frente a originalidad

El valor de PULSE puede estar en la selección y coordinación de componentes,
aunque muchos tengan antecedentes. Originalidad de ensamblaje, novedad teórica
y eficacia son claims distintos y requieren evidencia distinta.

## Próximo umbral de evidencia

Antes de elevar un claim de eficacia, un piloto necesita:

1. decisión, población y comparador definidos ex ante;
2. baseline y calidad de evidencia verificables;
3. autoridad humana y stop conditions operativas;
4. outcome, proceso, adopción y riesgo medidos por separado;
5. seguimiento suficiente para observar acción y aprendizaje;
6. publicación de resultados adversos, nulos y costos.

Consulte el registro machine-readable
`governance/registries/evidence-profiles.yml` para procedencia, derechos y
perfiles completos.
