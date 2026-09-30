# Composant Theme switcher

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : construit dans Figma (page `↳ Theme switcher`) avant que cette spec n'existe — rédigée le 2026-09-27 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Bascule le mode de la collection **Semantic** (Light ↔ Dark) pour tout le fichier ou toute l'application (`decisions.yaml` → `ThemeSwitcher`). Fonctionnel, pas un simple état visuel.

## Anatomie

- **Track** : rail horizontal 52×28, padding `Spacing/component-2xs` (4px) sur les 4 côtés, gap `Spacing/component-2xs`, fond `Action/secondary-active`, radius `Radius/card`.
- **Cell-active** / **Cell-inactive** : deux cellules 20×20, radius `Radius/control`. La cellule active a le fond `Background/elevated` ; l'inactive est transparente.
- **Sun-icon** / **Moon-icon** : instances du wrapper `Icon` (`Size=Small`, rendu 12×12, `Format=Outline`, `Weight=Regular`), pictogrammes `Sun` et `Moon`, couleur `Icon/primary`.

## Propriétés du composant Figma

- **Mode** (variant) : `Light` (défaut) / `Dark` — la cellule active est Sun en `Light`, Moon en `Dark`.
- **Motion** (variant) : `Static` (défaut) / `Tension` — voir ci-dessous.
- **State** (variant, ajouté le 2026-09-29) : `Default` / `Hover` / `Disabled` — voir "États" ci-dessous. Manquait malgré un vrai bouton interactif (`role="switch"`).

12 variantes (2 Mode × 2 Motion × 3 State).

## États (ajouté le 2026-09-29)

Règle de corrélation avec `Motion` : **Hover et Disabled ne touchent jamais la Tension-layer, l'Indicator, ni le filtre `asma-tension`** — identique en `Static` et en `Tension`, quel que soit le Mode. C'est une conséquence directe de la règle d'usage déjà posée sur `Motion=Tension` (`foundations.yaml` → `motion.usage_rules` : le filtre est réservé à un **changement d'état** porté par une forme opaque unique) — un survol ou un état désactivé n'est pas un changement d'état, donc n'anime/ne déforme jamais l'Indicator. Seuls `Track` et les icônes sont concernés par ces deux états.

- **Hover** : `Track` garde son fond `Action/secondary-active` inchangé (déjà au maximum d'intensité disponible dans cette famille de tokens — pas de `-hover` dédié), ajout d'un contour 1px `Border/default` autour du `Track`. Ni les cellules (`Cell-active`/`Cell-inactive` en Static, `Cell-sun`/`Cell-moon`/`Indicator` en Tension) ni les icônes ne changent.
- **Disabled** : `Track` passe en fond `Background/disabled` + bordure `Border/disabled`. Les icônes (`Sun-icon`/`Moon-icon`, les deux, dans les deux Motion) passent en `Icon/disabled`. La cellule active / l'`Indicator` **reste** `Background/elevated` inchangé — comme le Thumb de `Switch` qui reste blanc en Disabled — pour garder le toggle lisible malgré l'ensemble atténué. Non cliquable : la transition Light↔Dark (et donc l'effet Tension) ne peut jamais se déclencher dans cet état.

## Comportement

Au clic, deux actions Figma enchaînées : `CHANGE_TO` vers l'autre variante + `SET_VARIABLE_MODE` sur la collection Semantic (`Light` → `Dark`, `Dark` → `Light`). En code : poser ou retirer `data-theme="dark"` sur `<html>` (ou `<body>`).

## Accessibilité

- Élément interactif unique, atteignable au clavier : `<button role="switch" aria-checked="true|false">` avec un nom accessible explicite (ex. « Thème sombre »). Les icônes sont décoratives (`aria-hidden`).
- Focus visible : bordure `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE` (convention des contrôles du DS).
- L'état ne repose pas que sur la couleur : la position de la cellule active change.

## Variante Motion=Tension (ajoutée le 2026-09-27)

Même principe que `SegmentedControl` / `Motion=Tension` (spec de référence : `components/segmented-control/`, fondation : `foundations.yaml` → `motion`) :
- **Tension-layer** sous les deux cellules, en retrait `Spacing/component-2xs`, filtre `asma-tension`.
- **Indicator** opaque `Background/elevated`, 20×20, radius `Radius/control` : il porte le fond actif et se déplace entre les deux positions. Les deux cellules sont renommées **Cell-sun** / **Cell-moon** (positions fixes portant chacune son icône) et deviennent transparentes dans cette variante — c'est l'Indicator qui indique laquelle est active, pas leur propre fond.
- Au clic : bord d'attaque `Motion/Duration/sm` + `Motion/Easing/spring`, bord de fuite `Motion/Duration/md` + `Motion/Easing/standard` ; Drop sur l'ancienne cellule en `Motion/Duration/md` + `Motion/Easing/accelerate`.
- Contraintes respectées : cellules de 20px ≥ taille minimale (8px), écart de 4px ≤ pont maximal (6px) — les deux formes fusionnent pendant le trajet.
- `prefers-reduced-motion: reduce` → bascule sans transition. Accessibilité inchangée (`role="switch"`, `aria-checked`).

## Guidelines Figma

Page dédiée `↳ Theme switcher`.
