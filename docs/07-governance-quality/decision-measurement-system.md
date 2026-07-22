---
title: Sistema de medición de decisiones
description: Arquitectura candidata de seis lentes para medir prioridad, calidad, ejecución, tiempo, riesgo y aprendizaje alrededor de una decisión explícita.
status: candidate
version: 0.7.0-rc.1
artifact_type: candidate-framework
authority_level: candidate-synthesis
normative: false
owner: Javier Forero
domains:
  - Decision Metrics
  - Decision Quality
  - Responsible AI
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-ARCH-001
  - SRC-ACADEMIC-SCORING-RULES-001
  - SRC-NIST-AIRMF-001
claim_ids:
  - CLAIM-DM-SYSTEM-001
  - CLAIM-DM-CALIBRATION-001
  - CLAIM-DQ-PROFILE-001
last_reviewed: 2026-07-21
---

# Sistema de medición de decisiones

El **Sistema de medición de decisiones (Decision Measurement System)** es una síntesis candidata del CDI-BoK para instrumentar una decisión desde su baseline hasta la revisión. Su propósito es hacer observable el ciclo sin reducirlo a adopción, velocidad o ROI aislados.

## Seis lentes

| Lente | Qué observa | Ejemplos | Momento |
|---|---|---|---|
| **1. Prioridad y outcome** | Cambio material que justificó decidir | ingreso, costo, servicio, error, retención | Antes y después |
| **2. Calidad ex ante** | Integridad del proceso antes de conocer el outcome | perfil por dimensión, bloqueadores, revisión independiente | Antes |
| **3. Acción y ejecución** | Si la decisión se convirtió en comportamiento autorizado | inicio, finalización, fidelidad, adopción pertinente | Durante |
| **4. Tiempo y fricción** | Si la organización percibió, decidió y actuó a tiempo | latencia de decisión, latencia de acción, tiempo de escalamiento | Durante |
| **5. Riesgo y guardrails** | Costos, daños y límites que no deben ocultarse | incidentes, equidad, carga, calidad, privacidad, reversión | Durante y después |
| **6. Calibración y aprendizaje** | Correspondencia entre expectativa y resultado y cambio posterior | error de pronóstico, hipótesis revisadas, cierre del review | Después y entre ciclos |

Ningún lente sustituye a los demás. Una acción rápida puede ser incorrecta; un outcome positivo puede ocultar daño; un proceso completo puede no producir valor.

## Contrato de cada métrica

No incorpores una métrica si no puedes declarar:

| Campo | Pregunta |
|---|---|
| **Nombre y definición** | ¿Qué se cuenta y qué queda fuera? |
| **Decisión de uso** | ¿Qué acción o revisión cambiará cuando se mueva? |
| **Unidad y población** | ¿Cuál es la unidad de análisis y el denominador? |
| **Baseline y expectativa** | ¿Contra qué estado y rango se comparará? |
| **Fuente y owner** | ¿Quién responde por definición, calidad y acceso? |
| **Cadencia y horizonte** | ¿Cuándo se observa y cuándo debe evaluarse? |
| **Segmentación** | ¿Qué grupos o contextos no deben ocultarse en el promedio? |
| **Guardrail** | ¿Qué podría empeorar mientras la métrica mejora? |
| **Límite de atribución** | ¿Qué claim permite el diseño y cuál prohíbe? |
| **Regla de respuesta** | ¿Cuándo mantener, ampliar, detener, revertir o investigar? |

## Métricas calculables con condiciones

### Latencia

\[
L_{decisión}=t_{compromiso}-t_{señal\ elegible}
\]

\[
L_{acción}=t_{primera\ acción}-t_{compromiso}
\]

Registra por separado señal, disponibilidad de evidencia, compromiso y acción. Reducir la latencia solo es mejora si no deteriora calidad, derechos o riesgo. No uses una fecha retrospectiva elegida para favorecer el indicador.

### Fidelidad de ejecución

\[
F=\frac{\text{acciones elegibles ejecutadas según protocolo}}{\text{acciones elegibles planificadas}}
\]

