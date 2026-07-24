---
title: Señales futuras
description: Pronósticos y señales de industria gobernados como escenarios, no como hechos ni compromisos.
status: candidate
version: 0.9.0-rc.1
artifact_type: future-signals-register
authority_level: bounded-forecast-synthesis
normative: false
owner: Javier Forero
domains: [Research, Future Directions, AI Agents]
claim_ids: [CLAIM-FUTURE-SIGNALS-001, CLAIM-DMN-VERSION-001, CLAIM-NIST-REVISION-001]
source_ids: [SRC-GARTNER-PREDICTIONS-001, SRC-GARTNER-VALUE-001, SRC-OMG-DMN-001, SRC-OMG-DMN-BETA-001, SRC-NIST-AIRMF-001]
as_of: 2026-07-24
last_reviewed: 2026-07-24
---

# Señales futuras

Una señal futura ayuda a tensionar una estrategia. **No predice con certeza, no
prueba readiness y no autoriza una inversión por sí sola.** Los informes de
analista se registran por metadatos y hash; sus PDF no se redistribuyen.

## Registro de señales

| Señal | Horizonte | Incertidumbre principal | Pregunta de decisión | Evidencia que la revisa |
|---|---|---|---|---|
| Las interfaces conversacionales pueden absorber parte de la exploración que hoy ocurre en dashboards | corto–medio | adopción, exactitud, costo y adecuación de tarea | ¿Qué decisiones necesitan conversación, visualización o ambas? | telemetría por tarea y comparación contra la interfaz actual |
| Copilotos y agentes pueden pasar de explicar a proponer o ejecutar acciones | corto–medio | autoridad, errores en cadena, reversibilidad y control | ¿Qué derechos puede delegar el owner y bajo qué stop conditions? | incidentes, override, reversión, exactitud y outcome |
| El valor de datos e IA puede medirse más cerca de decisiones y outcomes | medio | atribución y métricas manipulables | ¿Qué decisión cambia y qué alternativa sirve de comparador? | línea base, contrafactual y seguimiento |
| Capas semánticas y modelos explícitos de decisión pueden ganar importancia | medio | interoperabilidad y costo de mantenimiento | ¿Qué semántica debe gobernarse antes de automatizar? | defectos, reutilización, trazabilidad y tiempo de cambio |
| La gobernanza puede desplazarse desde artefactos aislados hacia sistemas sociotécnicos | medio–largo | madurez regulatoria y fragmentación | ¿Qué controles siguen siendo efectivos cuando el sistema aprende o actúa? | auditorías, fallos de control y versiones oficiales |

## Cómo usar una señal

1. Traducirla a una decisión concreta, no a una tendencia genérica.
2. Declarar horizonte y supuesto crítico.
3. Diseñar un indicador temprano y una condición de abandono.
4. Comparar al menos dos escenarios plausibles.
5. Registrar qué observación confirmaría, refutaría o volvería irrelevante la
   señal.

## Señales normativas y de estándares

Las versiones también cambian. Al `2026-07-24`:

- OMG publica DMN 1.5 como especificación formal y DMN 1.7 Beta 1 como
  documento informativo; una decisión de conformidad debe verificar el
  inventario oficial vigente.
- NIST mantiene AI RMF 1.0 disponible e informa que está en revisión; no se
  presupone el contenido de una versión futura.

## Qué queda prohibido

- “Gartner dice que ocurrirá” como hecho;
- usar un año objetivo como probabilidad;
- convertir adopción esperada en beneficio esperado;
- presentar una beta como estándar formal;
- derivar readiness de mercado sin evaluar datos, procesos, personas y control;
- presentar una señal como validación de PULSE o CDI.

<div class="cdi-risk" markdown>
**Stop condition:** si una señal no cambia una decisión, un experimento o un
indicador, es contexto narrativo y no inteligencia de decisión.
</div>
