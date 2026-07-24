---
title: Estado del arte de Decision Intelligence
description: Evaluación candidata y trazable de los fundamentos, fronteras, evidencia y vacíos de Decision Intelligence y PULSE.
status: candidate
version: 0.9.0-rc.1
artifact_type: state-of-the-art
authority_level: bounded-evidence-synthesis
normative: false
owner: Javier Forero
domains: [Research, Decision Intelligence, Human-AI Collaboration]
claim_ids: [CLAIM-DI-MATURITY-001, CLAIM-DI-LAYERS-001, CLAIM-PULSE-SYNTHESIS-001, CLAIM-PULSE-BIOLOGICAL-LENSES-001, CLAIM-HUMAN-AI-EVIDENCE-001]
source_ids: [SRC-ACADEMIC-DECISION-ANALYSIS-001, SRC-OMG-DMN-001, SRC-NIST-AIRMF-001, SRC-ACADEMIC-INFOQUALITY-001, SRC-ACADEMIC-ORGLEARNING-001, SRC-ACADEMIC-HAI-001, SRC-ACADEMIC-AIEVAL-001, SRC-ACADEMIC-RUDIN-001, SRC-PULSE-DNA-001, SRC-PULSE-IDENTITY-002, SRC-JF-005, SRC-ARCH-001]
as_of: 2026-07-24
last_reviewed: 2026-07-24
---

# Estado del arte de Decision Intelligence

<span class="cdi-release">Candidato v0.9.0-rc.1 · Evaluación focalizada, no revisión sistemática</span>

## Conclusión ejecutiva

Decision Intelligence (DI) se entiende aquí como un **campo de práctica
integrador y emergente**: reúne disciplinas y prácticas maduras alrededor del
ciclo completo de una decisión, pero la revisión realizada no permite
presentarlo como una disciplina científica consolidada con fronteras, métodos y
corpus propios universalmente aceptados.

Esta es una evaluación candidata, fechada y falsable. La ausencia de evidencia
en este corpus no prueba que esa evidencia no exista.

## 1. ¿Qué es DI y de dónde proviene?

DI desplaza el foco desde producir información o modelos hacia diseñar,
ejecutar y aprender de decisiones. Su linaje no empieza con una tecnología
única:

| Capa | Aporte a DI | Límite |
|---|---|---|
| Teoría y análisis de decisiones | Alternativas, incertidumbre, preferencias, valor y calidad del proceso | No cubren por sí solos operación continua ni conversación |
| Investigación de operaciones y DSS | Modelos, optimización y apoyo computacional | Un resultado óptimo no garantiza adopción, control o aprendizaje |
| Calidad de datos e información | Aptitud de la evidencia para el uso | Calidad de datos no equivale a calidad de decisión |
| Modelado y automatización | Decisiones explícitas, reglas y ejecución reproducible | Automatizar no resuelve legitimidad, accountability o causalidad |
| Aprendizaje organizacional | Feedback, exploración y explotación | Registrar decisiones no demuestra que la organización aprenda |
| Human–AI Interaction | Diseño de colaboración, deliberación y control | Los efectos dependen de tarea, interfaz, usuario y comparación |

## 2. ¿Qué la diferencia de campos vecinos?

| Campo | Pregunta principal | Relación con DI |
|---|---|---|
| Business Intelligence | ¿Qué ocurrió y cómo se observa? | Aporta visibilidad; DI exige conectar evidencia con decisión y acción |
| Analytics y Data Science | ¿Qué patrón, pronóstico o efecto puede estimarse? | Aportan modelos; DI añade autoridad, alternativas, guardrails y seguimiento |
| Decision Analysis | ¿Cómo estructurar una decisión bajo incertidumbre? | Es un fundamento directo, no un antecedente que DI sustituya |
| Decision Support Systems | ¿Cómo apoyar una decisión con sistemas? | Aporta tradición sociotécnica y operativa |
| EDM y DMN | ¿Cómo modelar, gestionar y automatizar decisiones repetibles? | Son prácticas maduras en evolución dentro del mapa, no sinónimos de DI |
| Conversational Analytics | ¿Cómo explorar datos mediante lenguaje natural? | La conversación es una interfaz; no garantiza una decisión gobernada |
| Agentes de IA | ¿Qué tareas puede planificar o ejecutar un sistema? | La agencia aumenta la necesidad de derechos, stop conditions y trazabilidad |