El denominador requiere reglas previas y manejo explícito de excepciones. Si las acciones tienen importancia desigual, una tasa simple puede engañar; reporta componentes o pesos preregistrados.

### Cierre de aprendizaje

\[
C=\frac{\text{ciclos vencidos con revisión y cambio o confirmación documentada}}{\text{ciclos cuyo horizonte ya cerró}}
\]

Documentar una “lección” no basta. El numerador exige registrar qué se mantuvo o modificó y por qué.

### Calibración probabilística

Para eventos binarios repetidos y comparables, el Brier score es:

\[
BS=\frac{1}{N}\sum_{i=1}^{N}(p_i-y_i)^2
\]

donde \(p_i\) es la probabilidad registrada antes del evento y \(y_i\) vale 0 o 1. Menor es mejor. Las reglas de puntuación propias permiten evaluar pronósticos probabilísticos sin premiar reportes estratégicamente distorsionados.

**No uses Brier score para una decisión única, eventos redefinidos después, probabilidades no comparables o muestras demasiado pequeñas para inferir calibración.** Conserva además resolución, baseline y análisis por segmentos.

## Colaboración humano–IA

Mide el sistema sociotécnico, no solo el modelo.

| Señal | Lectura válida | Lectura inválida |
|---|---|---|
| **Override** | Motivo, contexto, resultado y si el control funcionó | “Menos overrides siempre es mejor” |
| **Acuerdo humano–IA** | Patrón diagnóstico junto con exactitud y dificultad | Sustituto automático de confianza o calidad |
| **Escalamiento** | Casos, tiempo, resolución y daño evitado | Penalizar al sistema por detenerse correctamente |
| **Incidente o near miss** | Severidad, población, respuesta y aprendizaje | Solo contar incidentes visibles |
| **Uso de recomendación** | Evidencia de integración al workflow | Prueba de impacto o de decisión correcta |

NIST AI RMF refuerza que las métricas deben responder al contexto de despliegue, documentar límites y combinar desempeño, riesgo, feedback y monitoreo. Esa fuente gobierna el componente de IA; no convierte este sistema CDI en un estándar NIST.

## Set mínimo viable

Para una decisión de riesgo bajo o medio, comienza con:

1. un outcome conectado a la prioridad;
2. una señal de fidelidad de ejecución;
3. al menos un guardrail material;
4. una expectativa con rango y horizonte;
5. una fecha y owner de revisión;
6. un bloqueador de calidad ex ante, si existe.

Agrega métricas solo si cambian una decisión, un control o una pregunta de aprendizaje.

## Anti-métricas

- **Número de decisiones tomadas:** premia volumen y fragmentación.
- **Velocidad sin calidad ni riesgo:** convierte demora en enemigo aunque esperar tenga valor.
- **Adopción o consultas al sistema:** mide uso, no consecuencia.
- **ROI sin baseline ni atribución:** convierte coincidencia temporal en impacto.
- **Tasa de override aislada:** no distingue corrección humana, fricción o complacencia.
- **Puntuación sintética universal:** permite compensar un bloqueador crítico con fortalezas irrelevantes.

## Agregación de portafolio

Agrega solo ciclos con definiciones, horizons, stakes y poblaciones comparables. Reporta distribuciones y segmentos antes que promedios. Las decisiones raras o críticas merecen revisión de caso, no una falsa serie temporal.

## Mejor contraargumento

Instrumentar seis lentes puede costar más que el valor de la decisión. El riesgo es real y de segundo orden: el registro se vuelve ritual, cambia incentivos y desplaza tiempo de actuar. La respuesta es proporcionalidad y set mínimo, no completar todos los campos por obligación.

**Alternativa potencialmente superior:** cuando exista una muestra longitudinal de decisiones reales, estimar fiabilidad entre revisores, sensibilidad al contexto, comportamiento adversarial de las métricas y relación con outcomes. Ese trabajo podría simplificar o reemplazar este candidato.

[Crear un Measurement Record →](measurement-record.md){ .md-button .md-button--primary }
