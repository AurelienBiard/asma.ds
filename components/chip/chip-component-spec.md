# Composant Chip

Étiquette compacte en version **outlined** — fond transparent par défaut, jamais de fond plein au repos (rôle réservé à Tag). Même structure que Tag (`Type` × `Size`, icônes, `Label`), sur sa propre page dédiée `↳ Chip`.

## Différence avec Tag

Voir le "Pattern" en tête de la page `↳ Tag` : la distinction n'est **pas** "plein vs contour" mais l'**usage** — Tag = étiquette d'affichage passive (métadonnée, catégorie, lecture seule), Chip = élément **interactif** (filtre actif, sélection, valeur dans un champ multi-valeurs comme TagInput).

## Propriétés

- `Type` (variant) : **`Neutral` / `Brand` uniquement** (restreint le 2026-09-28 — les 4 statuts Feedback ont été retirés de Chip : un filtre/sélection actif n'a pas besoin de sémantique de statut, contrairement à Tag qui les garde).
- `Size` (variant) : `Large`/`Medium`/`Small`. Text Style par `Size` — **`Small` → `Body/SM`, `Medium` → `Body/MD`, `Large` → `Body/LG`** (même correction que Tag, appliquée en même temps le 2026-09-25).
- `State` (variant, ajouté le 2026-09-28) : `Default` / `Hover` / `Active` / `Disabled` — voir "États" ci-dessous.
- Bordure, texte et icônes dans la couleur du `Type` en `Default` : `Border/strong` + `Text/primary` pour Neutral (**pas** `Border/default`, jugé trop faible sur fond transparent), `Action/primary` pour Brand.
- `Show-icon-leading`/`Show-icon-trailing` (Boolean, défaut `true`) — trailing par défaut = `X` (close), pour l'usage "retirable" le plus fréquent.
- Hauteur **identique à Tag** par palier de `Size` (36/24/22px) — corrigée après un écart de 2px dû à un bug connu (`strokeAlign: INSIDE` + hug auto-layout ajoute 2px même en INSIDE, empiriquement confirmé). Compensé par un padding vertical en **valeur littérale** (variable -1px) plutôt qu'en variable liée, en gardant le mode hug dynamique (pas de hauteur figée en `FIXED`).

24 variantes (`Type` × `Size` × `State`).

## États (ajouté le 2026-09-28)

Manquaient jusqu'ici alors que Chip est défini comme interactif ; définis pour couvrir le survol et la sélection (ex. filtre actif).

- **Default** : voir "Propriétés" — outlined, fond transparent, bordure/texte/icône colorés par `Type`.
- **Hover** : même traitement que `Segment` en `Selected=False` — bordure/texte/icône **inchangés**, ajout d'un fond `Action/ghost-hover` derrière le Chip (toujours outlined, pas de remplissage coloré). Aucun nouveau token requis.
- **Active** (sélectionné — filtre actif, valeur validée) : le Chip **se remplit** plutôt que de simplement s'assombrir — bordure retirée, fond passe à une couleur pleine du `Type`, texte/icône ajustés en conséquence :
  - **Neutral** : fond `Action/neutral-active` (**pas** `Action/neutral`, corrigé le 2026-09-28 — trop proche du fond de page, pas assez prononcé pour signaler un état sélectionné), texte `Text/primary`, icône `Icon/primary`.
  - **Brand** : fond `Action/primary`, texte `Text/on-brand`, icône `Icon/on-brand`.
  - **Survol d'un Chip Active** : comportement, pas une variante distincte — légère intensification du fond (`Action/neutral-hover` pour Neutral — à un cran de plus que `Action/neutral-active` —, `Action/primary-hover` pour Brand), comme la progression d'intensité déjà utilisée sur Button.
- **Disabled** : `Background/disabled` + `Text/disabled` + `Icon/disabled` + `Border/disabled`, pour les deux `Type` — même choix que Button (reconnaissance immédiate et cohérente prime sur la préservation de la couleur du Type ; ne pas "corriger" ce comportement).

## Usage dans TagInput

Les valeurs saisies dans le composant `TagInput` sont de **vraies instances de Chip** (`Type=Neutral`, `Size=Small`, icône trailing `X`) — jamais des Tag, cohérent avec la distinction ci-dessus (une valeur retirable dans un champ est un élément interactif). Ces instances utilisent l'état `Default` (pas `Active`) : leur seule présence dans le champ constitue déjà le signal de sélection, l'état `Active` du Chip reste réservé à l'usage "filtre".

## Guidelines Figma

Page `↳ Chip`, guidelines complètes propres à la page (Anatomie, Variants, Usage, Accessibilité) — distinctes de celles de Tag mais renvoyant au même "Pattern" partagé.
