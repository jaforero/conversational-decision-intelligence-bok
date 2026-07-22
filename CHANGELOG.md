# Changelog

Todos los cambios relevantes del CDI-BoK se documentan en este archivo.

## [Unreleased]

### Corregido

- Localización de la interfaz española para el nombre visible del portal, el módulo de calidad y medición y los tooltips de enlaces permanentes.
- Hero ES/EN reescrito para explicar el valor del CDI-BoK a usuarios de negocio con menos jerga técnica.
- Búsqueda separada por edición: cada selector ES/EN utiliza exclusivamente el índice y las rutas de su idioma.
- Gates estructurales y de navegador para impedir que una búsqueda vuelva a mezclar ambos corpus.

## [0.8.1] - 2026-07-21

### Promovido

- Portal bilingüe ES/EN a línea base editorial y técnica estable, después de ratificar `v0.8.1-rc.1`.
- 46 rutas españolas canónicas y 46 ediciones inglesas equivalentes, con selector contextual, búsqueda localizada, canonical y `hreflang`.
- Interfaz inglesa completa después del hotfix del PR #13, incluidos Learn, Practice Lab, controles de tema, footer y metadata social.
- ADR-026, manifiesto estable, notas ES/EN y autorización del tag `v0.8.1` únicamente después del merge y de los gates finales.

### Linaje verificado

- PR #12 fusionado mediante `655e3b80ad1cbd8b443b6339358996f9fe656083`.
- PR #13 fusionado mediante `5837657f6bfe0627f5bd0c8ada13640dba9a0a4b`.
- Validación post-hotfix `29882684997`, despliegue Pages `29882684960` y portal inglés verificado con HTTP 200.

### Límites preservados

- El español continúa como fuente canónica durante `0.x`; el inglés es traducción gobernada, no doctrina independiente.
- La promoción no eleva la autoridad de aprendizaje, medición o patrones ni cambia el caso B2B `instrumented-not-executed`.
- La estabilidad bilingüe no valida científicamente CDI o PULSE ni demuestra eficacia, adopción o impacto.

## [0.8.1-rc.1] - 2026-07-21

### Añadido

- Portal bilingüe estático con español canónico en las rutas existentes e inglés completo bajo `/en/`.
- Selector contextual de idioma, navegación, búsqueda, interfaz y metadatos sociales localizados.
- Canonical, `hreflang` para español e inglés y `x-default` por página equivalente.
- Registro controlado de 46 pares con versión, estado, owner, fecha y hash SHA-256 de la fuente española.
- ADR-025 y gates contra páginas ausentes, traducciones obsoletas, fallbacks y deriva de versión.

### Límites preservados

- `v0.8.0` permanece como release estable e inmutable.
- El inglés es una traducción gobernada, no doctrina co-canónica.
- La traducción no eleva autoridad o evidencia ni modifica el estado del caso B2B.

### Cierre

- Candidato ratificado, fusionado, desplegado y promovido a `v0.8.1`.
- Implementación bilingüe: PR #12, merge `655e3b80ad1cbd8b443b6339358996f9fe656083`.
- Corrección integral de interfaz inglesa: PR #13, merge `5837657f6bfe0627f5bd0c8ada13640dba9a0a4b`.

## [0.8.0] - 2026-07-21

### Promovido

- Portal integrado a una línea base editorial y técnica estable después de ratificar `v0.8.0-rc.1`.
- Arquitectura pública de 45 páginas, navegación, trazabilidad, build estricto, regresión visual y análisis Axe automatizados.
- ADR-024, manifiesto estable, nota pública y referencia inmutable `v0.8.0` creada únicamente después del merge y de los gates finales.
- Workflow estable generalizado para resolver versión, título, manifiesto y notas sin valores codificados para `v0.4.0`.

### Linaje verificado

- PR #10 fusionado mediante `bbc5c0583b28bbc3d4d2b6a2aedf28f8df336347`.
- Validación post-merge `29871891960` y despliegue `29871892015` aprobados.
- Portal público y área de patrones verificados con HTTP 200 antes de la promoción.

### Autoridad y evidencia preservadas

