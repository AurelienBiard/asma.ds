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
- **Show-logo** (Boolean, défaut `false`) : affiche, tout en haut de `Content` (au-dessus de `Period`), une instance exposée de `Logos` (variante au choix sur l'instance : `Ynov`, `Frinergy`, `CHStudio`, `Innlog`, `OuestFrance`) — logo de l'organisation.
- **Show-tools** (Boolean, défaut `false`) : affiche, sous `Description`, le bloc `Tools` (voir « Outils »). **Show-tool-1** à **Show-tool-5** (Boolean ; 1 et 2 `true`, 3 à 5 `false`) : affichent chaque `Tool-n` individuellement.
- **Show-connector** (Boolean, défaut `true`) : trait vertical vers l'élément suivant. À mettre sur `false` pour le **dernier** élément de la liste.

### Anatomie — Vertical

Conteneur horizontal, largeur 480px dans le composant (s'étire à la largeur de son conteneur), deux enfants :
- **Rail** (vertical, largeur 16px, `FILL` en hauteur, alignement centré) : `Marker` puis `Connector`. `Marker` : cercle 12×12, `Radius/pill`, bordure 2px, décalé de 2px du haut pour s'aligner sur la première ligne de texte. `Connector` : trait 2px de large, `FILL` en hauteur, `Border/default`, masquable.
- **Content** (vertical, `FILL`, gap `Spacing/component-2xs`, padding bas `Spacing/component-lg` — espace entre deux éléments) : `Period` (`Misc/Caption` + `Text/tertiary`), `Title` (`Misc/Label` + `Text/primary`), `Subtitle` (`Body/MD` + `Text/secondary`), `Description` (`Body/MD` + `Text/secondary`, masquable), et, en première position, `Logo` (instance exposée de `Logos`, masquée par défaut, voir ci-dessous).
- Gap horizontal Rail/Content : `Spacing/component-sm`.

### Anatomie — Horizontal

Conteneur **vertical**, largeur **240px** par élément (`FIXED`), gap `Spacing/component-sm`, deux enfants :
- **Rail** (horizontal, `FILL` en largeur, hauteur 12px, alignement centré, gap 4px) : `Marker` (même cercle 12×12) puis `Connector` (trait de 2px de haut, `FILL` en largeur, `Border/default`, masquable). Le connecteur relie le marqueur au suivant ; masqué sur le dernier élément.
- **Content** (vertical, `FILL`, gap `Spacing/component-2xs`, padding **droit** `Spacing/component-lg` — espace entre deux éléments) : mêmes `Period`, `Title`, `Subtitle`, `Description` que la version verticale.

À réserver à **3 à 5 étapes** qui tiennent sur une ligne ; au-delà, passer en `Vertical`. Sur écran étroit, une timeline horizontale doit se replier en verticale (ou défiler horizontalement avec un indicateur) — comportement non spécifié à ce jour.

### Outils

Dernier enfant de `Content`, sous `Description` : bloc **`Tools`** (auto-layout horizontal, `layoutWrap = WRAP`, gap et `counterAxisSpacing` `Spacing/component-xs`, `FILL` en largeur), **visible = `Show-tools`** (`false` par défaut). Il contient `Tool-1` à `Tool-5`, instances exposées de `Tag` (`Type=Neutral`, `Size=Medium`, sans icônes), libellé modifiable depuis l'instance ; même mécanique que le pattern `Skill`. Même emplacement dans les 4 variantes. `Show-tools` est nécessaire en plus des `Show-tool-n` : un bloc dont tous les enfants sont masqués garde sa hauteur dans Figma.

### Logo

Premier enfant de `Content`, au-dessus de `Period` : instance exposée du composant `Logos` (page Figma `↳ Logos`, section Foundation ; 40×40 ; variante par défaut `OuestFrance`), **visible = `Show-logo`** (`false` par défaut), même emplacement dans les 4 variantes ; gap `Spacing/component-2xs` avec `Period`. `alt` = nom de l'organisation (voir `Image`).

Limites connues : le `Marker` du `Rail` reste calé en haut (à hauteur du logo quand il est affiché, non de `Period`) ; la propriété de variante de `Logos` s'appelle encore `Property 1` dans Figma (non renommée).

### États (marqueur)

- **Default** : fond `Background/elevated`, bordure `Border/strong`.
- **Current** : fond et bordure `Action/primary` (cercle plein). Un seul `Current` par liste, normalement en tête ; avec le suivi du scroll, c'est l'élément actif qui le porte (voir « Suivi du scroll »).

Le texte garde les mêmes styles dans les deux états : le marqueur seul porte la distinction (pas de gras ni de couleur de texte supplémentaires).

### États (connecteur)

- **Vide** : `Border/subtle`.
- **Rempli** : `Action/primary`, sur toute la longueur du connecteur.
- **En remplissage** (comportement, voir « Suivi du scroll ») : la partie remplie est `Action/primary`, le reste `Border/subtle`, de haut en bas (vertical) ou de gauche à droite (horizontal). Dans Figma, seuls Vide et Rempli existent ; le remplissage partiel est un comportement code.

Le connecteur d'un élément relie son marqueur au suivant : il est donc rempli quand l'élément suivant a été atteint.

## Timeline (assemblage)

Instances de `Timeline-item` dans une frame auto-layout (gap 0) : **empilées verticalement** pour `Vertical` (rythme vertical = padding bas de `Content`), **alignées horizontalement** pour `Horizontal` (rythme = padding droit de `Content`). Ne jamais mélanger les deux orientations dans une même liste. Le dernier élément a `Show-connector=false`. Un seul sens chronologique par liste ; chaque élément porte sa date, l'ordre n'est jamais implicite.

## Comportement

- Non interactif : pas de `Hover`/`Focus`/`Disabled`. Si un élément doit ouvrir un détail, la cible cliquable est le `Title` (un lien, voir `Link`), pas le marqueur.
- Beaucoup d'éléments : afficher les plus récents puis « Voir plus » (`Button` Ghost) plutôt qu'une liste interminable.
- **Suivi du scroll** : voir ci-dessous. Comportement par défaut de toute `Timeline` verticale dans une page qui défile ; désactivable pour une liste courte entièrement visible.
- **Non spécifié à ce jour** : variante alternée gauche/droite (deux côtés du rail), repli responsive de l'horizontale, statuts (succès / erreur — pour un historique d'exécution, voir `Node` `Status`), logo d'organisation, groupement par année, comportement responsive (la version `Vertical` tient dès 320px).

### Suivi du scroll (scroll-spy)

Prototype validé le 2026-10-21. À appliquer à toute `Timeline` de plus d'un écran.

- **Ligne de repère** : ligne horizontale imaginaire, fixe dans la fenêtre, à **36 % de la hauteur de la fenêtre** (décision du 2026-10-21 : valeur fixe, et non plus calée sur le premier marqueur, la `Timeline` n'étant pas toujours en haut de page). Elle ne bouge pas quand on défile ; ce sont les éléments qui la traversent. Elle est invisible en production.
- **Élément actif** : le dernier élément dont le centre du marqueur est au-dessus ou sur la ligne de repère. Tant qu'aucun marqueur n'a atteint la ligne (liste plus bas dans la page), aucun élément n'est actif. Un seul élément actif à la fois ; au bas de la liste, c'est le dernier. L'actif prend le rendu de marqueur `Current` (fond et bordure `Action/primary`).
- **Marqueurs passés** : les éléments au-dessus de l'actif gardent un fond `Background/elevated` et une bordure `Action/primary` (anneau), pour garder la trace du chemin parcouru. Les éléments en dessous de l'actif restent `Default`.
- **Connecteur, remplissage continu** : le connecteur de chaque élément se remplit en `Action/primary` à mesure que la ligne de repère le parcourt, du haut vers le bas, proportionnellement à sa hauteur. Il est vide tant que la ligne n'a pas atteint son marqueur, plein une fois qu'elle l'a dépassé. **Un connecteur passé reste plein** ; il ne redevient vide qu'en remontant. Le connecteur du dernier élément reste masqué.
- **Horizontale** : même logique sur l'axe horizontal (scroll horizontal du conteneur), non prototypée.
- **Transitions** : le remplissage suit le scroll sans animation propre (aucun délai). Les changements d'état du marqueur (`Default` ↔ `Current`) durent `motion-duration-scale-sm` (240ms) avec `motion-easing-scale-standard`. `prefers-reduced-motion` : plus de transition de marqueur, le remplissage reste (il est lié au scroll, pas à l'animation).
- **Clic ou Entrée** sur un élément : fait défiler la page pour amener son marqueur sur la ligne de repère.
- **Réglage** : position de la ligne en % de la hauteur de la fenêtre (36 % par défaut). Ne la déplacer que pour tenir compte d'une barre fixe en haut de page.
- **Current et élément actif** (décision du 2026-10-21) : dans une `Timeline` avec suivi du scroll, seul l'élément actif porte le rendu `Current`. Aucun autre élément n'est marqué « en cours » (`State=Current` statique), sauf demande expresse ; l'information « en cours » reste portée par le texte de `Period` (« 2025 – Aujourd'hui »). Pas d'état `Active` distinct.

