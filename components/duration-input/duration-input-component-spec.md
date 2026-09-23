# Composant Duration Input

Saisie d'une durée (pas un point dans le temps — voir Calendar). Pattern segmenté HH:MM:SS.

## Duration-segment (atomique)

`Interaction` × `Content` (Default/Hover/Focus/Disabled × Empty/Filled), 8 variantes. Case 48×40, nombre à 2 chiffres centré (`Heading/SM`). Mêmes règles de bordure que TextInput.

## Duration-input (assemblage)

3 instances `Duration-segment` (heures/minutes/secondes) séparées par des deux-points (`Text/tertiary`), chacune surmontée d'un label d'unité (h/min/s, `Body/XS`). La validation globale (ex. minutes > 59) se gère au niveau de l'assemblage, pas du segment individuel — un segment seul n'a pas de notion de `Validation`.

## Usage

Réservé aux durées courtes/moyennes (minuteur, durée de réunion). Pour une durée en une seule unité avec choix libre (ex. "5" + sélecteur "jours/semaines/mois"), préférer TextInput numérique + Select.

Doc complète : guidelines Figma page `↳ Duration Input`.
