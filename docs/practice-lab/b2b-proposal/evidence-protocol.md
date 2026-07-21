---
title: Protocolo de evidencia B2B
description: Baseline reproducible, calidad de evidencia, contrafactual y reglas de atribución del caso Propuesta.
status: candidate
version: 0.5.0-rc.1
artifact_type: evidence-protocol
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains:
  - Decision Metrics
  - Research
  - Decision Quality
source_ids:
  - SRC-PRACTICE-B2B-001
  - SRC-PRACTICE-DASH-B2B-001
claim_ids:
  - CLAIM-PRACTICE-B2B-001
  - CLAIM-PRACTICE-B2B-002
  - CLAIM-PRACTICE-B2B-003
last_reviewed: 2026-07-21
---

# Protocolo de evidencia B2B

## Veredicto de readiness

| Dimensión | Estado | Evidencia |
|---|---|---|
| Decisión y alternativas | Lista | Contrato y cuatro opciones. |
| Baseline del demo | Reproducible | CSV agregados y validador del Sprint. |
| Fitness for purpose organizacional | **No demostrado** | Los datos públicos son simulados. |
| Owner y decision rights | **Pendientes** | Solo se identificaron roles. |
| Expectativa previa | **Pendiente** | El registro conserva campos nulos. |
| Contrafactual | Diseñado, no asignado | Preferencia por hold-out comparable + diferencia-en-diferencias. |
| Outcome | **No observado** | No hay acción ejecutada. |
| Atribución causal | **Bloqueada** | Requiere comparador y 2–3 ciclos. |

## Baseline reproducido

Los cálculos se derivaron de las matrices embebidas en el [dashboard comercial](https://dashboards.javierforero.co/claude/desempeno-comercial/) observado el 21 de julio de 2026. El dashboard declara datos simulados; los CSV de este repositorio son agregados para auditoría, no datos CRM reales.

### Cumplimiento

- Junio de 2026: `381.061,4 / 475.657 = 80,11%`.
- Es el menor cumplimiento ponderado entre enero de 2025 y junio de 2026.
- Los 8 vendedores del demo quedaron bajo 90% en junio.

### Propuesta

- Baseline provisional ene–mar 2026: `(46,5 + 50,4 + 47,2) / 3 = 48,03%`.
- Periodo deteriorado abr–jun 2026: `(37,4 + 34,5 + 37,7) / 3 = 36,53%`.
- Cambio: `−11,50 pp`.

La ventana ene–mar se eligió porque precede el descenso sostenido de abril. Debe someterse a sensibilidad contra 2025 completo y estacionalidad antes de aplicarla a una operación real.

### Canales

| Canal | Ganadas / cerradas | Win rate | Wilson 95% |
|---|---:|---:|---:|
| Evento / feria | 5 / 56 | 8,93% | 3,87%–19,26% |
| Referido | 10 / 126 | 7,94% | 4,37%–13,99% |
| Inbound digital | 4 / 111 | 3,60% | 1,41%–8,90% |

La dirección del ranking favorece evento y referido, pero los intervalos se superponen ampliamente. **No se sostiene “significativamente superiores” con esta evidencia.** La opción B queda bloqueada hasta contar con más observaciones, un modelo ajustado por mix o una prueba específica.

## Diseño preferido: hold-out + diferencia-en-diferencias

1. Definir unidades elegibles: vendedores, regiones o carteras con suficiente actividad en Propuesta.
2. Emparejar unidades por conversión previa, volumen, ticket, mix de canal y seniority.
3. Asignar la intervención a una parte y conservar un comparador operativo.
4. Preregistrar acción, expectativa y horizonte.
5. Calcular:

\[
\widehat{\tau}_{DiD} = (Y_{I,post}-Y_{I,pre})-(Y_{C,post}-Y_{C,pre})
\]

6. Revisar tendencias paralelas, cambios de composición y deals atípicos.
7. Reportar estimación, intervalo y sensibilidad; no solo dirección.

!!! warning "Si no existe hold-out"
    Usar una serie histórica o forecast como contrafactual es una alternativa más débil. Debe etiquetarse como `observed-noncausal` salvo que el diseño y los supuestos permitan una atribución más fuerte.

## Métricas

| Tipo | Métrica | Función |
|---|---|---|
| Primaria | Conversión Propuesta→Negociación | Mide la palanca intervenida. |
| Secundaria | Cumplimiento de ventas | Conecta la intervención con prioridad material. |
| Guardrail | Nuevos prospectos de calidad | Detecta si el coaching desplaza prospección. |
| Guardrail | Tiempo de ciclo y margen / descuento | Evita “mejorar” conversión sacrificando precio o velocidad. |
| Proceso | Rúbrica 0–10 | Separa calidad de decisión de suerte. |

## Reglas de aprendizaje

- Un ciclo sirve para inspeccionar implementación, no para declarar eficacia.
- Dos ciclos son el mínimo del caso; tres son preferibles.
- Un buen resultado con proceso débil no se institucionaliza como lección.
- Un mal resultado con proceso sólido exige revisar hipótesis, no castigar automáticamente la decisión.
- Todo cambio en definición, grupo o expectativa después de actuar queda en el log de auditoría.

## Archivos de evidencia

- [`demo-sales-monthly.csv`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/b2b-proposal/demo-sales-monthly.csv)
- [`demo-funnel-2026.csv`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/b2b-proposal/demo-funnel-2026.csv)
- [`demo-channel-win-rate.csv`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/b2b-proposal/demo-channel-win-rate.csv)
