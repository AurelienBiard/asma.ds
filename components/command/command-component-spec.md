# Composant Command

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Sélection de commande par recherche (`decisions.yaml` → `Command`), palette façon ⌘K.

## Command-item

Variant `State` : `Default` / `Hover` / `Active`. Propriétés `Label` (Text), `Shortcut-text` (Text), `Show-shortcut` (Boolean, défaut `true`). Icône de tête exposée (`isExposedInstance = true`).

## Command (assemblage)

Composant unique : une instance `Field` en recherche en tête (slot rempli par un `TextInput`), puis des sections regroupées (libellé de section + liste d'instances `Command-item`).

## Tokens

Conteneur `Background/elevated`, `Radius/lg`, `Shadow/xl` · Libellé section `Misc/Caption` + `Text/secondary` · Label item `Body/MD` · Badge raccourci `Background/subtle`, `Radius/sm`, `Misc/Caption`.

## Guidelines Figma

Page dédiée `↳ Command`. Regrouper les commandes par section au-delà de ~5 items, ne pas présenter une liste plate.
