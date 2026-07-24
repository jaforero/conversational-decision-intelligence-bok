---
id: ADR-028
title: Evidence Backbone y estado del arte de Decision Intelligence
status: accepted
date: 2026-07-24
decision_owner: Javier Forero
scope: Sprint 7 evidence governance and research candidate
---

# ADR-028: Evidence Backbone y estado del arte de Decision Intelligence

## Contexto

El portal estable `v0.8.2` contiene definiciones institucionales, fuentes
constitucionales de PULSE, literatura primaria, síntesis asistidas por IA,
material pedagógico y señales de industria. Esas piezas tienen autoridades,
métodos y usos legítimos diferentes. Una lista de referencias no evita que una
síntesis, un pronóstico o una metáfora termine soportando un claim más fuerte de
lo que permite su evidencia.

Sprint 7 incorpora doce fuentes de proyecto adicionales. Dos copias están
incompletas; dos son mapas de investigación asistida; dos informes de analista
tienen restricciones de redistribución; y varios documentos expresan el punto
de vista o diseños candidatos del autor, no validación empírica.

## Decisión

Crear `v0.9.0-rc.1` como candidato de **Evidence Backbone & Decision
Intelligence State of the Art** bajo estas reglas:

1. Cada fuente incorporada recibe identidad, hash del snapshot recibido,
   procedencia, completitud, derechos, uso permitido, uso prohibido y estado de
   verificación.
2. La fuerza de una fuente se representa con un perfil multidimensional:
   autoridad, independencia, método, directitud, actualidad, aplicabilidad,
   conflictos de interés y verificación. No se calcula una puntuación agregada.
3. Una copia incompleta no puede sustentar claims. Puede conservarse como
   registro de procedencia hasta ser reemplazada por un snapshot completo.
4. Una síntesis asistida por IA puede descubrir referencias y tensiones, pero no
   puede ser soporte directo ni soporte único de un fundamento establecido.
5. Un pronóstico de analista se publica como señal futura con horizonte,
   incertidumbre y condición de revisión; no como hecho, causalidad, readiness
   ni compromiso de producto.
6. Un documento del autor puede gobernar identidad, POV o diseño del proyecto
   dentro de su autoridad declarada; no demuestra eficacia independiente.
7. Los claims materiales del sprint declaran clase, fuentes, alcance, límites,
   contraevidencia o tensión y estado de revisión.
8. Los estándares y marcos cambiantes declaran versión y fecha `as_of`. Una
   beta no se presenta como especificación formal para conformidad.
9. Los PDF con derechos reservados se registran por metadatos y hash. Sus
   binarios y extractos sustanciales no se redistribuyen en el repositorio.
10. Español e inglés comparten los mismos `claim_ids` y `source_ids`; traducir
    no crea evidencia ni autoridad nuevas.

## Tesis de publicación

El CDI-BoK publica como evaluación provisional que Decision Intelligence es un
campo de práctica integrador y emergente, construido sobre disciplinas y
prácticas maduras, pero sin suficiente evidencia para declararlo una disciplina
científica consolidada con fronteras y corpus propios universalmente aceptados.

PULSE se presenta como una síntesis particular alrededor de decisión, acción,
resultado y aprendizaje. Sus metáforas biológicas y su arquitectura integrada
son hipótesis o lentes de diseño hasta que evidencia independiente permita una
afirmación más fuerte.

## Consecuencias

- Research distingue fundamentos establecidos, prácticas maduras en evolución,
  campos emergentes, síntesis PULSE, hipótesis y señales futuras.
- Los lectores pueden inspeccionar qué respalda cada afirmación y qué la haría
  cambiar.
- Aumenta el costo editorial: incorporar una fuente exige clasificarla y
  verificar compatibilidad con el claim.
- `v0.9.0-rc.1` no promueve el núcleo `v0.4.0`, no valida científicamente CDI o
  PULSE y no crea un tag estable.

## Contraargumento

Una clasificación estricta puede dar apariencia de rigor sin una revisión
sistemática completa, y la conclusión sobre madurez del campo puede depender
del alcance de búsqueda actual. El registro, por sí solo, tampoco mide calidad
de decisión ni impacto organizacional.

La objeción permanece abierta. La evaluación se publica como candidata,
fechada y falsable; cada vacío se transforma en una pregunta de investigación
y no en una conclusión definitiva.

## Alternativa potencialmente superior

Encargar una revisión sistemática preregistrada y una revisión externa
multidisciplinar antes de publicar cualquier síntesis. Produciría mayor
confianza académica, pero exige recursos y acceso bibliográfico que no forman
parte de este sprint. El backbone actual prepara esa revisión sin simular que
ya ocurrió.
