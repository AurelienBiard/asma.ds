# Composant Dialog

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Tâche/décision modale focalisée (`decisions.yaml` → `Dialog`). Scindé en **3 composants indépendants** — `Dialog-header`, `Dialog-body`, `Dialog-footer` — composés manuellement selon le cas d'usage plutôt qu'un assemblage rigide unique. `Drawer` réutilise les 3 mêmes sous-composants dans un conteneur positionné différemment.

## Dialog-header

Composant unique (pas de variantes — piloté par propriétés) :
- **Title**, **Subtitle** (Text)
- **Show-subtitle** (Boolean, défaut `false`)
- **Show-back** (Boolean, défaut `false`) — chevron retour, pour dialogues multi-étapes
- **Show-close** (Boolean, défaut `true`)

Fond `Background/elevated` · Title `Heading/SM` · Subtitle `Misc/Caption` + `Text/secondary`.

## Dialog-body

Composant unique avec une **vraie propriété Slot Figma** (`figma.createSlot()` n'existe pas via script — un Slot ne peut être créé que manuellement dans l'UI Figma — mais une fois créé ainsi, il est bien lisible/pilotable via l'API Plugin, confirmé sur ce composant).

Fond `Background/elevated` · Padding `Spacing/lg` (Responsive).

## Dialog-footer

Composant unique, **aucune propriété exposée** — placer des instances `Button` directement en enfants (typiquement un "Annuler" secondaire + une action primaire).

Fond `Background/elevated` · Bordure haute `Border/default` · Padding `Spacing/md`.

## Composition

Empiler header + body + footer dans un conteneur (radius `Radius/lg`, ombre `Shadow/xl`, largeur fixe selon breakpoint) avec un fond assombri plein écran (`Overlay/scrim`) derrière.

## Guidelines Figma

Page dédiée `↳ Dialog`.
