# Pattern Skill

> **Statut** : nouveau pattern, créé le 2026-10-14, construit dans Figma (page `↳ Skill`, section `💻 PATTERNS`). Issu des sections « Cartographie de compétences » et « Outils & technologies » de la page `About / Desktop` (Portfolio). Contrairement à `Filter bar`, c'est un **ComponentSet** (une ligne a un contenu borné) ; les choix marqués « par défaut » sont à valider.

## Purpose

Exprimer une compétence ou un domaine de pratique sur une ligne réutilisable : libellé, note (score, niveau, barre de progression), outils et technologies, rôle dans la pratique. Un seul composant couvre les deux sections de la page À propos.

## Use when

- Cartographie de compétences : libellé + niveau (Tag) + barre de progression.
- Tableau « Outils & technologies » : domaine + outils (Tag) + description.
- Les deux combinés dans une même ligne (note + outils + description).

## Do not use when

- Données comparables en colonnes → `Table`.
- Plus de 5 outils → liste de `Tag` séparée.
- Historique daté → `Timeline`. Progression d'une opération → `Progress`.

## Components

- `Tag` (`components/tag/`) — `Level` : `Type=Brand|Info|Neutral`, `Size=Small` ; `Tool-1..5` : `Type=Neutral`, `Size=Medium`, sans icônes.
- `Progress-linear` (`components/progress/`) — `State=Determinate`, `Percentage` 40/60/80/100, label de pourcentage masqué, largeur adaptable.

## Structure

ComponentSet `Skill`, propriété de variante **`Device` = `Desktop` (540px) | `Mobile` (328px)**. Racine : auto-layout vertical, padding `Spacing/component-md`, `itemSpacing` `Spacing/component-xs`, bordure basse 1px `Border/subtle`, fond transparent, `FILL` en largeur dans son conteneur (même style que la `Row` de « Outils & technologies »).

Enfants, dans l'ordre :
1. **Header** — Desktop : horizontal, centré, gap `Spacing/component-md`. Mobile : horizontal (ligne), centré, gap `Spacing/component-md` — comme Desktop ; `Label` en `FILL`, **tronqué sur une ligne** (`textTruncation = ENDING`, `maxLines = 1`, ellipse), `Note` en `HUG` à droite.
   - **Label** : `Misc/Label`, `Text/primary`, `FILL`.
   - **Progress** (Desktop seulement, entre `Label` et `Note`) : instance exposée de `Progress-linear`, 120px de large fixe.
   - **Note** : horizontal, centré, gap `Spacing/component-sm`, **`minWidth` 150px** (valeur littérale assumée) : **Score** (`Heading/SM`, `Text/primary`) puis **Level** (instance exposée de `Tag`).
2. **Progress** (Mobile seulement) : instance exposée de `Progress-linear`, `FILL`, sous le `Header`. Sur Desktop elle est dans le `Header` (voir ci-dessus).
3. **Tools** : horizontal, `layoutWrap = WRAP`, gap et `counterAxisSpacing` `Spacing/component-xs`. `Tool-1` à `Tool-5` : instances exposées de `Tag`.
4. **Description** : `Body/MD`, `Text/primary`, `FILL`.

## Propriétés du composant Figma

- **Device** (variant) : `Desktop` (défaut) / `Mobile`. 2 variantes.
- **Label** (Text, défaut « Design produit »), **Score** (Text, « 5 »), **Description** (Text).
- **Show-score**, **Show-level**, **Show-progress**, **Show-description**, **Show-tools** (Boolean, tous `true` par défaut), **Show-tool-1** à **Show-tool-5** (Boolean ; 1 et 2 `true`, les autres `false`).
- Instances exposées (`isExposedInstance`) : **Level** (`Type`, libellé), **Progress** (`Percentage`), **Tool-1..5** (libellé). Elles se modifient dans le panneau de l'instance, sans Swap manuel.

`Show-tools` est nécessaire en plus des `Show-tool-n` : un bloc dont tous les enfants sont masqués garde sa hauteur dans Figma.

## La note

Score + Level + Progress, activés indépendamment. Échelle de la cartographie :

| Score | Niveau | `Level` | `Percentage` |
|---|---|---|---|
| 5 | Expertise centrale | `Type=Brand` | 100 |
| 4 | Compétence forte | `Type=Info` | 80 |
| 3 | Compétence appliquée | `Type=Neutral` | 60 |
| 2 | Culture / exposition | `Type=Neutral` | 40 (par défaut, non utilisé à ce jour) |

Le `Tag` redit toujours le niveau en texte : l'information ne repose ni sur la couleur ni sur la longueur de la barre.

## Compositions types

- **Cartographie** : `Show-level` + `Show-progress` ; `Show-score`, `Show-tools`, `Show-description` à `false`.
- **Outils & technologies** : `Show-tools` + `Show-description` ; `Show-score`, `Show-level`, `Show-progress` à `false`.
- **Complète** : tout activé (exemple sur la page Figma).

Une liste est un empilement d'instances sans espace entre elles (la bordure basse sert de séparateur) ; `Spacing/section-*` uniquement autour de la liste.

## Responsive

`Device=Desktop` pour les mises en page larges (ligne de 540px), `Device=Mobile` en dessous de 768px (ligne de 328px, libellé tronqué pour garder la note à droite). Desktop : la barre est dans l'en-tête, entre libellé et note. Mobile : la barre s'étire sous l'en-tête. Dans les deux variantes les outils passent à la ligne et la description s'étire.

## Accessibility

- Liste de lignes : `<ul>` / `<li>`. Les outils forment une liste (`<ul>`) de `Tag` non interactifs.
- La note est annoncée en texte (« Expertise centrale, 5 sur 5 ») ; la barre `Progress` est décorative (`aria-hidden`) puisque le `Tag` porte le niveau.
- Contrastes portés par les composants `Tag` et `Progress`.

## Tokens

`Spacing/component-md`, `Spacing/component-xs`, `Spacing/component-sm`, `Spacing/component-2xs`, `Border/subtle`, `Text/primary`. Text Styles : `Misc/Label`, `Heading/SM`, `Body/MD`. Largeurs 540 / 328, `Progress` 120 (Desktop) et `minWidth` de `Note` 150 littérales assumées. Aucun token nouveau.

## Related

`Tag`, `Progress`, `Table`, `Timeline`, pattern `Filter bar` (même logique d'assemblage manuel pour les listes).
