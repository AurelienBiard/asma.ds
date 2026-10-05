# Changelog

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