Hors de ce comportement, la `Timeline` reste en lecture seule (voir ci-dessus) : le suivi du scroll n'ajoute ni état Hover ni Focus au marqueur.

#### Points à valider

- Anneau des marqueurs passés : choix par défaut, non encore reporté dans Figma.
- Connecteur coloré en `Action/primary` : aucun token dédié créé.

## Usage

- Historique d'expérience, parcours, journal d'activité, historique d'une fiche. Pas pour un parcours à accomplir (→ `Step-indicator`) ni pour des données comparables en colonnes (→ `Table`).
- `Period` toujours renseignée. `Title` court (une ligne), le détail va dans `Description`.
- Les compétences ou technologies associées à un élément : instances de `Tag` (`Neutral`, `Small`) sous la `Description`, sans composant dédié.

## Accessibilité

- Suivi du scroll : l'élément actif porte `aria-current="true"` (mis à jour sans annonce vocale : pas de `aria-live`) ; le remplissage du connecteur et l'anneau des marqueurs passés sont décoratifs. Le contraste du connecteur rempli (`Action/primary`) et vide (`Border/subtle`) doit rester ≥ 3:1 contre le fond.
- Liste ordonnée : `<ol>` / `<li>`, une entrée par `Timeline-item`. Le marqueur et le connecteur sont décoratifs (`aria-hidden`).
- `Period` dans un élément `<time>` avec `datetime` pour les dates précises ; « Aujourd'hui » s'accompagne de l'état `Current` annoncé en texte (« en cours »), jamais seulement par la couleur du marqueur.
- Contraste ≥ 3:1 du marqueur et du connecteur contre le fond ; `Text/tertiary` de `Period` au contraste texte normal (4,5:1) — vérifier sur le fond réel.
- Horizontale : l'ordre de lecture reste celui du DOM (gauche → droite) ; en `dir="rtl"`, le sens visuel s'inverse avec lui.
- Ordre de lecture = ordre visuel ; ne pas inverser par CSS (`flex-direction: column-reverse`) sans inverser le DOM.

## Tokens

`Background/elevated`, `Border/strong`, `Border/default`, `Action/primary`, `Text/primary`, `Text/secondary`, `Text/tertiary`, `Radius/pill`, `Spacing/component-2xs`, `Spacing/component-sm`, `Spacing/component-lg`. Text Styles : `Misc/Caption`, `Misc/Label`, `Body/MD`. Valeurs littérales assumées : largeur 480 (vertical) / 240 (horizontal), `Marker` 12, `Rail` 16 de large (vertical) / 12 de haut (horizontal), `Connector` 2.

## Guidelines Figma

Page dédiée `↳ Timeline` dans `❖ COMPONENTS` (entre `Theme switcher` et `Toast`), sections `Timeline-item` (4 variantes), `Exemple d'historique d'expérience` (une timeline verticale et une horizontale, 4 éléments chacune) et `Guidelines`.
