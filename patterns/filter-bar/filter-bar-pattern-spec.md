# Pattern Filter bar

> **Statut** : nouveau pattern, créé le 2026-10-05. Composition de composants existants, aucun composant nouveau. Les choix marqués « par défaut » sont à valider (comportement non précisé jusque-là).

## Purpose

Rechercher et filtrer un ensemble de données affiché en dessous (`Table`, liste). Rend visibles les filtres appliqués et permet de les retirer.

## Use when

- Un ensemble de données assez grand pour nécessiter recherche et/ou filtres.
- Les critères de filtre sont connus et peu nombreux (1 à 4).

## Do not use when

- Recherche seule sans filtres → `Search` directement.
- Beaucoup de critères ou critères imbriqués → `QueryBuilder` (pattern candidat, non construit).
- Choix d'une vue parmi des vues paires → `Tabs`.

## Components

- `Search` (`components/search-input/`) — instance, largeur fixe 280px.
- `Select` (`components/select/`) — un par critère ; `Content=Empty` au repos, `Content=Filled` quand un filtre est appliqué.
- `Chip` (`components/chip/`) — `Type=Neutral`, `Size=Medium`, `State=Active`, `Show-icon-leading=false`, icône trailing `X`.
- `Button` — `Type=Ghost` pour « Réinitialiser », `Type=Primary` pour l'action principale de la vue.

## Structure

Pas de ComponentSet : le nombre de filtres est arbitraire (même logique que `Table` et `Pagination`), assemblage manuel.

Conteneur vertical, `itemSpacing: Spacing/component-sm`.

- **Controls** (toujours) : rangée horizontale, `itemSpacing: Spacing/component-xs`, alignement centré. `Search`, puis un `Select` par critère, puis — seulement si au moins un filtre est appliqué — `Button` Ghost « Réinitialiser », puis un espaceur (FILL), puis l'action principale (`Button` Primary) alignée à droite.
- **Applied-filters** (seulement si au moins un filtre est appliqué) : rangée horizontale, `itemSpacing: Spacing/component-xs`. Un `Chip` par filtre appliqué (libellé « Critère : Valeur »), un espaceur (FILL), puis le compteur « N résultats » (`Body/MD` + `Text/secondary`).

## Interaction flow

- Changer un `Select` ou saisir dans `Search` met à jour les résultats **immédiatement** (par défaut — pas de bouton « Appliquer »).
- Le `Select` appliqué passe en `Content=Filled` et un `Chip` apparaît dans `Applied-filters`.
- Clic sur le `X` d'un `Chip` : retire ce filtre, le `Select` correspondant repasse en `Content=Empty`.
- « Réinitialiser » : retire tous les filtres et vide la recherche.

## States

- **Sans filtre** : `Controls` seule, pas de « Réinitialiser », pas de `Applied-filters`.
- **Filtré** : `Controls` avec « Réinitialiser » + `Applied-filters`.
- **Zéro résultat** : pas de composant dédié à ce jour — message simple avec l'action « Réinitialiser » (`EmptyState` non construit).

## Validation/errors

Aucune validation propre : les filtres sont des sélections dans des listes fermées. La recherche libre n'a pas de `Validation`.

## Accessibility

- `Controls` dans un conteneur `role="search"`.
- `Search` et chaque `Select` ont un nom accessible (`aria-label`) — pas de label visible.
- Chaque `Chip` est un bouton nommé « Retirer le filtre Statut : Actif ».
- Après retrait d'un `Chip`, le focus passe au `Chip` suivant, sinon au champ `Search`.
- Compteur « N résultats » en `aria-live="polite"`.
- Ordre de tabulation = ordre visuel : `Search`, `Select`s, « Réinitialiser », action principale, puis `Chip`s.

## Responsive behavior

Non spécifié à ce jour (au-delà de 3 à 4 `Select` ou en mobile : repli éventuel vers un `Popover` ou un `Drawer`).

## Tokens

`Spacing/component-xs`, `Spacing/component-sm`, `Text/secondary`, `Body/MD`.

## Related

`Search`, `Select`, `Chip`, `Button`, `Table`, `Pagination`.

## Guidelines Figma

Page `↳ Filter bar` (catégorie Patterns) : section `Filter bar` (exemples `Filter-bar — Default` et `Filter-bar — Filtered`) + section `Guidelines`.
