# Composant Breadcrumb

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, propriétés, tokens) se fait ici en premier, puis est répercutée dans Figma.

> **Statut** : construit dans Figma (page `↳ Breadcrumb`) avant que cette spec n'existe — rédigée le 2026-10-13 à partir d'une relecture de l'état Figma réel, puis corrigée le même jour (Text Style, `Link`, contraste).

Fil d'Ariane : situe la page courante dans la hiérarchie du site et permet de remonter aux niveaux parents (`decisions.yaml` → `Breadcrumb`). Navigation secondaire, placée au-dessus du titre de la page (H1). Composant unique, sans variantes.

## Anatomie

Auto-layout horizontal avec retour à la ligne (voir « Comportement — écran étroit »), gap `Spacing/component-xs`, hauteur 20px par ligne (ligne de `Body/MD`), largeur au contenu (`HUG`). Quatre enfants `Level-1` à `Level-4` (auto-layout horizontal, gap `Spacing/component-xs`), chacun masquable :
- **Level-1** : un `Link`.
- **Level-2**, **Level-3** : `Separator` puis un `Link`.
- **Level-4** (page courante) : `Separator` puis `Label (current)`.

Le **séparateur** « / » (`Body/MD`, `Text/tertiary`) appartient aux niveaux 2 à 4 : masquer un niveau masque aussi son séparateur.

## Propriétés du composant Figma

- **Show-level-1** … **Show-level-4** (Boolean, défaut `true`) : affichage de chaque niveau. Fil à 2 niveaux : `Level-1` + `Level-4` (`Show-level-2` et `Show-level-3` à `false`).
- **Level-4** (Text, défaut « Page courante ») : libellé de la page courante.
- **Level-1** à **Level-3** : instances **exposées** du composant `Link` (`Show-icon-trailing=false`, `State=Default`, largeur `HUG` sur l'instance). Le libellé se modifie via la propriété `Label` de l'instance `Link` ; il n'existe donc **pas** de propriété `Level-1/2/3` sur le Breadcrumb (limite de l'API Figma : une propriété texte parente ne peut pas piloter un `Label` imbriqué).

## Couleurs et typographie

- Niveaux 1 à 3 : `Link` (`Text/link`, souligné, `Body/MD`) — les états `Hover` / `Active` / `Disabled` sont ceux de `Link`.
- Page courante : `Body/MD` + `Text/secondary` (non cliquable). `Text/tertiary` n'est pas utilisé ici : en Dark il tombe à environ 3,75:1 sur `Background/default`, sous les 4,5:1 requis pour du texte de 14px.
- Séparateurs : `Body/MD` + `Text/tertiary` (décoratifs, hors exigence de contraste de texte).

## Usage

- Libellés courts : le nom de la page, pas son titre complet. Pas de fil d'Ariane sur la page d'accueil. Ne remplace pas la navigation principale.
- 4 niveaux maximum : au-delà, revoir l'architecture de l'information plutôt que d'ajouter un niveau. Le nombre de niveaux est fixé par des booléens (et non par un assemblage manuel comme `Table` ou `Timeline`) précisément parce que la profondeur est plafonnée.
- Un seul `Level-4` : la page courante est toujours le dernier niveau affiché.

## Comportement — écran étroit (2026-10-13)

- **Retour à la ligne** : le composant est en `layoutWrap = WRAP`, espacement entre lignes `Spacing/component-2xs` (`counterAxisSpacing`). Par défaut il reste sur une ligne (largeur au contenu). Dans une mise en page étroite (< 768px), l'**instance est placée en `FILL` en largeur** dans son conteneur : les niveaux passent alors à la ligne. Aucune information n'est masquée ni scrollée horizontalement.
- **Un niveau ne se coupe jamais** : séparateur « / » + lien forment une unité. Conséquence connue : un séparateur peut se retrouver en début de ligne.
- **Page courante (`Level-4`)** : `FILL` en largeur, largeur minimale 160px (valeur littérale assumée), libellé sur **une ligne** avec ellipse (`textTruncation = ENDING`, `maxLines = 1`). Elle passe à la ligne avant de se tronquer et c'est elle qui se tronque en premier ; les liens restent entiers. Dans le DOM, le texte complet reste présent (`title` ou `aria-label`).
- En code : conteneur `flex-wrap: wrap` ; niveaux `white-space: nowrap` ; page courante `min-width: 160px; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap`.
- **Non retenu à ce jour** : réduction des niveaux intermédiaires (« … » ouvrant un `Menu`), à envisager si des fils de 5 niveaux ou plus devaient être autorisés (le plafond est de 4).
- Exemple : `Exemple — Mobile, intitulés longs` (frame 360px, page Figma).

## Accessibilité

- `<nav aria-label="Fil d'Ariane">` contenant une liste ordonnée `<ol>`, un `<li>` par niveau.
- Page courante : `aria-current="page"`, non cliquable.
- Séparateurs décoratifs (`aria-hidden`, ou générés en CSS).
- Liens : comportement et focus de `Link` (soulignés, anneau de focus du DS).

## Tokens

`Text/link`, `Text/secondary`, `Text/tertiary`, `Spacing/component-xs`, `Spacing/component-2xs`. Text Style : `Body/MD`.

## Guidelines Figma

Page dédiée `↳ Breadcrumb` dans `❖ COMPONENTS` (entre `Blockquote` et `Button`), sections `Breadcrumb` (composant), `Exemples` (deux en-têtes de page : fil à 4 niveaux « Accueil / Projets / Design systems / asma.ds » et fil à 2 niveaux « Accueil / Contact », chacun au-dessus d'un titre `Heading/LG` et d'un paragraphe `Body/MD`) et `Guidelines`.
