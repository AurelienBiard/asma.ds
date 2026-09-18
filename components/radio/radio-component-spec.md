# Composant Radio

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Bouton radio — même logique de couleur que Checkbox, anatomie circulaire, pas d'état indéterminé (toujours binaire).

## Propriétés du composant Figma

- **Selected** (variant) : `False` / `True`.
- **Interaction** (variant) : `Default` / `Hover` / `Focus` / `Disabled`.
- **Validation** (variant) : `None` / `Error`.
- **Label** (Text), **Show-label** (Boolean, défaut `true`).

16 variantes (2 Selected × 4 Interaction × 2 Validation).

## Anatomie et couleurs

- **Radio-box** : frame conteneur 20×20, `cornerRadius: 10` (cercle parfait) — une ellipse ne peut pas avoir d'enfants, d'où l'usage d'un frame plutôt qu'une vraie forme elliptique pour porter le point central.
- **Dot** (point central) : ellipse 8×8, `Icon/inverse`, visible uniquement si `Selected=True`.
- Mêmes règles de couleur que Checkbox (Action/primary si sélectionné, Border/default sinon, Focus/Error/Disabled identiques).
- Gap Box↔Label : `Spacing/component-xs` (8px).

## Usage

Toujours en groupe d'au moins 2 options mutuellement exclusives — jamais un Radio isolé (utiliser Checkbox ou Switch selon le besoin réel).

## Leçons de construction

- `ellipse.appendChild(...)` échoue ("no such property 'appendChild' on ELLIPSE node") — les formes (Ellipse, Vector, Rectangle...) sont des nœuds feuilles sans enfants. Pour superposer un élément sur une forme, toujours passer par un `Frame` conteneur.

## Guidelines Figma

Page `↳ Selection inputs`, section "Radio" + section "Guidelines" complète.
