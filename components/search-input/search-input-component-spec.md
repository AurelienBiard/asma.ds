# Composant Search

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Champ de recherche — base identique à TextInput (32 variantes Interaction × Content × Validation), avec des ajouts spécifiques.

## Différences avec TextInput

- **Search-icon** (leading) et **Search-icon-trailing** : instances du composant `Icon` (pictogramme `MagnifyingGlass`), chacune indépendamment affichable via `Show-icon-leading` (Boolean, défaut `true`) et `Show-icon-trailing` (Boolean, défaut `false`). Icônes non interactives (contrairement au toggle de PasswordInput).
- **Search-button** (Boolean `Show-button`, défaut `false`) : bouton attaché après le champ — instance de `Button` (Type=Primary, Icon-only=true, Show-label=false), redimensionné à 40×40, radius gauche retiré pour un accolement propre. ⚠️ Affiche par défaut l'icône héritée de Button/Primary (pas la loupe) — à changer manuellement (Swap instance) si la cohérence visuelle avec la loupe du champ est souhaitée.
- Structure : `Row` (horizontal, FILL) contient `[Field, Search-button]` ; `Field` contient `[Search-icon, Placeholder/Value (gap 8px), Search-icon-trailing]`.

## Propriétés du composant Figma

Mêmes propriétés que TextInput (`Placeholder`, `Value`, `Message`) + `Show-icon-leading`, `Show-icon-trailing`, `Show-button` (Boolean).

## Leçons de construction

- Un clone hérite parfois de `layoutSizingVertical: FILL` de façon incorrecte (résidu du composant source), forçant une hauteur figée malgré `primaryAxisSizingMode: AUTO` — toujours vérifier `layoutSizingVertical` explicitement après un clonage, pas seulement `primaryAxisSizingMode`.
- Cloner un COMPONENT (pas une INSTANCE) pour l'insérer dans un autre composant lève une erreur ("Reparenting would create a component inside a component") — toujours utiliser `.createInstance()` sur le composant source, jamais `.clone()`, quand on niche un composant entier (ex. Button) dans un autre.

## Guidelines Figma

Page `↳ Text inputs`, section "Search". Guidelines partagées avec TextInput/PasswordInput (section générique) + note dédiée.
