---
title: Glosario normativo inicial
description: Vocabulario controlado del CDI-BoK con definiciones candidatas, owners conceptuales y límites de uso.
status: candidate
version: 0.4.0-rc.1
artifact_type: controlled-glossary
authority_level: normative-candidate
normative: false
owner: Javier Forero
domains:
  - Foundations
  - Conversational Decision Intelligence
  - PULSE
  - Decision Governance
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-PULSE-IDENTITY-002
  - SRC-DR-002
last_reviewed: 2026-07-21
---

# Glosario normativo inicial

!!! info "Cómo interpretar este glosario"
    **Normativo inicial** describe su función prevista; en `v0.4.0-rc.1` todas las entradas permanecen candidatas. Los conceptos propiedad de PULSE reproducen o resumen su DNA y no adquieren una definición independiente aquí.

| Término | Definición controlada | Owner conceptual | Límite clave |
|---|---|---|---|
| **Acción** | Ejecución de una decisión mediante un cambio observable en conducta, asignación, workflow, regla o control. | PULSE DNA | Una recomendación no ejecutada no es acción. |
| **Analítica conversacional** | Interacción gobernada con evidencia organizacional mediante lenguaje natural para preguntar, explicar, explorar y dar seguimiento. | PULSE DNA | No implica decisión, verdad ni autorización por sí sola. |
| **Aprendizaje** | Ajuste producido al comparar lo esperado con lo ocurrido y modificar percepción, supuestos, criterios, decisiones, acciones o controles. | PULSE DNA | Registrar una lección sin cambiar el siguiente ciclo no basta. |
| **CDI-BoK** | Sistema público, gobernado y versionado que organiza el conocimiento oficial del proyecto CDI. | CDI-GOV-001 | No es automáticamente un estándar reconocido. |
| **Contexto** | Procesos, reglas, historia, restricciones, excepciones, objetivos, relaciones e información local que dan significado operacional a la evidencia. | PULSE DNA | Más documentos no garantizan contexto suficiente. |
| **Conversación decisional** | Interacción iterativa humano–IA orientada a clarificar evidencia, supuestos, alternativas, criterios y próximos pasos de una decisión explícita. | CDI Constitution candidate | No equivale a conversación casual ni a simple NLQ. |
| **Conversational Decision Intelligence (CDI)** | Dominio de práctica interdisciplinar propuesto que estudia y diseña cómo humanos e IA colaboran mediante conversaciones para convertir evidencia y contexto en decisión, acción y aprendizaje. | CDI Constitution candidate | Definición del proyecto; reconocimiento externo pendiente. |
| **Copiloto de decisión** | Sistema habilitado por IA que apoya a una persona con evidencia, contexto, opciones, escenarios y workflow sin asumir accountability final. | PULSE DNA | Copilot no significa aprobación automática. |
| **Criterio de decisión** | Atributo o regla usada para comparar alternativas frente a objetivos, riesgos y restricciones. | CDI foundational core | Debe ser explícito y no confundirse con una métrica de desempeño. |
| **Datos confiables** | Evidencia con calidad, procedencia, definición, ownership, seguridad y relevancia suficientes para un uso específico. | PULSE DNA | “Confiable” siempre es fitness for purpose, no perfección absoluta. |
| **Decisión** | Elección comprometida entre alternativas, realizada por un owner autorizado bajo restricciones e incertidumbre. | PULSE DNA | Opinión o recomendación sin compromiso no es decisión. |
| **Decision Circle** | Ciclo PULSE: Perceive, Focus, Anticipate, Generate options, Decide and act, Learn. | PULSE DNA | No es un waterfall rígido. |
| **Decision Experience** | Experiencia humana y operacional completa mediante la cual se percibe evidencia, se comprende significado, se evalúan opciones, se decide, se actúa y se aprende. | PULSE DNA | No es sinónimo de interfaz visual. |
| **Decision Intelligence** | Uso coordinado de evidencia, análisis, juicio humano, tecnología, gobernanza y aprendizaje para mejorar un sistema de decisión. | PULSE DNA | CDI-BoK la usa como definición constitucional de PULSE; el campo externo tiene definiciones diversas. |
| **Decision latency** | Tiempo entre la disponibilidad de una señal relevante y una decisión suficientemente informada y autorizada. | PULSE DNA | Menor no siempre es mejor si degrada legitimidad o seguridad. |
| **Evidencia** | Material registrado u observable capaz de apoyar o cuestionar un claim. | PULSE DNA | Evidencia no es automáticamente completa, cierta o causal. |
| **Human-in-Control** | Condición de diseño y gobierno en la que humanos conservan autoridad sobre propósito, criterios, límites, riesgo, accountability, override y consecuencias. | PULSE DNA | Participar en un loop no demuestra control efectivo. |
| **Incertidumbre** | Falta relevante de certeza sobre datos, modelos, explicaciones, escenarios, acciones o resultados. | CDI foundational core | Debe expresarse de forma útil para la decisión, no como descargo genérico. |
| **Idea** | Significado de negocio derivado del entendimiento: explicación, oportunidad, riesgo o dirección posible. | PULSE DNA | Insight no es todavía una decisión. |
| **Organizational Intelligence** | Capacidad colectiva fortalecida para entender, decidir, actuar, aprender y anticipar a través de ciclos repetidos. | PULSE DNA | Es capacidad, no un score tecnológico. |
| **Owner de decisión** | Persona o cuerpo con autoridad legítima y accountability sobre una decisión definida. | CDI foundational core | Facilitar, recomendar o ejecutar no implica poseer la decisión. |
| **PDAMR** | Brújula PULSE: Priority, Decision, Action, Metric, Risk. | PULSE DNA | Orienta una iniciativa; no es un plan de proyecto completo. |
| **PULSE** | Metodología y filosofía operativa de Decision Intelligence centrada en las personas que reduce la distancia entre realidad organizacional y mejores decisiones mediante datos confiables, contexto, entendimiento, acción y aprendizaje. | PULSE DNA / Identity | Esta traducción orienta; la definición oficial completa en inglés permanece canónica. |
| **Recomendación** | Curso de acción propuesto con razones, evidencia, supuestos, restricciones y riesgo. | PULSE DNA | No es una decisión hasta que un owner autorizado se compromete. |
| **Resultado** | Consecuencia observable de una acción, incluidos efectos previstos y no previstos. | PULSE DNA | Un resultado favorable no demuestra buena decisión ni causalidad. |
| **Sistema de decisión** | Conjunto de personas, derechos, evidencia, procesos, modelos, interfaces, acciones, controles y feedback que producen decisiones repetidas. | CDI foundational core | No es necesariamente software. |
| **Trazabilidad** | Capacidad de reconstruir definiciones, fuentes, transformaciones, supuestos, versiones, recomendaciones, decisiones y acciones. | CDI-GOV-001 / PULSE DNA | Un log técnico sin significado de negocio es insuficiente. |

## Reglas de uso

1. Una definición controlada tiene un solo owner conceptual.
2. Las páginas derivadas pueden resumirla, pero deben enlazar o declarar el owner.
3. Los términos en inglés se conservan cuando son lenguaje canónico de PULSE o evitan ambigüedad.
4. **Must**, **should**, **may** y **must not** se reservan para requisitos, recomendaciones, opciones y prohibiciones respectivamente.
5. Un cambio semántico requiere análisis de impacto sobre navegación, claims, fuentes, casos y sistemas de recuperación.

