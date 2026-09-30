# Composant Cell

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveau composant, créé le 2026-09-30. Brique atomique du futur composant `Table` (`decisions.yaml` → `Table`, à créer) : une cellule = une colonne × une ligne.

## Propriétés du composant Figma

- **Content** (variant) : `Text` / `Avatar-text` / `Tag` / `Actions` / `Slot`.
- **Align** (variant) : `Left` (défaut) / `Right` — position du contenu dans la largeur de la cellule (`primaryAxisAlignItems`). `Right` réservé aux valeurs numériques et à `Actions` en fin de ligne ; les autres usages restent en `Left`.
- **Content-slot** (propriété Slot Figma, réelle — `component.createSlot()`, confirmé scriptable contrairement à une note obsolète dans `dialog-component-spec.md`) : n'existe que sur `Content=Slot`, pour tout contenu non prévu par les 4 autres valeurs.

10 variantes (5 Content × 2 Align).

## Anatomie commune

Conteneur horizontal, largeur **220px dans le composant** (dans `Table`, la cellule réelle s'étire pour remplir la largeur de sa colonne — comportement d'usage, pas une propriété Figma), hauteur hug. Padding `Spacing/component-sm` (horizontal) / `Spacing/component-xs` (vertical), `itemSpacing: Spacing/component-xs`, alignement vertical centré. Fond transparent — le fond (Default/Hover/Selected/Disabled) est porté par `Row` dans `Table`, jamais par `Cell` elle-même.

## Contenu par valeur de `Content`

- **Text** : un nœud texte, `Body/MD` + `Text/primary`.
- **Avatar-text** : instance `Avatar` (`Type=Initials, Size=Small`) + texte `Body/MD` + `Text/primary`. Réutilise `Avatar` tel quel — aucune nouvelle brique.
- **Tag** : instance `Tag` (`Type=Neutral, Size=Medium` par défaut, changeable par instance).
- **Actions** : instance `Button` (`Type=Ghost`, `Icon-only=true`, `Show-label=false`), icône par défaut `DotsThreeVertical` (déclencheur de menu contextuel — le cas le plus fréquent en fin de ligne de table). Remplaçable par n'importe quelle icône via Swap instance pour une action unique explicite (ex. `Trash`, `PencilSimple`).
- **Slot** : zone libre pour tout contenu non couvert (ex. mini-graphique, contrôle composé, plusieurs boutons).

## Ce que Cell ne fait pas

Pas d'état interactif propre (pas de `Hover`/`Active`/`Disabled`) : Cell est un contenu, pas un déclencheur. Les états (survol de ligne, ligne sélectionnée, ligne désactivée) sont portés par `Row` dans `Table`, jamais par les cellules qu'elle contient.

## Guidelines Figma

Page dédiée `↳ Cell`, positionnée dans `❖ COMPONENTS` (entre `Card` et `Chip`) — pas dans `💻 PATTERNS` : `figma.createPage()` ajoute toujours en fin de liste, la page a dû être déplacée manuellement après coup (`figma.root.insertChild`), à vérifier systématiquement à la création d'une page. Composée de deux sections : `Cell` (le ComponentSet) et `Guidelines` (texte de référence, ajoutée le 2026-09-30 — structure standard : `Components` en-tête, `H1`, `Body`, `H2` par sujet, bloc `Spec technique … (lecture agent)` final en `JetBrains Mono`, cf. patron déjà en place sur la page `Chip`). Composant `Table` (Header-cell avec tri, Row avec sélection, assemblage) construit — voir `components/table/`.
