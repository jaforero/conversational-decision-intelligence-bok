---
title: Catálogo de patrones conversacionales
description: Cinco patrones candidatos para enmarcar, fundamentar, deliberar, comprometer y aprender alrededor de una decisión.
status: candidate
version: 0.8.0-rc.1
artifact_type: pattern-catalog
authority_level: candidate-synthesis-and-guidance
normative: false
owner: Javier Forero
domains:
  - Decision Patterns
  - Conversational Decision Intelligence
  - Decision Governance
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-ARCH-001
  - SRC-ACADEMIC-HAI-001
  - SRC-ACADEMIC-OUTCOME-BIAS-001
claim_ids:
  - CLAIM-CDP-CATALOG-001
  - CLAIM-CDP-SELECTION-001
last_reviewed: 2026-07-21
---

# Catálogo de patrones conversacionales

Los cinco patrones cubren bloqueos recurrentes del ciclo, no cinco pantallas ni cinco prompts. Pueden guiar una reunión, un brief, un dashboard con seguimiento o un asistente conversacional gobernado. Ninguno exige IA.

| ID | Patrón | Momento | Salida mínima |
|---|---|---|---|
| `CDP-001` | Contrato de decisión | Enmarcar | Decisión, owner, alternativas, fecha y acción esperada |
| `CDP-002` | Frontera de evidencia | Fundamentar | Hechos, inferencias, desconocidos y fitness for purpose |
| `CDP-003` | Desafío de opciones | Deliberar | Opciones comparables, trade-offs y qué cambiaría la elección |
| `CDP-004` | Handoff decisión–acción | Comprometer | Elección autorizada, ejecución, guardrails y escalamiento |
| `CDP-005` | Revisión expectativa–resultado | Aprender | Desviación, atribución calibrada y ajuste del siguiente ciclo |

## CDP-001 — Contrato de decisión

**Contexto.** Una conversación comienza con “analiza ventas”, “¿qué hacemos?” o “dime qué está pasando”, pero no declara la elección que debe realizarse.

**Problema.** El sistema puede producir información relevante sin cambiar una decisión. La ausencia de owner, alternativas o fecha permite que cada participante interprete una tarea distinta.

**Fuerzas y trade-offs.** Enmarcar reduce ambigüedad, pero un contrato exhaustivo puede ralentizar decisiones reversibles. La urgencia puede exigir una definición mínima, no ausencia de definición.

**Movimientos.**

1. Convertir el tema en una pregunta de elección: “¿Quién debe elegir qué, entre cuáles alternativas y antes de cuándo?”.
2. Completar PDAMR sin redefinirlo: Priority, Decision, Action, Metric y Risk.
3. Declarar owner, personas afectadas, costo de error, costo de demora y reversibilidad.
4. Incluir **no actuar** cuando sea una alternativa material.
5. Confirmar el contrato con quien posee el decision right.

**Salida.** Un Decision Brief mínimo o un registro equivalente que otra persona pueda revisar sin reconstruir la conversación.

**Stop condition.** Si no existe una elección real o nadie puede asumir ownership, reclasificar la conversación como exploración informativa. No simular una decisión.

**Consecuencias y riesgos.** Mejora foco y trazabilidad; puede crear falsa legitimidad si un facilitador asigna owner sin autoridad. A segundo orden, el formulario puede sustituir criterio y convertirse en ritual burocrático.

**Alternativa superior en ciertos contextos.** Para decisiones repetitivas con criterios estables, una regla operativa o tabla de decisión puede ser más clara que una conversación.

**Relación con PULSE.** Business First, Decision First, PDAMR y Focus.

## CDP-002 — Frontera de evidencia

**Contexto.** La decisión ya está formulada, pero cifras, definiciones, filtros o explicaciones entran en conflicto.

**Problema.** Una respuesta fluida puede mezclar hecho, cálculo, inferencia, hipótesis y recomendación. El lenguaje natural oculta con facilidad una diferencia semántica o una fuente no apta.

