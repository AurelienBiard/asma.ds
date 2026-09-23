# Composant Tag

Étiquette compacte, **toujours pleine** (jamais outlined — réservé à Chip), pleinement arrondie (pilule, `Radius/pill`).

## Propriétés

- `Type` (variant) : `Neutral`/`Brand`/`Info`/`Success`/`Warning`/`Danger`. Neutral/Brand en fond plein (`Action/neutral`/`Action/primary`) ; les 4 statuts en fond teinté (`Feedback/{statut}/background`, sans bordure).
- `Size` (variant) : `Large`/`Medium`/`Small` (renommé depuis Medium/Small/Xsmall). Padding/gap en tokens `Spacing/component-md-xs-2xs` selon la taille ; Text Style `Body/SM` (Large), `Misc/Label` (Medium), `Body/XS` (Small). Gap le plus fin (Medium/Small) : **2px littéral**, aucun token n'existe à ce palier.
- `Label` (Text).
- `Show-icon-leading`/`Show-icon-trailing` (Boolean, défaut `true` tous les deux) : icônes indépendantes, instances directes du wrapper `Icon` (même montage que Button), colorées identiquement au texte.

18 variantes (`Type` × `Size`).

## Correction de contraste (impact système)

Les fonds Feedback (Info/Success/Warning/Danger) utilisaient l'extrémité de l'échelle Tailwind (grade `50` Light / `950` Dark) — insuffisamment détachés de la page. Corrigés d'un cran de profondeur (`100`/`900`). **Ce token étant partagé**, la correction s'applique aussi à Tooltip, TextInput/PasswordInput/Search/Textarea/Code-OTP/PIN (validation), Alert, Toast.

## Leçons de construction

- La coloration d'icône peut échouer silencieusement même en suivant la méthode standard si le mauvais ID de vecteur est utilisé pour le pictogramme swappé — toujours vérifier la couleur réellement appliquée (comparer icône vs texte via `.overrides`), pas seulement l'absence d'erreur.
- `Radius/pill` : variable dédiée (existe dans le système), ne jamais utiliser une valeur littérale 999 à la place.

## Guidelines Figma

Page `↳ Tag`, section "Guidelines" partagée avec Chip — voir le "Pattern" en tête de page qui distingue **Tag** (étiquette d'affichage passive) de **Chip** (élément interactif) : ce n'est pas une différence de style (plein vs contour) mais d'**usage**.
