# Composant Chip

Étiquette compacte en version **outlined** — fond transparent, jamais de fond plein (rôle réservé à Tag). Même structure que Tag (`Type` × `Size`, icônes, `Label`), sur sa propre page dédiée `↳ Chip`.

## Différence avec Tag

Voir le "Pattern" en tête de la page `↳ Tag` : la distinction n'est **pas** "plein vs contour" mais l'**usage** — Tag = étiquette d'affichage passive (métadonnée, catégorie, lecture seule), Chip = élément **interactif** (filtre actif, sélection, valeur dans un champ multi-valeurs comme TagInput).

## Propriétés

- `Type`/`Size` : identiques à Tag.
- Bordure, texte et icônes dans la couleur du `Type` : `Border/strong` + `Text/primary` pour Neutral (**pas** `Border/default`, jugé trop faible sur fond transparent), `Action/primary` pour Brand, `Feedback/{statut}/border` + `Feedback/{statut}/text` pour les 4 statuts.
- `Show-icon-leading`/`Show-icon-trailing` (Boolean, défaut `true`) — trailing par défaut = `X` (close), pour l'usage "retirable" le plus fréquent.
- Hauteur **identique à Tag** par palier de `Size` (36/24/22px) — corrigée après un écart de 2px dû à un bug connu (`strokeAlign: INSIDE` + hug auto-layout ajoute 2px même en INSIDE, empiriquement confirmé). Compensé par un padding vertical en **valeur littérale** (variable -1px) plutôt qu'en variable liée, en gardant le mode hug dynamique (pas de hauteur figée en `FIXED`).

18 variantes (`Type` × `Size`).

## Usage dans TagInput

Les valeurs saisies dans le composant `TagInput` sont de **vraies instances de Chip** (`Type=Neutral`, `Size=Small`, icône trailing `X`) — jamais des Tag, cohérent avec la distinction ci-dessus (une valeur retirable dans un champ est un élément interactif).

## Guidelines Figma

Page `↳ Chip`, guidelines complètes propres à la page (Anatomie, Variants, Usage, Accessibilité) — distinctes de celles de Tag mais renvoyant au même "Pattern" partagé.
