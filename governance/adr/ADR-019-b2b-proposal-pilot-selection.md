---
id: ADR-019
title: Selección y frontera del piloto B2B Propuesta
status: accepted
date: 2026-07-21
decision_owner: Javier Forero
scope: Sprint 3 first instrumented case
---

# ADR-019: Selección y frontera del piloto B2B Propuesta

## Contexto

El catálogo incluye decisiones financieras, comerciales, operativas y predictivas. El caso comercial B2B ya combina ventas, funnel y pipeline CRM; presenta una señal material y una acción reversible. Sin embargo, la implementación pública declara que los datos son simulados y todavía no existe evidencia registrada de acción, owner confirmado o resultado posterior.

## Decisión

Seleccionar `B2B-PROP-001` como primer caso instrumentado del CDI-BoK y asignarle estado `instrumented-not-executed` en `v0.5.0-rc.1`.

- La opción A —intervenir calidad y velocidad en Propuesta— queda como preferencia provisional por reversibilidad y ajuste al diagnóstico; no es todavía una decisión tomada.
- Las opciones B y C no se recomiendan hasta fortalecer la evidencia por canal. Evento y referido tienen tasas observadas superiores a inbound digital, pero los intervalos de Wilson al 95% se superponen.
- La expectativa cuantitativa, el owner real y los grupos de intervención/comparación deben fijarse antes de actuar.
- Un claim causal requiere al menos dos ciclos mensuales y un contrafactual defendible; tres ciclos son preferibles.

## Consecuencias

El sprint prueba la capacidad de especificar, preregistrar y auditar el bucle. No prueba que la intervención funcione ni que PULSE mejore decisiones. Para evaluar impacto, el protocolo debe trasladarse a datos CRM gobernados y a un owner con autoridad real.

## Alternativa potencialmente superior

Si no se obtiene owner o datos reales, usar el caso solo como prueba de instrumentación y priorizar después un piloto SLA con retención a nivel cliente. Esa alternativa puede tener mayor impacto transversal, pero hoy carece de la unión SLA–churn necesaria.
