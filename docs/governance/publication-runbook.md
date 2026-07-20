---
title: Publicación y dominio
description: Runbook reproducible para GitHub Pages, GitHub Actions y el subdominio decision.javierforero.co.
status: candidate
version: 0.3.0-rc.1
artifact_type: operations-runbook
authority_level: guidance
normative: false
owner: Javier Forero
domains:
  - Decision Governance
  - Enterprise Implementation
last_reviewed: 2026-07-20
---

# Publicación y dominio

## Arquitectura

```mermaid
flowchart TD
    A["Pull request"] --> B["Validación y revisión visual"]
    B --> C["Merge a main"]
    C --> D["Build estricto"]
    D --> E["GitHub Pages"]
    E --> F["decision.javierforero.co"]
```

## Activación inicial de Pages

1. En GitHub, abra **Settings → Pages**.
2. En **Build and deployment**, seleccione **GitHub Actions** como fuente.
3. Configure `decision.javierforero.co` como dominio personalizado antes de crear el DNS.
4. Cuando GitHub reconozca el dominio y el certificado esté disponible, active **Enforce HTTPS**.

## DNS requerido

En el proveedor DNS de `javierforero.co`, cree:

| Tipo | Nombre | Destino |
|---|---|---|
| `CNAME` | `decision` | `jaforero.github.io` |

No utilice una URL completa, un registro wildcard ni el nombre del repositorio como destino.

## Verificación

```bash
dig decision.javierforero.co +noall +answer -t CNAME
curl -I https://decision.javierforero.co
```

Los cambios DNS pueden tardar en propagarse. La presencia de `docs/CNAME` conserva el dominio objetivo en el repositorio, pero el workflow personalizado no reemplaza la configuración de Pages.

## Condiciones de publicación

- `main` es la única rama de producción.
- Un pull request valida sin desplegar.
- El build debe pasar `mkdocs build --strict` y las auditorías del repositorio.
- El workflow de deploy utiliza permisos mínimos y el entorno `github-pages`.
- La conformidad WCAG solo puede declararse después de auditar la release desplegada.

