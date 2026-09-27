# Changelog

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
