# Composant Image

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveau composant, créé le 2026-10-06. Brique de base pour vignettes, galeries et listes de logos (SVG ou bitmap) — un futur pattern de liste de logos s'appuiera dessus. Composant unique, pas de composition.

## Propriétés du composant Figma

- **Ratio** (variant) : `Square` (1:1) / `Landscape` (4:3) / `Wide` (16:9).
- **State** (variant) : `Default` / `Loading` / `Error`.
- **Caption** (Text) et **Show-caption** (Boolean, défaut `false`) : légende sous l'image.

9 variantes (3 Ratio × 3 State).

## Anatomie

Conteneur vertical, largeur **240px** dans le composant (s'étire à la largeur de son conteneur en usage réel), gap `Spacing/component-xs`, hauteur hug. Deux enfants :
- **Media** : frame auto-layout `FILL` en largeur, hauteur **fixée par `Ratio`** (`Square` 240, `Landscape` 180, `Wide` 135 pour 240 de large), `Radius/card`, `clipsContent: true`, contenu centré. L'image elle-même est le **Fill** du calque `Media` (mode `Fill` ou `Fit`, voir « Cover ou Contain »).
- **Caption** : `Body/SM` + `Text/tertiary`, `FILL` en largeur, masquable.

## États

- **Default** : emplacement avant le remplacement par une image — fond `Background/sunken`, bordure 1px `Border/default`, icône `Image` (instance `Icon`, `Size=Large`, `Icon/tertiary`). Dès qu'une vraie image est posée, remplacer le `Fill` de `Media` et retirer l'icône.
- **Loading** : fond `Background/disabled` (même token que `Skeleton`), sans icône ni bordure. Attente du contenu — en code, un état transitoire sans interaction.
- **Error** : comme `Default` avec l'icône `ImageBroken`. L'image n'a pas pu être chargée ; un lien « Réessayer » (`Button` Ghost) peut être ajouté à côté si le contexte s'y prête.

## Cover ou Contain

- **Cover** (`object-fit: cover`, Figma `Fill`) : l'image remplit `Media` et est rognée. Pour les photos et les vignettes.
- **Contain** (`object-fit: contain`, Figma `Fit`) : l'image est visible en entier avec des marges autour. Pour les **logos**, illustrations et captures — un logo ne doit jamais être étiré ni rogné. Un fond neutre (`Background/default` ou `Background/subtle`) peut être posé sous le `Fill` pour les marges.
- Ce choix est un réglage de `Fill`, pas une propriété du composant (le placeholder ne le montre pas) ; il est tracé ici pour qu'un agent le choisisse selon le contenu.

## Comportement

- Non interactif. Si l'image est cliquable (ouverture d'un agrandissement ou d'un lien), l'interaction est portée par un élément parent (`Link`, `Button`), jamais par `Image` elle-même.
- Chargement progressif : `Loading` → image ; en cas d'échec → `Error`. Réserver l'espace dès le départ (le ratio est fixe) pour éviter tout décalage de mise en page.
- **Non spécifié à ce jour** : ratio libre (`Auto`), coins non arrondis, image en arrière-plan d'une zone de contenu, `srcset` / formats responsive, zoom / lightbox.

## Usage

- Vignettes, galeries, illustrations d'articles ou de cartes, **logos** (en `Contain`).
- Un portrait d'utilisateur → `Avatar`. Un champ de dépôt de fichier → `Image-upload` ou `Dropzone`. Une icône de l'interface → `Icon`.
- Une liste de logos est un **pattern** (composition d'`Image` en `Contain`, `Ratio` homogène dans toute la liste), pas une variante d'`Image`.

## Accessibilité

- Chaque image informative a un texte alternatif (`alt`) qui décrit ce qu'elle apporte ; une image purement décorative a un `alt` vide (`alt=""`). Un logo a pour `alt` le nom de l'organisation.
- Une légende (`Caption`) ne remplace pas l'`alt` : en cas d'équivalence parfaite, l'`alt` peut être vide pour éviter la répétition.
- `Loading` : `aria-busy="true"` sur la région concernée ; `Error` : message d'erreur annoncé (`role="alert"` ou zone `aria-live`), jamais seulement visuel.
- Contraste ≥ 3:1 de l'icône et de la bordure du placeholder contre le fond de page.

## Tokens

`Background/sunken`, `Background/disabled`, `Border/default`, `Icon/tertiary`, `Text/tertiary`, `Radius/card`, `Spacing/component-xs`. Text Style : `Body/SM`. Valeurs littérales assumées : largeur 240, hauteurs 240 / 180 / 135.

## Guidelines Figma

Page dédiée `↳ Image` dans `❖ COMPONENTS` (entre `Icon` et `Label`), sections `Image` (9 variantes) et `Guidelines`.
