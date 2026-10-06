# Composant Timeline

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveau composant, créé le 2026-10-06, pour un historique d'expérience (parcours professionnel). Brique atomique `Timeline-item` ; la `Timeline` est un assemblage vertical manuel d'instances (nombre d'événements arbitraire, comme `Table`). Pas de composant monolithique.

## Différence avec Step-indicator

`Step-indicator` montre la progression dans un parcours **à accomplir** (formulaire, onboarding), interactif et orienté vers l'avenir. `Timeline` expose un historique **de faits datés**, en lecture seule, du plus récent au plus ancien (ou l'inverse, choix unique par liste). Un `Timeline-item` n'a ni numéro, ni état « à venir ». Le `Dot Indicator` (pastille de notification de 8px posée en overlay) n'est pas réutilisé : rôle différent, taille différente.

## Timeline-item

### Propriétés du composant Figma

- **Orientation** (variant) : `Vertical` (défaut) / `Horizontal`.
- **State** (variant) : `Default` / `Current`. `Current` = l'événement en cours (poste actuel).

4 variantes (2 Orientation × 2 State).
- **Period** (Text) : période ou date (« 2023 – Aujourd'hui »).
- **Title** (Text) : intitulé (poste, événement).
- **Subtitle** (Text) : organisation, lieu ou complément (« Studio Lumen · Paris »).
- **Description** (Text) et **Show-description** (Boolean, défaut `true`) : texte libre sous le sous-titre.
- **Show-connector** (Boolean, défaut `true`) : trait vertical vers l'élément suivant. À mettre sur `false` pour le **dernier** élément de la liste.

### Anatomie — Vertical

Conteneur horizontal, largeur 480px dans le composant (s'étire à la largeur de son conteneur), deux enfants :
- **Rail** (vertical, largeur 16px, `FILL` en hauteur, alignement centré) : `Marker` puis `Connector`. `Marker` : cercle 12×12, `Radius/pill`, bordure 2px, décalé de 2px du haut pour s'aligner sur la première ligne de texte. `Connector` : trait 2px de large, `FILL` en hauteur, `Border/default`, masquable.
- **Content** (vertical, `FILL`, gap `Spacing/component-2xs`, padding bas `Spacing/component-lg` — espace entre deux éléments) : `Period` (`Misc/Caption` + `Text/tertiary`), `Title` (`Misc/Label` + `Text/primary`), `Subtitle` (`Body/MD` + `Text/secondary`), `Description` (`Body/MD` + `Text/secondary`, masquable).
- Gap horizontal Rail/Content : `Spacing/component-sm`.

### Anatomie — Horizontal

Conteneur **vertical**, largeur **240px** par élément (`FIXED`), gap `Spacing/component-sm`, deux enfants :
- **Rail** (horizontal, `FILL` en largeur, hauteur 12px, alignement centré, gap 4px) : `Marker` (même cercle 12×12) puis `Connector` (trait de 2px de haut, `FILL` en largeur, `Border/default`, masquable). Le connecteur relie le marqueur au suivant ; masqué sur le dernier élément.
- **Content** (vertical, `FILL`, gap `Spacing/component-2xs`, padding **droit** `Spacing/component-lg` — espace entre deux éléments) : mêmes `Period`, `Title`, `Subtitle`, `Description` que la version verticale.

À réserver à **3 à 5 étapes** qui tiennent sur une ligne ; au-delà, passer en `Vertical`. Sur écran étroit, une timeline horizontale doit se replier en verticale (ou défiler horizontalement avec un indicateur) — comportement non spécifié à ce jour.

### États (marqueur)

- **Default** : fond `Background/elevated`, bordure `Border/strong`.
- **Current** : fond et bordure `Action/primary` (cercle plein). Un seul `Current` par liste, normalement en tête.

Le texte garde les mêmes styles dans les deux états : le marqueur seul porte la distinction (pas de gras ni de couleur de texte supplémentaires).

## Timeline (assemblage)

Instances de `Timeline-item` dans une frame auto-layout (gap 0) : **empilées verticalement** pour `Vertical` (rythme vertical = padding bas de `Content`), **alignées horizontalement** pour `Horizontal` (rythme = padding droit de `Content`). Ne jamais mélanger les deux orientations dans une même liste. Le dernier élément a `Show-connector=false`. Un seul sens chronologique par liste ; chaque élément porte sa date, l'ordre n'est jamais implicite.

## Comportement

- Non interactif : pas de `Hover`/`Focus`/`Disabled`. Si un élément doit ouvrir un détail, la cible cliquable est le `Title` (un lien, voir `Link`), pas le marqueur.
- Beaucoup d'éléments : afficher les plus récents puis « Voir plus » (`Button` Ghost) plutôt qu'une liste interminable.
- **Non spécifié à ce jour** : variante alternée gauche/droite (deux côtés du rail), repli responsive de l'horizontale, statuts (succès / erreur — pour un historique d'exécution, voir `Node` `Status`), logo d'organisation, groupement par année, comportement responsive (la version `Vertical` tient dès 320px).

## Usage

- Historique d'expérience, parcours, journal d'activité, historique d'une fiche. Pas pour un parcours à accomplir (→ `Step-indicator`) ni pour des données comparables en colonnes (→ `Table`).
- `Period` toujours renseignée. `Title` court (une ligne), le détail va dans `Description`.
- Les compétences ou technologies associées à un élément : instances de `Tag` (`Neutral`, `Small`) sous la `Description`, sans composant dédié.

## Accessibilité

- Liste ordonnée : `<ol>` / `<li>`, une entrée par `Timeline-item`. Le marqueur et le connecteur sont décoratifs (`aria-hidden`).
- `Period` dans un élément `<time>` avec `datetime` pour les dates précises ; « Aujourd'hui » s'accompagne de l'état `Current` annoncé en texte (« en cours »), jamais seulement par la couleur du marqueur.
- Contraste ≥ 3:1 du marqueur et du connecteur contre le fond ; `Text/tertiary` de `Period` au contraste texte normal (4,5:1) — vérifier sur le fond réel.
- Horizontale : l'ordre de lecture reste celui du DOM (gauche → droite) ; en `dir="rtl"`, le sens visuel s'inverse avec lui.
- Ordre de lecture = ordre visuel ; ne pas inverser par CSS (`flex-direction: column-reverse`) sans inverser le DOM.

## Tokens

`Background/elevated`, `Border/strong`, `Border/default`, `Action/primary`, `Text/primary`, `Text/secondary`, `Text/tertiary`, `Radius/pill`, `Spacing/component-2xs`, `Spacing/component-sm`, `Spacing/component-lg`. Text Styles : `Misc/Caption`, `Misc/Label`, `Body/MD`. Valeurs littérales assumées : largeur 480 (vertical) / 240 (horizontal), `Marker` 12, `Rail` 16 de large (vertical) / 12 de haut (horizontal), `Connector` 2.

## Guidelines Figma

Page dédiée `↳ Timeline` dans `❖ COMPONENTS` (entre `Theme switcher` et `Toast`), sections `Timeline-item` (4 variantes), `Exemple d'historique d'expérience` (une timeline verticale et une horizontale, 4 éléments chacune) et `Guidelines`.
