---
id: ADR-010
title: Fuente y distribución de IgraSans
status: accepted
date: 2026-07-19
decider: Javier Forero
domains:
  - Foundations
  - Decision Governance
  - Enterprise Implementation
---

# ADR-010: Fuente y distribución de IgraSans

## Contexto

IgraSans es la tipografía primaria del sistema Javier Forero. La guía facilita una URL WOFF2 autorizada para consumo web, pero el corpus auditado no contiene una licencia que pruebe el derecho de copiar el binario dentro de un repositorio público o redistribuirlo bajo la futura licencia del CDI-BoK.

## Decisión

1. La familia oficial permanece `'IgraSans', Aptos, Helvetica, Arial, sans-serif`.
2. En Sprint 0 solo se registra la referencia externa `https://javierforero.com/fonts/IgraSans.woff2`.
3. El binario **no se incorpora** al repositorio hasta registrar proveedor, licencia, alcance territorial, derecho de uso web y derecho de redistribución.
4. Si la licencia permite uso web pero no redistribución, el portal utilizará la URL autorizada y fallbacks.
5. Si la licencia permite redistribución, un cambio posterior deberá añadir archivo, licencia, checksum y procedencia al manifiesto.
6. Si la fuente externa falla o no puede cargarse, el contenido debe conservar legibilidad y geometría funcional con los fallbacks oficiales.

## Consecuencias

El diseño puede presentar variaciones tipográficas durante fallos de red, pero se evita una infracción potencial y una dependencia no auditada. La verificación de licencia es un gate de release para cualquier autoalojamiento, no un detalle operativo.

## Evidencia requerida para cambiar la decisión

- texto de licencia o contrato aplicable;
- titular o proveedor;
- derechos de webfont y redistribución;
- restricciones de dominio, tráfico o transformación;
- archivo autorizado y checksum reproducible.

## Alternativas descartadas

- **Copiar el WOFF2 porque la URL es pública:** acceso público no equivale a licencia de redistribución.
- **Sustituir IgraSans por otra tipografía no aprobada:** rompe el contrato de marca.
- **Bloquear el portal si no carga la fuente:** perjudica accesibilidad y resiliencia sin aportar control legal.

