# Composants Segment et Segmented-control

> Ce fichier est la **source de vérité** des deux composants (le second assemble le premier). Toute modification se fait ici en premier, puis est répercutée dans Figma.

## Composant atomique : Segment

Onglet individuel, réutilisé par Segmented-control.

- **Propriétés** : `Selected` (False/True) × `Interaction` (Default/Hover/Focus/Disabled), 8 variantes. Propriété texte `Label`.
- Selected=True : fond `Background/elevated` (se détache du conteneur neutre), texte `Text/primary`.
- Selected=False : transparent, texte `Text/tertiary` (Hover : fond `Action/ghost-hover`).
- Focus : bordure `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE`.
- Disabled : texte `Text/disabled`, fond `Background/disabled` si Selected=True sinon transparent.
- Padding : `Spacing/component-sm` (horizontal) / `Spacing/component-xs` (vertical), radius `Radius/control`.

## Segmented-control (assemblage)

Composant unique (pas de variantes) : conteneur `Action/neutral`, padding `Primitive/Spacing/2xs`, radius `Radius/control`, contenant 3 instances de `Segment` avec un gap de 4px. Exemple construit avec le 2ᵉ segment sélectionné.

## Usage

Réserver à un petit nombre d'options (2 à 5) toutes visibles sans défilement. Au-delà, utiliser un Select ou des Tabs.

## Guidelines Figma

Page `↳ Selection inputs`, section "Segment" et section "Segmented-control" + section "Guidelines" complète (couvre Checkbox/Radio/Switch/Segmented Control ensemble).
