---
title: 2. Sustentar con evidencia y contexto
description: Evalúa si la evidencia es adecuada para la decisión y separa hechos, inferencias, hipótesis y desconocidos.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains:
  - Decision Intelligence
  - Foundations
  - Data Storytelling
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-JF-005
  - SRC-ARCH-001
claim_ids:
  - CLAIM-PULSE-001
last_reviewed: 2026-07-21
---

# 2. Sustentar con evidencia y contexto

**Resultado del módulo:** un contrato que especifica qué evidencia necesita la decisión, qué tan confiable es, qué no permite concluir y qué información cambiaría la elección.

## Datos no son realidad

Los datos son evidencia registrada sobre una parte de la realidad. Pueden ser exactos y aun así no ser pertinentes; pueden llegar a tiempo y usar una definición equivocada; pueden mostrar asociación sin demostrar causa.

La pregunta útil no es solo **“¿los datos son buenos?”**, sino:

> **¿Son suficientemente confiables y pertinentes para esta decisión, este horizonte y este costo de error?**

## Seis etiquetas para no mezclar razonamientos

| Etiqueta | Ejemplo | Disciplina necesaria |
|---|---|---|
| **Hecho observado** | “Se registraron 420 solicitudes.” | Fuente, periodo, población y definición. |
| **Cálculo** | “La tasa fue 12,4%.” | Fórmula, numerador, denominador y tratamiento de faltantes. |
| **Inferencia** | “La caída parece concentrarse en un segmento.” | Método, incertidumbre y alternativas explicativas. |
| **Hipótesis** | “Reducir el tiempo de respuesta podría mejorar retención.” | Mecanismo plausible y prueba futura. |
| **Recomendación** | “Priorizar el segmento A.” | Criterios, trade-offs, riesgo y autoridad. |
| **Desconocido** | “No sabemos si cambió la mezcla de clientes.” | Impacto sobre la decisión y plan para reducir la brecha. |

Una narrativa puede contener las seis. El error aparece cuando una cambia de categoría sin aviso: una correlación se vuelve causa, una hipótesis se vuelve recomendación o una recomendación generada por IA se presenta como hecho.

## El contrato de evidencia

Para cada señal material documenta:

| Campo | Pregunta de control |
|---|---|
| **Procedencia** | ¿Quién produjo el dato, mediante qué proceso y con qué transformaciones? |
| **Definición** | ¿Todos entienden igual la entidad, métrica, evento y periodo? |
| **Calidad** | ¿Qué sabemos sobre completitud, duplicados, sesgo, error y oportunidad? |
| **Población** | ¿A quién o qué representa y qué queda fuera? |
| **Contexto** | ¿Qué proceso, regla, excepción, incentivo o cambio concurrente importa? |
| **Incertidumbre** | ¿Cuál es el rango plausible y qué supuestos lo determinan? |
| **Fitness for purpose** | ¿Qué decisiones permite sostener y cuáles no? |
| **Contraevidencia** | ¿Qué observación debilita la explicación preferida? |
| **Condición de cambio** | ¿Qué información cambiaría la conclusión o la acción? |

## El contexto que no vive en la tabla

El contexto incluye historia operacional, definiciones locales, incentivos, restricciones de capacidad, decisiones anteriores, excepciones y poder. Debe capturarse con procedencia: “lo dijo el equipo” no equivale a una regla aprobada ni a evidencia cuantitativa.

Separa al menos:

- **contexto estable:** reglas, estructura, contratos, límites regulatorios;
- **contexto temporal:** campañas, incidentes, estacionalidad, cambios de personal;
- **conocimiento local:** explicación de quienes ejecutan el proceso;
- **intereses e incentivos:** quién gana, pierde o controla la interpretación.

## Cuándo detener una conclusión

No avances a recomendación si ocurre alguno de estos casos y el defecto es material para la decisión:

- el denominador no puede reconstruirse;
- la definición cambió entre periodos sin ajuste;
- faltan segmentos afectados por la acción;
- el modelo se aplica fuera de la población evaluada;
- una explicación causal depende solo de simultaneidad;
- el dato sensible no tiene permiso o propósito legítimo;
- la incertidumbre cambia el orden de las alternativas.

Detener una conclusión no siempre detiene la decisión. Puede obligar a elegir una opción más reversible, reducir alcance o incorporar un guardrail.

## Prueba de estrés

- ¿Cuál es el mejor contraargumento a nuestra lectura?
- ¿Qué parte de la conclusión depende de un único supuesto?
- ¿Podría el mismo patrón surgir sin el mecanismo propuesto?
- ¿Qué grupo, periodo o resultado no estamos viendo?
- ¿La fuente tiene autoridad para definir el concepto o solo informa una observación?
- ¿Qué nivel de incertidumbre vuelve indistinguibles las opciones?

## Entregable

Construye una tabla con una fila por evidencia material y las nueve columnas del contrato. Cierra con tres listas: **sabemos**, **inferimos**, **aún no sabemos**.

**Siguiente:** [diseñar la experiencia que conecta evidencia y acción →](03-decision-experience.md)
