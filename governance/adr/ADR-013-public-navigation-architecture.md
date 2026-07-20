---
id: ADR-013
title: Arquitectura de navegación pública progresiva
status: accepted
date: 2026-07-20
decider: Javier Forero
domains:
  - Foundations
  - Decision Governance
  - Enterprise Implementation
---

# ADR-013: Arquitectura de navegación pública progresiva

## Decisión

La navegación inicial presenta nueve rutas orientadas al lector: Inicio, Empieza aquí, CDI-BoK, PULSE, Practice Lab, Research, Gobernanza, Versiones y Acerca de.

Los 29 dominios permanecen en el mapa intelectual, pero no se exponen como 29 opciones de primer nivel. Un dominio entra a navegación cuando dispone de un activo publicable, owner, estado, relación con PULSE y lugar inequívoco en `content-map.yml`.

Las páginas mínimas de Sprint 1 explican alcance, autoridad y rutas futuras; no simulan capítulos completos ni presentan placeholders como conocimiento consolidado.

## Consecuencias

- La navegación reduce carga cognitiva sin alterar la taxonomía oficial.
- Los dominios pueden crecer sin reestructurar de inmediato el portal completo.
- Ninguna página pública adquiere autoridad mayor que la declarada en su front matter y registro.

