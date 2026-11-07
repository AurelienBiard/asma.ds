# Composant Bouton

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

Une seule taille (MD), hauteur de 44px avec libellé (padding `Spacing/component-sm` × 2 + ligne de 20px ; la mention « 40px » des versions précédentes ne correspondait pas au composant Figma). Libellé en Text Style `Misc/Label` — 14px/20px, **Semi Bold** (même graisse que tous les contrôles de formulaire).

> **Correction (2026-09-27)** : Primary utilisait `Text/inverse` / `Icon/inverse`, qui valent Neutral/950 en Dark — texte quasi noir sur `Action/primary` Dark (#3f51e5), contraste ≈ 3,4:1 (échec AA). Remplacés par `Text/on-brand` / `Icon/on-brand` (blanc dans les deux thèmes, ≈ 6:1 en Dark). La graisse du libellé passe de Medium (500) à Semi Bold (600) pour suivre `Misc/Label`.

## Propriétés du composant Figma

- **Type** (variant) : `Primary` / `Outlined` / `Neutral` / `Ghost` / `Destructive` (ajouté le 2026-11-01) / `Destructive-ghost` (ajouté le 2026-11-02) — l'ancien Type `Link` a été retiré : utiliser le composant `Link` (`components/link/`) pour la navigation.
- **State** (variant) : `Default` / `Hover` / `Active` / `Disabled` / `Focus`
- **Pressed** (variant, `False` / `True`, ajouté le 2026-11-07) : état « activé » d'un bouton à bascule, **uniquement sur `Outlined` et `Ghost`** — voir « Pressed (bouton à bascule) » ci-dessous.
- **Icon-leading**, **Icon-trailing** : instances directes du composant `Icon` (16×16, `Format=Outline`, `Weight=Light`) — pas de Slot (retiré, plus de bénéfice une fois la recommandation de remplacement passée à "supprimer + glisser depuis Assets").
- **Show-icon-leading**, **Show-icon-trailing** (Boolean, défaut `false`) : visibilité des icônes.
- **Show-label** (Boolean, défaut `true`) : visibilité du label.
- **Label** (Text, défaut `"Enregistrer"`) : contenu du label, éditable par instance.
- **Icon-only** (Boolean, défaut `false`) : **non lié automatiquement** à `Show-label` — Figma ne permet pas de logique conditionnelle entre propriétés. À activer manuellement avec `Show-label=False` ; le bouton suit alors la règle « Bouton sans libellé » ci-dessous (44×44 fixe). Usages : `Search-button`, `Prev`/`Next` du composant `Pagination` (voir `components/pagination/`), actions de ligne de `Table`/`Cell`.

40 variantes : 30 (6 Type × 5 State, `Pressed=False`) + 10 (`Outlined` et `Ghost` × 5 State, `Pressed=True`).

## Règle : bouton sans libellé (2026-10-29)

Quand un Button n'a pas de libellé (`Show-label=False`, en pratique avec `Icon-only=true`), il garde la hauteur standard de **44 px** et sa largeur est **fixe à 44 px** : cible carrée de 44×44, icône centrée, `layoutSizingHorizontal` et `layoutSizingVertical` en `FIXED`, jamais en hug. Le padding n'a plus d'effet sur la taille.

- **Pourquoi** : même hauteur que le bouton avec libellé, donc alignement dans les rangées mixtes ; cible tactile confortable (WCAG 2.5.8 exige 24 px, 2.5.5 niveau AAA recommande 44 px).
- **Limite technique** : Figma ne lie pas `Icon-only` à la taille. La règle s'applique donc par instance (taille fixe 44×44) et reste à reporter dans le code (`width: 44px; height: 44px` sur un bouton sans texte visible).
- **Pas d'exception** : tous les champs de saisie font 44 px de haut (depuis le 2026-10-29), donc les boutons sans libellé qui les accompagnent (`Search-button`, − / + du `Stepper`) sont aussi en 44×44.
- **Piège** : `Show-label=false` seul ne suffit pas. Sans `Icon-only=true` et sans taille 44×44, le bouton retombe à 40 px de haut (icône 16 + padding 12 × 2, plus de ligne de libellé de 20 px). Toujours régler les trois ensemble : `Show-label=false`, `Icon-only=true`, 44×44 fixe. Contrôlé le 2026-10-31 : les 168 boutons sans libellé du fichier Figma sont en 44×44. **Atténuation (2026-11-06)** : tous les Buttons ont `minHeight = 44` dans Figma, donc la hauteur ne retombe plus à 40 px ; la largeur sans libellé reste de 48 px (padding horizontal 16 + icône 16 + 16), un `minWidth` ne la ramènerait pas à 44. Le carré 44×44 reste à régler par instance.
- **Nom accessible** : toujours un `aria-label` (voir Accessibilité).

## Correspondance couleur par Type

| Type | Fond (Default) | Bordure | Texte | Icône |
|---|---|---|---|---|
| Primary | `Action/primary` | — | `Text/on-brand` | `Icon/on-brand` |
| Outlined | `Action/secondary` | `Border/default` (Default) → `Border/strong` (Active) | `Text/primary` | `Icon/primary` |
| Neutral | `Action/neutral` | — | `Text/primary` | `Icon/primary` |
| Destructive | `Action/destructive` | — | `Text/on-brand` | `Icon/on-brand` |
| Ghost | transparent | — | `Text/primary` | `Icon/primary` |
| Destructive-ghost | transparent | — | `Feedback/Danger/text` | `Feedback/Danger/icon` |

## Pressed (bouton à bascule) — 2026-11-07

`Pressed=True` représente un bouton à bascule **activé** (favori, épingle, filtre actif, mode), l'équivalent de `aria-pressed="true"` en code. Variante, et non nouvel état de `State` : un bouton activé reste survolable, actif et focusable. Disponible sur `Outlined` et `Ghost` uniquement (les autres Types n'ont pas de sens « à bascule » : un `Primary` ou un `Destructive` déclenche une action).

