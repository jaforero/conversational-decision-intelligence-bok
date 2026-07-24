---
title: Alcance y fronteras de CDI
description: Definición oficial del proyecto Conversational Decision Intelligence, relación con campos adyacentes y criterios de inclusión y exclusión.
status: approved
version: 0.4.0
artifact_type: scope-standard
authority_level: institutional-approved
normative: true
owner: Javier Forero
domains:
  - Conversational Decision Intelligence
  - Decision Intelligence
  - Conversational Analytics
  - Responsible AI
source_ids:
  - SRC-PRIOR-CDI-001
  - SRC-PRIOR-CDI-002
  - SRC-ACADEMIC-HAI-001
  - SRC-ACADEMIC-AIEVAL-001
claim_ids:
  - CLAIM-CDI-001
  - CLAIM-CDI-PRIOR-001
  - CLAIM-CDI-EFFECT-001
last_reviewed: 2026-07-21
---

# Alcance y fronteras de CDI

## Definición oficial del proyecto

> **Conversational Decision Intelligence (CDI) es el dominio de práctica interdisciplinar propuesto que estudia y diseña cómo personas y sistemas de inteligencia artificial colaboran mediante conversaciones para convertir evidencia confiable y contexto en decisiones explícitas, acción responsable y aprendizaje medible.**

Esta es la **definición oficial del proyecto desde `v0.4.0`**, no una definición aceptada universalmente. CDI se presenta como dominio de práctica emergente mientras se desarrolla revisión comparativa, evidencia aplicada y evaluación externa.

## Qué hace específica a CDI

Una experiencia pertenece al núcleo de CDI cuando integra las cinco condiciones siguientes:

1. **Conversación iterativa:** permite preguntar, aclarar, contrastar, profundizar o revisar; no solo emitir un comando.
2. **Objeto decisional explícito:** identifica la decisión, el owner, las alternativas, los criterios, las restricciones y el costo del error o de la demora.
3. **Contrato de evidencia:** conecta respuestas con datos, definiciones, alcance, procedencia, incertidumbre y permisos.
4. **Transición a acción gobernada:** distingue explicación, recomendación, decisión y ejecución; conserva derechos de decisión y escalamiento.
5. **Bucle de aprendizaje:** registra expectativa, resultado, desviación y ajuste del siguiente ciclo.

Si falta el objeto decisional, normalmente estamos ante Conversational Analytics o asistencia informativa. Si falta conversación, puede existir Decision Intelligence, pero no CDI. Si faltan evidencia y gobernanza, existe una interfaz fluida, no una experiencia decisional confiable.

## Matriz de fronteras

| Campo o artefacto | Unidad principal | Conversación | Decisión explícita | Acción y aprendizaje | Relación con CDI |
|---|---|---:|---:|---:|---|
| **Business Intelligence** | Métrica o indicador | Opcional | No necesariamente | Limitados | Provee evidencia y monitoreo. |
| **Conversational AI** | Interacción o tarea lingüística | Sí | No necesariamente | Opcionales | Provee capacidades de diálogo. |
| **Conversational Analytics** | Pregunta sobre datos | Sí | Puede estar implícita | No necesariamente | Es una interfaz analítica dentro o fuera de CDI. |
| **Decision Support System** | Problema semiestructurado | Opcional | Sí | Variables | Es un antecedente funcional importante. |
| **Decision Intelligence** | Sistema de decisión | Opcional | Sí | Sí | Es el campo integrador del que CDI toma orientación decisional. |
| **Human–AI deliberation** | Desacuerdo, razones y revisión | Sí | Sí | Según el diseño | Aporta evidencia y patrones para colaboración conversacional. |
| **CDI** | Conversación alrededor de una decisión | Necesaria | Necesaria | Necesarios y gobernados | Integra las capacidades anteriores bajo un contrato común. |
| **PULSE** | Salud y ciclo de una decisión | Opcional | Sí | Sí | Framework of practice de este ecosistema; no es sinónimo de CDI. |

## Dentro del alcance

- exploración conversacional de evidencia para una decisión identificable;
- clarificación de preguntas, métricas, entidades, periodos y restricciones;
- comparación de alternativas, escenarios, trade-offs y reversibilidad;
- deliberación humano–IA que expone desacuerdo y razones;
- síntesis de evidencia con incertidumbre y procedencia;
- copilotos que apoyan preparación, recomendación o workflow bajo control humano;
- agentes que ejecutan acciones acotadas, observables, reversibles cuando sea posible y proporcionales al riesgo;
- medición de calidad de proceso, resultado, confianza apropiada y aprendizaje.

