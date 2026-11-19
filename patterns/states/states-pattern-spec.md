# Pattern States

> **Statut** : spec seule (2026-11-19). `Empty-state` existe comme composant et `Skeleton` aussi ; les traitements chargement et erreur ci-dessous sont la partie **candidate** (`ErrorState`, `LoadingState`, précédemment listés comme candidats). Les choix marqués « proposé » sont à valider.

## Purpose

Définir ce qu'une vue affiche quand elle n'a pas de données, charge ou a échoué — de façon homogène dans les tableaux, listes, cartes et pages.

## Use when

- Tout conteneur dont le contenu peut être vide, en attente ou en erreur.

## Do not use when

- Retour transitoire → `Toast`.
- Progression connue d'une opération → `Progress`.
- Erreurs de champ → pattern `Form`.

## Components

- `Empty-state` (`Size=Compact` dans les cartes, listes, cellules de tableau ; `Size=Page` pour les pages, panneaux, drawers) — vide.
- `Skeleton` (`Shape` Text/Circle/Rectangle) — chargement ; composé à la forme exacte du contenu final.
- `Alert` / `Banner` (Inline ou Page) — erreur, avec un `Button` de nouvelle tentative.

## Structure

Vide : icône (optionnelle), titre, description, une action. Chargement : skeletons à la taille exacte du contenu (aucun décalage ; shimmer côté code). Erreur : message disant ce qui a échoué et que faire, avec une action de nouvelle tentative ; proposé : réutiliser `Banner` Inline dans le conteneur.

## Interaction flow

1. Le chargement affiche immédiatement les skeletons (pas de spinner par-dessus).
2. En cas de succès : le contenu remplace les skeletons ; sur résultat vide : `Empty-state`.
3. En cas d'échec : message d'erreur avec nouvelle tentative ; réessayer ramène au chargement.

## States

Chargement, vide (premier usage : invitation à créer ; filtré : « aucun résultat » avec action de réinitialisation des filtres), erreur (avec ou sans nouvelle tentative possible).

## Validation/errors

Distinguer « vide parce que rien n'existe » de « vide à cause des filtres » : l'action diffère.

## Accessibility

Les conteneurs en chargement utilisent `aria-busy="true"` ; les skeletons sont décoratifs ; les changements d'état (chargé, vide, erreur) sont annoncés dans une région live polie ; l'action de nouvelle tentative est focusable et nommée.

## Responsive behavior

`Compact` en dessous du niveau page ; `Page` pour les états en pleine vue.

## Tokens

Aucun propre (voir `Empty-state`, `Skeleton`).

## Related components/patterns

`Empty-state`, `Skeleton`, `Alert`, `Banner`, `Button` ; patterns `DataTable`, `Search`, `Kanban`, `FileUpload`.
