# Changelog

## 2026-10-28 (4) — Heading/LG : line-height 32

- `Typography/heading-lg/Line-Height` passe de 40 (`6xl`) à 32 (`5xl`) en Mobile et Desktop (Figma, `tokens/responsive.json`, `dist/tokens.css`, `foundations.yaml`, `design-system-ai-guidelines.yaml`). Le Text Style `Heading/LG` suit (28/32 en Mobile, 32/32 en Desktop). Aucun nouveau token.
- **À noter** : en Desktop, taille et interligne sont égaux (32/32) ; à vérifier sur les titres de 2 lignes.

## 2026-10-28 (3) — DA : pictogrammes et logos remplacent les doodles (STYLE.md)

- `STYLE.md` mis à jour d'après la page Figma `↳ Logos` et la cover : nouveau §6 « Pictogrammes et logos » (`picto` 80×80, 8 variantes : 3 marques `concatenation` / `asma-ds` / `asma-os` + 5 pôles ; tuile `Feedback/Info/background`, glyphe `Icon/primary`, coins `Radius/card` ; lockups `logo / concatenation`, `logo / asma-ds`, `logo / asma-os` = `picto` 32 + wordmark vectoriel, gap 8).
- Cover (§7) : grille de 8 `picto` 160×160 pivotée de 5° à la place des deux bandes de doodles (conservées dans le fichier, masquées). Bloc titre inchangé.
- Doodles passés en historique (§6 bis) ; la dalle cyan littérale (`#cffafe` / `#18fefe`) n'est plus une règle : la tuile des pictogrammes est liée à une variable.
- §1, §2, §8 et §9 alignés ; §10 signale que `Cover/preview.html` (entête de l'artefact) reproduit encore l'ancienne DA.
- **À valider** : sort des doodles (supprimer ou archiver), renommage de la propriété `Property 1` de `picto`, marges de protection des logos.

## 2026-10-28 (2) — Élévation plus douce (valeurs de Frame 225)

- Les 5 Effect Styles `Elevation/1` à `5` passent de deux ombres avec étalement négatif à **une seule ombre douce, sans étalement**, toutes colorées par `Shadow/subtle` : 1 → `0 5 10`, 2 → `0 10 25`, 3 → `0 20 50`, 4 → `0 32 70`, 5 → `0 50 100` (x y flou).
- Valeurs reprises de la frame de référence `Frame 225` (flat, overlay, sticky-nav, dialog) pour les niveaux 1, 2, 3 et 5 ; le niveau 4 (Drawer) est calculé entre les niveaux 3 et 5. Le niveau 4 est la seule valeur non dessinée.
- `Shadow/strong` n'est plus utilisé par les niveaux (conservé pour l'instant). La couleur d'ombre reste `Color/Neutral/950` à 10 % (Light) / 35 % (Dark), pas le `#141414` de la référence.
- Mis à jour : page Figma `↳ Elevation` (textes et tableau), `foundations.yaml` (`elevation`).

## 2026-10-28 — KPI : nouveau composant, minicourbe et chargement

