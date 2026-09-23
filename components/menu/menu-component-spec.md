# Composant Menu-item

Item de navigation réutilisable (menu, sidebar), avec support de sous-menu et d'indentation.

## Propriétés

`State` = `Default`/`Hover`/`Active`/`Disabled` × `Indent` = `False`/`True`, 8 variantes. `Active` = fond `Action/secondary-active`, `Hover` = `Action/ghost-hover`. `Indent=True` décale le padding gauche à 32px (item de sous-menu).

`Leading-icon`, `Expand-icon` (chevron `CaretDown`, signale un sous-menu dépliable) : instances imbriquées du wrapper `Icon`, `isExposedInstance = true` — exposées pour permettre de changer le pictogramme directement depuis le panneau de propriétés d'une instance (pas besoin de Swap instance manuel).

Propriétés : `Label` (Text), `Show-icon`, `Has-submenu`, `Show-label` (Boolean).

## Leçon de construction

`isExposedInstance` **est scriptable** (`instance.isExposedInstance = true`) — contrairement à ce qui était supposé plus tôt dans le projet. Confirmé fonctionnel sur Tag/Chip puis Menu-item.

## Patterns associés (page `↳ Navigation`, catégorie Patterns — pas Components)

`Sidebar`, `Topbar` (SaaS), `Site-nav` (vitrine) sont des **compositions de référence**, pas des ComponentSets — voir `patterns/README.md`. `Sidebar` a un variant `Mode=Expanded/Collapsed` (icônes seules, 64px, réutilise `Show-label=false` sur ses Menu-item).

Doc complète : guidelines Figma page `↳ Menu` (composant) et `↳ Navigation` (patterns).
