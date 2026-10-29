# Composant Bouton

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

Une seule taille (MD), hauteur de 44px avec libellé (padding `Spacing/component-sm` × 2 + ligne de 20px ; la mention « 40px » des versions précédentes ne correspondait pas au composant Figma). Libellé en Text Style `Misc/Label` — 14px/20px, **Semi Bold** (même graisse que tous les contrôles de formulaire).

> **Correction (2026-09-27)** : Primary utilisait `Text/inverse` / `Icon/inverse`, qui valent Neutral/950 en Dark — texte quasi noir sur `Action/primary` Dark (#3f51e5), contraste ≈ 3,4:1 (échec AA). Remplacés par `Text/on-brand` / `Icon/on-brand` (blanc dans les deux thèmes, ≈ 6:1 en Dark). La graisse du libellé passe de Medium (500) à Semi Bold (600) pour suivre `Misc/Label`.

## Propriétés du composant Figma

- **Type** (variant) : `Primary` / `Outlined` / `Neutral` / `Ghost` — l'ancien Type `Link` a été retiré : utiliser le composant `Link` (`components/link/`) pour la navigation.
- **State** (variant) : `Default` / `Hover` / `Active` / `Disabled` / `Focus`
- **Icon-leading**, **Icon-trailing** : instances directes du composant `Icon` (16×16, `Format=Outline`, `Weight=Light`) — pas de Slot (retiré, plus de bénéfice une fois la recommandation de remplacement passée à "supprimer + glisser depuis Assets").
- **Show-icon-leading**, **Show-icon-trailing** (Boolean, défaut `false`) : visibilité des icônes.
- **Show-label** (Boolean, défaut `true`) : visibilité du label.
- **Label** (Text, défaut `"Enregistrer"`) : contenu du label, éditable par instance.
- **Icon-only** (Boolean, défaut `false`) : **non lié automatiquement** à `Show-label` — Figma ne permet pas de logique conditionnelle entre propriétés. À activer manuellement avec `Show-label=False` ; le bouton suit alors la règle « Bouton sans libellé » ci-dessous (44×44 fixe). Usages : `Search-button`, `Prev`/`Next` du composant `Pagination` (voir `components/pagination/`), actions de ligne de `Table`/`Cell`.

20 variantes (4 Type × 5 State).

## Règle : bouton sans libellé (2026-10-29)

Quand un Button n'a pas de libellé (`Show-label=False`, en pratique avec `Icon-only=true`), il garde la hauteur standard de **44 px** et sa largeur est **fixe à 44 px** : cible carrée de 44×44, icône centrée, `layoutSizingHorizontal` et `layoutSizingVertical` en `FIXED`, jamais en hug. Le padding n'a plus d'effet sur la taille.

- **Pourquoi** : même hauteur que le bouton avec libellé, donc alignement dans les rangées mixtes ; cible tactile confortable (WCAG 2.5.8 exige 24 px, 2.5.5 niveau AAA recommande 44 px).
- **Limite technique** : Figma ne lie pas `Icon-only` à la taille. La règle s'applique donc par instance (taille fixe 44×44) et reste à reporter dans le code (`width: 44px; height: 44px` sur un bouton sans texte visible).
- **Pas d'exception** : tous les champs de saisie font 44 px de haut (depuis le 2026-10-29), donc les boutons sans libellé qui les accompagnent (`Search-button`, − / + du `Stepper`) sont aussi en 44×44.
- **Nom accessible** : toujours un `aria-label` (voir Accessibilité).

## Correspondance couleur par Type

| Type | Fond (Default) | Bordure | Texte | Icône |
|---|---|---|---|---|
| Primary | `Action/primary` | — | `Text/on-brand` | `Icon/on-brand` |
| Outlined | `Action/secondary` | `Border/default` (Default) → `Border/strong` (Active) | `Text/primary` | `Icon/primary` |
| Neutral | `Action/neutral` | — | `Text/primary` | `Icon/primary` |
| Ghost | transparent | — | `Text/primary` | `Icon/primary` |

## États communs à tous les Types

- **Hover / Active** : progression d'intensité du fond.
- **Disabled** : `Background/disabled` + `Text/disabled` + icônes `Icon/disabled` pour **tous** les Types — choix volontaire confirmé (reconnaissance immédiate et cohérente prime sur la préservation de la couleur du Type). Ne pas "corriger" ce comportement.
- **Focus** : bordure `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE`. Sur `Ghost`, un fond léger (`Action/ghost-hover`) est ajouté en Focus pour délimiter visuellement la zone cliquable.
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