| State | Fond avec `Pressed=True` | Bordure |
|---|---|---|
| Default | `Action/neutral-hover` | inchangée (`Border/strong` pour Outlined, aucune pour Ghost) |
| Focus | `Action/neutral-hover` | `Border/focus` |
| Hover | `Action/neutral-active` | inchangée |
| Active | `Action/neutral-active` | inchangée |
| Disabled | `Background/disabled` (identique à `Pressed=False`) | inchangée |

Texte et icônes gardent leurs couleurs (`Text/primary`, `Icon/primary`). Aucun token créé. En `Pressed=True`, Hover et Active partagent le même fond : Active est instantané. Contraste de `Text/primary` sur `Action/neutral-active` à mesurer lors de l'implémentation.

**Règle : icône pleine = actif.** Le fond teinté seul ne suffit pas (la couleur ne porte jamais le sens seule). Un bouton à bascule avec icône utilise le même pictogramme en deux poids : `Weight=Light` (contour) quand il est inactif, `Weight=Fill` (pleine) quand il est activé (étoile, épingle, cœur, marque-page). Le libellé ne change pas (« Épingler » reste « Épingler ») : l'état est porté par `aria-pressed`, pas par le texte.

**Code** : `<button aria-pressed="true|false">` ; ne jamais combiner avec `aria-label` modifié selon l'état. Pour une bascule à deux choix visibles, préférer `SegmentedControl`.

## États communs à tous les Types

