# Composant Drawer

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Tâche/contenu secondaire contextuel (`decisions.yaml` → `Drawer`). Réutilise `Dialog-header` + `Dialog-toolbar` (optionnelle) + `Dialog-body` + `Dialog-footer` dans un conteneur ancré à un bord plutôt que centré.

## Propriétés

- **Position** (variant) : `Right` / `Left` / `Bottom`
- **Show-toolbar** (Boolean, défaut `false`, ajouté le 2026-11-06) : affiche la `Dialog-toolbar` entre l'en-tête et le corps, quand le panneau a besoin d'actions supplémentaires. Zone fixe comme l'en-tête et le pied (seul le corps défile). Voir `components/dialog/`. Présent sur les 3 `Position`. Reste à `false` dans un formulaire de création (rien à terminer ni à supprimer) ; règles des actions dans `components/dialog/`.

## Dimensionnement

- `Right`/`Left` : panneau largeur fixe, pleine hauteur, glisse depuis le bord nommé.
- `Bottom` : **largeur 900px**, ancré en bas — comportement bottom-sheet. Corrigé depuis 480px initial : à 480px, visuellement indiscernable d'un `Dialog` centré ; 900px rend la silhouette bottom-sheet non ambiguë même sur écran large.

## Tokens

Fond `Background/elevated` · Radius : aucun (coins carrés, voir ci-dessous) · Ombre : aucune ombre tokenisée — l'architecture n'a pas de famille Shadow (Semantic = couleur uniquement) · Fond assombri : voile plein écran sans token dédié — aucun token Overlay n'existe.

## Coins carrés (2026-11-02)

**Un `Drawer` a des coins carrés**, quelle que soit la `Position` (`Right`, `Left`, `Bottom`) et dans le bottom-sheet mobile : le conteneur n'a aucun arrondi, et les instances `Dialog-header` et `Dialog-footer` qu'il contient non plus (les 4 coins de chaque instance à 0 — override, variable de rayon déliée). `Dialog-header` (coins hauts) et `Dialog-footer` (coins bas) ne portent un arrondi `Radius/card` que lorsqu'ils composent un `Dialog` (voir `components/dialog/`). En code : aucun `border-radius` sur le panneau, son en-tête ni son pied. Aligné sur ASMA OS (drawer d'édition : droite, 480 px, pleine hauteur, voile).

## Drawer vs Dialog

Drawer : panneau secondaire dismissible ancré à un bord (filtres, détail d'un item, formulaire large) ou bottom-sheet explicite. Dialog : interruption centrée qui demande attention immédiate (confirmation, formulaire court, alerte).

## Guidelines Figma

Page dédiée `↳ Drawer`.

> **Correction (2026-09-27)** : la spec citait des tokens inexistants (`Radius/lg`, `Spacing/lg`/`Spacing/md` en Responsive, `Shadow/*`, `Overlay/scrim`). Remappés sur l'existant (`Radius/card`, `Spacing/component-md` — valeur déjà utilisée dans Figma) ; ombre et voile documentés sans token, aucun token créé. À répercuter dans Figma.
