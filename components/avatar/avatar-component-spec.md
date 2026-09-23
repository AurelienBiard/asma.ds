# Composant Avatar

Représentation visuelle d'un utilisateur/entité, toujours circulaire.

## Propriétés

`Type` = `Image`/`Initials`/`Icon` × `Size` = `Small`(24)/`Medium`(32)/`Large`(40), 9 variantes.
- `Image` : simule une photo (fond `Action/neutral` — à remplacer par un vrai remplissage en usage réel).
- `Initials` : fond `Action/primary` + texte **`Text/on-brand`**, taille de police à 40% de la taille de l'avatar. Propriété texte `Initials`.
- `Icon` : fond `Action/neutral` + pictogramme `User` en `Icon/tertiary` — état par défaut quand ni photo ni nom ne sont disponibles.

## Ordre de repli recommandé

1. Image si téléversée. 2. Initials si un nom est connu (cas le plus fréquent). 3. Icon uniquement en dernier recours.

## Intégration réelle

Utilisé dans le pattern `Topbar` (page `↳ Navigation`) — remplace le placeholder cercle initial par une vraie instance `Type=Initials, Size=Medium`.

Doc complète : guidelines Figma page `↳ Avatar`.
