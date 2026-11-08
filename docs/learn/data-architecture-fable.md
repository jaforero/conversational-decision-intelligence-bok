---
title: La Aldea de los Datos · La entrega que faltaba
description: Una fábula sobre arquitectura de datos, definiciones compartidas y una decisión que tiene hora de cierre.
status: candidate
version: 0.9.0
artifact_type: learning-module
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Decision Architectures, Semantic Layers, Decision Governance]
source_ids: [SRC-JF-004, SRC-PULSE-DNA-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# La Aldea de los Datos · La entrega que faltaba

*Continuación didáctica de [La Aldea de los Datos, fábula original de Javier Forero](https://javierforero.co/2025/04/02/arquitectura-de-datos-moderna-fabula/). Los personajes, los lugares y la metáfora vienen del relato original. El incidente y las cifras de este capítulo son ficticios.*

## Ochenta en un libro, setenta y seis en el otro { #the-decision }

La segunda vez que Adriana llegó a la aldea, don Martín la esperaba en la plaza con dos hojas y un reloj.

—A las nueve, las escuelas necesitan ochenta cajas para empezar la jornada —le dijo—. El almacén dice que ya entregó ochenta. Las escuelas dicen que recibieron setenta y seis. Tenemos cuatro de reserva. ¿Las enviamos?

Adriana leyó los encabezados. En ambas hojas decía «Entregadas». Estuvo a punto de pedir que corrigieran una de las cifras.

—Antes de decidir —dijo—, ¿qué tuvo que pasar para que cada persona hiciera una marca en su hoja?

## El viaje de una caja

En el **Lago Misterioso**, Adriana encontró los registros tal como habían llegado. El almacén guardaba la hora de salida de cada caja. Cada escuela firmaba el recibo al tenerla en su puerta. Los sellos decían cosas distintas y la aldea había conservado ambos. El cuidador del Lago le indicó qué podía consultar para el reparto y quién podía abrir los recibos originales.

En la **Gran Biblioteca**, la bibliotecaria buscó una de las cajas por su número. Tenía salida registrada y carecía de recibo. Otra caja aparecía dos veces en el archivo de la escuela. La bibliotecaria le mostró cómo las dos copias correspondían a la misma recepción. Así reconstruyeron el recuento y dejaron visible el camino hasta cada registro de origen.

En la **Tienda Especializada** ya tenían la lista de cajas por escuela. Para el reparto importaba saber dónde faltaban y cuánto tardaría en llegar una reserva. Las cuatro pendientes iban a la misma escuela, a diez minutos del depósito. Con esa información, Adriana podía dejar preparadas las cuatro reservas y esperar hasta las ocho y cuarenta y cinco. Enviar antes podía duplicar el reparto. Esperar más dejaba poco margen para llegar a tiempo.

La encargada del almacén y la directora de la escuela se encontraron en el **Vecindario Colaborativo**. Cada una asumió el cuidado de su registro y acordaron compartir el identificador de cada caja. La directora sería responsable de confirmar la recepción. Ambas aprobaron el significado de *recibida a tiempo*: una caja esperada y única, con recibo confirmado en la escuela de destino a más tardar a las nueve.

El **Telar Mágico** ayudó a seguir el hilo desde la Tienda hasta los registros de origen. El tablero pasó a mostrar «Despachadas» y «Recibidas confirmadas» por separado, con su hora de corte. Cuando Adriana preguntó «¿Cuántas entregamos?», el asistente le pidió elegir entre salidas del almacén y recepciones en las escuelas. Al elegir recepciones, pudo ver de dónde salía el recuento y qué cajas seguían pendientes.

## La caja que salió de reserva { #action-and-learning }

A las ocho y cuarenta y cinco llegaron tres recibos. El repartidor confirmó que la cuarta caja seguía en ruta y llegaría después de las nueve. Adriana, responsable del reparto, autorizó enviar una caja de reserva a esa escuela, vinculada al pedido original y avisó que la caja demorada debía volver al depósito.

La escuela confirmó la recepción de la reserva antes de las nueve. Al cierre, el registro mostró **80 de 80 cajas recibidas a tiempo**, una de reserva. Adriana anotó el costo del viaje adicional y dejó por separado el regreso de la caja original al depósito. En la siguiente jornada revisaría si la ventana de quince minutos seguía dando margen para activar la reserva con el tiempo real de traslado. Un reparto bastaba para revisar la regla con el equipo. Para adoptarla en otras rutas, necesitarían observar más jornadas y sus tiempos.

Don Martín miró de nuevo las dos hojas.

—¿Qué cambió en la aldea?

—Ahora puedo seguir una caja desde que sale hasta que alguien la recibe —dijo Adriana—. Y sé a quién llamar cuando el camino se interrumpe.

## Del cuento al diseño { #architecture-map }

| Lugar | Papel en este caso | Pregunta para tu equipo |
|---|---|---|
| **Lago · Data Lake** | Conserva los registros originales con procedencia y acceso controlado. | ¿Podemos recuperar qué llegó de cada fuente y cuándo? |
| **Biblioteca · Data Warehouse** | Integra registros, distingue eventos y documenta cómo trató el duplicado. | ¿Podemos reconstruir el recuento desde sus insumos? |
| **Tienda · Data Mart** | Prepara una vista por escuela para el equipo de reparto. | ¿Qué detalle necesita el responsable para actuar a tiempo? |
| **Vecindario · Data Mesh** | Ilustra la responsabilidad de cada dominio sobre sus datos y los acuerdos compartidos. | ¿Quién responde cuando cambia la definición o falla el registro? |
| **Telar · Data Fabric** | Ilustra cómo metadatos e integración permiten rastrear la evidencia entre sistemas. | ¿Podemos seguir el hilo desde la cifra hasta su fuente? |

La capa semántica aplica la definición acordada de «recibida a tiempo» para que el tablero y el asistente calculen el mismo recuento. Estos lugares representan responsabilidades y enfoques de diseño. Una misma plataforma puede cubrir varias responsabilidades. Elige lo que necesitas según la decisión, el riesgo y el costo de operar cada pieza.

## Pruébalo con tus datos { #try-it }

Elige dos reportes que usen el mismo nombre para una cifra. Anota qué evento cuenta cada uno, la unidad, la hora de corte, la fuente y quién responde por la definición. Reconstruye un registro desde su origen. Después escribe qué acción cambia si usas una definición u otra, quién la autoriza y con qué resultado revisarías la regla.

En el [caso resuelto de tasas de cambio](../practice-lab/fx-worked-case.md), el cambio de lectura aparece al comparar por **fecha de vigencia** o por **día de mercado**. Usa el [contrato de evidencia](02-evidence-context.md) y la [especificación de PULSE](../03-pulse/specification.md) para conectar la definición y la procedencia con la decisión y su revisión.

*Nota editorial. Capítulo pedagógico candidato. La redacción y la traducción recibieron apoyo de IA.*
