# Changelog

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
