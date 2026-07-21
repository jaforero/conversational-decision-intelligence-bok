---
title: Catálogo de anti-patrones
description: Seis anti-patrones candidatos para detectar conversación decorativa, drift semántico, certeza artificial, autoridad indebida, métricas de adopción engañosas y aprendizaje retrospectivo.
status: candidate
version: 0.8.0-rc.1
artifact_type: anti-pattern-catalog
authority_level: candidate-synthesis-and-guidance
normative: false
owner: Javier Forero
domains:
  - Decision Anti-patterns
  - Conversational Decision Intelligence
  - Responsible AI
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-ARCH-001
  - SRC-ACADEMIC-OUTCOME-BIAS-001
  - SRC-NIST-AIRMF-001
claim_ids:
  - CLAIM-CDP-CATALOG-001
last_reviewed: 2026-07-21
---

# Catálogo de anti-patrones

Estas entradas son **diagnósticos candidatos**, no relaciones causales universales. Un síntoma aislado no prueba que una implementación sea dañina; exige revisar contexto, frecuencia, stakes y consecuencias.

## ANTI-CDI-001 — Dashboard disfrazado de conversación

**Comportamiento.** Se añade un chat a métricas existentes, pero las respuestas no conocen decisión, owner, alternativas, acción ni horizonte.

**Por qué parece útil.** Reduce clics y responde preguntas ad hoc.

**Daño probable.** Confunde acceso a información con soporte decisional y aumenta respuestas sin compromiso. A segundo orden, la adopción del chat puede justificar inversión adicional aunque la decisión permanezca igual.

**Señal de detección.** Después de una conversación satisfactoria nadie puede decir qué elección cambió, quién actuará o cuándo se revisará.

**Reparación.** Aplicar `CDP-001`; si solo se necesita consulta, nombrar la experiencia como Conversational Analytics y evaluarla por exactitud y utilidad informativa, no como CDI.

**Alternativa superior.** Mejorar definiciones, alertas o navegación del dashboard puede resolver el problema con menos complejidad.

## ANTI-CDI-002 — Conversación sin semántica ni procedencia

**Comportamiento.** El sistema responde cifras sin definición, población, filtros, fecha de corte, fuente o permisos verificables.

**Por qué parece útil.** La respuesta es rápida, natural y evita detalles técnicos.

**Daño probable.** Dos respuestas plausibles pueden usar denominadores distintos. A segundo orden, la fluidez normaliza inconsistencias y amplía su circulación.

**Señal de detección.** La misma pregunta produce valores incompatibles que no pueden reconciliarse mediante alcance o lineage.

**Reparación.** Aplicar `CDP-002`, incorporar capa semántica mínima y mostrar alcance junto con la respuesta.

**Alternativa superior.** Reporte controlado cuando las definiciones son reguladas o no existe readiness conversacional.

## ANTI-CDI-003 — Certeza fluida

**Comportamiento.** Inferencia, predicción o recomendación se expresan como hechos; los rangos y desconocidos desaparecen para mantener una narrativa segura.

**Por qué parece útil.** Reduce ambigüedad percibida y facilita una respuesta ejecutiva.

**Daño probable.** Eleva la fuerza del claim por encima de la evidencia. A segundo orden, recompensa al sistema más persuasivo en lugar del más calibrado.

**Señal de detección.** No aparece contraevidencia ni información capaz de cambiar la conclusión.

**Reparación.** Separar clases de afirmación, mostrar incertidumbre material y usar `CDP-002` + `CDP-003`.

**Alternativa superior.** Abstenerse o pedir revisión experta cuando la incertidumbre impide una recomendación segura.

## ANTI-CDI-004 — Autoridad sin derechos

**Comportamiento.** Una recomendación de IA se presenta como decisión o un agente ejecuta porque “el usuario estuvo de acuerdo”, sin aprobación, límites o escalamiento explícitos.

**Por qué parece útil.** Reduce handoffs y acelera acción.

**Daño probable.** Produce acciones no autorizadas y accountability difuso. A segundo orden, los humanos pueden dejar de cuestionar recomendaciones o aprobarlas de forma ritual.

**Señal de detección.** No es posible distinguir quién recomendó, decidió, aprobó y ejecutó.

**Reparación.** Aplicar `CDP-004`, reducir permisos al mínimo y exigir confirmación positiva para compromisos materiales.

**Alternativa superior.** Workflow determinista con segregación de funciones y rollback cuando la acción es repetitiva.

## ANTI-CDI-005 — Adopción como impacto

**Comportamiento.** Sesiones, preguntas, usuarios activos, aceptación de recomendaciones o reducción de tiempo se reportan como prueba de mejores decisiones.

**Por qué parece útil.** Son métricas tempranas, disponibles y atribuibles al producto.

**Daño probable.** Optimiza engagement aunque la acción o el outcome no mejoren. A segundo orden, fomenta nudges hacia uso frecuente y reduce atención a efectos distributivos o errores silenciosos.

**Señal de detección.** El business case no contiene baseline decisional, action fidelity, outcome ni guardrails.

**Reparación.** Mantener adopción como métrica de uso y conectarla con el Decision Measurement System; no elevarla a valor por sí sola.

**Alternativa superior.** Piloto comparativo que observe proceso, acción, outcome y riesgo durante un horizonte apropiado.

## ANTI-CDI-006 — Expectativa reconstruida

**Comportamiento.** Después de conocer el outcome, el equipo redefine lo que “realmente esperaba”, las alternativas que “siempre consideró” o el objetivo que “quería optimizar”.

**Por qué parece útil.** Produce una historia coherente y protege reputación.

**Daño probable.** Impide calibración y confunde buena decisión con buen resultado. A segundo orden, institucionaliza una explicación falsa y ajusta el siguiente ciclo en la dirección equivocada.

**Señal de detección.** No existe snapshot previo, timestamp o expectativa en rango; el registro histórico cambia durante la revisión.

**Reparación.** Aplicar `CDP-005`, preservar snapshots y etiquetar la revisión como exploratoria cuando falte el preregistro.

**Alternativa superior.** Revisión independiente o análisis agregado de ciclos cuando los incentivos favorecen hindsight.

## Control de segundo orden

El propio catálogo puede convertirse en anti-patrón si:

- se usa como checklist universal sin costo proporcional;
- una etiqueta reemplaza el análisis de causa;
- se clasifica a personas en lugar de comportamientos observables;
- el sistema “detecta” anti-patrones y sanciona sin revisión humana;
- el equipo optimiza conformidad con el catálogo en lugar de outcomes y aprendizaje.

La reparación es tratar cada entrada como hipótesis diagnóstica: buscar evidencia a favor y en contra, registrar incertidumbre y probar una intervención reversible.