- El núcleo `v0.4.0` conserva su autoridad aprobada; no se reversionan ni amplían sus definiciones.
- Aprendizaje, medición, patrones y anti-patrones permanecen candidatos aunque estén incluidos en el bundle estable.
- El caso B2B permanece `instrumented-not-executed`, sin owner real confirmado, acción, outcome o impacto atribuible.
- La estabilidad del portal no valida científicamente CDI o PULSE, no prueba eficacia y no establece conformidad completa con WCAG 2.2 AA.

## [0.8.0-rc.1] - 2026-07-21

### Añadido

- Área pública de Conversational Decision Patterns & Anti-patterns.
- Lenguaje candidato con anatomía, movimientos, estados de madurez, stop conditions y selección proporcional.
- Cinco patrones para enmarcar, fundamentar, deliberar, comprometer y aprender.
- Seis anti-patrones para conversación decorativa, drift semántico, certeza artificial, autoridad indebida, adopción como impacto y expectativa reconstruida.
- Registro machine-readable y plantilla YAML con null states, derechos, evidencia, riesgos y medición.
- Demostración detenida sobre el caso B2B simulado, sin inventar owner, acción, expectativa ni outcome.
- ADR-023, claims calibrados y validador específico de Sprint 6.

### Decisión crítica

- El catálogo no se presenta como secuencia universal, librería de prompts o sistema validado. Una regla, reporte, checklist o workflow puede ser una alternativa superior a la conversación.

### Calibración

- Las once entradas son una taxonomía institucional candidata, no consenso académico ni evidencia de eficacia.
- La selección parte del bloqueo decisional y usa el patrón mínimo suficiente según stakes, incertidumbre, reversibilidad y daño potencial.
- El núcleo `v0.4.0`, la autoridad constitucional de PULSE y el estado `instrumented-not-executed` del caso B2B no cambian.

## [0.7.0-rc.1] - 2026-07-21

### Añadido

- Área pública de Decision Quality & Measurement.
- Perfil ex ante de siete dimensiones con evidencia y bloqueadores.
- Decision Measurement System de seis lentes para prioridad, calidad, ejecución, tiempo, riesgo y aprendizaje.
- Contratos y fórmulas con límites de aplicación para latencia, fidelidad, cierre de aprendizaje y Brier score.
- Criterios de medición humano–IA y anti-métricas para adopción, override, velocidad, ROI y scores sintéticos.
- Decision Measurement Record versionado con snapshot previo y outcome review posterior.
- ADR-021, fuentes académicas y profesionales, claims calibrados y validador específico de Sprint 5.

### Decisión crítica

- No se publica un Decision Health Score universal: la evidencia disponible no permite pesos, benchmarks ni comparabilidad transversal defendibles.

### Calibración

- El sistema es una síntesis candidata y no un instrumento validado.
- Una plantilla completa demuestra trazabilidad, no eficacia ni atribución causal.
- El núcleo `v0.4.0` y el estado `instrumented-not-executed` del caso B2B no cambian.

### Cierre y gobierno

- Ratificado por Javier Forero el 21 de julio de 2026; fusionado mediante PR #8 y commit `e84f53a6caaca696a8143a2aab2e7a24e9bdb4e8`.
- Validación post-merge y despliegue de Pages completados mediante runs `29863235105` y `29863234835`.
- ADR-022 sustituye la regla ambigua de ADR-005: los tags son obligatorios para releases estables y opcionales, con autorización explícita, para candidatos congelados.
- No se crean tags retrospectivos para `v0.5.0-rc.1`, `v0.6.0-rc.1` o `v0.7.0-rc.1`; su procedencia se conserva mediante manifiestos, PR y SHA.
- `v0.7.0-rc.1` permanece candidato; no se promueve `v0.7.0` ni se altera la autoridad estable de `v0.4.0`.

## [0.6.0-rc.1] - 2026-07-21

### Añadido

- Ruta didáctica de cinco módulos: decisión, evidencia y contexto, Decision Experience, control humano–IA y aprendizaje.
- Plantilla reutilizable de Decision Brief para integrar PDAMR, evidencia, derechos, acción, métricas y revisión.
- Navegación por problema del lector y salidas explícitas para cada módulo.
- ADR-020 y manifiesto de Sprint 4 para gobernar la arquitectura de aprendizaje.

