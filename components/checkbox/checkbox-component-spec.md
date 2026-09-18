# Composant Checkbox

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Case à cocher — première anatomie de la famille Selection inputs (cercle/carré + label, pas un champ texte).

## Propriétés du composant Figma

- **Checked** (variant) : `False` / `True` / `Indeterminate` (état intermédiaire — sélection de groupe partielle).
- **Interaction** (variant) : `Default` / `Hover` / `Focus` / `Disabled`.
- **Validation** (variant) : `None` / `Error` (case requise dans un formulaire).
- **Label** (Text), **Show-label** (Boolean, défaut `true`).

24 variantes (3 Checked × 4 Interaction × 2 Validation).

## Anatomie et couleurs

- **Box** : 20×20, radius `Radius/control`.
- Coché/Indéterminé : fond `Action/primary` (`Action/primary-hover` en Hover), icône `Check` (coché) ou `Minus` (indéterminé) en `Icon/inverse`, 14×14, pas de bordure sauf Focus/Error.
- Non coché : fond `Background/elevated`, bordure `Border/default` (`Border/strong` en Hover).
- Focus : bordure `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE`.
- Error : bordure `Feedback/Danger/border` (même si coché).
- Disabled : fond `Background/disabled`, bordure `Border/disabled`, icône/texte `Text/disabled`.
- Gap Box↔Label : `Spacing/component-xs` (8px, variable liée).

## Leçons de construction

- Contrairement au composant `Icon` (wrapper à 2 niveaux d'instanciation, où `findOne`/lecture directe échoue sur une instance fraîche), une icône Phosphor **brute** en un seul niveau (`icon.createInstance()` direct, sans wrapper) reste lisible via `findOne(n => n.type === 'VECTOR')` même fraîchement créée — la limitation d'accès aux instances concerne spécifiquement la double imbrication, pas toutes les instances.
- `clipsContent` doit être retiré manuellement sur le composant externe si besoin (limitation rencontrée et corrigée à la main par l'utilisateur pour ce composant).

## Guidelines Figma

Page `↳ Selection inputs`, section "Checkbox" + section "Guidelines" complète (couvre aussi Radio/Switch/Segmented Control).
