---
title: Caso resuelto · Tasas de cambio
description: Reconstruye dos índices, verifica un arrastre y decide si una señal cambiaria activa la revisión de un presupuesto simulado.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Conversational Analytics, Semantic Layers, Decision Governance]
source_ids: [SRC-PULSE-DNA-001, SRC-PRACTICE-FX-001, SRC-PRACTICE-FX-SNAPSHOT-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# Caso resuelto · Tasas de cambio

El 6 de noviembre de 2026, el índice de USD–COP marca **101,42** si usas la TRM por vigencia. Si comparas los mismos días de mercado que usa el FIX de México, marca **100,07**. La diferencia decide si el equipo abre una revisión bajo la regla de este ejercicio.

## Decisión y criterio { #decision }

Planeación de una empresa importadora simulada revisa presupuestos locales para pagos en USD en Colombia y México. La prioridad es identificar qué presupuesto merece una revisión extraordinaria. Antes de calcular, el responsable fija el criterio didáctico **revisar si la moneda local por USD sube al menos 1 % entre el 3 y el 6 de noviembre de 2026, por día de mercado**. Las alternativas son revisar primero Colombia, revisar primero México o seguir el calendario ordinario.

El umbral pertenece al escenario simulado. Para una decisión de pagos, el responsable contrasta además la moneda de facturación, el importe, la fecha, la tasa aplicable y las coberturas vigentes.

## Evidencia y cálculo { #evidence }

El corte del [repositorio de tasas](https://github.com/jaforero/fx-bancos-centrales/tree/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series) está fijado al commit `dd7a205`. El periodo usa los días 3 y 6 para el índice, y el sábado 7 para comprobar el arrastre. La TRM por vigencia se contrastó con los [datos de la Superintendencia Financiera de Colombia](https://www.datos.gov.co/Econom-a-y-Finanzas/Tasa-de-Cambio-Representativa-del-Mercado-TRM/32sa-8pi3). El [Banco de México](https://www.banxico.org.mx/tipcamb/tipCamMIAction.do?idioma=sp) distingue el FIX determinado del publicado en el DOF y de la tasa para pagos.

El índice es `100 × tasa final ÷ tasa inicial`. Las unidades son COP o MXN por USD. Un aumento indica que hacen falta más unidades de moneda local por dólar. Se aplica el umbral al cambio sin redondear.

| Serie y base temporal | 3 nov. | 6 nov. | Índice final | Cambio |
| --- | ---: | ---: | ---: | ---: |
| USD–COP · [TRM por vigencia](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/usd_cop_trm.json) | 3.182,99 | 3.228,26 | 101,42 | +1,42 % |
| USD–COP · [TRM alineada al día de mercado](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/usd_cop_trm_mkt.json) | 3.235,59 | 3.237,83 | 100,07 | +0,07 % |
| USD–MXN · [FIX determinado](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/usd_mxn_fix.json) | 18,7592 | 18,6297 | 99,31 | −0,69 % |

El 7 de noviembre la serie FIX muestra **18,6297 MXN por USD** como arrastre del 6. La TRM de **3.237,83 COP por USD** tiene vigencia del 7 al 9 y corresponde al mercado del 6. Para la [cruzada MXN–COP del 6](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/mxn_cop_cross.json), divide los insumos del mismo día de mercado. `3.237,83 ÷ 18,6297 = 173,7994 COP por MXN` a cuatro decimales.

## Pruebas observadas { #observed-checks }

Probé el [tablero](https://dashboards.javierforero.co/tasas-cambio/) en Chromium con esta [versión del código](https://github.com/jaforero/dashboards/tree/9ba5a468627fb58136fa83febb5122c182490fd7/tasas-cambio) y los datos fijados a `dd7a205`. En **Comparación base 100**, elegí el 3 de noviembre y leí la fila del día 6. Revisé también el histórico de USD–MXN y el conversor. La columna asistida registra respuestas de una corrida editorial con ChatGPT sobre los JSON fijados. La misma revisión preparó y comprobó los casos.

| Pregunta | Resultado esperado | Tablero observado | Respuesta asistida observada |
| --- | --- | --- | --- |
| ¿Cuánto cambió cada moneda entre el 3 y el 6? | Declarar par y base temporal. Distinguir la vista del tablero del cálculo alineado. | La tabla muestra 101,4 para COP por vigencia y 99,3 para MXN por determinación. | Identificó +1,42 % y −0,69 % en la vista del tablero. Al alinear por mercado, recalculó COP en +0,07 %. |
| ¿A cuánto está el dólar? | Pedir moneda de contraparte y fecha antes de responder. | El tablero ofrece un selector de pares y un histórico por fecha. | «¿En qué moneda y para qué fecha necesitas la tasa de referencia del USD?» |
| ¿Hubo un FIX nuevo el sábado 7? | Identificar el arrastre y fechar la observación original. | El histórico etiqueta el día 7 como repetición del último valor oficial y el día 6 como oficial. | Identificó 18,6297 MXN por USD, con determinación del viernes 6 y arrastre el sábado 7. |
| ¿Cuántos COP valía un MXN el 6? | Reconstruir la cruzada y citar los dos insumos del mismo día de mercado. | El conversor muestra 173,80 COP por MXN, con fecha 6 y etiqueta «Calculada». | Calculó 173,7994 COP por MXN con TRM por mercado y FIX determinado el 6. |

La corrida comprueba estos comportamientos en el corte elegido. Para comparar tiempos en una prueba independiente, usa preguntas nuevas y alterna el orden de los canales. Cronometra desde la pregunta hasta una respuesta con cifra o aclaración, unidad, fecha y procedencia cuando correspondan. Para reproducir los valores desde la raíz del CDI-BoK, ejecuta el [script de verificación](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/fx-case/reproduce.py) con `python evidence/fx-case/reproduce.py`.

## Acción y revisión { #review}

**Decisión del caso.** Mantener el calendario ordinario. Ambas series quedan por debajo del umbral cuando se comparan por día de mercado. Si la regla interna estuviera definida por vigencia, la lectura de COP sí activaría una revisión. El dueño del presupuesto debe confirmar qué convención usa antes de aplicar el criterio a un pago real.

Registra el corte y la convención elegida. Repite el cálculo en el siguiente cierre previsto o si cambia materialmente el importe expuesto. La [guía de dashboards](dashboards.md#fx) y el [laboratorio de evaluación de asistentes](conversational-evidence.md#public-data-exercises) permiten reutilizar este protocolo.

*Nota editorial. Caso didáctico con datos públicos y política presupuestaria simulada. La redacción, la traducción y la corrida asistida recibieron apoyo de IA.*