## 3. ¿Qué está establecido?

“Establecido” no significa infalible ni universal. Significa que el componente
tiene un linaje propio y fuentes primarias u oficiales verificables:

- análisis de decisiones y estructuración bajo incertidumbre;
- investigación de operaciones y sistemas de apoyo;
- calidad de datos e información dependiente del uso;
- outcome bias y separación entre proceso y resultado;
- reglas de puntuación para pronósticos probabilísticos repetidos;
- modelado de decisiones mediante la especificación formal DMN;
- gestión de riesgo de IA mediante marcos públicos como NIST AI RMF;
- aprendizaje organizacional como problema de feedback y adaptación.

## 4. ¿Qué permanece emergente o en disputa?

- qué frontera separa DI de una integración bien gobernada de disciplinas
  existentes;
- cuándo una interfaz conversacional mejora deliberación o solo aumenta
  fluidez y confianza;
- cómo comparar humano, humano+IA e IA sola sin confundir aceptación con
  calidad;
- qué control humano es significativo cuando un agente puede actuar;
- cómo medir contribución a outcomes sin atribuir causalidad a la interfaz;
- si existe un corpus acumulativo propio de DI y bajo qué criterios.

La evidencia revisada sobre humano–IA es dependiente del contexto. Un estudio
exploratorio de deliberación no autoriza un efecto universal; una evaluación en
otro dominio puede encontrar ausencia de mejora. En decisiones de alto riesgo,
la interpretabilidad del modelo puede ser una propiedad de diseño preferible a
una explicación posterior de una caja negra.

## 5. ¿Qué integra PULSE?

PULSE organiza una síntesis propia alrededor de:

- **PDAMR:** Priority, Decision, Action, Metric y Risk;
- **Decision Circle:** realidad, decisión, acción, resultado y aprendizaje;
- **cinco verbos:** enfocar, comprender, decidir, actuar y aprender;
- **Human-in-Control:** autoridad, escalamiento y responsabilidad explícitos;
- **Decision Experience:** evidencia y contexto convertidos en una experiencia
  orientada a acción.

Las fuentes constitucionales gobiernan esta identidad. Los textos del autor
explican su linaje y propósito. Ninguno de los dos tipos demuestra por sí solo
que PULSE produzca mejores outcomes que una alternativa.

## 6. ¿Qué no está validado?

No está establecido que:

- CDI sea una disciplina científica madura o que el proyecto haya acuñado el
  término;
- PULSE sea superior, universal o causalmente eficaz;
- la arquitectura L0–L7 sea doctrina aprobada;
- interocepción, alostasis u “organismo decisional” sean mecanismos
  organizacionales literales;
- cinco niveles de analítica constituyan una escala universal de madurez;
- conversación, copilotos o agentes mejoren siempre la decisión;
- el caso B2B represente una intervención ejecutada o un outcome atribuible.

## 7. ¿Qué evidencia cambiaría esta conclusión?

Elevaríamos o reduciríamos la fuerza de los claims ante:

1. una revisión sistemática reproducible del corpus DI;
2. estudios comparativos multicontexto con humano, humano+IA e IA sola;
3. replicaciones y resultados nulos o adversos publicados;
4. pilotos PULSE preregistrados con baseline, comparador, guardrails y
   seguimiento;
5. evidencia externa sobre validez, utilidad y costo de sus artefactos;
6. nuevas versiones oficiales de estándares y marcos registrados;
7. revisión académica y profesional independiente del mapa.

<div class="cdi-risk" markdown>
**Límite de decisión:** este mapa permite decidir qué investigar y cómo hablar
con precisión. No autoriza afirmar que CDI o PULSE ya estén científicamente
validados.
</div>

## Fuentes primarias seleccionadas

- [Decision Analysis: Practice and Promise](https://doi.org/10.1287/mnsc.34.6.679)
- [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/About-DMN)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Human–AI deliberation, CHI 2025](https://doi.org/10.1145/3706598.3713423)
- [Evaluación de humano, humano+IA e IA sola](https://arxiv.org/abs/2403.12108)
- [Modelos interpretables en decisiones de alto riesgo](https://doi.org/10.1038/s42256-019-0048-x)

Continúe con el [mapa de evidencia de PULSE](pulse-evidence-map.md) o la
[agenda de investigación](research-agenda.md).
