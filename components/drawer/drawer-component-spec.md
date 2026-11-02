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

Fond `Background/elevated` · Radius uniquement sur les coins côté contenu (`Radius/card`) · Ombre : aucune ombre tokenisée — l'architecture n'a pas de famille Shadow (Semantic = couleur uniquement) · Fond assombri : voile plein écran sans token dédié — aucun token Overlay n'existe.

## Dialog-header / Dialog-footer dans un Drawer (2026-11-02)

`Dialog-header` (coins hauts) et `Dialog-footer` (coins bas) portent un arrondi `Radius/card` quand ils composent un `Dialog` (voir `components/dialog/`). **Dans un `Drawer`, ils n'ont aucun arrondi propre** : les 4 coins de chaque instance sont à 0 (override de l'instance, variable de rayon déliée), dans les trois `Position` et dans le bottom-sheet. Seul le conteneur du `Drawer` porte un arrondi, uniquement sur ses coins côté contenu (`Radius/card`, jamais sur les coins collés au bord de l'écran). En code : pas de `border-radius` sur l'en-tête et le pied du panneau, quelle que soit la `Position`. Vérifié contre ASMA OS : le drawer d'édition (droite, 480 px, pleine hauteur, voile) réutilise ces composants sans arrondi propre.

## Drawer vs Dialog

Drawer : panneau secondaire dismissible ancré à un bord (filtres, détail d'un item, formulaire large) ou bottom-sheet explicite. Dialog : interruption centrée qui demande attention immédiate (confirmation, formulaire court, alerte).

## Guidelines Figma

Page dédiée `↳ Drawer`.

> **Correction (2026-09-27)** : la spec citait des tokens inexistants (`Radius/lg`, `Spacing/lg`/`Spacing/md` en Responsive, `Shadow/*`, `Overlay/scrim`). Remappés sur l'existant (`Radius/card`, `Spacing/component-md` — valeur déjà utilisée dans Figma) ; ombre et voile documentés sans token, aucun token créé. À répercuter dans Figma.