- **Hover / Active** : progression d'intensité du fond.
- **Disabled** : `Background/disabled` + `Text/disabled` + icônes `Icon/disabled` pour **tous** les Types — choix volontaire confirmé (reconnaissance immédiate et cohérente prime sur la préservation de la couleur du Type). Ne pas "corriger" ce comportement.
- **Destructive** (ajouté le 2026-11-01, nommé `Danger` jusqu'au 2026-11-02) : action **destructive ou irréversible** (supprimer, archiver définitivement). Fond `Action/destructive` (Default), `Action/destructive-hover` (Hover), `Action/destructive-active` (Active) ; Focus : fond Default + bordure `Border/focus`. Disabled : gris neutre commun. Contraste du texte `Text/on-brand` sur le fond : 4,83:1 au repos, en Light **et** en Dark (en Dark le fond était `Red/500` à 3,76:1 jusqu'au 2026-11-02 ; `Action/destructive` / `-hover` / `-active` pointent désormais `Red/600` / `700` / `800` dans les deux thèmes). Réservé à l'action qui détruit — jamais pour un simple avertissement (→ `Alert`). Quand l'action est irréversible, demander une confirmation avant (`Dialog`). Le nom du Type suit le mot d'usage « Danger » ; les tokens restent `Action/destructive*` (« Destructive is an action, Danger is feedback »). **À valider** : contraste du texte blanc sur `Action/destructive` — Light `Red/600` 4,83:1 (AA), Dark `Red/500` 3,76:1 (sous 4,5:1 ; hover Dark `Red/600` 4,83:1). Correctif possible : Dark default → `Red/600`, hover → `Red/700`, active → `Red/800`.
- **Destructive-ghost** (ajouté le 2026-11-02) : même sémantique que `Destructive` (action qui détruit), sans fond plein. Transparent par défaut ; Hover `Action/ghost-hover`, Active `Action/ghost-active` (mêmes fonds que `Ghost`, aucun token créé) ; Focus : fond `Action/ghost-hover` + bordure `Border/focus` (comme `Ghost`) ; Disabled : gris neutre commun. Texte `Feedback/Danger/text` et icônes `Feedback/Danger/icon` : aucun token `Action/destructive*` n'est lisible comme texte en Dark (`Red/600` sur fond sombre), alors que `Feedback/Danger/*` s'inverse par thème — exception assumée à « Destructive is an action, Danger is feedback », limitée à la couleur du texte et de l'icône de ce Type. Contraste Light : texte 6,47:1 (repos), 5,25:1 (Active) ; icône 4,83:1 → 3,92:1 (≥ 3:1). Dark : texte 9,41:1 (sur `Background/default`), 5,46:1 (Active) ; icône 6,45:1 → 3,74:1. Usage : action destructive secondaire ou répétée (supprimer dans une ligne de `Table`, une liste, une barre d'outils) où un fond rouge plein serait trop lourd ; une seule action `Destructive` pleine par écran, mêmes règles de confirmation (`Dialog`) si irréversible. En Dark, le fond Hover `Action/ghost-hover` vaut `Background/elevated` : le survol ne se voit pas sur une surface élevée (limite héritée de `Ghost`).
- **Focus** : bordure `Border/focus' + `Primitive/Border/medium`, `strokeAlign: OUTSIDE`. Sur `Ghost`, un fond léger (`Action/ghost-hover`) est ajouté en Focus pour délimiter visuellement la zone cliquable.
- Une tentative de halo (Drop Shadow) à la place de la bordure de Focus a été testée puis abandonnée — retour à la bordure classique.

## Icônes — construction et limitation connue

**Format par défaut : `Outline`** (pas `Stroke`). Taille 16×16px.

**Méthode de coloration (à réutiliser pour tout futur composant nichant une icône colorée) :**
1. Ne jamais utiliser `figma.createInstance()` à froid — une instance fraîchement créée n'a **aucun override matérialisé**, ses descendants sont introuvables via l'API tant qu'aucun override n'existe dessus.
2. **Cloner** une instance qui a déjà un override existant sur ce même vecteur.
3. **Colorer AVANT** de changer le pictogramme via `setProperties({"Instance#46:0": nouvelId})` — l'ordre inverse échoue de façon non fiable.
4. Accès au vecteur interne via un ID à 3 segments : `I<id instance clonée>;<id fixe instance Phosphor interne au composant Icon>;<id fixe du vecteur>`.
5. **Vérification fiable** : ne pas se fier à `getNodeByIdAsync` sur l'ID du vecteur dans un appel séparé (peut retourner `null` de façon trompeuse) — vérifier via `instance.overrides`.
6. **Piège évité** : une propriété Instance-swap partagée pour le remplacement libre a été abandonnée — une seule valeur possible pour tout le ComponentSet, incompatible avec 3 teintes différentes selon le Type. Le remplacement libre reste possible via Swap instance natif.

## Contraste (correction système)

`Text/disabled` avait des valeurs Light/Dark quasiment inversées. Corrigé globalement :
- Light : `Neutral/600` `#475569` → 6.92:1
- Dark : `Neutral/400` `#94a3b8` → 5.71:1

## Leçons de construction

- `.clone()` ne préserve pas les `componentPropertyReferences` — les rebinder explicitement après.
- `combineAsVariants` peut échouer sur des composants héritant de références d'un autre ComponentSet — préférer `existingSet.appendChild(newComponent)`.
- Un ComponentSet vidé de tous ses membres est supprimé automatiquement par Figma.

## Guidelines Figma

Page dédiée `↳ Button`, section "Guidelines" complète + frame "Presentation" (4 Types en Default côte à côte).
