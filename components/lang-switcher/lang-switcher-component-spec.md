# Composant Lang switcher

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma.

> **Statut** : construit le 2026-10-12 dans Figma (page `↳ Lang switcher`), par duplication de `Theme-switcher` dont les pictogrammes sont remplacés par des codes de langue en typographie.

Bascule binaire de la langue de l'interface (FR ↔ EN) (`decisions.yaml` → `LangSwitcher`). Même squelette que `Theme switcher` (voir `components/theme-switcher/`), mais **sans icône** : le contenu de chaque cellule est un code de langue ISO 639-1 en capitales.

## Anatomie

- **Track** : rail horizontal 52×28, padding `Spacing/component-2xs` (4px), gap `Spacing/component-2xs`, fond `Action/secondary-active`, radius `Radius/card`.
- **Cell-active** / **Cell-inactive** : deux cellules 20×20, radius `Radius/control`. L'active a le fond `Background/elevated` ; l'inactive est transparente.
- **Label-fr** / **Label-en** : texte « FR » / « EN », style `Body/XS` (Inter 10px). Actif `Text/primary`, inactif `Text/tertiary`.

## Propriétés du composant Figma

- **Lang** (variant) : `FR` (défaut) / `EN` — la cellule active est celle de la langue courante.
- **Motion** (variant) : `Static` (défaut) / `Tension` — identique à `Theme switcher` : **Indicator** opaque `Background/elevated` 20×20 sur une **Tension-layer** (filtre `asma-tension`), cellules renommées `Cell-fr` / `Cell-en` et transparentes.
- **State** (variant) : `Default` / `Hover` / `Disabled`.

12 variantes (2 Lang × 2 Motion × 3 State).

## États

Règles identiques à `Theme switcher` : Hover et Disabled ne touchent jamais l'Indicator ni le filtre `asma-tension`.

- **Hover** : contour 1px `Border/default` autour de la `Track`, rien d'autre ne change. Le contour est `INSIDE` avec `strokesIncludedInLayout = false` : la `Track` garde 52×28 dans tous les états (sinon le composant, qui rogne son contenu, coupe le bord droit et bas).
- **Disabled** : `Track` en `Background/disabled` + `Border/disabled` ; les deux codes en `Text/disabled` ; cellule active / Indicator reste `Background/elevated`. Non cliquable.

## Comportement

Au clic : `CHANGE_TO` vers l'autre langue (même Motion, même State), `SMART_ANIMATE` en `Tension`. **Aucun `SET_VARIABLE_MODE`** : la langue n'est pas une variable Figma. En code : mettre à jour la locale de l'application (`<html lang>`) et recharger le contenu (`tokens/content.json` / `data-copy`).

## Règles d'usage

- Codes de **langue** ISO 639-1 (`FR`, `EN`), pas des codes de pays : `EN` n'est pas un pays ; ne pas utiliser `GB`/`US`, ni drapeaux.
- Choix binaire uniquement. À 3 langues ou plus : `Select` ou `Menu`.
- Une seule instance par écran (en-tête ou paramètres).

## Accessibilité

- Élément interactif unique : `<button role="switch" aria-checked>` avec nom accessible (« Langue de l'interface »). Chaque code porte `lang="fr"` / `lang="en"` et un `aria-label` complet (« Français », « English »).
- Focus visible : `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE`.
- L'état ne repose pas que sur la couleur : la position de la cellule active change. Contraste : `Text/primary` sur `Background/elevated` et `Text/tertiary` sur `Action/secondary-active` — à vérifier si les tokens évoluent.

## Guidelines Figma

Page dédiée `↳ Lang switcher`.