- Nouveau composant `KPI` (page Figma `↳ KPI`), construit à partir du design de l'utilisateur (frames `KPI / Desktop` et `KPI / Mobile` converties en ComponentSet) : `Icon` Small + `Label`, `Value` en `Display/SM`, `Tag` Small pour la variation et `Caption`.
- 12 variantes : `Device` (Desktop 280 px / Mobile 160 px, grille 2 colonnes d'un écran 360) × `Trend` (Neutral / Positive / Negative = `Type` du Tag Neutral / Success / Danger + flèche ; jugement, pas direction) × `State` (Default / Loading). `Device` fixe le mode Responsive.
- **Minicourbe** : nouveau sous-composant `Sparkline` (variant `Trend`), présenté en pastille (fond `Background/subtle`, radius `Radius/card`, padding `Spacing/component-sm`, tracé 72 × 32 en `Border/medium` coloré `Feedback/Success/icon` / `Feedback/Danger/icon` / `Icon/secondary`), propriété `Show-chart` (défaut `false`). À droite de la valeur en Desktop (96 × 56), sous la valeur en Mobile (pleine largeur × 56). Décorative ; tracé Figma indicatif, vraies données en code.
- **Chargement** : `State=Loading` remplace chaque élément par une instance `Skeleton` (Circle / Text / Rectangle) aux hauteurs exactes de l'état Default (aucun décalage). `Trend` sans effet dans cet état.
- Microcopy française conservée dans les défauts et les exemples : `+8,2 %`, `−3,1 %`, `0,0 %`.
- Propriétés : `Label`, `Value`, `Caption` (Text), `Show-icon` / `Show-delta` / `Show-caption` / `Show-chart` (Boolean), instances exposées `Icon` (Instance-swap) et `Tag`.
- Spec `components/kpi/kpi-component-spec.md` ; entrée `KPI` dans `decisions.yaml`. Aucun token créé. Exemples Desktop, Mobile et Chargement sur la page Figma.
- Contrastes du trait de la minicourbe sur `Background/subtle` (Light / Dark) : Success 3,15 / 9,34, Danger 4,62 / 5,88, Neutral 7,24 / 6,34 — tous ≥ 3:1.
- **À valider** : forme du tracé placeholder.

## 2026-10-27 (4) — Icônes : graisse Light par défaut

- Convention : les icônes d'interface (Phosphor, `Format=Outline`) utilisent **`Weight=Light`** par défaut (avant : Regular). Mis à jour dans `foundations.yaml` (`icons.weight`), le guide IA et les specs Icon, Button, Theme switcher et Pagination.
- Figma : toutes les instances `Weight=Regular` passées en `Weight=Light` (composants, patterns, Userflow, Prototypes, Dossier de compétences, Portfolio) via la propriété Instance-swap du wrapper `Icon` ; défaut du composant `Icon` = `Acorn` Light ; glyphes Checkbox, PasswordInput et Line migrés directement. Couleurs liées aux variables conservées.
- Inchangés : 32 icônes `Weight=Thin` et 2 `Fill` déjà présentes dans Dossier de compétences / Portfolio.

## 2026-10-27 (3) — Voile (scrim) : token Shadow/scrim et règle (proposition)

- **1 nouveau token Semantic** `Shadow/scrim` : Light → `Color/Shadow/35` (35 %), Dark → `Color/Shadow/60` (60 %). Aucune nouvelle Primitive. `--color-shadow-scrim`. Portée Figma : remplissages (frame / forme), pas un Effect Style.
- Règle (`foundations.yaml` → `elevation.scrim`) : voile uniquement derrière les overlays modaux bloquants (niveaux 4–5 : Drawer modal, Dialog, Command) ; aucun voile pour les niveaux 1–3 ; ordre contenu < voile < overlay ; un seul voile à la fois ; clic sur le voile ou Échap ferme sauf overlay bloquant ; contenu sous le voile inerte ; voile décoratif (`aria-hidden`) ; apparition en opacité avec les tokens Motion existants.
- Page Figma `↳ Elevation` : aperçus Light / Dark du voile sous un Dialog (niveau 5).
- **À valider** : opacités 35 % (Light) / 60 % (Dark), Drawer toujours modal ou non.

## 2026-10-27 (2) — Elevation : 5 niveaux et tokens Shadow (proposition)

- Page Figma `↳ Elevation` (Foundation) : 5 Effect Styles `Elevation/1` à `Elevation/5` (deux ombres chacun) et aperçus Light / Dark. Niveaux : 1 Raised (Card), 2 Floating (Popover, Menu, Select, Tooltip), 3 Overlay (Toast), 4 Panel (Drawer), 5 Modal (Dialog, Command).
- **4 nouvelles Primitive** `Color/Shadow/10`, `/20`, `/35`, `/60` = `Color/Neutral/950` (`#020617`) à N % d'opacité (hex à 8 chiffres : `#0206171a`, `#02061733`, `#02061759`, `#02061799`). Dérogation assumée à l'échelle 50–950 : le palier est le pourcentage d'opacité.
- **2 nouveaux tokens Semantic** : `Shadow/subtle` (Light → `Color/Shadow/10`, Dark → `/35` ; niveaux 1–2) et `Shadow/strong` (Light → `/20`, Dark → `/60` ; niveaux 3–5). Portée Figma `EFFECT_COLOR`. CSS : `--color-shadow-subtle`, `--color-shadow-strong` (`dist/tokens.css` régénéré). Nouveau groupe `Shadow` dans `foundations.yaml` (`semantic_roles`) et section `elevation`.
- Les Effect Styles sont liés aux tokens ; le niveau est porté par le décalage, le flou et l'étalement (niveaux 3–5 resserrés pour compenser l'opacité unique).
- **À valider** : rattachement des composants aux niveaux, surfaces Dark par niveau, scrim des overlays. Aucun composant n'utilise encore ces styles.

## 2026-10-21 (2) — Tag Neutral : nouveau token Background/strong

- Nouveau token Semantic **`Background/strong`** : Light → Neutral/200 (`#e2e8f0`), Dark → Neutral/700 (`#334155`). `--color-background-strong` dans `dist/tokens.css` (régénéré).
- `Tag` `Type=Neutral` : fond `Action/neutral` → `Background/strong` (contre la page : 1,10 → 1,23:1 Light, 1,22 → 1,72:1 Dark ; texte `Text/primary` 14,5:1 / 9,9:1). Statuts et Brand inchangés. Spec Tag, `foundations.yaml`, `design-system-ai-guidelines.yaml` et `DESIGN.md` mis à jour.

## 2026-10-21 — Timeline : suivi du scroll