**Fuerzas y trade-offs.** Mayor trazabilidad aumenta confianza y revisión, pero agrega fricción. La respuesta más reciente o detallada no es necesariamente la más apropiada para la decisión.

**Movimientos.**

1. Restablecer alcance: población, periodo, unidad de análisis, filtros y definición de métrica.
2. Identificar fuente, corte, owner, lineage y permisos.
3. Separar **hecho**, **cálculo**, **inferencia**, **hipótesis**, **recomendación** y **desconocido**.
4. Evaluar fitness for purpose según costo del error; no exigir perfección irrelevante ni aceptar calidad insuficiente.
5. Exponer contraevidencia, sensibilidad e información que cambiaría la conclusión.
6. Responder, abstenerse o escalar con una razón verificable.

**Salida.** Un paquete de evidencia delimitado y una conclusión cuya fuerza no excede sus fuentes.

**Stop condition.** Si definiciones materiales no pueden reconciliarse, faltan permisos o la calidad no alcanza el uso previsto, no avanzar a recomendación.

**Consecuencias y riesgos.** Reduce drift semántico y claims excesivos. Puede generar sobre-gobernanza o retrasar una acción segura y reversible. A segundo orden, los usuarios pueden aprender a tratar la cita como autoridad sin revisar su calidad.

**Alternativa superior en ciertos contextos.** Un reporte controlado es preferible cuando la pregunta, el cálculo y el formato están regulados o son recurrentes.

**Relación con PULSE.** Trust First, Context First, Evidence Before Authority y Perceive.

## CDP-003 — Desafío de opciones

**Contexto.** La conversación llega con una recomendación dominante, una dicotomía falsa o una lista de ideas sin comparación.

**Problema.** Generar muchas opciones no equivale a deliberar. Sin supuestos, criterios, trade-offs y reversibilidad, la lista amplifica disponibilidad o preferencia previa.

**Fuerzas y trade-offs.** Más alternativas pueden reducir premature closure, pero también aumentar carga cognitiva y demorar. La diversidad aparente puede ser cosmética si todas las opciones preservan el mismo supuesto.

**Movimientos.**

1. Explicitar criterios, restricciones y pesos solo cuando sean defendibles.
2. Construir dos o más alternativas materialmente distintas, incluida no actuar cuando aplique.
3. Para cada opción, declarar mecanismo esperado, supuesto frágil, costo, demora, riesgo y reversibilidad.
4. Formular el mejor contraargumento contra la opción preferida.
5. Buscar una alternativa potencialmente superior, no una variante decorativa.
6. Indicar qué evidencia o escenario cambiaría el ranking.

**Salida.** Una comparación auditable con opción provisional, condiciones de cambio y confianza calibrada.

**Stop condition.** Si el tiempo exige aplicar una regla preaprobada o si generar alternativas aumenta daño inmediato, ejecutar el protocolo de emergencia correspondiente y registrar la excepción.

**Consecuencias y riesgos.** Hace visibles trade-offs y fragilidad. Puede producir “option theater”, donde el sistema genera alternativas inverosímiles para aparentar rigor. A segundo orden, criterios numéricos no validados pueden ocultar juicios políticos o distributivos.

**Alternativa superior en ciertos contextos.** Taller facilitado, análisis de decisión formal o revisión multidisciplinaria cuando existen stakeholders en conflicto o impactos de alta consecuencia.

**Relación con PULSE.** Generate options, Anticipate y Evidence Before Authority.

## CDP-004 — Handoff decisión–acción

**Contexto.** Existe una recomendación o una preferencia, pero no está claro si se decidió, quién puede comprometer recursos o qué sucede después.

**Problema.** El lenguaje “deberíamos” permite confundir consejo, aprobación y ejecución. Un agente puede transformar esa ambigüedad en una acción no autorizada.

