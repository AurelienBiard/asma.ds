# Composant Tooltip

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Info-bulle contextuelle. 36 variantes (3 State × 12 Position).

## Propriétés du composant Figma

- **State** (variant) : `Default` / `Error` / `Warning`
- **Position** (variant) : `top-left/center/right`, `bottom-left/center/right`, `left-top/center/bottom`, `right-top/center/bottom`
- **Message** (Text, défaut `"Information complémentaire"`) : texte du tooltip, éditable.
- **Show-icon** (Boolean, défaut `true`) : visibilité de l'icône.

## Correspondance State → tokens

| State | Fond | Bordure | Texte | Icône | Pictogramme |
|---|---|---|---|---|---|
| Default | `Background/elevated` | `Border/default` | `Text/primary` | `Icon/primary` | `Info` |
| Error | `Feedback/Danger/background` | `Feedback/Danger/border` | `Feedback/Danger/text` | `Feedback/Danger/icon` | `WarningCircle` |
| Warning | `Feedback/Warning/background` | `Feedback/Warning/border` | `Feedback/Warning/text` | `Feedback/Warning/icon` | `Warning` |

(Default utilisait initialement `Background/inverse`/`Text/inverse`/`Icon/inverse` — changé sur demande pour s'aligner avec le reste du DS et recevoir une bordure comme les autres States.)

## Architecture anti-jonction (leçon la plus importante de ce composant)

**Problème initial** : une languette positionnée en `ABSOLUTE` par-dessus un corps bordé (`Body`) laisse une ligne de jonction visible entre la bordure du corps et la languette.

**Solution (reproduite depuis une référence fournie par l'utilisateur, `FeatureCallout`)** :
- `Arrow` (frame transparent, taille **fixe**, pas de FILL) et `InnerTooltip` (fond+bordure+radius) sont des **frères en flux normal** dans un outer auto-layout — jamais l'un superposé en absolu sur l'autre.
- L'outer a un **gap négatif (`itemSpacing: -1`)** entre les deux, créant un léger chevauchement qui masque toute ligne de jonction résiduelle (anti-aliasing).
- `Arrow` contient un sous-frame `Frame 85` (`clipsContent: true`) avec 2 vecteurs superposés : `Vector` (fill, coloré comme le fond) et `Outline` (stroke seul, tracé ouvert sur les 2 côtés visibles seulement — pas le côté qui touche le corps).
- **Positionnement latéral** : contrôlé par `counterAxisAlignItems` de l'**outer** (`MIN`/`CENTER`/`MAX`), jamais par un alignement interne à `Arrow` (qui reste toujours à sa taille naturelle).
- **Canvas stacking** (`itemReverseZIndex`) : `true` pour `Position=top-*` et `left-*` (Arrow apparaît en premier dans le flux, donc "First on top" nécessaire pour qu'il passe visuellement devant dans la zone de chevauchement) ; `false` (défaut, "Last on top") pour `bottom-*`/`right-*` où Arrow est déjà en dernier dans le flux.
- **Padding latéral `Spacing/component-xs`** sur `Arrow` pour les positions non centrées (`top-left`, `top-right`, etc.) — évite que la languette soit collée au coin exact.
- Ordre des enfants dans l'outer : `Arrow` en premier si `Position` commence par `top-` ou `left-`, sinon `InnerTooltip` en premier.

**Orientations du triangle** (tracé directement en 4 variantes, jamais par rotation d'un même vecteur — la rotation Figma introduit des décalages de point d'ancrage difficiles à corriger sans vérification visuelle) :
```
up:    M 9.9 0 L 19.8 9.9 L 0 9.9 Z       (pour top-*)
down:  M 9.9 9.9 L 19.8 0 L 0 0 Z         (pour bottom-*)
left:  M 0 9.9 L 9.9 0 L 9.9 19.8 Z       (pour left-*)
right: M 9.9 9.9 L 0 0 L 0 19.8 Z         (pour right-*)
```

## Message

Text Style `Body/SM`. `layoutSizingHorizontal: FILL`, `textAutoResize: HEIGHT` (retour à la ligne activé, pas de troncature). `maxWidth: 400` sur `InnerTooltip` et sur le composant entier.

## Icône

Construction identique à la méthode standard du DS (voir spec Button) : cloner une instance déjà matérialisée, colorer avant de swapper le pictogramme.

`Show-icon` (Boolean) contrôle la visibilité. **Pas de propriété Instance-swap partagée** pour changer le pictogramme (même piège que Button : une seule valeur possible pour tout le ComponentSet, incompatible avec Info/WarningCircle/Warning différents selon State). Alternative confirmée fonctionnelle par l'utilisateur : action manuelle "Expose nested instance" sur l'instance `Icon`, une fois par instance de Tooltip placée — fait remonter le sélecteur de pictogramme dans le panneau du Tooltip parent.

## Leçons de construction spécifiques

- Un ComponentSet vidé de tous ses membres (ex. en retirant tous les enfants avant d'ajouter les remplaçants) est **supprimé automatiquement** par Figma — toujours ajouter les nouveaux membres avant de retirer les anciens, ou recombiner via `combineAsVariants` immédiatement après.
- Le champ `description` d'un composant **échappe automatiquement les apostrophes** en `&#39;` — éviter les apostrophes dans les descriptions, préférer une reformulation ou les guillemets « » qui ne posent pas ce problème.

## Guidelines Figma

Page dédiée `↳ Tooltip`, section "Guidelines" complète (Anatomie, Variants State, Usage, Accessibilité, Do/Don't, Spécifications techniques).