- `Timeline` : nouveau comportement documenté (section « Suivi du scroll » + « États (connecteur) » dans `timeline-component-spec.md`). Ligne de repère fixe à 36 % de la hauteur de la fenêtre (décision du 2026-10-21, plus calée sur le premier marqueur), actif = dernier marqueur au-dessus de la ligne (aucun actif tant qu'aucun n'a atteint la ligne), connecteur rempli en continu en `Action/primary` et reste plein une fois passé, anneau sur les marqueurs passés. Seul l'élément actif porte le rendu `Current` (pas d'état `Active` distinct). Aucun changement Figma ni token.

## 2026-10-15 (3) — Skill Desktop : Progress dans le header

- `Skill` `Device=Desktop` : `Progress` déplacée dans le `Header`, entre `Label` et `Note` (120px fixe) ; `Label` tronqué. Mobile inchangé (barre sous le header). `Note` : `minWidth` 150px (Desktop et Mobile). Spec et guidelines Figma mises à jour.

## 2026-10-15 (2) — Skill Mobile : libellé tronqué

- `Skill` `Device=Mobile` : `Header` en ligne (flex row, comme Desktop), `Label` en `FILL` tronqué sur une ligne (ellipse), `Note` à droite. Spec `skill-pattern-spec.md` et guidelines Figma mises à jour.

## 2026-10-15 — Border/subtle : contraste rehaussé

- `Border/subtle` Light : Neutral/100 → **Neutral/300** (`#cbd5e1`) — 1.48:1 sur `default`, 1.42:1 sur `subtle` (auparavant 1.1:1 et 1.05:1, presque invisible). Neutral/200 écarté : identique à `Border/disabled`.
- `Border/subtle` Dark : Neutral/700 → **Neutral/600** (`#475569`) — 2.36:1 sur `default`, 2.15:1 sur `subtle`, 1.93:1 sur `elevated` (auparavant 1.72, 1.57, 1.41).
- Reste en dessous de `Border/default` (Neutral/500). Appliqué dans Figma (variable Semantic), `tokens/semantic.json` et `dist/tokens.css` régénéré. Affecte tout ce qui utilise `Border/subtle` (Table, Skill, séparateurs…).

## 2026-10-14 (2) — Timeline-item : outils (Show-tools)

- `Timeline-item` : bloc `Tools` sous `Description` (booléen `Show-tools`, `false` par défaut) avec `Tool-1..5` (`Tag` Neutral Medium, exposés, `Show-tool-1..5`), comme sur le pattern `Skill`. 4 variantes. Spec `timeline-component-spec.md` mise à jour.

## 2026-10-14 — Pattern Skill (ComponentSet Mobile/Desktop)

- Nouveau **pattern `Skill`** (page Figma `↳ Skill`, section `💻 PATTERNS`) : ligne de compétence couvrant les sections « Cartographie de compétences » et « Outils & technologies » de `About / Desktop`, au style de la Row « Outils & technologies » (vertical, bordure basse `Border/subtle`).
- ComponentSet `Device=Desktop|Mobile` ; propriétés `Label`, `Score`, `Description` (Text), `Show-score`, `Show-level`, `Show-progress`, `Show-description`, `Show-tools`, `Show-tool-1..5` (Boolean) ; instances exposées `Level` (Tag), `Progress` (Progress-linear), `Tool-1..5` (Tag). La note = Score + Level + Progress.
- Spec `patterns/skill/skill-pattern-spec.md`, entrée `Skill` dans `decisions.yaml`, ligne dans `patterns/README.md`. Aucun token nouveau. Page Figma : sections Skill, Exemples (cartographie, outils, complète, mobile) et Guidelines.
- Non fait : remplacement des lignes existantes de la page Portfolio par des instances de `Skill`.

## 2026-10-13 (5) — Entête de l'artefact alignée sur la cover

- Entête (`Cover/preview.html`) de l'artefact asma.ds redessinée d'après la cover Figma (`STYLE.md` §7). Nouvelle section `STYLE.md` §10 qui la décrit. Aucun token modifié.

## 2026-10-13 (4) — Breadcrumb : spec, correctifs et entrée dans le repo

- **Breadcrumb** (composant déjà construit dans Figma, page `↳ Breadcrumb`) : spec `components/breadcrumb/breadcrumb-component-spec.md`, entrée `Breadcrumb` dans `decisions.yaml`, ligne dans le README.
- **Correctifs Figma** : Text Style `Body/MD` appliqué (texte sans style auparavant : JetBrains Mono 12 en capitales) ; niveaux 1 à 3 = instances exposées de `Link` (les propriétés `Level-1/2/3` sont supprimées, le libellé se modifie sur l'instance) ; page courante en `Text/secondary` au lieu de `Text/tertiary` (contraste Dark d'environ 3,75:1 insuffisant) ; mention « page Portfolio — APropos et Asma.ds » retirée des guidelines.
- Section d'exemples `Exemples` ajoutée sur la page Figma `↳ Breadcrumb` (fil à 4 niveaux et fil à 2 niveaux au-dessus d'un titre de page).
- **Comportement écran étroit** : `layoutWrap = WRAP` (gap de lignes `component-2xs`), instance en `FILL` dans son conteneur ; `Level-4` en `FILL`, min. 160px, une ligne avec ellipse. Exemple `Exemple — Mobile, intitulés longs` (frame 360px) : le fil passe sur 3 lignes, la page courante reste visible. Aucun nouveau token ; réduction « … » des niveaux intermédiaires non retenue.