**Fuerzas y trade-offs.** Un handoff explícito reduce pérdida entre análisis y ejecución, pero puede añadir aprobación innecesaria. La automatización aumenta velocidad y también escala el error.

**Movimientos.**

1. Distinguir **recomienda**, **decide**, **aprueba**, **ejecuta**, **detiene** y **responde**.
2. Registrar opción elegida, alternativas descartadas y razón en el momento de decisión.
3. Traducir la elección en acción, responsable, fecha, dependencias y confirmación.
4. Declarar permisos de IA, revisión humana, guardrails, stop conditions, reversión y escalamiento.
5. Fijar expectativa, horizonte y fecha de revisión antes de ejecutar.
6. Emitir un comprobante de compromiso; no inferir aprobación por silencio.

**Salida.** Una decisión autorizada y un plan de acción trazable, o una abstención/escalamiento explícito.

**Stop condition.** Sin decision right, aprobación requerida o capacidad de reversión proporcional al riesgo, el sistema solo puede preparar el handoff.

**Consecuencias y riesgos.** Reduce recomendaciones huérfanas y authority laundering. Puede concentrar poder si los decision rights están mal diseñados; a segundo orden, la traza puede usarse para castigar desacuerdo legítimo y disminuir dissent.

**Alternativa superior en ciertos contextos.** Workflow transaccional con controles deterministas cuando la acción es repetitiva y sus reglas están aprobadas.

**Relación con PULSE.** Decide and Act, Governance Enables Speed y Human-in-Control.

## CDP-005 — Revisión expectativa–resultado

**Contexto.** Terminó el horizonte de una decisión y el equipo necesita aprender sin juzgar el proceso únicamente por el outcome.

**Problema.** Conocer el resultado favorece reconstruir expectativas, olvidar alternativas y atribuir causalidad a una intervención sin contrafactual suficiente.

**Fuerzas y trade-offs.** La revisión genera aprendizaje potencial, pero resultados ruidosos pueden enseñar la lección equivocada. Un ciclo aislado rara vez separa suerte, ejecución y decisión.

**Movimientos.**

1. Abrir el snapshot previo sin sobrescribirlo: expectativa, rango, horizonte, supuestos y opción elegida.
2. Registrar outcome, métricas de proceso, guardrails, efectos no previstos y calidad de ejecución.
3. Comparar esperado y observado; describir la desviación antes de explicarla.
4. Evaluar contrafactual, confusores, tamaño de muestra y fuerza de atribución.
5. Separar calidad ex ante, fidelidad de ejecución y resultado.
6. Decidir qué mantener, ampliar, detener, revertir o investigar en el siguiente ciclo.

**Salida.** Un aprendizaje que cambia percepción, criterio, acción o control; no solo una narrativa retrospectiva.

**Stop condition.** Si no existe snapshot previo, etiquetar la revisión como exploratoria y prohibir claims fuertes sobre precisión de expectativa o efecto de la decisión.

**Consecuencias y riesgos.** Protege contra outcome bias y cierre ceremonial. Puede institucionalizar ruido como política si el equipo fuerza una lección. A segundo orden, una cultura punitiva puede inducir pronósticos conservadores o registros defensivos.

**Alternativa superior en ciertos contextos.** Evaluación causal, auditoría independiente o agregación de múltiples ciclos cuando el costo de atribuir mal es alto.

**Relación con PULSE.** Learn, Value Must Be Observable y Decision Measurement Record.

## Qué validaría o refutaría el catálogo

La conclusión cambiaría si el uso longitudinal muestra que los patrones:

- no mejoran completitud, trazabilidad o action fidelity frente a prácticas actuales;
- aumentan materialmente la latencia sin reducir error;
- producen gaming, conformity pressure o delegación indebida;
- requieren clases de decisión diferentes a las cinco propuestas;
- funcionan mejor como reglas, formularios o workflows sin conversación.

Hasta obtener esa evidencia, el catálogo conserva madurez `candidate-synthesis`.
