# Composant Drawer

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Tâche/contenu secondaire contextuel (`decisions.yaml` → `Drawer`). Réutilise `Dialog-header` + `Dialog-body` + `Dialog-footer` dans un conteneur ancré à un bord plutôt que centré.

## Propriétés

- **Position** (variant) : `Right` / `Left` / `Bottom`

## Dimensionnement

- `Right`/`Left` : panneau largeur fixe, pleine hauteur, glisse depuis le bord nommé.
- `Bottom` : **largeur 900px**, ancré en bas — comportement bottom-sheet. Corrigé depuis 480px initial : à 480px, visuellement indiscernable d'un `Dialog` centré ; 900px rend la silhouette bottom-sheet non ambiguë même sur écran large.

## Tokens

Fond `Background/elevated` · Radius uniquement sur les coins côté contenu (`Radius/lg`) · Ombre `Shadow/xl` · Fond assombri `Overlay/scrim`.

## Drawer vs Dialog

Drawer : panneau secondaire dismissible ancré à un bord (filtres, détail d'un item, formulaire large) ou bottom-sheet explicite. Dialog : interruption centrée qui demande attention immédiate (confirmation, formulaire court, alerte).

## Guidelines Figma

Page dédiée `↳ Drawer`.
