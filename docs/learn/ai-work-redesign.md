---
title: Rediseñar el trabajo con IA · La promesa del jueves
description: Una historia sobre cuándo incorporar IA a un proceso, cómo repartir la autoridad y qué evidencia justifica ampliar un piloto.
status: candidate
version: 0.9.0
artifact_type: learning-module
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Decision Architectures, Decision Governance, AI Native Analytics]
source_ids: [SRC-PULSE-DNA-001, SRC-JF-BLOG-1973, SRC-JF-BLOG-2705, SRC-JF-BLOG-2529, SRC-JF-BLOG-2748, SRC-JF-BLOG-2806, SRC-JF-BLOG-2828, SRC-JF-BLOG-2942]
claim_ids: []
last_reviewed: 2026-11-08
---

# Rediseñar el trabajo con IA · La promesa del jueves

*Capítulo narrativo basado en los artículos de Javier Forero en Philia Sophia. La empresa, los personajes, las políticas y los resultados del piloto son ficticios.*

## Una respuesta impecable { #the-decision }

El jueves, a las ocho y doce, el asistente redactó su primera respuesta de prueba para un cliente que esperaba un repuesto. «Confirmamos que su pedido saldrá hoy».

El correo estaba listo en segundos. Lucía, que llevaba el turno de servicio, abrió el registro de inventario. Quedaba una unidad. En otra pantalla encontró el dato que faltaba en el borrador. La unidad estaba reservada para otro pedido.

—¿Quién prometió el despacho? —preguntó Mateo, el analista nuevo.

—Todavía nadie —dijo Lucía, y cerró el borrador—. Estamos probando. Si lo enviamos, la promesa es nuestra.

El viernes, Irene, responsable de Operaciones, debía decidir **si cambiaba la forma de resolver las solicitudes de repuestos y qué parte del trabajo le confiaría a la IA**. Su prioridad era que el cliente recibiera antes una respuesta que el equipo pudiera cumplir. Equivocarse significaba rehacer el caso, desplazar otro pedido o incumplir una promesa. Esperar también tenía un costo. El cliente seguía sin saber cómo organizar su reparación.

## IA predice, tú piensas { #prediction-and-judgment }

Al revisar juntos el borrador, Lucía le pidió a Mateo separar tres cosas. El texto era **una propuesta**. La reserva registrada en Almacén era **evidencia**. Comprometer una fecha era **una decisión** con consecuencias para el cliente y para el pedido que ya tenía la pieza asignada.

El modelo podía redactar una respuesta plausible con el contexto que recibía. Verificar el estado del pedido, valorar qué hacer si dos registros discrepaban y responder por la promesa requerían acceso, tiempo y autoridad. Irene protegió esas tres condiciones para el equipo. Lucía podía rechazar el borrador, pedir una confirmación y seguir atendiendo al cliente por el flujo habitual.

