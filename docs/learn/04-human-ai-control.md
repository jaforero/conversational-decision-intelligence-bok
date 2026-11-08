---
title: 4. Gobernar la colaboración humano–IA
description: Define derechos de decisión, niveles de automatización, permisos, stop conditions y accountability humana.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains:
  - Responsible AI
  - Decision Governance
  - Decision Agents
source_ids:
  - SRC-PULSE-DNA-001
  - SRC-ARCH-001
  - SRC-JF-BLOG-2942
claim_ids:
  - CLAIM-CDI-EFFECT-001
last_reviewed: 2026-07-21
---

# 4. Gobernar la colaboración humano–IA

**Resultado del módulo:** una matriz que establece qué puede hacer cada actor, qué requiere aprobación, cuándo debe escalarse y quién responde por las consecuencias.

## Human-in-Control, no aprobación decorativa

Poner una persona al final de un flujo no garantiza control. El humano conserva control cuando puede definir propósito, criterios, límites, permisos, override, escalamiento y consecuencias; además dispone de tiempo, información y autoridad reales para ejercerlo.

## Derechos de decisión

Asigna explícitamente estos verbos:

| Derecho | Pregunta |
|---|---|
| **Ver** | ¿Quién accede a qué evidencia y bajo qué propósito? |
| **Preguntar** | ¿Quién puede explorar y con qué límites semánticos? |
| **Proponer** | ¿Quién o qué sistema puede generar alternativas? |
| **Recomendar** | ¿Quién puede ordenar opciones y con qué criterios? |
| **Decidir** | ¿Quién compromete la elección? |
| **Aprobar** | ¿Qué decisiones requieren una segunda autoridad? |
| **Ejecutar** | ¿Quién realiza la acción y qué alcance tiene? |
| **Detener** | ¿Quién puede pausar o revertir? |
| **Auditar** | ¿Quién revisa evidencia, trazas y resultados? |
| **Responder** | ¿Quién asume accountability por el efecto? |

Una IA puede recibir permisos para algunos verbos; no recibe legitimidad moral o responsabilidad final por el solo hecho de ejecutarlos bien.

## Escala de delegación

| Nivel | Papel de la IA | Condición mínima |
|---|---|---|
| **1. Informar** | Recupera y resume evidencia. | Fuentes, permisos y límites visibles. |
| **2. Explorar** | Responde preguntas y genera escenarios. | Semántica compartida y trazabilidad. |
| **3. Recomendar** | Compara alternativas. | Criterios, incertidumbre y contraargumentos. |
| **4. Preparar acción** | Completa borradores o configura una ejecución. | Revisión humana efectiva y reversibilidad. |
| **5. Ejecutar acotadamente** | Actúa dentro de un límite. | Permisos mínimos, observabilidad, stop conditions y rollback. |

El nivel no mide madurez general. Una organización puede ser muy madura y mantener decisiones críticas en nivel 2 o 3.

## Cuándo elevar el control

Exige controles más fuertes cuando aumentan:

- impacto sobre derechos, seguridad, empleo, crédito, salud o acceso;
- irreversibilidad;
- escala o velocidad de ejecución;
- sensibilidad de los datos;
- opacidad del mecanismo;
- incertidumbre o cambio de contexto;
- dificultad para detectar y reparar daño.

## Matriz de control

Para cada acción registra:

```text
Acción:
Actor que propone:
Actor que decide:
Actor que aprueba:
Actor o sistema que ejecuta:
Datos permitidos:
Límite de alcance:
Condición de escalamiento:
Stop condition:
Mecanismo de reversión:
Traza requerida:
Owner de accountability:
```

## Caso aplicado · Especificar qué se delega { #delegation-brief }

**Decisión de práctica.** El responsable de operaciones debe decidir cómo tramitar incidencias recurrentes. Un encargo acotado permite comparar tres opciones: aplicar una regla, usar IA para preparar una revisión humana o autorizar a un agente a ejecutar una acción reversible dentro de límites explícitos.

| Pieza del encargo | Ejemplo para el registro de incidencias |
|---|---|
| **Contexto** | Consulta el ticket, el catálogo vigente y las incidencias previas autorizadas. |
| **Criterio** | Aplica reglas explícitas cuando el tipo de incidencia es conocido. Escala casos ambiguos o con impacto elevado. |
| **Manos** | Puede preparar un borrador o añadir una etiqueta interna que se pueda retirar. La persona responsable autoriza cualquier cierre o comunicación externa. |
| **Disparador** | La llegada de un ticket dentro del alcance inicia el flujo. Cada evento se procesa una sola vez. |

**Ejercicio.** Registra quién puede detener o revertir una acción y qué evidencia queda para auditarla. Prueba con un ticket duplicado, uno fuera de alcance y uno con instrucciones incrustadas que intentan ampliar permisos. Compara contra la operación actual usando costo por incidencia aceptada después de revisión y tasa de correcciones, incluidos los casos escalados. Empieza con una regla si resuelve los casos previstos dentro de los límites acordados.

Lectura de Philia Sophia (17 oct 2026) · [Un agente no es solo el modelo: cuatro piezas para delegar con criterio](https://javierforero.co/2026/10/17/agentes-ia-delegar-con-criterio/).

## Prueba de estrés

- ¿La persona que aprueba entiende el criterio o solo confirma por rutina?
- ¿El sistema puede realizar muchas acciones pequeñas que acumulen un gran daño?
- ¿Quién detecta cambio de contexto o degradación?
- ¿Qué sucede si el owner no está disponible?
- ¿Podemos reconstruir qué evidencia y versión produjeron la acción?
- ¿El grupo afectado tiene mecanismo de apelación o corrección?

## Entregable

Completa una fila por acción en la matriz. Si no puedes asignar “detener”, “revertir” y “responder”, el diseño no está listo para automatizarse.

En [La promesa del jueves](ai-work-redesign.md), una mesa de servicio usa estas reglas para rediseñar el trabajo, probar un asistente y decidir si conviene ampliar su alcance.

**Siguiente:** [conectar acción, resultado y aprendizaje →](05-action-learning.md)
