# Composant List-group-header (2026-11-07)

Page Figma : `↳ List-group-header`. Composant unique. **Promu depuis ASMA OS** (`OS / List-group-header`) le 2026-11-07 : les instances des maquettes OS suivent le composant.

En-tête de groupe dans une liste : un **libellé** et un **compteur**, sur un bandeau pleine largeur. Il sépare les groupes d'une même liste sans ouvrir de nouvelle carte.

## Propriétés et anatomie

- `Label` (Text) — nom du groupe.
- `Count` — instance de `Count` (`Type=Neutral`, `Size=Medium`) : nombre d'éléments du groupe.
- Rangée horizontale, gap `Spacing/component-xs`, padding `Spacing/component-xs` (vertical) et `Spacing/component-md` (horizontal), largeur `FILL`, hauteur 37 px.

## Tokens

| Élément | Token |
|---|---|
| Fond | `Background/sunken` |
| Bordure | `Border/subtle`, bas uniquement (1 px) |
| Libellé | `Text/secondary`, `Misc/Label` |

Aucun token créé.

## Règles d'usage

- À placer avant les éléments qu'il regroupe, au même niveau que les lignes (`Card-item`, lignes de `Table`, `Command-item`).
- Un groupe sans élément n'est pas affiché.
- Pas un titre de section : pour un titre de bloc de page, utiliser `Block-header` (`components/card-collection/`).
- Usages dans ASMA OS : tâches (par échéance), notes, ressources, notifications, résultats de recherche (`Search-results`), corbeille.

## Accessibilité

- Dans une liste : `role="group"` avec `aria-labelledby` pointant le libellé ; si le groupe est une section de page, un titre (`h3`).
- Le compteur est lu avec le libellé (« Notes, 2 »).
- Contraste `Text/secondary` sur `Background/sunken`.