## 2026-10-13 (3) — Toast et Menu-item : espacements hors échelle liés aux tokens

- **Toast** : padding vertical 10px → `Spacing/component-sm` (12px), identique au padding horizontal. Hauteur 42 → 46px (4 variantes).
- **Menu-item** : `Indent=True`, padding gauche 32px → `Spacing/component-xl` (32px en Desktop, **24px en Mobile**). Le canvas Figma, en mode Mobile par défaut, affiche donc 24px (largeur 172 → 164px) ; ajuster si l'alignement sur 32px doit rester fixe.
- Reste en attente (catégorie B de l'audit du 2026-10-13) : 2px, 3/7/11/12px, 6px, 10px de Line.

## 2026-10-13 (2) — Figma : liaison des paddings et gaps aux tokens Spacing

- **Audit** des 36 pages de composants (paddings et gaps des auto-layouts). 273 valeurs non liées ou liées à une bibliothèque externe sont désormais liées aux variables locales : 4px → `Spacing/component-2xs`, 8px → `component-xs`, 12px → `component-sm`, 16px → `component-md`. Aucune valeur ni taille de composant modifiée (vérifié par comparaison avant/après sur chaque composant).
- Pages touchées : Calendar, Card, Command, Duration Input, Line (+ copie dans Tooltip, qui était liée à des variables d'une autre bibliothèque), Menu, Node (Port), Pagination, Selection inputs (Segmented-control), Step Indicator, Table (Header-cell), Text inputs (gaps), Timeline (gap du Rail), Tooltip.
- **Restent en dur, volontairement** (décision en attente) : 2px (gaps Card/Tag/Chip, padding du Rail de Timeline-item), 3 / 7 / 11 / 12px (paddings verticaux de Chip et des champs de saisie : probable compensation de la bordure de 1px), 6px/2px (Shortcut-badge de Command), 10px (Line, Toast), 32px (indentation du Menu-item) ; gaps de −1px de Popover/Tooltip (chevauchement voulu de la flèche).
- Non audités : page Icon, Patterns, frames d'exemple, radius et bordures.

## 2026-10-13 — Règle de choix des spacings

- **DESIGN.md** : ajout de la règle `component-*` (dans un composant) vs `section-*` (entre blocs de page), avec les chevauchements de valeurs et les assemblages manuels.
- **design-system-ai-guidelines.yaml** : `component-2xs` (4px, existant dans `tokens/responsive.json`) ajouté aux rôles responsive ; règles de choix ajoutées. Aucun token créé ni modifié.

## 2026-10-12 (3) — Progress Linear : largeur adaptable

- **Progress Linear** : le `Fill` suit désormais la largeur de l'instance (contrainte `SCALE`, `Track` sans auto-layout, `Fill` à x=0) dans les 12 variantes ; avant, sa largeur était figée en pixels (instance étirée = barre fausse). Aucun nouveau token.
- Page Figma `↳ Dossier de compétences` : les 16 instances nommées `Skill-level` (instances de `Progress-linear`) passent en `FILL` en largeur dans leur ligne.

## 2026-10-12 (2) — Timeline-item : logo

- **Timeline-item** : ajout de `Show-logo` (Boolean, défaut `false`) et d'une instance exposée de `Logos` en première position de `Content`, au-dessus de `Period` (4 variantes). Remplace le `Slot` puis le `Skeleton` essayés plus tôt le même jour (retirés). Aucun nouveau token.
- Non ajusté : alignement du `Marker` quand le logo est affiché ; propriété de variante `Property 1` de `Logos` non renommée. Le composant `Logos` (page `↳ Logos`) n'a pas encore de spec dans le repo.

## 2026-10-12 — Nouveau composant Lang switcher

- **Lang switcher** (nouveau) : basé sur `Theme switcher`, pictogrammes remplacés par des codes de langue ISO 639-1 (`FR` / `EN`) en `Body/XS` (Inter 10px). Propriétés `Lang` FR/EN × `Motion` Static/Tension × `State` Default/Hover/Disabled (12 variantes). Track 52×28, cellules 20×20 (comme Theme switcher). Réaction `CHANGE_TO` uniquement (pas de `SET_VARIABLE_MODE`). Page Figma `↳ Lang switcher` + Guidelines. Aucun nouveau token.
- **decisions.yaml** : ajout de `LangSwitcher` à `component_selection`.
- **Correctif Hover/Disabled** (Lang switcher et Theme switcher) : le contour 1px était rogné (Track 1px plus grande que le composant). `strokesIncludedInLayout = false`, Track de la taille du composant dans tous les états ; Track 52×28 pour les deux.
- Choix à confirmer : codes de langue (pas de pays), 2 langues seulement.

## 2026-10-08 — Nouveau composant Blockquote

- **Blockquote** (nouveau) : `Style` `Default` / `Accent` (2 variantes) ; propriétés `Text`, `Citation`, `Show-citation`. Barre de 4px à gauche (`Border/strong` / `Action/primary`), texte `Body/LG`, citation `Body/SM`. Page Figma `↳ Blockquote` (entre `Avatar` et `Button`) + Guidelines. Aucun nouveau token.
- **decisions.yaml** : ajout de `Blockquote` à `component_selection` ; rattrapage de `Node`, `Timeline` et `Image` (déjà publiés dans l'artefact mais absents du repo).
- Non spécifié : variante à fond, guillemets décoratifs, avatar de l'auteur, « pull quote » en `Heading`.

## 2026-10-07 (3) — Dark : échelle de surfaces Background

- **Primitive** : ajout de `Color/Neutral/850` (`#172033`), cran intermédiaire entre 800 et 900.
- **Semantic (Dark)** : `Background/sunken` → Neutral/950 (`#020617`), `Background/default` → Neutral/900 (`#0f172a`), `Background/subtle` → Neutral/850 (`#172033`, était une valeur littérale égale à 950), `Background/elevated` → Neutral/800 (`#1e293b`). Light inchangé. Avant, `default`, `subtle` et `sunken` étaient identiques en Dark (`#020617`).
- Échelle Dark : plus une surface est élevée, plus elle est claire ; `sunken` reste la plus sombre.
- `Background/disabled` (Dark, Neutral/800) est volontairement identique à `elevated` : collision acceptée. `Text/disabled` y garde 5,71:1.
- `Border/subtle` (Dark) : Neutral/800 → Neutral/700 (`#334155`) — 1,41:1 sur `elevated`, 1,57:1 sur `subtle`, 1,72:1 sur `default` (il était invisible sur `elevated`, 1:1). Identique à `Border/disabled` (Dark).
- `Icon/disabled` (Dark) : Neutral/600 → Neutral/500 (`#64748b`) — 3,07:1 sur `disabled` (était 1,93:1). Même valeur que `Icon/tertiary`, comme `Text/disabled` et `Text/tertiary` en Dark.
- `dist/tokens.css` régénéré (`scripts/build_css.py`).

## 2026-10-07 (2) — STYLE.md (identité graphique, cover)

- **STYLE.md** (nouveau, racine) : identité graphique lisible par les agents — principes, couleur, typographie, cadre de page 1920×1080, composants éditoriaux, 5 doodles par pôle, cover, do/don't. Complète `DESIGN.md` ; aucun nouveau token.
- **STYLE.md** : section Cover (bandes de doodles inclinées −12,14°, bloc titre aligné bas-droite) et dalle des doodles (cyan `#cffafe` @20 % + ombres intérieures `#18fefe` @8 %) documentées ; variantes `Doodle` : `Pole=ProductDesign` / `DesignSystem` / `UX/UI` / `Tech` / `IA`.
- Piste mezzotint abandonnée (aucun shader ni cadre de test restant dans le fichier).

## 2026-10-07 — Edge : tracé vertical

- **Edge** : `Shape=Vertical` (droite verticale) ajouté — 16 variantes (4 Shape × 4 State). Les `Handle` de `Port` restant à gauche/droite, un graphe vertical de bout en bout (prises en haut/bas) et les bézier à tangentes verticales ne sont pas spécifiés.

## 2026-10-06 (5) — Timeline horizontale, nouveau composant Image

### Composants
- **Timeline** : ajout de la propriété `Orientation` (`Vertical` / `Horizontal`) × `State` — 4 variantes au lieu de 2. Horizontale : élément de 240px, rail au-dessus du contenu, connecteur qui s'étire jusqu'à l'élément suivant ; à réserver à 3–5 étapes. Exemple Figma avec les deux orientations.
- **Image** (nouveau) : `Ratio` (`Square`/`Landscape`/`Wide`) × `State` (`Default`/`Loading`/`Error`), 9 variantes ; `Caption` + `Show-caption`. L'image est le `Fill` du calque `Media` (`Cover` pour les photos, `Contain` pour les logos). Loading au même token que `Skeleton` (`Background/disabled`). Page Figma `↳ Image` + Guidelines. Aucun nouveau token.
- **decisions.yaml** : ajout de `Image` à `component_selection`.
- Non spécifié : ratio libre, image en arrière-plan, `srcset`, lightbox ; repli responsive de la timeline horizontale. La liste de logos sera un pattern.

## 2026-10-06 (4) — Nouveau composant Timeline

### Composants
- **Timeline** (nouveau) : `Timeline-item` (brique atomique, `State` `Default`/`Current`, 2 variantes ; propriétés `Period`, `Title`, `Subtitle`, `Description`, `Show-description`, `Show-connector`) assemblé en liste verticale manuelle. Marqueur 12px + connecteur 2px (`Rail`), `Content` en `Misc/Caption` / `Misc/Label` / `Body/MD`. Pour un historique de faits datés en lecture seule (parcours professionnel, journal d'activité) — distinct de `Step-indicator` (parcours à accomplir). Aucun nouveau token. Page Figma `↳ Timeline` avec exemple d'historique d'expérience (4 postes) et Guidelines.
- **decisions.yaml** : ajout de `Timeline` à `component_selection`.
- Non spécifié : tracé horizontal ou alterné, statuts, logo d'organisation, groupement par année.

## 2026-10-06 (3) — Edge : tracés droit et descendant

- **Edge** : ajout de la propriété `Shape` (`Curve-up` / `Curve-down` / `Straight`) × `State` — 12 variantes au lieu de 4. Les variantes existantes deviennent `Shape=Curve-up`.

## 2026-10-06 (2) — Node : corrections

- **Node** : `Body` et `Ports` avaient un fond blanc par défaut qui masquait la bordure (côtés et bas) — fonds retirés. `Icon` est de nouveau une instance imbriquée de `Icon` (exposée) au lieu d'un glyphe brut lié à une propriété Instance swap ; propriété `Icon` supprimée. Ajout de `Show-input` / `Show-output` ; `Icon`, `Status-icon`, `Port-input`, `Port-output` exposés.
- **Port** : ajout des booléens `Show-label` et `Show-handle`.
- **Edge** : tirets 10/10 sur tous les états (le tiret 4/4 de `Disabled` est abandonné).

## 2026-10-06 — Nouveaux composants Node, Port, Handle, Edge

### Composants
- **Node** (nouveau) : carte de graphe de nœuds (workflow, pipeline, agents), 240px — `Header` (`Icon`, `Title`, `Status-icon`), `Body`, `Ports`. `State` (`Default`/`Hover`/`Selected`/`Disabled`) × `Status` (`None`/`Success`/`Error`), 12 variantes. Propriétés `Title`, `Description`, `Show-body`, `Icon` (Instance swap).
- **Port** (nouveau) : ligne de 24px portant un `Handle` à cheval sur le bord du nœud, `Side` (`Input`/`Output`), propriété `Label`.
- **Handle** (nouveau) : point de connexion 12px, `State` (`Default`/`Hover`/`Connected`/`Invalid`/`Disabled`), cible réelle 24×24 en code.
- **Edge** (nouveau) : liaison vectorielle 2px (bézier), gabarit de style `State` (`Default`/`Selected`/`Error`/`Disabled`) — dessinée entre les nœuds, pas étirable.
- Assemblage manuel (nombre de nœuds/ports/liaisons arbitraire), comme `Table`. Aucun nouveau token. Page Figma `↳ Node` avec exemple de graphe (4 nœuds, 3 liaisons) et Guidelines.
- **decisions.yaml** : ajout de `Node` à `component_selection`.
- Non spécifié : animation de flux, état `Running`, mini-carte, zoom/pan, regroupement.

## 2026-10-05 (4) — Resynchronisation asma.ds

### Corrections
- **Chip** : la spec indiquait encore `Action/neutral-active` pour `Active`/`Neutral`, alors que Figma (et la décision du 2026-09-28) est `Background/inverse` + `Text/inverse`. Spec réalignée ; la ligne « survol d'un Chip Active » (basée sur `neutral-active`) retirée faute de valeur vérifiée dans Figma.
- **Cell, Table** : les modifications de troncature et de fond `Background/subtle` du `Header-row` n'étaient pas présentes dans les fichiers du dossier local — réappliquées.
- **Artefact asma.ds** : ajout de `Pagination`, `Progress`, du pattern `Filter bar` ; `Cell`, `Table`, `Chip`, `Avatar` resynchronisés.

## 2026-10-05 (3) — Documentation de Progress

### Composants
- **Progress** (documenté) : `Progress-linear` et `Progress-circular` existaient dans Figma (page `↳ Progress`) sans spec dans le repo. `components/progress/progress-component-spec.md` créé à partir de l'état réel : `State` (`Determinate`/`Indeterminate`) × `Percentage` (0 à 100 par pas de 10, `none`), 12 variantes chacun. Non spécifié à ce jour : animation `Indeterminate`, `prefers-reduced-motion`, variantes de statut.
- **Guidelines Figma** de la page `↳ Progress` corrigées : anneau 48×48 en `arcData` (`innerRadius 0.7`) et non 40×40 / trait 4px / extrémités arrondies, 12 variantes et non 11.

## 2026-10-05 (2) — Nouveau pattern Filter bar

### Patterns
- **Filter bar** (nouveau) : `Search` + `Select`(s) + « Réinitialiser » + action principale, puis ligne de `Chip` (`Neutral`/`Medium`/`Active`) pour les filtres appliqués et compteur de résultats. Composition de composants existants, assemblage manuel (nombre de filtres arbitraire). Application immédiate par défaut. `FilterBar` retiré des patterns candidats.

### Corrections
- **Chip** : `Label`, `Show-icon-leading`, `Show-icon-trailing` n'étaient pas branchés sur les variantes `Hover`/`Active`/`Disabled` (18 variantes) — corrigé.

## 2026-10-05 — Audit : aucun texte sans Text Style

### Règle
- Tout nœud texte du fichier Figma porte un Text Style (aucune police/taille en dur). Audit sur toutes les pages (hors instances) : 19 textes corrigés.

### Corrections
- **Pagination** : `Label` des `Page-item`, `Ellipsis` et texte « Page {n} sur {N} » en `Misc/Label` (construits à la main au départ).
- **Toast** : bouton « Annuler » (4 variantes `Status`) en `Misc/Label`.
- **Avatar** : initiales en `Body/XS` / `Body/SM` / `Body/LG` (Regular) au lieu de Semi Bold 9,6/12,8/16 px sans style.
- **Guidelines** (pages `Button`, `Numeric inputs`, `Navigation`) : 12 paragraphes à mise en forme mixte — lead-in en `Misc/Label`, suite en `Body/MD`. Les paragraphes de la page `Button` passent de 16 px à 14 px (alignés sur les autres pages).

## 2026-10-04 — Nouveau composant Pagination

### Composants
- **Pagination** (nouveau) : `Page-item` (brique atomique, `State=Default/Hover/Current`, 3 variantes, 32×32) + `Prev`/`Next` (instances de `Button`, `Type=Ghost, Icon-only=true` — deuxième usage réel du gabarit 32×32 établi sur `Search-button`). Pas de composant paramétrique unique — assemblage manuel comme `Table` (nombre de pages arbitraire). Deux structures : `Numbered` (fenêtrage avec `Ellipsis`, texte non componentisé) et `Simple` (« Page {n} sur {N} », espace contraint ou total inconnu). Icônes `CaretLeft`/`CaretRight` (pas de famille `Chevron` dans la fondation).
- **Button** : note mise à jour sur `Icon-only` — `Pagination` en devient le deuxième usage réel (après `Search-button`).
- **decisions.yaml** : ajout de `Pagination` au vocabulaire de `component_selection`.

## 2026-09-30 — Chip/Command-item/Theme switcher : états manquants + Cell, Table

### Composants
- **Chip** : ajout de la propriété `State` (`Default`/`Hover`/`Active`/`Disabled`) — manquait alors que Chip est défini comme interactif. `Active` remplit le Chip (bordure retirée) plutôt que de l'assombrir. `Type` restreint à `Neutral`/`Brand` uniquement (les 4 statuts Feedback retirés — un filtre/sélection actif n'a pas besoin de sémantique de statut). Neutral `Active` corrigé deux fois (`Action/neutral` → `Action/neutral-active` → `Background/inverse`, sur retour direct : pas assez prononcé). 24 variantes (`Type` × `Size` × `State`).
- **Command-item** : ajout de `State=Disabled` — une commande indisponible dans le contexte courant (permission manquante) n'avait aucun traitement visuel prévu.
- **Theme switcher** : ajout de `State` (`Default`/`Hover`/`Disabled`), 12 variantes (2 Mode × 2 Motion × 3 State). Règle de corrélation avec `Motion` posée explicitement : Hover et Disabled ne touchent jamais la Tension-layer/l'Indicator/le filtre `asma-tension`, dans aucune combinaison Mode/Motion.
- **Cell** (nouveau) : brique de contenu d'une cellule de data table — `Content` (`Text`/`Avatar-text`/`Tag`/`Actions`/`Slot`) × `Align` (`Left`/`Right`), 10 variantes. Pas d'état propre : les états sont portés par `Row` dans `Table`.
- **Table** (nouveau) : `Header-cell` (tri `None`/`Asc`/`Desc`, 12 variantes) + `Row` (sélection, `State`×`Selectable`, 8 variantes), construits sur `Cell`. Pas de composant paramétrique unique — assemblage manuel comme `Command`.

## 2026-09-27 (4) — Nettoyage de formulations

### Composants
- **Segmented control** : retiré « Composant unique (pas de variantes) », devenu contradictoire depuis l'ajout de la propriété `Motion` — remplacé par un renvoi explicite à `Motion=Static/Tension`.
- **Theme switcher** : anatomie de la variante `Motion=Tension` clarifiée — les cellules `Cell-active`/`Cell-inactive` y sont renommées `Cell-sun`/`Cell-moon` (positions fixes), c'est l'`Indicator` qui porte l'état actif.
- **Button** : ligne "Guidelines Figma" encore à « 5 Types » après le retrait de `Link` — corrigée en 4 Types.

## 2026-09-27 (3) — Fondation Motion

### Tokens (Primitive)
- **Ajoutés** `Motion/Duration/sm` (240), `Motion/Duration/md` (440) — en ms.
- **Ajoutés** `Motion/Easing/spring`, `Motion/Easing/standard`, `Motion/Easing/accelerate` (courbes cubic-bezier, STRING).
- **Ajoutés** `Motion/Tension/blur` (4), `Motion/Tension/contrast` (18), `Motion/Tension/offset` (−7) — paramètres du filtre SVG de tension de surface.
- `scripts/build_css.py` : génère `--motion-duration-scale-*` (ms), `--motion-easing-scale-*` (courbe brute), `--motion-tension-scale-*`. `dist/tokens.css` régénéré.

### Guidelines
- `foundations.yaml` : Motion ajouté à l'architecture (Primitive uniquement), section `motion` (valeurs, technique, contraintes géométriques, **règles d'usage**).
- `decisions.yaml` : un traitement de mouvement est une variante (`Motion=Static|Tension`), jamais un nouveau composant ; SegmentedControl et ThemeSwitcher autorisés.
- `DESIGN.md`, `README.md` : section Motion, convention de nommage CSS.

### Composants
- **SegmentedControl** : variante `Motion=Tension` documentée (anatomie, comportement, règle d'usage, accessibilité, implémentation de référence).
- **Theme switcher** : variante `Motion=Tension` documentée (4 variantes : 2 Mode × 2 Motion).

### À répercuter dans Figma
- Variables Primitive `Motion/*` (FLOAT/STRING, scopes vides) ; propriété `Motion` sur Segmented-control et Theme-switcher (le filtre n'a pas d'équivalent Figma : la variante Tension y est documentaire / prototype Smart Animate).

## 2026-09-27 (2)

Alignement repo ↔ Figma après répercussion de la MAJ précédente dans Figma.

### Composants
- **Button** : Type `Link` retiré de la spec, de `button.css` (`.btn--link`) et de `button.html` — remplacé par le composant `Link`. 20 variantes (4 Type × 5 State). Disabled : icônes en `Icon/disabled` pour tous les Types.
- **Dialog, Card** : padding `Spacing/component-md` (valeur réellement utilisée dans Figma) au lieu de `Spacing/component-lg`.
- **Theme switcher** : radius du Track = `Radius/card` (lié dans Figma).

### Figma (fait)
- Variable `Icon/on-brand` créée (Semantic, alias Neutral/0, scope SHAPE_FILL).
- Button : icônes Primary → `Icon/on-brand` ; Primary Disabled texte → `Text/disabled` (était `Text/on-brand`, quasi invisible) ; icônes Disabled de tous les Types → `Icon/disabled`.
- `Radius/card` lié sur Card (3 variantes), Command, Drawer (coins côté contenu), Theme switcher.

### Réglé
- **Popover** : `Radius/md` (16px) lié dans Figma, conforme à la spec.

## 2026-09-27

Corrections issues du prototype ASMA OS (écran Entreprises) et d'un audit de cohérence repo / Figma.

### Tokens
- **Ajouté** `Icon/on-brand` (Semantic, Neutral/0 en Light et Dark) — icônes posées sur un fond de marque.
- **Modifié** `Feedback/{Info,Success,Warning,Danger}/background` : grade 50/950 → **100/900** (correction annoncée dans la spec Tag et déjà appliquée dans Figma, jamais reportée dans `tokens/semantic.json`).
- **Corrigé** `scripts/build_css.py` : les familles de police génèrent désormais `--font-family-scale-*` (nom documenté, attendu par `button.css`) au lieu de `--family-scale-*`. `dist/tokens.css` régénéré.

### Guidelines
- `foundations.yaml` : `Icon/on-brand` ajouté aux rôles ; note sur les fonds Feedback ; règle d'usage d'Alternate (JetBrains Mono) étendue au style `Misc/Caption`.
- `DESIGN.md` : valeurs réalignées sur les tokens (`border-default` #64748b, `border-strong` #475569, `text-secondary` #334155, échelle typo, `label` 14/20 Semi Bold, `caption` JetBrains Mono 12/16) ; règle `on-brand` documentée.
- `README.md` : paragraphe obsolète « Restent : … » retiré ; liens vers les nouvelles specs.

### Composants
- **Button** : Primary `Text/inverse` / `Icon/inverse` → `Text/on-brand` / `Icon/on-brand` (texte quasi noir en Dark, contraste ≈ 3,4:1) ; libellé en Semi Bold (600) comme `Misc/Label`. `button.css` mis à jour.
- **Dialog, Drawer, Card, Command, Popover** : références à des tokens inexistants (`Radius/lg`, `Spacing/lg`/`Spacing/md` Responsive, `Shadow/*`, `Overlay/scrim`) remappées sur `Radius/card`, `Spacing/component-lg`, `Spacing/component-md` ; ombre et voile documentés sans token.
- **Theme switcher** : nouvelle spec `components/theme-switcher/`, rédigée depuis Figma.

### Patterns
- **Sidebar** : nouvelle spec `patterns/navigation/sidebar-pattern-spec.md`, rédigée depuis Figma.

### À répercuter dans Figma
- Variable `Icon/on-brand` à créer ; Button/Primary à relier à `Text/on-brand` / `Icon/on-brand` et passer en Semi Bold.
- Dialog, Drawer, Card, Command, Popover : vérifier que les liaisons de variables correspondent au remapping.
- Theme switcher : lier le radius du Track à `Radius/card`.
