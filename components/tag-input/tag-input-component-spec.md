# Composant TagInput

Champ de saisie à valeurs multiples. Interaction × Content × Validation, 32 variantes — même famille que TextInput/Search.

## Anatomie

- `Field` : `layoutWrap: WRAP` (retour à la ligne si plusieurs valeurs), hauteur **minimale** 40px (pas figée — grandit si le contenu wrap sur plusieurs lignes). `clipsContent: false` sur le composant externe (bug de bordure Focus coupée sinon, même cause que sur les autres Input).
- Valeurs saisies = **vraies instances de Chip** (`Type=Neutral`, `Size=Small`, icône trailing `X`) — jamais des Tag (voir spec Chip pour la distinction Tag/Chip).
- Zone de saisie libre (texte placeholder "Ajouter...") pour ajouter une nouvelle valeur.
- **Clear-all** : icône `X` seule, visible uniquement si `Content=Filled` et non `Disabled`.
- **Status-icon** : icône de validation (WarningCircle/Warning/CheckCircle) en tête de champ, présente sur les 24 variantes avec `Validation≠None`.
- Message d'erreur sous le champ (Body/XS), pour un texte mal renseigné (ex. valeur invalide saisie).

## Propriétés

`Placeholder`, `Message` (Text).

## Guidelines Figma

Section dédiée dans les guidelines génériques de la page `↳ Text inputs`.