### Mejorado

- Portada reescrita desde la transformación del lector: qué podrá formular, evaluar, diseñar, gobernar y aprender.
- Hero de dos columnas con una ruta visible desde prioridad hasta aprendizaje.
- Accesibilidad, responsive y componentes editoriales para rutas y resultados.

### Calibración

- La ruta enseña y operacionaliza el método; no constituye evidencia de impacto organizacional.
- El caso B2B permanece `instrumented-not-executed` en `v0.5.0-rc.1`.
- El núcleo fundacional estable `v0.4.0` no cambia de autoridad.

### Cierre

- Ratificado por Javier Forero el 21 de julio de 2026.
- Fusionado mediante PR #7 y commit `958e2ee0c5326b2329e3f0a64259d149362571df` después de gates canónicos exitosos.
- Validación post-merge y despliegue de Pages completados mediante runs `29858379946` y `29858379825`.
- La ratificación del candidato no equivale a promoción estable ni a verificación de impacto.

## [0.5.0-rc.1] - 2026-07-21

### Añadido

- Catálogo verificado de los portafolios Claude y ChatGPT Work.
- Primer caso instrumentado: intervención sobre Propuesta en Comercial B2B.
- Contrato PDAMR, alternativas, decision rights, prerregistro y rúbrica de calidad de proceso.
- Baseline reproducible de cumplimiento, funnel y win rate por canal sobre datos simulados.
- Protocolo de hold-out + diferencia-en-diferencias, registro YAML y log mensual CSV.
- ADR-018 para el ciclo de evidencia y ADR-019 para selección y frontera del piloto.
- Validador específico contra outcomes o causalidad inventados.

### Hallazgo crítico

- Junio de 2026 es el peor mes del demo: 80,11% de cumplimiento y 8/8 vendedores bajo 90%.
- La conversión de Propuesta cae 11,50 pp entre ene–mar y abr–jun de 2026.
- Evento y referido superan a inbound digital en la tasa observada, pero los intervalos se superponen; no se conserva lenguaje de superioridad significativa ni se recomienda reasignar presupuesto con esta evidencia.

### Frontera

- El caso permanece `instrumented-not-executed`: sin owner confirmado, expectativa bloqueada, acción, outcome o efecto atribuible.
- Los datos son de demostración simulados. Sirven para probar instrumentación, no impacto organizacional.
- El núcleo fundacional `v0.4.0` no cambia de autoridad.

## [0.4.0] - 2026-07-21

### Ratificado

- Constitución y fronteras de CDI como lenguaje institucional aprobado del proyecto.
- Glosario y mapa de ocho áreas y 29 dominios como activos controlados.
- Especificación nuclear de PULSE como proyección aprobada y derivada de sus fuentes constitucionales.

### Añadido

- ADR-017 para registrar la decisión de ratificación, autoridad diferenciada y límites de la promoción.
- Manifiesto reproducible y nota pública de la release estable.
- Gate automatizado que crea el tag y GitHub Release solo después de preflight, build, regresión visual y Axe sobre `main`.

### Calibración

- Una definición oficial del proyecto no equivale a consenso académico externo.
- La estabilidad de la release no demuestra eficacia generalizable ni estandarización externa.
- Research, Practice Lab y los activos no ratificados conservan su estado candidato.
- La especificación pública de PULSE no sustituye sus fuentes constitucionales.

## [0.4.0-rc.1] - 2026-07-21

### Añadido

- Constitución candidata del CDI-BoK con autoridad, principios, límites éticos y control de cambios.
- Definición candidata y fronteras de CDI frente a BI, Conversational AI, Conversational Analytics, DSS, DI y PULSE.
- Declaración explícita de prior art: el proyecto no reclama haber acuñado “Conversational Decision Intelligence”.
- Glosario controlado inicial con 27 términos, owner conceptual y límites de uso.
- Mapa completo de ocho áreas y 29 dominios con preguntas rectoras y madurez inicial.
- Especificación nuclear de PULSE derivada de DNA, Documentation Map e Identity canónicos.
- ADR-014 a ADR-016, manifiesto Sprint 2 y registros ampliados de conceptos, claims y fuentes.

