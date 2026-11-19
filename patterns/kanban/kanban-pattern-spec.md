# Pattern Kanban

> **Statut** : reclassé le 2026-11-19 depuis le composant `Kanban-card` (créé le 2026-11-16). Un Kanban est un workflow (colonnes = statuts, les cartes passent de l'une à l'autre) ; la carte en est la brique. Page Figma : `↳ Kanban` (section `💻 PATTERNS`, anciennement `↳ Kanban-card`). La brique reste un ComponentSet Figma (`Kanban-card`) pour pouvoir être instanciée. Les points marqués « proposé » sont à valider.

## Purpose

Afficher des éléments regroupés par statut ou par étape, une colonne par statut, et permettre de déplacer un élément d'une colonne à l'autre. Le pattern porte l'agencement (colonnes, ordre, déplacement), pas seulement la carte.

## Use when

- Des éléments traversent un petit nombre de statuts ordonnés (à faire / en cours / terminé, étapes d'un pipeline).
- Changer un élément de statut est une action fréquente.

## Do not use when

- Les éléments n'ont pas de progression de statut → `List` ou `Table`.
- Beaucoup d'attributs comparables par élément → `Table`.
- Un groupe d'entrées liées en lecture seule dans une page → pattern `Collection card`.
- Contenu riche par élément (image, plusieurs actions) → `Card`.

## Components

- `Kanban-card` (brique, ComponentSet `State`) — une carte par élément. Voir « Brique : Kanban-card » plus bas.
- `List-group-header` (`components/list-group-header/`) — en-tête de colonne proposé : libellé du statut + `Count`.
- `Menu` — menu « ⋯ » de la carte (Modifier · Terminer · Supprimer · Déplacer vers…).
- `Empty-state` (`Size=Compact`) — colonne vide. `Skeleton` — colonne en chargement.
- `Toast` — retour après un déplacement ou une suppression (avec Annuler).

## Structure

Assemblage manuel (nombre de colonnes et de cartes arbitraire, même logique que `Table`) : une rangée horizontale de colonnes ; chaque colonne = en-tête + pile verticale de `Kanban-card` (gap `Spacing/component-xs`). La largeur de colonne est celle de la carte (256 px). La rangée défile horizontalement si les colonnes débordent. L'ordre dans une colonne est défini par le produit (ex. échéance).

## Interaction flow

1. La carte ouvre le détail de l'élément (clic / Entrée).
2. Le glisser-déposer déplace la carte vers une autre colonne ; la carte est en `State=Dragging` et son emplacement d'origine reste visible (cadre en pointillés, côté code uniquement).
3. Alternative clavier (obligatoire) : le menu de la carte propose « Déplacer vers… » avec la liste des colonnes.
4. Après le déplacement, le changement de colonne est annoncé (`aria-live`) et un `Toast` avec Annuler le confirme.

## States

Par carte : `Default`, `Hover`, `Focus`, `Dragging`, `Done` (voir la brique). Par colonne : remplie, vide (`Empty-state` Compact), en chargement (`Skeleton`), cible de dépôt mise en évidence pendant le glissement (proposé : `Border/focus`).

## Validation/errors

Un déplacement que le produit refuse (transition interdite, droits) ramène la carte dans sa colonne d'origine et affiche un `Toast` d'erreur. Un déplacement en échec ne laisse jamais la carte dans un état intermédiaire.

## Accessibility

Voir la section de la brique pour la carte. Colonnes : `role="list"` avec un nom accessible = libellé du statut + nombre ; chaque carte est un élément de liste. Le glisser-déposer a toujours l'alternative clavier ci-dessus.

## Responsive behavior

Desktop : colonnes côte à côte, défilement horizontal. Mobile (< 768 px) : une colonne à la fois (proposé : `Tabs` ou `SegmentedControl` pour changer de statut), glisser-déposer remplacé par « Déplacer vers… ».

## Tokens

Ceux de la brique ; gap entre colonnes `Spacing/component-sm` (proposé). Aucun nouveau token.

## Related components/patterns

`Kanban-card`, `List-group-header`, `Count`, `Menu`, `Empty-state`, `Toast` ; patterns `Collection card`, `DataTable`, `BulkActions`.

---

## Brique : Kanban-card

ComponentSet Figma `Kanban-card`, 5 variantes (`State`). Carte d'un élément dans une **colonne de tableau Kanban** : titre, contexte, information secondaire, marqueur d'importance. Composant **générique** : l'élément peut être une tâche, un ticket, une candidature, une demande.

**Réutilisation (2026-11-19)** : `OS / Task-card` (ASMA OS, Kanban des Tâches) est un composant local qui **contient une instance exposée de `Kanban-card`** ; ses propriétés (`Title`, `Context`, `Meta` = échéance, `Show-meta`, `Show-flag`, `State`) se règlent sur cette instance. Les cartes de la colonne « Terminé » sont en `State=Done`, la carte glissée en `State=Dragging`, l'échéance en retard est colorée en `Feedback/Danger/text`.

### Variantes

- **`State`** : `Default` · `Hover` · `Focus` · `Dragging` · `Done`.
  - `Default` : bordure 1 px `Border/default`.
  - `Hover` : bordure `Border/strong` + élévation `Elevation/2`.
  - `Focus` : bordure `Border/focus` 2 px.
  - `Dragging` : carte soulevée, `Elevation/2`. **Côté code** : rotation de −2° et emplacement d'origine matérialisé par un cadre en pointillés (non reproduits dans Figma).
  - `Done` : titre barré en `Text/secondary` (élément terminé). **Le barré n'existe que sur cette variante.** Limite Figma : si le `Title` de `Done` reste lié à la propriété texte, le barré se propage à toutes les variantes ; ce `Title` n'est donc **pas branché** sur la propriété `Title` — dans une instance `State=Done`, modifier le texte directement sur le calque.
- Pas d'axe `Interactive` : une carte Kanban est toujours cliquable (ouvre le détail) et déplaçable.

Largeur fixe **256 px** (la colonne la remplit), hauteur selon le contenu (un titre long passe à la ligne).

### Anatomie

`Kanban-card` (vertical, fond `Background/elevated`) → `Title` · `Context` · `meta` (`Meta` + `flag`).

### Propriétés

| Propriété | Type | Défaut | Rôle |
|---|---|---|---|
| `State` | Variant | `Default` | État visuel |
| `Title` | Text | « Revoir la maquette du tableau de bord » | Libellé de l'élément |
| `Context` | Text | « Projet Alpha · Équipe Design » | Rattachement (projet · client · contact…) |
| `Meta` | Text | « 29 oct. » | Information secondaire : échéance, date, compteur |
| `Flag-label` | Text | « Haute » | Libellé du marqueur d'importance |
| `Show-context` | Boolean | `true` | Affiche `Context` |
| `Show-meta` | Boolean | `true` | Affiche `Meta` |
| `Show-flag` | Boolean | `true` | Affiche le marqueur (icône `Flag` + `Flag-label`) |

Si `Show-meta` et `Show-flag` sont tous deux à `false`, la ligne `meta` est vide mais garde son espacement : masquer aussi la ligne côté code.

### Tokens

- Fond `Background/elevated` · bordure `Border/default` (`Border/strong` Hover, `Border/focus` Focus) · `Radius/card` · padding `Spacing/component-sm` · espacement `Spacing/component-xs` · ombre `Elevation/2` (Hover, Dragging).
- `Title` : Text Style `Misc/Label`, `Text/primary` (`Text/secondary` + barré en `Done`) · `Context`, `Meta` : `Body/SM`, `Text/secondary` · `Flag` : icône + libellé `Body/SM` en `Feedback/Danger`.
- `Meta` est neutre par défaut ; pour signaler un retard, le passer en `Feedback/Danger/text` (usage ASMA OS).

### Usage

- Dans une colonne de Kanban. Ne pas imbriquer dans une `Card`.
- Pas d'action inline : menu « ⋯ » (Modifier · Terminer · Supprimer) et glisser-déposer. Le marqueur ne s'affiche que pour le niveau le plus élevé.

### Accessibilité

- La carte est un lien ou un bouton englobant (ouvre le détail), nom accessible = `Title` + `Context`.
- Glisser-déposer : **alternative clavier obligatoire** (« Déplacer vers… » dans le menu de la carte) ; le changement de colonne est annoncé (`aria-live`).
- Le marqueur ne repose pas sur la couleur seule (icône + libellé) ; un élément `Done` n'est pas signalé par le seul barré : la colonne porte le statut.
