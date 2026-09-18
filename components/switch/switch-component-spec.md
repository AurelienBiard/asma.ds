# Composant Switch

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Interrupteur (toggle) — bascule instantanée d'un réglage, pas un champ de formulaire.

## Propriétés du composant Figma

- **On** (variant) : `False` / `True`.
- **Interaction** (variant) : `Default` / `Hover` / `Focus` / `Disabled`.
- **Label** (Text), **Show-label** (Boolean, défaut `true`).

8 variantes (2 On × 4 Interaction). **Pas de propriété Validation** — un switch s'applique immédiatement, il n'est pas soumis à une validation de formulaire comme Checkbox/Radio.

## Anatomie et couleurs

- **Track** : 40×24, `cornerRadius: 12` (pilule). Off : `Border/strong`. On : `Action/primary` (`Action/primary-hover` en Hover). Disabled : `Background/disabled` + bordure `Border/disabled`.
- **Thumb** : ellipse 18×18, toujours `Background/elevated` (blanc), position `x=3` (Off) ou `x=19` (On), `y=3`.
- Focus : bordure `Border/focus` + `Primitive/Border/medium` sur `Track`, `strokeAlign: OUTSIDE`.

## Usage

Réserver à un effet immédiat sans confirmation. Si l'action nécessite un bouton "Enregistrer" ou équivalent, utiliser Checkbox à la place.

## Guidelines Figma

Page `↳ Selection inputs`, section "Switch" + section "Guidelines" complète.
