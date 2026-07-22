---
id: ADR-025
title: Arquitectura bilingüe ES/EN del portal
status: accepted
date: 2026-07-21
decider: Javier Forero
---

# ADR-025: Arquitectura bilingüe ES/EN del portal

## Contexto

El sistema de marca establecía una experiencia ES/EN, pero `v0.8.0` era monolingüe: no existían rutas inglesas, selector, búsqueda localizada, metadatos alternativos ni control de paridad. Cambiar solo etiquetas en el navegador habría creado una apariencia bilingüe sin resolver contenido, SEO, enlaces directos ni mantenimiento.

## Decisión

1. El español permanece canónico durante `0.x` conforme a ADR-002.
2. Cada página pública española debe tener una traducción inglesa estática bajo `/en/`.
3. `mkdocs-static-i18n` gobierna selección contextual, interfaz y búsqueda por idioma.
4. Cada par se registra con versión, estado, owner, fecha de revisión y hash SHA-256 de la fuente española.
5. CI bloquea páginas ausentes, versiones divergentes, hashes obsoletos, fallbacks o metadatos incompletos.
6. Las excepciones requieren owner, justificación y fecha de expiración; `v0.8.1-rc.1` no publica excepciones.
7. La traducción no cambia autoridad, evidencia, madurez ni propiedad conceptual.

## Alternativas rechazadas

- **Traducción dinámica en el navegador:** falla en indexación, búsqueda, accesibilidad, enlaces directos y trazabilidad.
- **Inglés parcial:** reduce costo inicial, pero normaliza una edición desigual y debilita el contrato de marca.
- **Rutas simétricas `/es/` y `/en/`:** son coherentes, pero romperían enlaces españoles existentes sin beneficio proporcional.

## Riesgos

- costo editorial aproximadamente duplicado;
- traducciones correctas técnicamente pero semánticamente débiles;
- falsa sensación de co-canonicidad;
- gate basado en hash que exige revisión aun cuando un cambio español no altera significado.

## Mitigaciones

Español canónico, revisión humana, hashes bloqueantes, equivalencia de versión y estructura, pruebas contextuales y posibilidad futura de adoptar un TMS mediante un nuevo ADR.

## Consecuencia

Un cambio en una página española invalida su par hasta que la edición inglesa sea revisada y el hash se actualice en el mismo pull request.
