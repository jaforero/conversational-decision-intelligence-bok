---
id: ADR-018
title: Ciclo de evidencia para casos del Practice Lab
status: accepted
date: 2026-07-21
decision_owner: Javier Forero
scope: Practice Lab and case evidence
---

# ADR-018: Ciclo de evidencia para casos del Practice Lab

## Contexto

Una demo puede demostrar diseño, cálculo o interacción sin demostrar que una decisión mejoró. Sprint 3 necesita conectar el BoK con práctica observable sin transformar resultados simulados o una interfaz convincente en evidencia causal.

## Decisión

Todo caso del Practice Lab avanzará por cinco estados trazables:

1. `catalogued`: la demo existe y su alcance fue inspeccionado;
2. `selected`: existe una razón explícita para priorizarla;
3. `instrumented-not-executed`: decisión, baseline, alternativas, expectativa y protocolo están definidos, pero no hay acción ni resultado;
4. `observed-noncausal`: existe resultado posterior, sin atribución suficiente;
5. `evaluated`: el análisis compara intervención y contrafactual con limitaciones explícitas.

El estado debe publicarse junto al caso. Ningún caso puede saltar de demo a evidencia de impacto. La calidad del proceso decisional se registra antes de observar el resultado; el resultado y la atribución se evalúan por separado.

## Consecuencias

- El Practice Lab puede publicar instrumentos útiles antes de tener resultados reales.
- Una release candidata no promueve automáticamente un caso a evidencia validada.
- La ausencia de owner, acción, expectativa o contrafactual se muestra como bloqueo, no se completa por inferencia.
- El ciclo reduce outcome bias, pero añade fricción; por eso el registro mínimo debe ser proporcional al costo del error y de la demora.

## Alternativas descartadas

- **Publicar solo demos:** no prueba el bucle de aprendizaje.
- **Esperar hasta tener un experimento completo:** oculta trabajo reproducible que ya es útil para diseñar la decisión.
- **Usar esperado versus real sin comparador:** confunde cambio temporal con efecto atribuible.
