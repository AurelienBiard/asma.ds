# Composants Dropzone, Image Upload, Color Picker

Trois composants groupés sur la page `↳ File & media` (pas de raison structurelle de les séparer — voir décision explicite : contrairement à Tag/Chip, ils ne partagent ni anatomie ni pattern à documenter ensemble, mais le regroupement par catégorie de la roadmap est conservé volontairement).

## Dropzone

`State` = `Default`/`Hover`/`Dragging`/`Error`/`Disabled`, 5 variantes. Bordure en pointillés (`dashPattern`), épaissie et colorée (`Border/focus`) + fond `Action/ghost-hover` en `Dragging`. `Error` utilise les tokens `Feedback/Danger`. Propriété texte `Title` (le sous-titre disparaît en `Dragging`, remplacé par "Déposez pour importer").

## Image Upload

`State` = `Empty`/`Filled`/`Hover`/`Disabled`, 4 variantes. `Empty` = pointillés + icône `Image`. `Filled` simule une image (fond `Action/neutral` — à remplacer par un vrai remplissage en usage réel). `Hover` = voile sombre 50% + icône `Upload` en `Icon/inverse`. Carré 96×96, `Radius/control` (pour un avatar rond, appliquer un radius à 50% séparément — voir plutôt le composant **Avatar** dédié pour ce cas précis).

## Color Picker

`Interaction` = `Default`/`Hover`/`Focus`/`Disabled`, 4 variantes. **Déclencheur uniquement** : pastille de couleur (`Swatch`, 20×20, bordure `Border/default`) + valeur hexadécimale (`Misc/Label`). Propriété texte `Hex-value`.

⚠️ Le panneau de sélection (grille de teintes, slider de luminosité, champ hex éditable) **n'est pas construit** dans cette version — à faire si un besoin réel se confirme, sur le modèle du `Select-menu` (assemblage séparé du déclencheur).

Doc complète : guidelines Figma page `↳ File & media`.
