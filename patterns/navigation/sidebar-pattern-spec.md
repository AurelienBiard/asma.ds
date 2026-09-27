# Pattern Sidebar

> **Statut** : composition de référence construite dans Figma (page `↳ Navigation`, catégorie Patterns) avant que cette spec n'existe — rédigée le 2026-09-27 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

## Purpose

Navigation persistante d'une application SaaS, entre les sections principales de l'espace de travail. Complète le pattern `Topbar`.

## Use when

- L'application a plusieurs sections de premier niveau consultées en alternance.
- La navigation doit rester visible en permanence (desktop).

## Do not use when

- Site vitrine → `Site-nav`.
- Navigation entre vues pairs d'un même contexte → `Tabs`.

## Components

- `Menu-item` (instances, `State` = `Default` / `Active`, `Indent` pour les sous-items, `Has-submenu` pour un parent dépliable).
- `Link` (lien de pied, ex. « Aide & support »).
- Logo : bloc 28×28, radius 6px, fond `Action/primary`.

## Structure

Variant `Mode` = `Expanded` / `Collapsed`.

- Conteneur vertical, fond `Background/elevated`, padding `Spacing/component-md` (haut/bas) × `Spacing/component-sm` (côtés), gap `Spacing/component-2xs`.
- **Expanded** (largeur au contenu) :
  - `Workspace-header` : logo + nom de l'espace en `Heading/SM` Bold `Text/primary`, gap `Spacing/component-sm`, padding bas 16px, gauche 8px.
  - `Section-label` : `Misc/Caption` (JetBrains Mono, 12/16) en capitales, `Text/tertiary`, padding gauche 8px, bas 4px.
  - `Menu-item` : hauteur 36px, padding `Spacing/component-xs`, gap `Spacing/component-xs`, radius `Radius/control`, icône 16px, libellé `Body/MD` Regular `Text/primary`. `Active` = fond `Action/secondary-active` ; `Hover` = `Action/ghost-hover` ; `Indent=True` = padding gauche 32px.
  - `Footer-link` : instance `Link`.
- **Collapsed** : 64px de large, éléments centrés. Logo seul, espace de 16px, puis les `Menu-item` en `Show-label=false` (32×36, icône seule). Pas de libellé de section ni de lien de pied.

## Interaction flow

- Clic sur un `Menu-item` : navigation vers la section, l'item passe en `Active`.
- Bascule Expanded ↔ Collapsed via un bouton `Button` Ghost Icon-only (hors du pattern, typiquement en tête du `Topbar`), `aria-expanded` synchronisé.

## States

`Menu-item` : Default / Hover / Active / Disabled. Sidebar : Expanded / Collapsed.

## Accessibility

- Conteneur `<nav>` avec un nom accessible ; item courant avec `aria-current="page"`.
- En `Collapsed`, chaque item icône seule garde un nom accessible (`aria-label`) et une infobulle (`Tooltip`) portant son libellé.
- Icônes décoratives (`aria-hidden`) en `Expanded`.

## Responsive behavior

Desktop : Expanded par défaut, repliable. Mobile : non spécifié à ce jour.

## Tokens

`Background/elevated`, `Text/primary`, `Text/tertiary`, `Action/secondary-active`, `Action/ghost-hover`, `Spacing/component-2xs/xs/sm/md`, `Radius/control`, `Heading/SM`, `Body/MD`, `Misc/Caption`.

## Related

`Menu-item` (`components/menu/`), `Link`, `Topbar`, `Site-nav`, `Tooltip`.
