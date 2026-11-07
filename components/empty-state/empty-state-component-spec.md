# Composant Empty-state (2026-11-07)

Page Figma : `↳ Empty-state`. ComponentSet `Empty-state`, 2 variantes (`Size`).

État d'un conteneur **sans contenu à afficher** : icône optionnelle, titre, description, action optionnelle. Il explique pourquoi la zone est vide et propose, si possible, la prochaine étape.

## Variantes

- **`Size`** :
  - `Compact` : dans une carte, une liste ou une cellule de tableau. 280 px par défaut (`FILL` dans le conteneur), icône 24 px, padding `Spacing/component-lg`, gap `Spacing/component-sm`.
  - `Page` : page entière, panneau ou Drawer. 480 px par défaut, centré dans la zone, icône 32 px, padding `Spacing/component-xl`, gap `Spacing/component-md`.

Aucun fond ni bordure : le conteneur parent porte le cadre.

## Anatomie

`emptyStateRoot` (vertical, centré) → `Empty-icon` · `textGroup` (`Title`, `Description`, gap `Spacing/component-2xs`) · `Action`.

## Propriétés

| Propriété | Type | Défaut | Rôle |
|---|---|---|---|
| `Size` | Variant | `Compact` | Taille |
| `Title` | Text | « Aucun résultat » | Ce qui est vide, en quelques mots |
| `Description` | Text | « Modifiez vos filtres… » | Cause et suite possible, 1 à 2 phrases |
| `Show-icon` | Boolean | true | Affiche `Empty-icon` |
| `Show-action` | Boolean | true | Affiche `Action` |

Instances exposées : `Empty-icon` (instance de `Icon`, pictogramme échangeable, défaut `Tray`) et `Action` (instance de `Button` : `Outlined` en Compact, `Primary` en Page).

## Tokens

| Élément | Token / style |
|---|---|
| Titre | `Text/primary` ; `Misc/Label` (Compact), `Heading/SM` (Page) |
| Description | `Text/secondary` ; `Body/MD` (Compact), `Body/LG` (Page) |
| Icône | `Icon/tertiary` |
| Espacements | `Spacing/component-2xs`, `-sm`, `-md`, `-lg`, `-xl` |

Aucun token créé.

## Règles d'usage

- À utiliser pour : première utilisation (action = créer), recherche ou filtres sans résultat (action = réinitialiser), contenu supprimé ou non accessible. Un seul Empty-state par zone.
- Empty-state ≠ Skeleton : le Skeleton remplace le contenu pendant le chargement ; l'Empty-state apparaît une fois le chargement terminé.
- Empty-state ≠ Alert / Banner : une erreur de chargement est un message de feedback, pas une absence de contenu.
- Ton neutre ou positif, jamais de reproche ; l'action propose une issue concrète.
- Le pattern Filter bar l'utilise pour le cas « zéro résultat » (action « Réinitialiser les filtres »).

## Accessibilité

- Pictogramme décoratif (`aria-hidden="true"`) : le sens est porté par le texte.
- Titre : titre de la hiérarchie de la page (`h2`/`h3`) en `Page`, simple paragraphe en `Compact`.
- Vide consécutif à une action utilisateur (recherche, filtre) : annoncer le résultat dans une région `aria-live="polite"`.
- `Action` : vrai bouton ou lien, atteignable au clavier, cible 44 px.
- Contrastes : `Text/primary` et `Text/secondary` sur le fond du conteneur.
