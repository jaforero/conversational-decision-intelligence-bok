---
title: 3. Diseñar la Decision Experience
description: Selecciona la interfaz y estructura la experiencia alrededor de atención, comprensión, opciones, decisión, acción y feedback.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains:
  - Decision Architectures
  - Decision Narratives
  - Conversational Analytics
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-JF-002
  - SRC-ARCH-001
claim_ids:
  - CLAIM-PULSE-ROLE-001
  - CLAIM-CDI-EFFECT-001
last_reviewed: 2026-07-21
---

# 3. Diseñar la Decision Experience

**Resultado del módulo:** un blueprint que conecta usuario, evidencia, incertidumbre, alternativas, decisión, acción, riesgo y feedback en la interfaz menos compleja que resuelve la necesidad.

## La unidad de diseño es la decisión

Un dashboard puede ser correcto y no cambiar nada. Una conversación puede ser fluida y producir falsa confianza. Una Decision Experience se diseña desde la elección y su consecuencia, no desde la herramienta disponible.

Antes de dibujar una pantalla define:

- usuario y contexto de uso;
- decisión y owner;
- acción posterior;
- evidencia y contexto necesarios;
- incertidumbre que debe permanecer visible;
- riesgos y permisos;
- métrica de resultado;
- señal de feedback para aprender.

## Elegir la interfaz

| Necesidad dominante | Interfaz inicial | Riesgo frecuente |
|---|---|---|
| Hechos controlados y repetibles | **Reporte** | Entregar información sin señalar decisión. |
| Monitoreo y detección | **Dashboard** | Exceso de KPIs y ausencia de umbrales accionables. |
| Interpretación ejecutiva | **Narrativa** | Ocultar contraevidencia o convertir inferencia en causalidad. |
| Exploración de preguntas | **Conversación** | Respuestas fluidas sin semántica, fuente o límites. |
| Síntesis y preparación | **Copilot** | Recomendaciones sin criterio o accountability. |
| Coordinación de acción | **Workflow** | Automatizar un proceso mal definido. |
| Ejecución acotada | **Agente** | Autoridad excesiva y stop conditions débiles. |

No existe una progresión obligatoria hacia agentes. La solución superior puede ser un reporte breve si la decisión es estable y la ambigüedad baja.

## Ordenar la experiencia

Una secuencia útil para decisiones complejas es:

1. **Atención:** ¿qué requiere mirada ahora?
2. **Importancia:** ¿por qué importa y para quién?
3. **Cambio:** ¿qué se movió frente a baseline, meta o expectativa?
4. **Explicación:** ¿qué sabemos, inferimos y desconocemos?
5. **Futuro:** ¿qué escenarios son plausibles y con qué incertidumbre?
6. **Opciones:** ¿qué alternativas existen y cuáles son sus trade-offs?
7. **Decisión y acción:** ¿quién elige, qué sigue y cuándo?
8. **Riesgo:** ¿qué puede salir mal, cómo se detiene y quién responde?
9. **Aprendizaje:** ¿qué resultado observaremos y cómo cambiará el siguiente ciclo?

La secuencia no obliga a mostrar todo al mismo tiempo. La divulgación progresiva reduce carga, pero nunca debe esconder una limitación que cambiaría la elección.

## Conversación con estructura

Una interfaz conversacional añade valor cuando permite explorar sin perder el contrato decisional. Toda respuesta material debería poder exponer:

- definición y procedencia de la métrica;
- filtros, población y periodo;
- cálculo o método;
- incertidumbre y supuestos;
- contraevidencia relevante;
- permisos aplicados;
- vínculo con la decisión;
- siguiente acción autorizada.

La conversación no es una fuente de verdad. Es una interfaz sobre datos, semántica, contexto y reglas de gobierno.

## Blueprint mínimo

| Capa | Pregunta | Componente posible |
|---|---|---|
| **Señal** | ¿Qué cambió? | Alerta, titular, comparación. |
| **Comprensión** | ¿Por qué podría importar? | Desglose, narrativa, conversación. |
| **Criterio** | ¿Cómo comparamos opciones? | Matriz, escenarios, restricciones. |
| **Compromiso** | ¿Quién decide qué? | Decision Brief, aprobación, firma. |
| **Acción** | ¿Qué ocurre después? | Workflow, tarea, regla, responsable. |
| **Feedback** | ¿Qué aprenderemos? | Outcome, guardrail, revisión programada. |

## Prueba de estrés

- Si quitamos la IA, ¿la lógica decisional sigue siendo comprensible?
- ¿La interfaz ayuda a elegir o solo facilita explorar?
- ¿Qué contenido puede captar atención sin ser importante?
- ¿La recomendación muestra alternativas y condiciones de cambio?
- ¿Existe una salida segura cuando falta evidencia?
- ¿El feedback llega al mismo sistema que originó la decisión?

## Entregable

Dibuja seis bloques —señal, comprensión, criterio, compromiso, acción y feedback— y anota en cada uno contenido, actor, permiso y riesgo. Solo después elige componentes visuales o conversacionales.

**Siguiente:** [definir control humano y límites de la IA →](04-human-ai-control.md)
