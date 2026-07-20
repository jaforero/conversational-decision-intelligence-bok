---
id: ADR-004
title: Estados editoriales y visibilidad pública
status: accepted
date: 2026-07-19
decider: Javier Forero
---

# ADR-004: Estados editoriales y visibilidad pública

## Decisión

Solo activos `candidate`, `approved`, `deprecated` o `superseded` podrán entrar en la navegación pública. Borradores y revisiones pueden existir en ramas o pull requests, pero deben mostrar su estado y no deben desplegarse como contenido oficial.

## Consecuencias

La transparencia del repositorio no se confundirá con autoridad editorial. El pipeline deberá fallar si un activo `draft` aparece en la navegación de producción.

