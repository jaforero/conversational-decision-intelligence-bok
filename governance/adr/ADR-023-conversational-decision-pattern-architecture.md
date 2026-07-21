---
id: ADR-023
title: Arquitectura de patrones de decisión conversacional
status: accepted
date: 2026-07-21
decision_owner: Javier Forero
scope: Sprint 6 conversational decision pattern candidate
---

# ADR-023: Arquitectura de patrones de decisión conversacional

## Contexto

El mapa estable `v0.4.0` declara Decision Patterns y Decision Anti-patterns como dominios por desarrollar. Los Sprints 4 y 5 ya aportan una ruta de aprendizaje, Decision Brief y medición, pero no existe un lenguaje reusable para organizar conversaciones recurrentes alrededor de una decisión.

El riesgo principal es convertir observaciones de diseño en recetas universales o confundir un patrón cognitivo con un prompt, componente o producto de IA. El PULSE Documentation Map reserva además fronteras futuras distintas para Decision Patterns, Pattern Library, Conversational Analytics y Component Library; el CDI-BoK no debe apropiarse de esas autoridades mediante un sprint candidato.

## Decisión

Crear `v0.8.0-rc.1` como candidato de **Conversational Decision Patterns & Anti-patterns** con estas reglas:

1. Un patrón describe un problema recurrente, fuerzas, movimientos, derechos, evidencia, salidas, riesgos y contraindicaciones; no una pantalla o prompt.
2. El catálogo inicial usa cinco momentos —enmarcar, fundamentar, deliberar, comprometer y aprender— como taxonomía candidata, no como secuencia obligatoria.
3. Cada patrón debe poder terminar en respuesta, abstención, escalamiento o cambio de interfaz.
4. La selección parte del bloqueo decisional y usa el patrón mínimo suficiente según stakes, incertidumbre, reversibilidad y daño potencial.
5. Los roles de recomendar, decidir, aprobar, ejecutar, detener y responder permanecen explícitos; conversación no transfiere autoridad a la IA.
6. Proceso, outcome, adopción y riesgo se miden por separado. Uso o aceptación no prueban impacto.
7. Cada anti-patrón describe comportamiento observable, daño plausible, riesgo de segundo orden, detección y reparación; la etiqueta no sustituye diagnóstico.
8. Procedencia y madurez se registran. `candidate-synthesis` no equivale a eficacia, consenso externo ni validación transversal.
9. El caso B2B se usa solo como demostración detenida. No se añade una interfaz conversacional ni cambia su estado `instrumented-not-executed`.
10. El catálogo se mantiene en un registro machine-readable y una plantilla con null states, stop conditions y tested contexts.

## Autoridad

- PULSE DNA gobierna Decision First, PDAMR, Decision Circle, Human-in-Control, evidencia, acción y aprendizaje.
- PULSE Documentation Map gobierna las fronteras entre sistemas, patrones y componentes futuros.
- La arquitectura por cinco momentos y las once entradas son una síntesis candidata del CDI-BoK.
- Outcome bias y AI risk se vinculan con fuentes registradas; esas fuentes no validan el catálogo completo.

## Consecuencias

- Decision Patterns y Decision Anti-patterns pasan de dominios declarados a guía pública candidata.
- Los equipos obtienen un vocabulario común para revisar conversaciones sin exigir una interfaz de IA.
- Aumenta el riesgo de burocracia, clasificación superficial y conformity pressure; se mitiga con proporcionalidad, contraindicaciones y salida de abstención.
- No se altera el núcleo estable `v0.4.0`, la autoridad constitucional de PULSE ni la evidencia del caso B2B.

## Contraargumento

Las conversaciones expertas son contextuales y dependen de conocimiento tácito; formalizarlas puede ralentizar decisiones, homogeneizar pensamiento y crear una ilusión de control. Además, cinco patrones elegidos editorialmente pueden reflejar la arquitectura previa del proyecto en lugar de la realidad organizacional.

La objeción permanece abierta. El candidato no exige usar el catálogo completo, permite reglas o workflows alternativos y requiere comprobar si reduce omisiones o solo agrega carga.

## Alternativa potencialmente superior

Observar primero una muestra diversa de conversaciones decisionales reales, codificar fallas y movimientos emergentes, y construir la taxonomía desde esa evidencia. Esta alternativa tendría mayor validez ecológica, pero hoy no existe el corpus ni la autorización. El catálogo candidato funciona como instrumento de prueba falsable y debe revisarse cuando aparezcan esos datos.
