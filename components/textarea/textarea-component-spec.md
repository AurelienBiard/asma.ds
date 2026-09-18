# Composant Textarea

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Champ de saisie multiligne — base TextInput adaptée pour du texte long.

## Différences avec TextInput

- **Alignement** : `counterAxisAlignItems: MIN` (texte aligné en haut, pas centré) — le contenu grandit vers le bas.
- **Pas de troncature** : `textTruncation: DISABLED`, retour à la ligne actif.
- **Text Style** : `Body/SM` (pas `Misc/Label`) — plus adapté à un volume de texte important.
- **Dimensions** : `Field` en largeur fixe 280px, hauteur fixe **160px** (pas de hug — représente une zone de saisie à défilement, le texte peut dépasser visuellement plutôt que d'étirer le composant indéfiniment).
- Pas d'icône (Status-icon retiré — pas de place pertinente dans une zone de texte multiligne).

## Propriétés du composant Figma

`Placeholder`, `Value` (contenu multiligne par défaut, ex. 3 lignes), `Message` — mêmes propriétés que TextInput.

## Leçons de construction

- Un `resize()` sur un enfant peut faire basculer le **parent** en `layoutSizingVertical: FIXED`/`primaryAxisSizingMode: FIXED` avec une valeur transitoire figée — après tout resize de contenu, revérifier et corriger le sizing mode du ou des parents (composant externe ET Field), pas seulement celui de l'élément visé.
- Texte en `layoutSizingHorizontal: FILL` à l'intérieur d'un parent en `HUG` crée un conflit de taille (le parent hug se réduit à une largeur minimale dégénérée) — donner une largeur fixe explicite au parent (`Field`) plutôt que de compter sur le hug quand son enfant texte est en FILL.

## Guidelines Figma

Page `↳ Text inputs`, section "Textarea". Guidelines partagées + note dédiée.
