# Composant Progress

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : composants construits dans Figma (page `↳ Progress`) avant que cette spec n'existe — rédigée le 2026-10-05 à partir d'une relecture de l'état Figma réel. Deux composants, `Progress-linear` et `Progress-circular`, partageant les mêmes propriétés. À valider si un détail diverge de l'intention d'origine.

## Propriétés (communes aux deux composants)

- **State** (variant) : `Determinate` (pourcentage connu) / `Indeterminate` (durée ou quantité inconnue).
- **Percentage** (variant) : `0`, `10`, `20`, … `100` (pas de 10) pour `Determinate` ; `none` pour `Indeterminate` uniquement. Le pourcentage est une propriété de variante, pas une valeur continue : Figma ne représente que des paliers de 10 ; en code, la valeur réelle est continue.

12 variantes par composant (11 paliers `Determinate` + 1 `Indeterminate`).

## Progress-linear

Barre horizontale, 240px de large dans le composant (en usage réel, s'étire à la largeur de son conteneur).

### Anatomie

- Conteneur vertical, gap 4px, `clipsContent: true`. Deux enfants en `Determinate`, un seul en `Indeterminate`.
- **Percentage-label** (`Determinate` uniquement) : `Misc/Label` + `Text/primary`, `FILL` en largeur, aligné à droite, au-dessus de la barre.
- **Track** : 240×8, fond `Action/neutral`, radius 4px (valeur littérale, pas de token), `clipsContent: true`.
- **Fill** : hauteur 8, fond `Action/primary`, radius 4px. Largeur fixe = pourcentage × largeur du `Track` (50 % → 120px ; 0 % → 0px).

### Indeterminate

Pas de label (hauteur totale 8px). `Fill` de largeur fixe 72px (30 % de la piste), posé à gauche dans Figma (statique). En usage réel, ce segment glisse en boucle sur toute la longueur de la piste ; `clipsContent` sur `Track` garantit qu'il ne déborde jamais pendant l'animation.

## Progress-circular

Indicateur circulaire de style donut (anneau plein avec trou central), 48×48.

### Anatomie

Conteneur sans auto-layout, trois enfants superposés :
- **Track** : ellipse 48×48, anneau complet (`arcData` de −π/2 à 3π/2, `innerRadius: 0.7`, soit une épaisseur d'anneau d'environ 7,2px), fond `Action/neutral`.
- **Fill** : même ellipse, arc partiel superposé, fond `Action/primary`. Départ à midi (−π/2), sens horaire, fin à −π/2 + 2π × pourcentage (50 % → π/2).
- **Percentage-label** (`Determinate` uniquement) : `Body/XS` + `Text/primary`, centré horizontalement dans l'anneau, positionné à la main (texte hors auto-layout).

### Indeterminate

Pas de label. `Fill` = arc fixe de 90° (de −π/2 à 0), statique dans Figma. En usage réel, il tourne en boucle autour de l'anneau.

## Comportement

- **Determinate** : la largeur du `Fill` (Linear) ou l'angle de fin de l'arc (Circular) suit la valeur réelle ; le label affiche le pourcentage.
- **Indeterminate** : uniquement quand la durée est réellement inconnue — sinon `Determinate` donne une meilleure perception du temps restant.
- Composant non interactif : pas d'états `Hover`/`Focus`/`Disabled`.
- Non spécifié à ce jour : durée et courbe de l'animation `Indeterminate`, comportement sous `prefers-reduced-motion`, variantes de statut (succès, erreur) et transition animée entre deux valeurs `Determinate`.

## Usage

- **Linear** : progression intégrée à une mise en page (barre en haut de page, upload de fichier).
- **Circular** : espace restreint ou indicateur autonome (bouton en cours de chargement, chargement de page).
- Attente de contenu dont la forme est connue → `Skeleton` ; progression d'une opération → `Progress` ; progression dans un parcours d'étapes → `Step-indicator`.

## Accessibilité

- `role="progressbar"` avec `aria-valuenow`, `aria-valuemin`, `aria-valuemax` pour `Determinate`.
- `Indeterminate` : omettre `aria-valuenow` (ou utiliser `aria-busy="true"` sur la région concernée) plutôt que de mentir sur une valeur.
- Un nom accessible (`aria-label` ou `aria-labelledby`) décrit l'opération en cours.
- Annoncer un changement d'état significatif (terminé, erreur) via une zone `aria-live`, jamais seulement visuellement.

## Tokens

`Action/neutral` (Track), `Action/primary` (Fill), `Text/primary` (label), `Misc/Label` (label Linear), `Body/XS` (label Circular).

## Leçons de construction

- Un arc partiel s'obtient via `ellipse.arcData = { startingAngle, endingAngle, innerRadius }` (angles en radians, −π/2 = midi). Un seul objet ellipse suffit, sans masque ni formes découpées.
- Un texte inséré dans un frame en auto-layout suit le flux normal (il se place à côté des autres enfants) sauf si `layoutPositioning = "ABSOLUTE"` est défini — ne jamais supposer qu'un texte se centre tout seul par-dessus une forme sans le positionner explicitement.
- Deux sections du même nom peuvent coexister sur une page (après suppression puis recréation) : `findAll(...)[0]` prend la première dans l'ordre du document, pas forcément la bonne — vérifier le nombre d'enfants de chaque résultat en cas de doute.

## Guidelines Figma

Page dédiée `↳ Progress`, sections `Guidelines`, `Progress-linear` et `Progress-circular`. Le 2026-10-05, trois affirmations des guidelines ont été corrigées pour coller au composant réel : anneau `48×48` en `arcData` avec `innerRadius 0.7` (et non `40×40`, trait de 4px, extrémités arrondies), 12 variantes (et non 11), label de `Progress-linear` aligné à droite.
