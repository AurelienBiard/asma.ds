# Canvas-dotted (2026-11-19)

> Ce fichier est la **source de vérité**. Toute modification se fait ici en premier, puis est répercutée dans Figma.

> **Statut** : proposition, sans nouveau token. Les strates `Background/*` sont décrites dans `guidelines/foundations.yaml` → `background`.

Page Figma : `↳ Background` (fondations, après `↳ Elevation`). Composant `Canvas-dotted` (1088×480).

Fond de travail des **surfaces libres** où l'on place, relie et déplace des éléments : graphes de nœuds (`Node`, `Port`, `Edge`), tableaux blancs, éditeurs de workflow. La grille de points donne une échelle et un repère de déplacement sans tracer de lignes qui entreraient en concurrence avec les liens.

## Anatomie

`Canvas-dotted` (fond `Background/subtle`, coins 8 px (= `Radius/card`), contenu rogné) → `Dots` (un seul vecteur : 68 × 30 points).

| Élément | Valeur |
|---|---|
| Fond | `Background/subtle` (Neutral/50 en Light, Neutral/850 en Dark) |
| Points | `Border/subtle`, Ø 2 px, **pas 16 px** (multiple de la grille de placement des nœuds), centrés dans chaque case |
| Contraste points / fond | 1.42:1 (Light), 2.15:1 (Dark) — volontairement discret, points décoratifs |
| Éléments posés dessus | `Background/elevated` + `Border/default` : 4.55:1 (Light) et 3.42:1 (Dark) contre le fond |

Le fond seul ne sépare pas un élément du canvas (`elevated` sur `subtle` : 1.05:1 en Light, 1.11:1 en Dark) : **la bordure est obligatoire**.

Valeurs littérales assumées : Ø 2 px, pas 16 px. Aucun token créé.

## Code

```css
.canvas-dotted {
  background-color: var(--color-background-subtle);
  background-image: radial-gradient(circle, var(--color-border-subtle) 1px, transparent 1px);
  background-size: 16px 16px;
}
@media (forced-colors: active) {
  .canvas-dotted { background-image: none; }
}
```

Le thème sombre passe par `data-theme="dark"` : les deux tokens changent seuls.

## Comportement

- Le motif **suit la vue** : taille de tuile = 16 px × zoom, position = décalage (pan) de la vue.
- Les éléments se **calent sur le pas de 16 px** (magnétisme).
- Non interactif.

## Usage

- Réservé aux surfaces où les éléments se placent librement. **Pas** derrière du contenu de lecture, un formulaire ou une table de données ; **jamais** dans une `Card` ou un `Dialog`.
- Un seul canvas par vue ; il occupe tout l'espace entre les barres.
- Éléments posés dessus : surfaces `Background/elevated` avec bordure (`Node`, `Card-item`, `Kanban-card`).
- Une zone de contenu ordinaire garde `Background/default`.

## Accessibilité

- Le motif est **décoratif** : CSS uniquement, aucun élément DOM, aucune information portée par les points.
- Contraste élevé (`forced-colors`) : pas de points.
- Le déplacement d'un élément a une alternative clavier (flèches = un pas de 16 px) — cohérent avec la spec `Node`.

## Figma

Instance du composant `Canvas-dotted` ; pour couvrir plus grand, placer plusieurs instances côte à côte (les points sont dessinés, pas un remplissage répété). Les démonstrations Light et Dark de la page `↳ Background` montrent 4 `Node` (dont un `Selected`) sur le canvas.
