# Composant Link

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Navigation (`decisions.yaml` → `Link`). Remplace l'ancienne variante `Type=Link` de `Button`, retirée comme doublon une fois ce composant livré — **ne pas la réintroduire**.

## Propriétés

- **State** (variant) : `Default` / `Hover` / `Active` / `Disabled`
- **Label** (Text)
- **Show-icon-trailing** (Boolean, défaut `false`)

## Tokens

Texte `Text/link` (ou `Text/on-brand` en contexte inversé sur fond `Background/brand`) · `Body/MD` · `Hover` : soulignement · `Disabled` : `Text/disabled`.

## Usage

`Button` pour une action qui déclenche quelque chose ; `Link` pour naviguer vers une autre page/section. Utilisé dans `Site-nav`, `Sidebar`, `Menu-item`.

## Guidelines Figma

Page dédiée `↳ Link`.
