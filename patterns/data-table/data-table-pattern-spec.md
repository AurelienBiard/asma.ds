# Pattern DataTable

> **Statut** : spec seule (2026-11-19), pas encore de page Figma. Composition de composants et patterns existants ; aucun composant ni token nouveau. Les choix marqués « proposé » sont à valider.

## Purpose

Parcourir un grand jeu de données tabulaires : le rechercher et le filtrer, sélectionner des lignes, agir sur la sélection, changer de page, et traiter de façon homogène les cas vide et chargement.

## Use when

- Enregistrements comparables présentés en colonnes (entreprises, factures, utilisateurs).
- Le jeu est trop grand pour être affiché d'un bloc (filtres et pagination nécessaires).

## Do not use when

- Cellules éditables et modèle clavier de tableur → `DataGrid`.
- Un groupe court d'entrées liées dans une page → pattern `Collection card`.
- Éléments regroupés par statut → pattern `Kanban`.

## Components

- Pattern `Filter bar` — au-dessus du tableau (`patterns/filter-bar/`).
- `Table` (`Selectable=True` quand des actions portent sur les lignes) — `components/table/`.
- `Pagination` — sous le tableau.
- Pattern `BulkActions` — `Bulk-action-bar`, affichée tant que des lignes sont sélectionnées.
- `Empty-state` (`Size=Compact`, dans la zone du tableau) et lignes `Skeleton` — voir le pattern `States`.

## Structure

Pile verticale : barre de filtres → tableau → pagination, gap `Spacing/component-md` (proposé). Le conteneur du tableau porte la bordure extérieure ; la dernière ligne n'a pas de bordure basse (règle de `Table`). La `Bulk-action-bar` flottante ne pousse pas la mise en page ; réserver un espace en bas tant qu'elle est visible.

## Interaction flow

1. Saisir ou choisir un filtre met à jour le tableau, revient à la page 1 et vide la sélection.
2. Sélectionner des lignes affiche la `Bulk-action-bar` ; « Tout sélectionner » ne couvre que les lignes visibles filtrées.
3. Changer de page ou de tri vide la sélection.
4. Après une action groupée, la sélection est vidée et un `Toast` rend compte du résultat.

## States

Chargement (lignes `Skeleton` à la même hauteur que les lignes, sans décalage), rempli, vide sans filtres (`Empty-state` avec une action de création), vide avec filtres (`Empty-state` « Aucun résultat » avec une action de réinitialisation), erreur (`Banner` Inline avec nouvelle tentative), lignes sélectionnées.

## Validation/errors

Un chargement en échec conserve les filtres précédents et affiche l'erreur ; une action groupée en échec conserve la sélection (voir `BulkActions`).

## Accessibility

Sémantique native de tableau (spec `Table`) ; région live annonçant le nombre de résultats après filtrage ; cases de sélection nommées par ligne ; le focus n'est pas déplacé à l'apparition de la barre d'actions. `Pagination` est un `nav` avec `aria-label`.

## Responsive behavior

Desktop : tableau complet. Mobile (< 768 px) : proposé — défilement horizontal avec première colonne figée, `Pagination` compacte ; ne pas passer en cartes sans spec.

## Tokens

Aucun propre ; hérités des composants assemblés.

## Related components/patterns

`Table`, `Pagination`, `Empty-state`, `Skeleton` ; patterns `Filter bar`, `BulkActions`, `States`, `Confirmation`.
