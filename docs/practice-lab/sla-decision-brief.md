---
title: Decision Brief resuelto · SLA de entregas
description: Un ejemplo completo de cómo actuar sobre una caída del SLA, decidir si hace falta un pronóstico y revisar el resultado.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Decision Intelligence, Decision Governance, Decision Metrics]
source_ids: [SRC-PULSE-DNA-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# Decision Brief resuelto · SLA de entregas

**Ejemplo con datos simulados.** Las rutas, cifras y decisiones de esta página se construyeron para el ejercicio. Sigue la [plantilla Decision Brief](../learn/decision-brief.md) y desarrolla el caso de SLA del [laboratorio de dashboards](dashboards.md).

**Decisión registrada el viernes de la semana 4.** Trasladar una ventana de despacho por día hábil de la ruta B a la ruta A durante la semana 5, con reversión preparada y revisión diaria.

## 1. Prioridad

Recuperar el cumplimiento de entregas de A hasta el **95 %** sin que B caiga por debajo del **97 %**, el umbral de protección de este piloto. En las cuatro semanas previas, A cumplió el **92 %** y B el **98 %**. Esperar deja a A expuesta a otro corte por debajo de la meta. El horizonte de prueba es una semana.

## 2. Decisión y alternativas

La jefatura de Operaciones aprueba el viernes antes de cerrar la programación. Coordinación de Despacho ejecuta y puede restituir la ventana a B el siguiente día hábil. Las dos rutas y sus clientes quedan afectados.

| Alternativa | Beneficio esperado | Costo o condición |
|---|---|---|
| **A. Trasladar una ventana al día durante cinco días hábiles** | A gana capacidad antes del cierre con recursos existentes. | B cede margen. Solo se mueve la ventana si sus pedidos confirmados caben y conserva una ventana de reserva. |
| **B. Mantener la asignación y esperar otro corte** | B conserva su margen y no hay costo de reasignación. | A sigue expuesta a incumplir. Se elige si la reserva de B no puede verificarse. |
| **C. Agregar una ventana con horas extra** | A gana capacidad sin reducir la reserva de B. | Requiere presupuesto y autorización. Queda disponible si ambas rutas necesitan capacidad. |

## 3. Evidencia y contexto disponibles antes de actuar

**Definición.** SLA = entregas elegibles a tiempo ÷ entregas elegibles con fecha prometida en la semana. Se usa la misma regla en ambas rutas y en todos los cortes. Cada celda muestra entregas a tiempo sobre entregas elegibles.

| Corte | Ruta A | Ruta B |
|---|---:|---:|
| Semana 1 | 94/100 | 98/100 |
| Semana 2 | 93/100 | 98/100 |
| Semana 3 | 91/100 | 98/100 |
| Semana 4 | 90/100 | 98/100 |
| **Baseline de cuatro semanas** | **368/400 = 92 %** | **392/400 = 98 %** |

- **Hechos del escenario.** Se cotejaron el tablero, el registro de despacho y el plan de capacidad. Los cuatro cortes de A quedaron bajo la meta y 23 de sus 32 entregas tardías salieron después del cierre del centro. El plan de la semana 5 permite trasladar una ventana diaria y conservar una de reserva en B con los pedidos confirmados.
- **Inferencia e hipótesis.** La concentración de salidas tardías justifica probar capacidad antes del cierre. Algunas demoras también podrían surgir en la carga o en la ruta. Los registros disponibles no separan esos mecanismos.
- **Qué bastó.** La brecha repetida, un mecanismo plausible y capacidad comprobable justifican un cambio acotado y reversible. Si B pierde la reserva o los registros muestran que el retraso ocurre después del despacho, cambia la opción elegida.

## 4. Experiencia de decisión y umbral para pronosticar

La jefatura usa el tablero para localizar la brecha y el plan de capacidad para comparar las tres opciones. El registro diario indica si la ventana se usó y si B conservó su reserva. Para este piloto bastan los pedidos confirmados, la verificación diaria y la opción de revertir.

**¿Cuándo haría falta un pronóstico?** Si una parte importante de la demanda aún no está confirmada y puede consumir la reserva de B, o si el traslado debe durar varias semanas y resulta más costoso revertirlo. En ese caso, estima rangos de demanda por ruta y compáralos con la capacidad posterior al traslado. Si hasta el escenario alto cabe con la reserva acordada, la opción A sigue siendo viable. Si la reserva se agota en un escenario plausible, conserva la asignación o solicita horas extra según el costo de esperar.

## 5. Control humano y ejecución

Operaciones decide y aprueba, y Despacho ejecuta desde el lunes. En el ejercicio, una IA podría resumir las métricas agregadas y señalar diferencias para revisión. Cambiar turnos, aprobar horas extra y emitir instrucciones queda a cargo de las personas autorizadas. El registro conserva el corte usado, la opción aprobada, las ventanas trasladadas y cualquier excepción.

## 6. Acción, métricas y regla de revisión acordada

- **Proceso.** Registrar cuántas de las cinco ventanas previstas se usaron. Revisar a diario los pedidos confirmados y la reserva de B. Si la reserva se pierde, detener el traslado y restituir la ventana el siguiente día hábil.
- **Resultado esperado antes de actuar.** SLA semanal de A de **92 % / 95 % / 97 %** en escenarios bajo, central y alto. Son supuestos de trabajo para la revisión. El piso de B es **97 %**.
- **Revisión al cierre de la semana 5.** Mantener el traslado durante otro ciclo acotado si A llega al **95 %** y B conserva al menos **97 %**. Si A queda por debajo y B está protegida, revisar si la ventana se usó y dónde persiste la demora antes de repetir. Si B baja de **97 %**, revertir aunque A llegue a su meta.
- **Comparación.** Usar el baseline de cada ruta para comparar desempeño. B también recibe la intervención porque pierde capacidad y no sirve como grupo de control.

## 7. Resultado simulado y decisión revisada

| Ruta | Baseline | Semana 5 | Cambio | Lectura según la regla |
|---|---:|---:|---:|---|
| A | 92 % | 96/100 = **96 %** | **+4 pp** | Cumple la meta. |
| B | 98 % | 96/100 = **96 %** | **−2 pp** | Incumple el umbral de protección. |

Se usaron **5 de 5** ventanas y la reserva de B se mantuvo en el plan diario. Aun así, al cierre B quedó por debajo del umbral. **Operaciones revierte el traslado el lunes de la semana 6** y revisa si la reserva operativa de B cubre la variabilidad de la semana. La mejora en A y la caída en B son cambios observados en la simulación. Comparar una semana posterior con el baseline no permite atribuirlos al traslado.

**Registro de cuestionamiento.** El supuesto más frágil era que una ventana de reserva bastaba para proteger B. La composición de pedidos o incidentes de despacho también pudo cambiar los resultados. Mantener el traslado pese al umbral podría acumular incumplimientos en B y erosionar el servicio a sus clientes. La confianza es **media para probar una acción reversible** y **baja para atribuirle el resultado**. Antes de ampliar, contrastar cortes comparables y evaluar horas extra o una prueba escalonada con una ruta comparable que conserve su capacidad.
