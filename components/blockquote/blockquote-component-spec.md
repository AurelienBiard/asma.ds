# Composant Blockquote

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveau composant, créé le 2026-10-08. Citation mise en exergue dans un contenu (propos d'une personne, témoignage, extrait). Composant unique, pas de composition.

## Propriétés du composant Figma

- **Style** (variant) : `Default` / `Accent`.
- **Text** (Text) : la citation.
- **Citation** (Text) : auteur et source, précédés d'un tiret cadratin (« — Nom, source »).
- **Show-citation** (Boolean, défaut `true`) : affiche la ligne de citation.

2 variantes.

## Anatomie

Conteneur vertical, largeur **480px** dans le composant (s'étire à la largeur de son conteneur en usage réel), hauteur hug, sans fond, sans coins arrondis.
- **Barre** : trait de **4px** sur le bord gauche uniquement (`strokeLeftWeight` 4, autres côtés 0, alignement intérieur). `Border/strong` en `Default`, `Action/primary` en `Accent`.
- **Padding** : gauche `Spacing/component-md`, haut et bas `Spacing/component-xs`, droite 0. Gap `Spacing/component-xs`.
- **Text** : `Body/LG` + `Text/primary`, `FILL` en largeur. Pas de guillemets ajoutés, pas d'italique : la barre suffit à signaler la citation.
- **Citation** : `Body/SM` + `Text/secondary`, `FILL` en largeur, masquable.

## Variantes

- **Default** : citation courante d'un contenu.
- **Accent** : une citation clé par page ou section. Pas plus d'un `Accent` par vue (règle « un seul accent fort » de `STYLE.md`).

## Comportement

- Non interactif. Si la source est un lien, l'interaction est portée par un `Link` dans la ligne de citation, jamais par le Blockquote.
- Citation de plusieurs paragraphes : plusieurs blocs de texte empilés dans le même Blockquote, une seule barre.
- **Non spécifié à ce jour** : variante à fond (`Background/subtle`), guillemets décoratifs, avatar de l'auteur, grande citation « pull quote » en `Heading`.

## Usage

- Citer une personne, un témoignage, un extrait d'un texte.
- Un message système → `Alert`. Un conteneur de contenu → `Card`. Une aide contextuelle → `Tooltip`.

## Accessibilité

- Balisage : `<figure>` contenant `<blockquote cite="…">` puis `<figcaption>` avec `<cite>` pour la source. Sans citation, `<blockquote>` seul.
- La barre est décorative : aucune alternative textuelle, aucun rôle ARIA.
- Contraste du texte ≥ 4.5:1 sur le fond de la page ; la barre ne porte aucune information qui ne soit pas dans le texte.
- Langue différente du reste de la page : attribut `lang` sur le `<blockquote>`.

## Tokens

`Border/strong`, `Action/primary`, `Text/primary`, `Text/secondary`, `Spacing/component-md`, `Spacing/component-xs`. Text Styles : `Body/LG`, `Body/SM`. Valeurs littérales assumées : largeur 480, barre 4px.

## Guidelines Figma

Page dédiée `↳ Blockquote` dans `❖ COMPONENTS` (entre `Avatar` et `Button`), sections `Blockquote` (2 variantes) et `Guidelines`.
