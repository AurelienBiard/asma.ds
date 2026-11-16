# Composant Kanban-card (2026-11-16)

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Page Figma : `↳ Kanban-card`. ComponentSet `Kanban-card`, 5 variantes (`State`).

Carte d'un élément dans une **colonne de tableau Kanban** (une colonne par statut ou par étape) : titre, contexte, information secondaire, marqueur d'importance. Composant **générique** : l'élément peut être une tâche, un ticket, une candidature, une demande.

**Exemple de réutilisation** : `OS / Task-card` (ASMA OS, Kanban des Tâches) est une carte de tâche construite sur ce modèle — le composant local garde son vocabulaire (« tâche », échéance, priorité *Haute*), `Kanban-card` porte la structure et les règles réutilisables.

## Variantes

- **`State`** : `Default` · `Hover` · `Focus` · `Dragging` · `Done`.
  - `Default` : bordure 1 px `Border/default`.
  - `Hover` : bordure `Border/strong` + élévation `Elevation/2`.
  - `Focus` : bordure `Border/focus` 2 px.
  - `Dragging` : carte soulevée, `Elevation/2`. **Côté code** : rotation de −2° et emplacement d'origine matérialisé par un cadre en pointillés (non reproduits dans Figma).
  - `Done` : titre barré en `Text/secondary` (élément terminé). **Le barré n'existe que sur cette variante.** Limite Figma : si le `Title` de `Done` reste lié à la propriété texte, le barré se propage à toutes les variantes ; ce `Title` n'est donc **pas branché** sur la propriété `Title` — dans une instance `State=Done`, modifier le texte directement sur le calque.
- Pas d'axe `Interactive` : une carte Kanban est toujours cliquable (ouvre le détail) et déplaçable.

Largeur fixe **256 px** (la colonne la remplit), hauteur selon le contenu (un titre long passe à la ligne).

## Anatomie

`Kanban-card` (vertical, fond `Background/elevated`) → `Title` · `Context` · `meta` (`Meta` + `flag`).

## Propriétés

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

## Tokens

- Fond `Background/elevated` · bordure `Border/default` (`Border/strong` Hover, `Border/focus` Focus) · `Radius/card` · padding `Spacing/component-sm` · espacement `Spacing/component-xs` · ombre `Elevation/2` (Hover, Dragging).
- `Title` : Text Style `Misc/Label`, `Text/primary` (`Text/secondary` + barré en `Done`) · `Context`, `Meta` : `Body/SM`, `Text/secondary` · `Flag` : icône + libellé `Body/SM` en `Feedback/Danger`.
- `Meta` est neutre par défaut ; pour signaler un retard, le passer en `Feedback/Danger/text` (usage ASMA OS).

## Usage

- Dans une colonne de Kanban. Pour lister un groupe d'éléments dans une carte, utiliser `Card-collection` ; pour un contenu riche (image, plusieurs actions), `Card`. Ne pas imbriquer dans une `Card`.
- Pas d'action inline : menu « ⋯ » (Modifier · Terminer · Supprimer) et glisser-déposer. Le marqueur ne s'affiche que pour le niveau le plus élevé.
- Ordre dans la colonne : défini par le produit (ex. échéance).

## Accessibilité

- La carte est un lien ou un bouton englobant (ouvre le détail), nom accessible = `Title` + `Context`.
- Glisser-déposer : **alternative clavier obligatoire** (« Déplacer vers… » dans le menu de la carte) ; le changement de colonne est annoncé (`aria-live`).
- Le marqueur ne repose pas sur la couleur seule (icône + libellé) ; un élément `Done` n'est pas signalé par le seul barré : la colonne porte le statut.

## Guidelines Figma

Page dédiée `↳ Kanban-card` (gabarit des autres composants).
