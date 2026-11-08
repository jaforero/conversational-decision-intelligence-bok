---
title: De los cinco niveles de analítica a PULSE
description: El linaje editorial que conecta las capacidades analíticas con una forma de decidir, actuar y aprender.
status: candidate
version: 0.9.0
artifact_type: learning-guide
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [PULSE, Decision Intelligence, Business Intelligence Evolution]
source_ids: [SRC-JF-006, SRC-JF-PULSE-PUBLIC-001, SRC-PULSE-DNA-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# De los cinco niveles de analítica a PULSE

**Los cinco niveles ayudan a elegir qué análisis aporta a una decisión. PULSE organiza cómo convertir ese aporte en acción responsable y aprendizaje.**

El artículo sobre los cinco niveles, publicado en enero de 2026, ordena las preguntas que la analítica puede responder, desde describir lo ocurrido hasta explorar datos y contexto mediante el lenguaje natural. En junio de 2026, el artículo que presenta PULSE cambia la unidad de análisis. El foco pasa de la capacidad analítica al **sistema de decisión** que la usa. Así evoluciona el marco del autor: las capacidades se conservan y se eligen según lo que la decisión necesita.

## Qué aporta cada capacidad al ciclo

| Capacidad analítica | Pregunta que ayuda a responder | Aporte posible al Decision Circle |
|---|---|---|
| **Descriptiva** | ¿Qué ocurrió y dónde cambió? | **Percibir** señales con definiciones, periodos y denominadores comparables. |
| **Diagnóstica** | ¿Qué cambió exactamente y qué explicaciones merecen prueba? | **Enfocar** el problema y distinguir hallazgos de hipótesis sobre sus causas. |
| **Predictiva** | ¿Qué podría ocurrir y con qué incertidumbre? | **Anticipar** escenarios que cambiarían la preparación o el momento de actuar. |
| **Prescriptiva** | ¿Qué opciones funcionan mejor bajo estas restricciones? | **Generar opciones** y apoyar la elección humana con supuestos y trade-offs explícitos. |
| **Cognitiva** | ¿Qué podemos aclarar al conversar con los datos y su contexto? | Explorar evidencia, contrastar opciones y revisar resultados en distintos momentos del ciclo, con fuentes y permisos verificables. |

La tabla muestra usos posibles. Una misma capacidad puede servir en varios momentos del ciclo y una decisión puede resolverse con solo algunas. Los cinco verbos de PULSE, **Understand, Decide, Act, Learn y Anticipate**, expresan el valor que se busca. Se pueden fortalecer con capacidades distintas.

## Qué cambia al aplicar PULSE

1. **Empieza por la decisión.** PDAMR precisa la prioridad, la elección y su responsable, la acción, la métrica y el riesgo. Esa definición indica qué evidencia y capacidad hacen falta.
2. **Escoge la capacidad y la interfaz adecuadas.** Un reporte con definiciones claras puede bastar para decidir a tiempo. Un pronóstico, una optimización o una conversación se justifican cuando resuelven una incertidumbre o restricción relevante.
3. **Cierra el ciclo.** La persona responsable elige y registra qué espera de la acción. Después compara esa expectativa con el resultado y documenta qué criterio o práctica cambiará en el siguiente ciclo.

## Ejemplo de práctica · Cumplimiento del SLA

**Decisión.** La persona responsable de operaciones elige entre reasignar capacidad a una ruta o mantener la asignación y revisar el siguiente corte.

El tablero descriptivo ubica el incumplimiento frente al umbral acordado. El análisis diagnóstico revisa si la señal se concentra en una ruta y si cambió el denominador o la mezcla de entregas. Si esa evidencia basta para una reasignación reversible, se registra la decisión, la expectativa, la fecha de revisión y una condición de reversión, como un deterioro inaceptable en otra ruta. Si el volumen futuro puede cambiar la elección, se prueban escenarios. Una interfaz conversacional puede facilitar las preguntas sobre la evidencia. El aprendizaje llega al comparar el resultado observado con la expectativa y decidir si se ajusta la regla.

**Practícalo.** Usa la ruta de SLA del [laboratorio de dashboards](../practice-lab/dashboards.md) y registra la decisión con la [plantilla Decision Brief](../learn/decision-brief.md). El ejemplo es ilustrativo y el laboratorio usa datos simulados.

## Fuentes y alcance

Esta es una lectura pedagógica de la evolución del trabajo de Javier Forero. El marco de cinco niveles clasifica capacidades para enseñar. La [especificación nuclear de PULSE](specification.md) conserva la autoridad sobre la metodología. El [mapa de evidencia](../research/pulse-evidence-map.md) delimita qué permite afirmar cada tipo de fuente.

- Enero de 2026 · [Analítica de Datos en 5 Niveles](https://javierforero.co/2026/01/26/analitica-datos-5-niveles/).
- Junio de 2026 · [PULSE: tómale el pulso a tus decisiones](https://javierforero.co/2026/06/30/pulse-decidir-mejor-con-datos/).
