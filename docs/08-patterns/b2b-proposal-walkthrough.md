---
title: Patrones aplicados al caso B2B
description: Aplicación didáctica y detenida de los patrones conversacionales al caso simulado de Propuesta B2B, sin inventar owner, acción ni outcome.
status: candidate
version: 0.8.0-rc.1
artifact_type: pattern-demonstration
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains:
  - Decision Patterns
  - Case Studies
  - PULSE
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-PRACTICE-B2B-001
  - SRC-PRACTICE-DASH-B2B-001
claim_ids:
  - CLAIM-PRACTICE-B2B-001
  - CLAIM-PRACTICE-B2B-002
  - CLAIM-PRACTICE-B2B-003
  - CLAIM-PRACTICE-B2B-HYP-001
  - CLAIM-CDP-CATALOG-001
last_reviewed: 2026-07-21
---

# Patrones aplicados al caso B2B

<div class="cdi-insight" markdown>

**Demostración detenida.** El caso usa datos simulados y permanece `instrumented-not-executed`. La conversación puede ordenar la revisión, pero no convertir owner, acción, expectativa u outcome ausentes en hechos.

</div>

La fuente del MVP concluye que una interfaz conversacional sería **decorativa para un solo ciclo**. Esta página respeta ese límite: aplica los patrones como protocolo de una reunión o revisión guiada. Un asistente podría facilitarlo, pero un checklist, un brief o una persona competente son alternativas más simples y actualmente suficientes.

## Estado de entrada

| Elemento | Evidencia disponible | Estado |
|---|---|---|
| Priority | Recuperar cumplimiento tras el deterioro abril–junio del demo | Provisional, solo para demostración |
| Decision | Dónde intervenir primero sin ampliar innecesariamente adquisición | Formulada |
| Owner | Director(a) Comercial propuesto | **No confirmado** |
| Action | Depende de la opción elegida | **No ejecutada** |
| Metric | Conversión de Propuesta y cumplimiento | Baseline simulado disponible |
| Risk | Reversión a la media, confusores, muestras pequeñas, sobrecarga | Identificado |
| Outcome | Ninguno posterior a una intervención | **No observado** |

## Movimiento 1 — Contrato de decisión

**Facilitador:** “¿La elección es intervenir Propuesta, reasignar canales, combinar acciones o no actuar todavía?”

**Registro permitido:** las opciones A–D ya existen en el contrato. La preferencia por A es provisional por cercanía a la señal y reversibilidad.

**Desafío:** “¿Quién tiene derecho a elegir y antes de qué fecha?”

**Salida real:** el owner continúa **por confirmar**. `CDP-001` no autoriza avanzar a compromiso; transforma esa ausencia en un bloqueo visible.

## Movimiento 2 — Frontera de evidencia

La conversación debe mantener separadas estas clases:

| Clase | Declaración permitida |
|---|---|
| Hecho sobre la fuente | El dashboard declara datos simulados. |
| Cálculo reproducido | Junio registra 80,11% de cumplimiento y Propuesta cae 11,50 pp entre los trimestres observados. |
| Inferencia | El deterioro parece más localizado en conversión que en volumen. |
| Hipótesis | Intervenir calidad y velocidad de propuestas puede mejorar conversión frente a un comparador. |
| Desconocido | Operación real, owner, acción, expectativa, comparabilidad y outcome. |

**Desafío:** “¿Las tasas por canal justifican mover presupuesto?”

**Respuesta calibrada:** evento y referido presentan tasas observadas mayores que inbound digital, pero los intervalos son amplios y se superponen. La evidencia disponible no establece superioridad robusta ni autoriza reasignar presupuesto.

## Movimiento 3 — Desafío de opciones

| Opción | Mejor argumento | Contraargumento fuerte | Qué cambiaría su estado |
|---|---|---|---|
| A · Mejorar Propuesta | Señal cercana y acción reversible | Pricing o mix podrían explicar el deterioro | Diagnóstico operativo, owner y capacidad de ejecución |
| B · Reasignar canales | Tasas observadas mayores en evento/referido | Muestra pequeña y evidencia no concluyente | Más observaciones, diseño comparativo y costo incremental |
| C · A + B | Ataca conversión y origen | Impide atribuir qué componente funcionó | Diseño factorial o capacidad para medir componentes |
| D · No actuar | Evita reaccionar a una anomalía | La demora puede profundizar la brecha | Evidencia de estacionalidad o nuevo corte temporal |

**Salida:** A conserva preferencia para una **primera prueba**, no para ejecución automática. B y C permanecen bloqueadas; D es comparador activo.

## Movimiento 4 — Handoff decisión–acción

Este patrón encuentra sus stop conditions:

- no hay decision owner confirmado;
- no existe opción formalmente elegida;
- acción, responsable y fecha están pendientes;
- la expectativa inferior, central y superior no está congelada;
- el alcance real y el comparador no están asignados.

Por tanto, la única salida válida es:

> **Preparado para revisión del owner; no autorizado para ejecutar.**

Una conversación que produjera “ejecutemos A” estaría incurriendo en **ANTI-CDI-004 — Autoridad sin derechos**.

## Movimiento 5 — Revisión expectativa–resultado

`CDP-005` todavía **no aplica**. No hay expectativa congelada, acción ejecutada, horizonte cerrado ni outcome observado. Crear una revisión narrativa simularía evidencia y activaría **ANTI-CDI-006 — Expectativa reconstruida**.

El próximo paso no es redactar un aprendizaje. Es completar el gate previo:

1. confirmar owner y decision rights;
2. seleccionar o rechazar una opción;
3. registrar acción, alcance, responsable y fecha;
4. congelar expectativa en rango y horizonte;
5. definir comparación, guardrails y stop conditions;
6. ejecutar solo después de aprobación;
7. observar al menos el horizonte acordado.

## Lo que demuestra y lo que no

**Demuestra dentro del artefacto:** los patrones pueden revelar omisiones, preservar las clases de evidencia y detener una conversación antes de fabricar compromiso o aprendizaje.

**No demuestra:** que una interfaz conversacional mejore la decisión, que A sea eficaz, que PULSE produzca impacto comercial o que el catálogo sea superior a una facilitación competente.

### Alternativa potencialmente superior

Para el estado actual, completar el [contrato de decisión](../practice-lab/b2b-proposal/decision-contract.md) en una reunión con el owner es más simple y defendible que construir un copilot. Una interfaz conversacional solo debería considerarse si varios ciclos recurrentes muestran fricción de acceso o deliberación que el protocolo manual no resuelve.

<div class="cdi-actions" markdown>
[Revisar el caso](../practice-lab/b2b-proposal/index.md){ .md-button .md-button--primary }
[Volver al catálogo](catalog.md){ .md-button }
</div>
