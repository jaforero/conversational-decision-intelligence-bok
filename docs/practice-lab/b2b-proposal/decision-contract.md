---
title: Contrato de decisión B2B
description: PDAMR, alternativas, derechos de decisión y prerregistro mínimo para la intervención sobre Propuesta.
status: candidate
version: 0.5.0-rc.1
artifact_type: decision-contract
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains:
  - Decision Patterns
  - Decision Governance
  - Decision Quality
source_ids:
  - SRC-PRACTICE-B2B-001
  - SRC-PRACTICE-DASH-B2B-001
claim_ids:
  - CLAIM-PRACTICE-B2B-HYP-001
last_reviewed: 2026-07-21
---

# Contrato de decisión B2B

Este contrato operacionaliza PDAMR sin redefinirlo. Los campos pendientes son deliberados: deben ser completados por personas con autoridad y conocimiento operativo, no por el CDI-BoK.

## PDAMR instanciado

| Elemento | Contrato del caso |
|---|---|
| **Priority** | Recuperar el cumplimiento comercial después del deterioro observado entre abril y junio. |
| **Decision** | Elegir la primera intervención sobre el funnel y decidir si actuar ahora. |
| **Action** | Traducir la opción elegida en alcance, responsable, fecha y stop conditions. **Pendiente.** |
| **Metric** | Conversión de Propuesta y cumplimiento; expectativa en rango; horizonte de 1–2 meses. |
| **Risk** | Reversión a la media, confusores, n pequeño por canal, sobrecarga operativa y aprendizaje falso. |

## Derechos de decisión

| Derecho | Rol propuesto | Estado |
|---|---|---|
| Decide | Director(a) Comercial | **Por confirmar** |
| Aprueba presupuesto | Finanzas, si aplica reasignación | **Condicional** |
| Ejecuta | Líderes de ventas | **Por confirmar** |
| Escala | Comité comercial | **Por confirmar** |
| Audita expectativa y resultado | Analítica / Decision Steward | **Por asignar** |

Sin owner confirmado no existe piloto organizacional: existe un diseño de piloto.

## Alternativas

| Opción | Acción | Mejor argumento | Riesgo principal | Reversibilidad | Estado |
|---|---|---|---|---|---|
| **A** | Mejorar calidad, velocidad, coaching y seguimiento de propuestas. | Ataca la mayor caída observada y puede acotarse. | Consume capacidad; el problema real podría ser pricing o mix. | Alta | Preferencia provisional. |
| **B** | Mover presupuesto de digital masivo a evento/referido. | Las tasas observadas son mayores. | Muestras pequeñas; la diferencia no está establecida con precisión. | Media | Evidencia insuficiente. |
| **C** | Ejecutar A + B. | Ataca conversión y calidad de origen. | Impide saber qué componente produjo el cambio. | Media | No recomendada para el primer ciclo. |
| **D** | No actuar todavía. | Protege contra reaccionar a una anomalía. | Un mes adicional puede profundizar la brecha. | Alta | Comparador activo. |

## Criterio de elección

La opción A domina como **primera prueba**, no como verdad: es más reversible, está más cerca de la señal y permite preservar B para un ciclo posterior. La conclusión cambia si el deterioro desaparece con una definición robusta de estacionalidad, si pricing explica la caída o si no existe capacidad para intervenir.

## Prerregistro obligatorio

Antes de actuar, el owner debe fijar y bloquear:

- opción elegida y alternativas descartadas;
- alcance de vendedores, regiones u oportunidades;
- acción, responsable, fecha y condiciones de parada;
- baseline aprobado y análisis de sensibilidad;
- expectativa inferior, central y superior;
- horizonte;
- intervención y comparación;
- confusores conocidos;
- puntuación de calidad de proceso.

[Descargar el registro YAML](../../assets/data/b2b-proposal-decision-record.yml){ .md-button .md-button--primary }

## Rúbrica de calidad de proceso

Se puntúa **antes** de conocer el resultado, de 0 a 2 por criterio.

| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| Alternativas reales | Solo opción preferida | Dos opciones poco diferenciadas | Opciones materiales, incluida no actuar |
| Evidencia clasificada | Mezclada | Clasificación parcial | Hecho, cálculo, inferencia e hipótesis separados |
| Incertidumbre | Omitida | General | Supuestos, rango y qué cambiaría declarados |
| Trade-offs | Omitidos | Parciales | Costos, demora, reversibilidad y efectos secundarios |
| Expectativa previa | No existe | Punto sin rango | Rango, horizonte y timestamp bloqueados |

Un puntaje alto no garantiza un buen outcome; documenta que el proceso evitó omisiones básicas.
