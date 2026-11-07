# Composant Chip

Étiquette compacte en version **outlined** — fond transparent par défaut, jamais de fond plein au repos (rôle réservé à Tag). Même structure que Tag (`Type` × `Size`, icônes, `Label`), sur sa propre page dédiée `↳ Chip`.

## Différence avec Tag

Voir le "Pattern" en tête de la page `↳ Tag` : la distinction n'est **pas** "plein vs contour" mais l'**usage** — Tag = étiquette d'affichage passive (métadonnée, catégorie, lecture seule), Chip = élément **interactif** (filtre actif, sélection, valeur dans un champ multi-valeurs comme TagInput).

## Propriétés

- `Type` (variant) : **`Neutral` / `Brand` / `Info` / `Success` / `Warning` / `Danger`**, alignés sur ceux de `Tag` (réintroduits le 2026-11-07 ; les 4 statuts avaient été retirés le 2026-09-28). Neutral/Brand restent le choix par défaut d'un filtre ou d'une sélection ; les statuts servent quand le critère filtré porte lui-même un statut (ex. filtre « En erreur », « Avertissements »). Ils ne remplacent jamais `Alert`/`Toast` pour signaler un état.
- `Size` (variant) : `Large`/`Medium`/`Small`. Text Style par `Size` — **`Small` → `Body/SM`, `Medium` → `Body/MD`, `Large` → `Body/LG`** (même correction que Tag, appliquée en même temps le 2026-09-25).
- `State` (variant, ajouté le 2026-09-28) : `Default` / `Hover` / `Active` / `Disabled` — voir "États" ci-dessous.
- Bordure, texte et icônes dans la couleur du `Type` en `Default` : `Border/strong` + `Text/primary` pour Neutral (**pas** `Border/default`, jugé trop faible sur fond transparent), `Action/primary` pour Brand ; pour les 4 statuts, bordure `Feedback/{statut}/border`, texte **et icônes** `Feedback/{statut}/text` (même règle que `Tag` : icône de la couleur du texte — `Feedback/*/icon` est sous 3:1 pour Warning sur fond clair une fois posé sur un fond teinté ou survolé).
- `Show-icon-leading`/`Show-icon-trailing` (Boolean, défaut `true`) — trailing par défaut = `X` (close), pour l'usage "retirable" le plus fréquent.
- Hauteur **identique à Tag** par palier de `Size` (36/24/22px) — corrigée après un écart de 2px dû à un bug connu (`strokeAlign: INSIDE` + hug auto-layout ajoute 2px même en INSIDE, empiriquement confirmé). Compensé par un padding vertical en **valeur littérale** (variable -1px) plutôt qu'en variable liée, en gardant le mode hug dynamique (pas de hauteur figée en `FIXED`).

72 variantes (6 `Type` × 3 `Size` × 4 `State`).

## États (ajouté le 2026-09-28)

Manquaient jusqu'ici alors que Chip est défini comme interactif ; définis pour couvrir le survol et la sélection (ex. filtre actif).

- **Default** : voir "Propriétés" — outlined, fond transparent, bordure/texte/icône colorés par `Type`.
- **Hover** (tous les `Type`, statuts compris) : même traitement que `Segment` en `Selected=False` — bordure/texte/icône **inchangés**, ajout d'un fond `Action/ghost-hover` derrière le Chip (toujours outlined, pas de remplissage coloré). Aucun nouveau token requis.
- **Active** (sélectionné — filtre actif, valeur validée) : le Chip **se remplit** plutôt que de simplement s'assombrir — bordure retirée, fond passe à une couleur pleine du `Type`, texte/icône ajustés en conséquence :
  - **Neutral** : fond `Background/inverse` (noir plein en Light / blanc plein en Dark), texte `Text/inverse`, icône `Icon/inverse` — corrigé deux fois le 2026-09-28 (`Action/neutral` puis `Action/neutral-active` jugés pas assez prononcés, retour explicite du produit : « je veux du noir sur l'active »).
  - **Brand** : fond `Action/primary`, texte `Text/on-brand`, icône `Icon/on-brand`.
  - **Info / Success / Warning / Danger** (2026-11-07) : fond `Feedback/{statut}/background` (teinte, comme `Tag`), **bordure retirée**, texte et icônes `Feedback/{statut}/text`. Pas de fond plein : le texte blanc sur les couleurs `Feedback/*/border` n'atteint pas 4,5:1 pour Info, Success et Warning.
- **Disabled** : `Background/disabled` + `Text/disabled` + `Icon/disabled` + `Border/disabled`, pour tous les `Type` — même choix que Button (reconnaissance immédiate et cohérente prime sur la préservation de la couleur du Type ; ne pas "corriger" ce comportement).

## Contrastes des statuts (2026-11-07)

Texte `Feedback/{statut}/text` — Light : sur la page 5,36 (Info), 5,02 (Success), 7,09 (Warning), 6,47 (Danger) ; sur le fond Hover (`Action/ghost-hover`) 4,58 à 6,47 ; sur le fond Active 4,57 à 6,37. Dark : 9,41 à 12,71 sur la page, 5,28 à 6,49 sur le fond Active. Bordure en `Default`/`Hover` : 3,19:1 (Warning) à 4,83:1 (Danger) en Light, au-dessus de 3:1 dans tous les cas. Les `Active` des statuts mesurent 2 px de moins que leurs `Default` (pas de bordure), comme `Neutral` et `Brand` jusqu'ici.

## Leçon de construction (2026-10-05)

Les variantes `Hover`, `Active` et `Disabled` ajoutées le 2026-09-28 n'avaient pas leurs propriétés de composant branchées : `Label`, `Show-icon-leading` et `Show-icon-trailing` n'avaient aucun effet sur les instances de ces états (le libellé restait « Chip »). Corrigé sur les 18 variantes concernées (`componentPropertyReferences`). À vérifier systématiquement à l'ajout d'un nouvel axe de variantes : les références de propriétés ne se copient pas toutes seules.

## Usage dans TagInput

Les valeurs saisies dans le composant `TagInput` sont de **vraies instances de Chip** (`Type=Neutral`, `Size=Small`, icône trailing `X`) — jamais des Tag, cohérent avec la distinction ci-dessus (une valeur retirable dans un champ est un élément interactif). Ces instances utilisent l'état `Default` (pas `Active`) : leur seule présence dans le champ constitue déjà le signal de sélection, l'état `Active` du Chip reste réservé à l'usage "filtre".

## Guidelines Figma

Page `↳ Chip`, guidelines complètes propres à la page (Anatomie, Variants, Usage, Accessibilité) — distinctes de celles de Tag mais renvoyant au même "Pattern" partagé.
