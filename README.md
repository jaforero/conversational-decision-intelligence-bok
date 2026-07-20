# Conversational Decision Intelligence Body of Knowledge

Repositorio fundacional y versionado del **CDI-BoK**, el sistema de conocimiento de Conversational Decision Intelligence. Este repositorio gobierna conceptos, claims, fuentes, decisiones editoriales, PULSE y la relación entre conocimiento y práctica.

## Estado

- Release de gobernanza: `v0.2.0`
- Fase: Sprint 0 completado y publicado
- Idioma canónico durante `0.x`: español
- Norma fundacional: `governance/00_CDI-BoK_Architecture_and_Editorial_Governance.md`
- Portal previsto: `https://decision.javierforero.co`
- Practice Lab externo: `https://dashboards.javierforero.co`
- Repositorio oficial: `https://github.com/jaforero/conversational-decision-intelligence-bok`

La etiqueta `v0.2.0` ratifica la arquitectura y la gobernanza; **no** afirma que CDI sea todavía un estándar internacional reconocido ni que PULSE cuente con validación científica generalizable.

## Fuentes de autoridad

1. CDI-GOV-001 aprobado.
2. Documentos constitucionales vigentes de PULSE.
3. Registros controlados de conceptos, claims, fuentes y activos.
4. ADR aceptados.
5. Guías, casos y evidencia con alcance explícito.

## Estructura Sprint 0

- `governance/`: norma fundacional, ADR, registros y contratos editoriales.
- `brand/`: fuente de marca, tokens y manifiesto de activos.
- `sources/constitutional/`: copias controladas de las fuentes constitucionales de PULSE.
- `scripts/`: validadores de integridad del repositorio.

## Uso local

```bash
python3 scripts/validate_sprint0.py
```

## Licenciamiento

No se concede licencia de reutilización en esta release. ADR-003 preserva todos los derechos mientras se realiza una revisión legal independiente para contenido, código, marca, tipografía y activos de terceros.