## Fuera del núcleo

- chatbots de servicio sin decisión organizacional explícita;
- texto-a-SQL o búsqueda conversacional sin conexión a opciones, owner o acción;
- dashboards que solo incorporan una caja de preguntas;
- generación automática de narrativas sin trazabilidad ni control de claims;
- recomendadores que ocultan criterios, incertidumbre o conflictos de interés;
- agentes con objetivos abiertos y autoridad no delimitada;
- automatización de decisiones irreversibles o rights-affecting sin autoridad humana legítima;
- cualquier sistema cuyo éxito se mida solo por uso, fluidez, engagement o volumen de respuestas.

## Antecedentes y originalidad calibrada

La expresión **Conversational Decision Intelligence** tiene usos públicos anteriores a este CDI-BoK. En 2022 se utilizó para describir una plataforma de inferencia conversacional; en 2025 otro autor propuso CDI como categoría para diálogo orientado a decisiones. Por tanto:

- el proyecto **no reclama haber acuñado la expresión**;
- la coincidencia terminológica no prueba equivalencia conceptual;
- la contribución candidata está en el contrato integral de decisión, evidencia, acción, gobierno y aprendizaje, y en su integración con PULSE;
- cualquier claim de novedad deberá compararse con antecedentes académicos, industriales y de práctica de manera explícita.

Consulte los antecedentes registrados en [fuentes](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/governance/registries/sources.yml).

## Hipótesis central y criterio de prueba

**Hipótesis candidata:** en una decisión y contexto específicos, una experiencia conversacional gobernada puede reducir fricción o latencia y mejorar comprensión, exploración o calidad de proceso sin reducir exactitud, control, equidad o accountability.

La hipótesis no se confirma porque el sistema responda correctamente una vez. Requiere comparación contra una alternativa pertinente—por ejemplo humano solo, dashboard, analyst-mediated workflow o sistema no conversacional—y debe separar:

- desempeño del modelo;
- desempeño del humano;
- desempeño del equipo humano–IA;
- calidad del proceso;
- resultado de la decisión;
- costo y riesgo introducidos.

La investigación disponible muestra resultados heterogéneos: algunas formas deliberativas tienen potencial para mejorar confianza apropiada y desempeño en tareas específicas, mientras otras evaluaciones encuentran que recomendaciones de IA no mejoran y pueden deteriorar decisiones. La conclusión correcta es condicional, no universal.

## Preguntas que permanecen abiertas

- ¿Cuándo la conversación mejora el razonamiento y cuándo solo aumenta persuasión o sobreconfianza?
- ¿Qué combinación de visualización y diálogo sirve mejor a cada decisión?
- ¿Cómo medir calidad decisional separada de suerte y resultado?
- ¿Cómo preservar contexto tácito, desacuerdo y poder organizacional?
- ¿Qué decisiones deben permanecer simples, no conversacionales o no automatizadas?
- ¿Qué controles hacen que la delegación sea real y no supervisión nominal?
- ¿Qué evidencia permitiría elevar CDI de dominio propuesto a disciplina reconocida?

## Referencias directas utilizadas

- Martin Schoeman, [“Conversational Decision Intelligence (CDI) Strategy Begins in Conversation”](https://medium.com/@mschoeman3/conversational-decision-intelligence-cdi-strategy-begins-in-conversation-0f2d1fc50381), 2025. Antecedente terminológico; no autoridad del CDI-BoK.
- Akeel Attar, [“Turbo charge your Conversational AI with Conversational Decision Intelligence”](https://www.linkedin.com/pulse/turbo-charge-your-conversational-ai-decision-akeel-attar), 2022. Antecedente terminológico y de producto.
- Ma et al., [“Towards Human-AI Deliberation”](https://doi.org/10.1145/3706598.3713423), CHI 2025. Estudio exploratorio de deliberación humano–IA.
- Ben-Michael et al., [“Does AI help humans make better decisions?”](https://arxiv.org/abs/2403.12108), 2024. Framework de evaluación y evidencia de que la asistencia no mejora automáticamente el desempeño.
