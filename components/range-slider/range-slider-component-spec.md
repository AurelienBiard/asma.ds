# Composant Range Slider

Sélecteur de valeur continue ou de plage.

## Propriétés

`Type` = `Single` (une valeur, un thumb) / `Range` (un intervalle, deux thumbs) × `Interaction` = `Default`/`Hover`/`Focus`/`Disabled`, 8 variantes.

## Anatomie

`Track` (200×4, `Border/strong`), `Fill` coloré (`Action/primary`) entre le(s) thumb(s), `Thumb(s)` en ellipse 16×16 (`Background/elevated` + contour `Action/primary`, épaissi en Focus). Pas de propriété texte (valeur portée par la position du thumb).

## Usage

Stepper pour une quantité entière à paliers clairs. Range Slider pour une valeur perçue comme continue (prix, pourcentage, luminosité) où un geste de glissement est plus naturel qu'un nombre tapé.

Doc complète : guidelines Figma page `↳ Numeric inputs`.