### Calibración

- CDI se posiciona como dominio de práctica interdisciplinar propuesto, no como disciplina científica consolidada.
- La evidencia sobre colaboración humano–IA se presenta como heterogénea y dependiente del contexto.
- La especificación pública de PULSE no adquiere autoridad independiente ni redefine sus fuentes.

### Validado en GitHub Actions

- Preflight completo: 96 controles de Sprint 2, 147 controles heredados, sincronización, auditorías y build estricto.
- Dieciséis comparaciones visuales y nueve ejecuciones automatizadas de Axe aprobadas en el runner canónico Ubuntu; nueve duplicados móviles de Axe se omiten deliberadamente.
- Las pruebas automatizadas no constituyen por sí solas una declaración de conformidad WCAG 2.2 AA.

### Cierre

- Ratificado por Javier Forero el 21 de julio de 2026.
- Promovido a la release estable `v0.4.0` mediante ADR-017.

## [0.3.0-rc.1] - 2026-07-20

### Añadido

- Portal MkDocs Material con navegación pública progresiva de nueve rutas.
- Páginas iniciales para orientación, CDI-BoK, PULSE, Practice Lab, Research, gobernanza, versiones y autoría.
- Sincronización ejecutable de design tokens y de la norma editorial publicada.
- Modos claro y oscuro, diseño adaptable y personalización coherente con la marca Javier Forero.
- GitHub Actions separados para validación, regresión visual/accesibilidad y despliegue a Pages.
- Dependencias Python con hashes y dependencias Node bloqueadas.
- Baselines visuales de cuatro rutas representativas en escritorio, móvil, modo claro y modo oscuro.
- Runbook para activar GitHub Pages, `decision.javierforero.co`, DNS y HTTPS.
- ADR-012 y ADR-013 para gobernar publicación y navegación.

### Validado localmente

- Build estricto de MkDocs y auditoría semántica de 14 páginas HTML generadas.
- 127 controles de integridad heredados del Sprint 0.
- 20 pruebas de navegador aprobadas; cuatro duplicados de Axe en móvil se omiten deliberadamente porque el mismo conjunto automatizado se ejecuta en escritorio.

### Validado en GitHub Actions

- Preflight editorial, integridad, sincronización de marca, build estricto y auditoría semántica aprobados.
- Dieciséis comparaciones visuales y cuatro ejecuciones de reglas Axe aprobadas sobre el runner canónico Ubuntu; cuatro duplicados móviles se omiten deliberadamente.

### Pendiente antes de promover la release

- Merge explícito a `main`.
- Activación de Pages, configuración del dominio, propagación DNS y HTTPS.
- Auditoría humana de accesibilidad de la release desplegada; no se declara todavía conformidad WCAG 2.2 AA.

## [0.2.0] - 2026-07-19

### Ratificado

- CDI-GOV-001 como norma fundacional, aprobada y normativa.
- Ocho áreas de conocimiento y 29 dominios.
- MkDocs y GitHub Pages como arquitectura objetivo del portal.
- Javier Forero como masterbrand respaldante.
- `dashboards.javierforero.co` como Practice Lab externo.

### Añadido

- Registros iniciales de conceptos, claims, fuentes, activos y demos.
- Documentos constitucionales vigentes de PULSE.
- `brand-source.yml`, design tokens en JSON/CSS y manifiesto de activos.
- ADR-001 a ADR-011, incluidos los cierres de marca, IgraSans y accesibilidad.
- Validador reproducible del Sprint 0.
- Publicación del repositorio oficial en GitHub y establecimiento de `main` como rama canónica.

### Limitaciones explícitas

- No se declara conformidad WCAG 2.2 AA hasta auditar una release completa del portal.
- IgraSans no se redistribuye dentro del repositorio hasta verificar derechos y licencia.
- No se otorga licencia de reutilización en `v0.2.0`.
