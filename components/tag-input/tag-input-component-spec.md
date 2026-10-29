# Composant TagInput

Champ de saisie à valeurs multiples. Interaction × Content × Validation, 32 variantes — même famille que TextInput/Search.

## Anatomie

- `Field` : `layoutWrap: WRAP` (retour à la ligne si plusieurs valeurs), hauteur **minimale 44px** (depuis le 2026-10-29 ; 40px auparavant), alignée sur la hauteur réelle des autres champs (TextInput, Select, Search) dans Figma. Pas figée : grandit si les Chips passent sur plusieurs lignes. Contenu centré verticalement. `clipsContent: false` sur le composant externe (bug de bordure Focus coupée sinon, même cause que sur les autres Input).
- Padding du Field : `Spacing/component-xs` (haut, bas, gauche) ; à droite **32px** (8 + 16 d'icône + 8) pour réserver la place de Clear-all : les Chips et la saisie ne passent jamais sous l'icône.
- Valeurs saisies = **vraies instances de Chip** (`Type=Neutral`, `Size=Small`, icône trailing `X`) — jamais des Tag (voir spec Chip pour la distinction Tag/Chip).
- Zone de saisie libre (texte placeholder "Ajouter...") pour ajouter une nouvelle valeur.
- **Clear-all** : icône `X` seule, **en position absolue, ancrée à droite et centrée verticalement** (contraintes droite / centre), donc toujours au bord droit quel que soit le nombre de Chips. Visible uniquement si `Content=Filled` et non `Disabled`.
- **Status-icon** : icône de validation (WarningCircle/Warning/CheckCircle) en tête de champ, présente sur les 24 variantes avec `Validation≠None`.
- Message d'erreur sous le champ (Body/XS), pour un texte mal renseigné (ex. valeur invalide saisie).

## Propriétés

`Placeholder`, `Message` (Text).

## Comportement : autocomplétion et création

Le TagInput s'utilise avec une **liste de suggestions** qui permet de retrouver une valeur existante ou d'en créer une nouvelle sans quitter le formulaire.

- **Ouverture** : au focus (suggestions = valeurs les plus utilisées, valeurs déjà appliquées exclues) et à chaque saisie. **Fermeture** : Échap, clic extérieur, Tab.
- **Autocomplétion** : filtrage dès le premier caractère, insensible à la casse et aux accents. La première correspondance est l'option active. 8 suggestions au maximum.
- **Création** : l'option « Créer « … » » est la dernière de la liste, après un séparateur, et n'apparaît que si aucune valeur ne porte exactement ce nom après normalisation (casse, accents, espaces superflus). Quand rien ne correspond, la liste affiche « Aucun … « saisie » » puis l'option de création, active par défaut. La valeur est créée avec son seul nom, aussitôt appliquée ; ses attributs secondaires (couleur, description) se complètent plus tard.
- **Doublon** : une saisie qui correspond à une valeur existante (ex. « sante » → « Santé ») propose cette valeur, sans option de création.
- **Valeur ajoutée** : elle devient un Chip retirable (×), la saisie est vidée et le champ reste actif pour enchaîner.
- **Garde-fou métier (optionnel)** : le produit peut signaler qu'une saisie relève d'un autre champ, par un message d'information (`Feedback/Info`) en tête de liste. La création reste possible en dernier recours. Exemple ASMA OS : « Client » est un type de relation, pas un tag.
- Le tri des suggestions par fréquence d'usage et le garde-fou métier sont des comportements proposés par le produit, pas imposés par le composant.

## Clavier

- ↑ ↓ : parcourir la liste.
- Entrée : ajouter l'option active (ou créer la valeur).
- Retour arrière dans une saisie vide : retirer le dernier Chip.
- Échap : fermer la liste sans effacer la saisie.

## Liste de suggestions

Pas encore de composant Listbox dédié : composition de `Select-option` (sans checkbox, radio ni switch ; icône `Plus` en `Icon/brand` pour l'option de création) dans un conteneur `Background/elevated`, bordure `Border/subtle`, `Radius/control`, padding `Spacing/component-2xs`. Libellé de groupe en `Misc/Caption` / `Text/tertiary`, message « aucun résultat » en `Body/SM` / `Text/secondary`, séparateur 1px `Border/subtle`. La liste est placée 4px sous le champ, au-dessus du contenu suivant : elle ne décale pas la mise en page.

**À valider** : niveau d'élévation de la liste (proposition : `Elevation/2`, niveau « overlay » de la fondation Elevation).

## Accessibilité

- Champ : `role="combobox"`, `aria-expanded`, `aria-activedescendant` sur l'option active.
- Liste : `role="listbox"`, options `role="option"` ; l'option de création est annoncée « Créer … ».
- Chaque Chip est un bouton nommé « Retirer … ».

## Guidelines Figma

Bloc « TagInput » dans les guidelines génériques de la page `↳ Text inputs`. Référence visuelle : section « TagInput — comportement (autocomplétion & création) » sur la même page (8 états + règles de comportement).

## À valider

- La spec TextInput indique une hauteur de Field de 40px, alors que TextInput, Select et Search mesurent 44px dans Figma (padding vertical `Spacing/component-sm`). TagInput a été aligné sur la mesure réelle (44px) ; la spec TextInput est à corriger dans un sens ou dans l'autre.
