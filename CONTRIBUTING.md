# Contribuir al CDI-BoK

El CDI-BoK acepta contribuciones como cambios gobernados de conocimiento, no como publicaciones aisladas.

## Antes de proponer contenido

1. Identifique el dominio, concepto y decisión que el cambio fortalece.
2. Revise `governance/content-map.yml` y los registros existentes.
3. Determine si el aporte es definición, evidencia, guía, patrón, caso o propuesta original.
4. Abra una rama temporal y mantenga un solo propósito por pull request.

## Controles mínimos

```bash
python3 scripts/preflight_sprint1.py
```

Todo claim material debe declarar clase, evidencia, alcance y límites. La etiqueta `Original Contribution` requiere comparación documentada con antecedentes; sin ella se utiliza `Original Contribution Proposal`.

## Autoridad

Una contribución pública no se vuelve normativa por haber sido fusionada. El estado y la autoridad se determinan mediante CDI-GOV-001, front matter, registros y aprobación explícita del owner correspondiente.

