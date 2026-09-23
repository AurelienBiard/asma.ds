# Composant Skeleton

Placeholder de chargement, à la même taille/forme que le contenu final — évite le layout shift.

## Propriétés

`Shape` = `Text` (ligne, 160×12, radius 4) / `Circle` (avatar, 40×40, radius plein) / `Rectangle` (image/bloc, 160×90, radius control), 3 variantes. Fond `Background/disabled` (réutilisé, pas de token dédié créé).

## Usage

Composer plusieurs instances pour reconstituer la structure d'une carte/ligne de liste avant chargement. Toujours prévoir une animation de pulsation/shimmer en code — un Skeleton statique se lit comme une erreur de rendu.

Doc complète : guidelines Figma page `↳ Skeleton`.