Esta es la distinción que propone Javier Forero en [IA predice, tú piensas](https://javierforero.co/2025/11/28/ia-predice-tu-piensas-hype-tecnologico/). En la mesa de servicio, controlar la decisión significaba poder cambiar el criterio o detener la acción antes de que una propuesta se volviera un compromiso.

## La demora vivía entre dos escritorios { #the-workflow }

Lucía y Mateo reconstruyeron el camino de una solicitud. Servicio leía el correo, pedía un identificador, consultaba la política y preguntaba a Almacén por el inventario. Almacén contestaba cuando alguien podía interrumpir su turno. Servicio volvía al correo y hacía una promesa. A veces repetía la consulta porque el primer mensaje había quedado en un buzón personal.

—El asistente puede leer el correo —dijo Mateo—. ¿Qué hacemos con la espera?

El equipo probó primero un formulario común, un identificador por caso y una consulta autorizada que distinguía **existencias registradas** de **unidades disponibles para ese pedido**. Las solicitudes incompletas seguían abiertas con un responsable y una hora para el próximo contacto. El equipo podía operar con esos cambios usando reglas y plantillas.

Sobre ese flujo acordaron un alcance para la IA. El sistema aplicaría reglas explícitas a los campos obligatorios y a la asignación estándar. El modelo extraería datos del texto libre y prepararía un borrador con referencias al registro y a la política vigente. Si faltaba la confirmación de Almacén, el borrador podía pedirla o proponer una actualización sin fecha de despacho. La política y el estado del pedido eran la evidencia para sostener una promesa.

## Las llaves de la mesa { #decision-rights }

Para el piloto, la identidad de quien atendía el caso determinaba qué registros se recuperaban **antes** de enviar contexto al modelo. La consulta tenía acceso de lectura al pedido asignado y a la política vigente. Una discrepancia de inventario, una condición contractual especial o un registro fuera del alcance iba a revisión manual. El borrador mostraba la fuente y su hora de consulta. Almacén confirmaba la reserva en el sistema de pedidos. Servicio comprobaba esa confirmación antes de comprometer una fecha.

| Zona de juicio | Qué hace el sistema | Qué cambia en el rol |
|---|---|---|
| **Delegar** | Ordena la solicitud y extrae campos para su revisión. Las reglas verifican los campos estructurados y aplican la asignación estándar. | Mateo deja de copiar datos entre pantallas y aprende a comprobar de dónde salió cada campo. |
| **Co-crear** | Prepara una respuesta que se puede contrastar con el pedido y la política. | Servicio verifica la evidencia, modifica o rechaza el borrador y registra el motivo cuando detecta un error. |
| **Proteger** | Deriva las excepciones a una persona y presenta los hechos permitidos. | Almacén confirma la reserva. Servicio conserva la autoridad de comprometer una fecha dentro de la política. Irene aprueba las excepciones y responde por el proceso. |

Mateo propuso que, más adelante, el asistente moviera solicitudes entre colas internas. Irene le pidió describir primero qué delegaría. El **disparador** sería un caso estándar validado. El **contexto** incluiría el identificador, el estado y las reglas vigentes. El **criterio** sería una regla de destino y una salida a revisión ante ambigüedad. Las **manos** serían un permiso para cambiar solo la cola interna, con registro y reversión. Si la regla bastaba para elegir la cola, una automatización convencional podía hacerlo. El piloto se quedó en lectura y preparación de borradores.

Lucía también reservó tiempo para que los nuevos resolvieran casos sin el asistente y luego compararan criterios con alguien del turno. En un ejercicio, les mostró dos borradores igual de convincentes y pidió decidir cuál podía enviarse siguiendo cada afirmación hasta su fuente. Los errores de borrador se discutirían como fallas del proceso o del sistema que merecían investigación. Los registros del piloto servirían para corregir el flujo y capacitar al equipo.

## Cuatro semanas para probar el cambio { #pilot-and-learning }

Irene comparó tres opciones. **Quedarse con el flujo rediseñado y reglas** era la alternativa de menor complejidad y el respaldo operativo. **Probar ese mismo flujo con un asistente** permitía evaluar si leer texto libre y preparar respuestas añadía valor. **Autorizar ejecución autónoma** requería evidencias y controles de los que el equipo aún carecía, incluida la capacidad de detectar y revertir una acción incorrecta. Eligió el piloto de asistencia.

Primero se trabajó en modo sombra, sin usar borradores para responder. Luego, durante cuatro semanas, se asignaron casos estándar al azar dentro de cada turno y tipo de solicitud. Un grupo usó el flujo rediseñado con reglas y plantillas. El otro usó el mismo flujo con el asistente y revisión humana. Los dos tenían el mismo acceso a las fuentes. Los casos especiales siguieron el proceso manual. Para contar como primera respuesta verificable, el mensaje debía indicar un estado confirmado o el siguiente paso con responsable y plazo. La revisión dejó siete días completos de seguimiento por caso.

Antes de empezar, Irene fijó como criterios didácticos ahorrar al menos tres minutos de trabajo por caso y vigilar que la reapertura no aumentara más de dos puntos porcentuales. Una exposición de datos, un envío sin aprobación o un compromiso sin reserva confirmada activaría la pausa inmediata, la vuelta al flujo de respaldo y una revisión del registro por Operaciones y el responsable de acceso. El flujo debía poder seguir funcionando con el asistente apagado.

| Observación simulada | Flujo con reglas y plantillas | Mismo flujo con asistente |
|---|---:|---:|
| Casos estándar asignados | 120 | 120 |
| Trabajo humano medio por caso, incluida la revisión | 14 min | 10 min |
| Mediana hasta la primera respuesta verificable, en horario laboral | 90 min | 74 min |
| Casos reabiertos en siete días | 6 de 120 (5,0 %) | 7 de 120 (5,8 %) |
| Incidentes que obligaban a pausar | 0 observados | 0 observados |

Los cuatro minutos de diferencia equivalían a **ocho horas de trabajo en los 120 casos del grupo asistido**. Parte de ese tiempo se destinó a revisar expedientes rezagados. Para establecer el beneficio realizado faltaba medir el efecto de ese trabajo sobre el rezago y sumar integración, capacitación, soporte y operación. El aumento observado en reaperturas fue de 0,8 puntos porcentuales. Con tan pocos casos, seguía siendo incierto si el aumento real respetaba el límite. La ausencia de incidentes en el piloto daba poca información sobre fallas infrecuentes.

**Decisión de Irene.** Mantener la asistencia en la mesa piloto y conservar el flujo con reglas como respaldo. En el siguiente corte de cuatro semanas revisaría las causas de reapertura por turno y tipo de caso, el costo total por caso cerrado, las horas destinadas al rezago y las pruebas de bloqueo y escalamiento. Consideraría ampliar a otra mesa si la calidad se sostenía con evidencia suficiente y el equipo podía demostrar qué valor obtuvo del tiempo liberado.

Mateo volvió al caso del jueves. Ya sabía dónde mirar antes de prometer un despacho. En su cuaderno anotó una pregunta para el turno siguiente.

—Si dos fuentes dicen cosas distintas, ¿quién puede comprobar qué ocurrió?

## Lleva el caso a tu empresa { #try-it }

Escoge un flujo donde la demora o el retrabajo importe. Usa el [Decision Brief](decision-brief.md) para documentar estos cinco puntos de PULSE antes de elegir la intervención.

| Punto | Pregunta que tu equipo debe contestar |
|---|---|
| **Prioridad** | ¿Qué resultado importa y quién experimenta hoy la demora o el error? |
| **Decisión** | ¿Quién elige entre conservar el flujo, simplificarlo con reglas, asistirlo con IA o delegar una acción delimitada? |
| **Acción** | ¿Qué cambia en el trabajo de cada rol? ¿Quién conserva la autoridad para comprometer recursos, resolver excepciones y detener la ejecución? |
| **Métrica** | ¿Con qué línea base comparable evaluarás tiempo total, calidad y costo? ¿Quién se hará cargo de convertir el tiempo liberado en un resultado observable? |
| **Riesgo** | ¿Qué evidencia y permisos necesita cada acción? ¿Qué señal activa una pausa y quién puede volver al flujo de respaldo? |

Dibuja el recorrido de un caso antes y después. Ensaya una solicitud estándar, una excepción y un intento de consultar un registro fuera de alcance. Pide a la persona que ejecuta el trabajo que muestre cuándo corrige al asistente y cómo se registra esa corrección. Cierra con una fecha de revisión y la evidencia que te haría ampliar, limitar o suspender el cambio.

Puedes seguir la evidencia hasta su origen en [La Aldea de los Datos](data-architecture-fable.md), asignar autoridad con el módulo de [control humano–IA](04-human-ai-control.md) y preparar la revisión con [acción y aprendizaje](05-action-learning.md). El [laboratorio de evaluación de asistentes](../practice-lab/conversational-evidence.md) ofrece ejercicios para probar la calidad de las respuestas. El [puente de los cinco niveles de analítica a PULSE](../03-pulse/from-five-levels.md) permite ubicar qué análisis hace falta antes de actuar.

## Las lecturas detrás del caso { #source-readings }

| Artículo de Javier Forero | Aporte al capítulo |
|---|---|
| [IA predice, tú piensas](https://javierforero.co/2025/11/28/ia-predice-tu-piensas-hype-tecnologico/) | Es el eje del caso. Separa la propuesta generada de la evidencia y de la decisión que asume el equipo. |
| [AI-Native y el rediseño del trabajo](https://javierforero.co/2026/07/11/ai-native-redisenar-trabajo-empresa/) | Da el hilo conductor. La capacidad de la IA, el juicio humano, la plataforma, el flujo de trabajo y el aprendizaje explican qué cambió en la mesa de servicio. |
| [Alfabetización en IA y juicio](https://javierforero.co/2026/06/11/alfabetizacion-ia-delegar-cocrear-proteger/) | Aporta las zonas de delegar, co-crear y proteger, y orienta la práctica con la que Mateo desarrolla criterio. |
| [RAG empresarial y permisos](https://javierforero.co/2026/07/28/rag-empresarial-permisos/) | Motiva recuperar evidencia según el acceso de la persona, antes de entregarla al modelo. |
| [Dos mapas para usar la IA con criterio](https://javierforero.co/2026/08/16/triangulo-ia-modelo-prompt-contexto/) | Ayuda a separar reglas estables de tareas que requieren interpretar texto ambiguo. |
| [Cuatro piezas para delegar con criterio](https://javierforero.co/2026/10/17/agentes-ia-delegar-con-criterio/) | Da el vocabulario para delimitar contexto, criterio, manos y disparador antes de permitir una acción. |
| [Cómo medir el retorno de la IA](https://javierforero.co/2026/08/30/roi-ia-medir-retorno-valor/) | Distingue el ahorro de tiempo observado del valor capturado y pone la calidad en la decisión de ampliar. |

*Nota editorial. Capítulo pedagógico candidato. Los artículos aportan el punto de vista del autor. El caso y sus cifras se construyeron para practicar decisiones de diseño. La redacción y la traducción recibieron apoyo de IA.*
