# Composant Bouton

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

Une seule taille (MD), hauteur fixe 40px.

## Propriétés du composant Figma

- **Type** (variant) : `Primary` / `Outlined` / `Neutral` / `Ghost` / `Link`
- **State** (variant) : `Default` / `Hover` / `Active` / `Disabled` / `Focus`
- **Icon-leading**, **Icon-trailing** : instances directes du composant `Icon` (16×16, `Format=Outline`, `Weight=Regular`) — pas de Slot (retiré, plus de bénéfice une fois la recommandation de remplacement passée à "supprimer + glisser depuis Assets").
- **Show-icon-leading**, **Show-icon-trailing** (Boolean, défaut `false`) : visibilité des icônes.
- **Show-label** (Boolean, défaut `true`) : visibilité du label.
- **Label** (Text, défaut `"Enregistrer"`) : contenu du label, éditable par instance.
- **Icon-only** (Boolean, défaut `false`) : **non lié automatiquement** à `Show-label` — Figma ne permet pas de logique conditionnelle entre propriétés. À activer manuellement avec `Show-label=False`, et fixer le padding à `Spacing/component-xs` (8px) sur les 4 côtés pour un rendu carré (convention établie suite à l'audit `improve-ui` du 2026-09-18 — appliquée sur `Search-button`, seul usage réel actuel).

25 variantes (5 Type × 5 State).

## Correspondance couleur par Type

| Type | Fond (Default) | Bordure | Texte | Icône |
|---|---|---|---|---|
| Primary | `Action/primary` | — | `Text/inverse` | `Icon/inverse` |
| Outlined | `Action/secondary` | `Border/default` (Default) → `Border/strong` (Active) | `Text/primary` | `Icon/primary` |
| Neutral | `Action/neutral` | — | `Text/primary` | `Icon/primary` |
| Ghost | transparent | — | `Text/primary` | `Icon/primary` |
| Link | transparent | — | `Text/link` | `Icon/link` |

## États communs à tous les Types

- **Hover / Active** : progression d'intensité du fond (sauf Link : soulignement au lieu de fond).
- **Disabled** : `Background/disabled` + `Text/disabled` pour **tous** les Types — choix volontaire confirmé (reconnaissance immédiate et cohérente prime sur la préservation de la couleur du Type). Ne pas "corriger" ce comportement.
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

Page dédiée `↳ Button`, section "Guidelines" complète + frame "Presentation" (5 Types en Default côte à côte).
