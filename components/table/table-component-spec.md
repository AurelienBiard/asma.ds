# Composant Table

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveau composant, créé le 2026-09-30. Composé de deux briques atomiques (`Header-cell`, `Row`), elles-mêmes construites sur `Cell` (voir `components/cell/`). Pas de ComponentSet monolithique « Table » — le nombre de colonnes est arbitraire, donc l'assemblage se fait par composition manuelle d'instances, comme `Command` (voir `components/command/`) et non par une matrice de variants.

## Header-cell

En-tête de colonne, cliquable quand la colonne est triable.

### Propriétés du composant Figma

- **Sort** (variant) : `None` (défaut) / `Asc` / `Desc`.
- **Align** (variant) : `Left` (défaut) / `Right` — même règle que `Cell` : `Right` réservé aux valeurs numériques et à la colonne d'actions.
- **State** (variant) : `Default` / `Hover`.
- **Label** (Text).
- **Show-sort-icon** (Boolean, défaut `true`) : `false` pour une colonne non triable (ex. colonne Actions) — masque l'icône, la cellule reste alors non cliquable et non hoverable en pratique même si la variante `State=Hover` existe techniquement.

12 variantes (3 Sort × 2 Align × 2 State).

### Anatomie

Conteneur horizontal 220px (largeur du composant, comme `Cell` — s'étire pour remplir sa colonne dans `Table`), hauteur hug. Padding `Spacing/component-sm` (horizontal, 12px) / `Spacing/component-2xs` (vertical, 4px), `itemSpacing: Spacing/component-2xs` (4px), alignement vertical centré. Deux enfants : `Label` (texte) puis instance `Sort-icon` (wrapper `Icon`, `Size=Small`).

### États et couleurs

- **Sort=None** : `Label` en `Misc/Label` + `Text/secondary`. `Sort-icon` = pictogramme `CaretUpDown`, couleur `Icon/tertiary` — indique une colonne triable mais inactive (au repos, la moins appuyée visuellement).
- **Sort=Asc** : `Sort-icon` = `CaretUp`. `Sort=Desc` : `Sort-icon` = `CaretDown`. Dans les deux cas, `Label` passe en `Text/primary` et `Sort-icon` en `Icon/primary` — la colonne activement triée se distingue visuellement des autres en-têtes.
- **Hover** : fond `Action/ghost-hover`, `Radius/control` (4px), sur les trois valeurs de `Sort`. Ne s'applique qu'aux colonnes triables (`Show-sort-icon=true`) — une colonne non triable n'a pas de retour visuel au survol.

### Comportement

Au clic (colonne triable uniquement) : cycle `None → Asc → Desc → None`. Le `Label` seul (pas seulement l'icône) déclenche le tri — toute la cellule est la zone cliquable, comme un `Menu-item`.

## Row

Ligne de données, conteneur de `Cell`.

### Propriétés du composant Figma

- **State** (variant) : `Default` / `Hover` / `Selected` / `Disabled`.
- **Selectable** (variant) : `False` / `True` — présence ou non de la colonne de sélection (checkbox).

8 variantes (4 State × 2 Selectable).

### Anatomie

Conteneur horizontal, hauteur hug (44px avec le contenu par défaut, portée par `Cell`), largeur hug (s'étire pour remplir le tableau dans un contexte réel). Bordure basse uniquement, 1px `Border/subtle` (`strokeBottomWeight`, les 3 autres côtés à 0).

- **Select-cell** (`Selectable=True` uniquement) : frame 44×44 centrée, contient une instance exposée `Checkbox` (`Show-label=false`) — juste la case, sans label.
- **Cells** : frame horizontale hug, contient les instances `Cell` de la ligne (autant que de colonnes). Pas de Slot Figma scriptable ici (contrairement à `Cell` elle-même) — `component.createSlot()` ne s'attache qu'à un `COMPONENT`, pas à une frame interne, et un Slot au niveau du composant `Row` se serait positionné hors de la frame `Cells` plutôt que de remplacer son contenu. Composition manuelle : dupliquer l'instance `Row` et remplacer le contenu de `Cells` par les instances `Cell` voulues, comme pour `Body`/`Footer` sur `Card`.

### États et couleurs

- **Default** : fond transparent.
- **Hover** : fond `Action/ghost-hover`.
- **Selected** : fond `Action/secondary-active`. Le `Checkbox` de `Select-cell` passe en `Checked=True`.
- **Disabled** : fond transparent (pas de surbrillance), **toute la ligne à `opacity: 48%`** — plutôt qu'un remap token-par-token des `Cell` internes (`Cell` ne porte pas ses propres états, voir `components/cell/`, donc `Row` ne peut pas réécrire leurs bindings de couleur individuellement sans détacher chaque instance). L'opacité réduite atténue uniformément le texte, les icônes et le `Checkbox` sans casser la composition. Le `Checkbox` de `Select-cell` passe en `Interaction=Disabled`. Ligne non cliquable, non sélectionnable.

## Table (assemblage)

Pas de composant unique paramétrique : une instance `Header-row` (assemblage manuel — `Select-cell` avec `Checkbox` en `Checked=Indeterminate` si sélection partielle / `True` si tout est sélectionné / `False` sinon, puis une instance `Header-cell` par colonne) suivie d'instances `Row`, le tout dans une frame conteneur (`Background/elevated`, bordure `Border/subtle`, `Radius/card`, `clipsContent: true` pour que la bordure basse de la dernière ligne ne dépasse pas).

Exemple construit sur la page `↳ Table` : `Header-row` (checkbox indéterminée + colonne "Colonne" triée `Asc` + colonne "Colonne" non triable alignée à droite) + 3 `Row` (`Default`, `Hover`, `Selected`), toutes `Selectable=True`.

### Tri (comportement)

Au clic sur un `Header-cell` triable : ce `Header-cell` passe à l'état de tri suivant (`None→Asc→Desc→None`), **tous les autres `Header-cell` triables du tableau repassent à `Sort=None`** — un seul critère de tri actif à la fois (pas de tri multi-colonnes dans cette première version).

### Sélection (comportement)

- Checkbox de `Select-cell` sur une `Row` : bascule cette ligne seule entre `Default`/`Selected` (ou `Hover`/`Selected` si survolée).
- Checkbox de `Select-cell` sur `Header-row` (« tout sélectionner ») : `Checked=False` → sélectionne toutes les lignes non-`Disabled` ; `Checked=True` ou `Indeterminate` → désélectionne tout. `Indeterminate` = état visuel uniquement quand une sélection partielle existe (au moins une ligne sélectionnée, pas toutes) ; ne se clique pas vers un état "indéterminé", c'est un état dérivé, jamais choisi directement par l'utilisateur.
- Une ligne `Disabled` ignore les clics sur sa checkbox et n'est jamais comptée dans le « tout sélectionner ».

## Accessibilité

- `Header-cell` triable : `<th>` avec un bouton/contrôle de tri au clavier (`Enter`/`Space`), `aria-sort="none"|"ascending"|"descending"` sur le `<th>`.
- `Row` sélectionnable : la checkbox de chaque ligne a un nom accessible explicite (ex. « Sélectionner la ligne <valeur clé> »), jamais un simple « Sélectionner ». Checkbox d'en-tête : « Tout sélectionner », `aria-checked="mixed"` pour l'état indéterminé.
- `Row` en `Disabled` : `aria-disabled="true"` sur la ligne, checkbox native `disabled`.
- Navigation clavier : `Tab` déplace le focus de checkbox en checkbox / cellule interactive en cellule interactive (pas cellule par cellule sur du contenu non interactif), cohérent avec la lecture d'un tableau de données standard.

## Guidelines Figma

Page dédiée `↳ Table`, avec `Header-cell`, `Row` et un exemple d'assemblage `Table (example)`. `Cell` reste sur sa propre page `↳ Cell` — brique partagée, potentiellement réutilisable hors `Table` à l'avenir.
