# Pattern Search

> **Statut** : reclassé le 2026-11-19 depuis le composant `Search-results` (promu depuis ASMA OS le 2026-11-07). Le pattern est « champ de recherche + panneau de résultats groupés » ; `Search-results` est la brique panneau (composant Figma conservé). Page Figma : `↳ Search` (section `💻 PATTERNS`, anciennement `↳ Search-results`). Les points marqués « proposé » sont à valider.

## Purpose

Saisir une requête dans un champ `Search` et obtenir un aperçu des meilleurs résultats groupés par famille, avec un lien vers tous les résultats. Le pattern porte tout le parcours : champ, panneau, navigation clavier, états.

## Use when

- Recherche globale ou de section dont les résultats couvrent plusieurs familles (projets, notes, tâches, contacts).
- Un aperçu suffit, avec un lien « Voir tous les résultats ».

## Do not use when

- Commandes et navigation au clavier (palette modale, `Ctrl/Cmd + K`) → `Command`.
- Choix d'une valeur dans un formulaire → `Select`.
- Filtrer un jeu de données déjà affiché → pattern `Filter bar`.
- Mobile : ne pas utiliser le panneau ; écran de recherche dédié (récentes, puis résultats).

## Components

- `Search` (`components/search-input/`) — le champ d'ancrage.
- `Search-results` (brique, composant Figma) — le panneau. Voir « Brique : Search-results ».
- `List-group-header` (`components/list-group-header/`) — un par famille : libellé + nombre de résultats.
- Lignes `Card-item` (`patterns/collection-card/`) — une ligne par résultat.
- `Empty-state` (`Size=Compact`) — aucun résultat. `Skeleton` — chargement.

## Structure

Champ `Search`, puis panneau ancré dessous (largeur 480 px). Les groupes sont assemblés à la main : le nombre de familles est arbitraire (même logique que `Table`).

## Interaction flow

1. Focus sur le champ vide : récentes (état à prévoir).
2. Saisie : les résultats apparaissent groupés, cinq lignes maximum par groupe ; une famille sans résultat n'apparaît pas.
3. Flèches haut/bas pour naviguer, Entrée pour ouvrir, Échap pour fermer et rendre le focus au champ.
4. Le lien de pied « Voir tous les résultats pour « … » » ouvre la page de résultats complète.

## States

Récentes (champ vide), chargement (`Skeleton`), résultats, aucun résultat (`Empty-state` Compact), erreur (proposé : `Alert` inline dans le panneau avec nouvelle tentative).

## Validation/errors

Pas de validation. Une requête en échec affiche l'état d'erreur et conserve le texte saisi. Le nombre de résultats est annoncé.

## Accessibility

Voir la section de la brique (pattern combobox, `aria-live`).

## Responsive behavior

Desktop : panneau ancré. Mobile : écran de recherche dédié, pas de panneau.

## Tokens

Ceux de la brique. Aucun nouveau token.

## Related components/patterns

`Search`, `Search-results`, `List-group-header`, `Card-item`, `Command`, `Empty-state`, `Skeleton` ; patterns `Filter bar`, `Collection card`.

---

## Brique : Search-results

Page Figma `↳ Search` (composant unique). Panneau déroulant de **résultats groupés**, ancré à un champ `Search` : aperçu des meilleurs résultats par famille, puis un lien « Voir tous les résultats ». Proche d'un `Combobox` et de `Command`, mais sans saisie propre : c'est la liste attachée au champ `Search`.

### Search-results, Command, Select

| Composant | Rôle |
|---|---|
| `Command` | Palette modale (`Ctrl/Cmd + K`) de commandes et de navigation. |
| `Search-results` | Aperçu des résultats d'un champ `Search`, ancré sous lui, secondaire. |
| `Select` | Choix d'une valeur dans un formulaire (aucun rapport). |

### Anatomie

- **Groupes** : `List-group-header` (famille + nombre de résultats) suivi de ses lignes `Card-item` (`Projet`, `Note`, `Tâche`, `Contact`…), séparées par `Border/subtle`, sans séparateur sur la dernière ligne d'un groupe. Cinq lignes maximum par groupe ; une famille sans résultat n'apparaît pas.
- **Pied** (`searchFooter`) : `Footer-label` (lien « Voir tous les résultats pour « … » », `Text/link`) et `Footer-hint` (raccourci, `Text/tertiary`), masquables via `Show-footer`. Fond `Background/subtle`.

L'exemple fourni montre Projets, Notes et Tâches.

### Propriétés

`Show-footer` (Boolean, `true`), `Footer-label` (Text), `Footer-hint` (Text).

### Tokens

Largeur 480 px · fond `Background/elevated` · bordure `Border/subtle` (1 px) · ombre `Elevation/2` (Effect Style) · pied `Background/subtle`. Aucun token créé.

### Accessibilité

- Pattern combobox : le champ `Search` a `role="combobox"` avec `aria-expanded` et `aria-controls` vers la liste (`role="listbox"`) ; chaque ligne `role="option"`, chaque groupe `role="group"` avec `aria-labelledby`.
- Flèches haut/bas pour naviguer, Entrée pour ouvrir, Échap pour fermer et rendre le focus au champ.
- Nombre de résultats annoncé dans une région `aria-live="polite"`.
