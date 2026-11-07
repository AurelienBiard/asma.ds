# Composant Search-results (2026-11-07)

Page Figma : `↳ Search-results`. Composant unique. **Promu depuis ASMA OS** (cadre `searchResults` de la recherche globale desktop, `Ctrl/Cmd + K`) le 2026-11-07.

Panneau déroulant de **résultats groupés**, ancré à un champ `Search` : aperçu des meilleurs résultats par famille, puis un lien « Voir tous les résultats ». Proche d'un `Combobox` et de `Command`, mais sans saisie propre : c'est la liste attachée au champ `Search`.

## Search-results, Command, Select

| Composant | Rôle |
|---|---|
| `Command` | Palette modale (`Ctrl/Cmd + K`) de commandes et de navigation. |
| `Search-results` | Aperçu des résultats d'un champ `Search`, ancré sous lui, secondaire. |
| `Select` | Choix d'une valeur dans un formulaire (aucun rapport). |

En mobile, ne pas utiliser ce panneau : écran de recherche dédié (récentes, puis résultats).

## Anatomie

- **Groupes** : `List-group-header` (famille + nombre de résultats) suivi de ses lignes `Card-item` (`Projet`, `Note`, `Tâche`, `Contact`…), séparées par `Border/subtle`, sans séparateur sur la dernière ligne d'un groupe. Cinq lignes maximum par groupe ; une famille sans résultat n'apparaît pas.
- **Pied** (`searchFooter`) : `Footer-label` (lien « Voir tous les résultats pour « … » », `Text/link`) et `Footer-hint` (raccourci, `Text/tertiary`), masquables via `Show-footer`. Fond `Background/subtle`.

Les groupes sont **assemblés à la main** : le nombre de familles est arbitraire (même logique que `Table`). L'exemple fourni montre Projets, Notes et Tâches.

## Propriétés

`Show-footer` (Boolean, `true`), `Footer-label` (Text), `Footer-hint` (Text).

## Tokens

Largeur 480 px · fond `Background/elevated` · bordure `Border/subtle` (1 px) · ombre `Elevation/2` (Effect Style) · pied `Background/subtle`. Aucun token créé.

## États à prévoir

Récentes (champ vide), chargement (`Skeleton`), aucun résultat (`Empty-state` `Compact`).

## Accessibilité

- Pattern combobox : le champ `Search` a `role="combobox"` avec `aria-expanded` et `aria-controls` vers la liste (`role="listbox"`) ; chaque ligne `role="option"`, chaque groupe `role="group"` avec `aria-labelledby`.
- Flèches haut/bas pour naviguer, Entrée pour ouvrir, Échap pour fermer et rendre le focus au champ.
- Nombre de résultats annoncé dans une région `aria-live="polite"`.
