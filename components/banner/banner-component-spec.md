# Composant Banner (2026-11-07)

Page Figma : `↳ Banner`. ComponentSet `Banner`, 8 variantes (`Status` × `Form`).

Feedback **persistant** et **de portée contextuelle** : un message qui concerne une zone ou toute la page, avec une ou deux actions et une fermeture optionnelles. Il reste visible jusqu'à fermeture ou résolution de la condition.

## Banner, Alert, Toast : quand utiliser quoi

| Composant | Portée | Durée | Position |
|---|---|---|---|
| Toast | Confirmation d'une action | Éphémère (auto-fermeture) | Flottant, `position: fixed` |
| Alert | Un bloc ou un formulaire (titre + description) | Persistant | Dans le flux, au niveau du contenu concerné |
| Banner | Une page entière ou une section, avec actions | Persistant | `Inline` dans le contenu, `Page` sous la barre du haut |

Le Banner est une ligne unique (message court + actions). Pour un titre et une description, utiliser Alert. Ne pas créer d'Alert pour un message de page : utiliser `Banner/Page`.

## Variantes

- **`Status`** : `Info` · `Success` · `Warning` · `Danger`. Tokens `Feedback/{Status}` correspondants.
- **`Form`** :
  - `Inline` : arrondi (`Radius/control`), bordure 1 px sur les 4 côtés, largeur 560 par défaut (le composant se met en `FILL` dans le contenu) ;
  - `Page` : pleine largeur (1280 par défaut, `FILL` en code), **angles droits**, bordure **inférieure uniquement** (1 px), placé directement sous la barre du haut, dans le flux (il repousse le contenu, jamais en superposition).

## Anatomie

`bannerRoot` (horizontal, padding 12 sur les 4 côtés, gap 8, alignement vertical centré)
→ `Status-icon` (20 × 20) · `Message` (FILL, `Body/MD`) · `Action-1` · `Action-2` · `Close-icon` (16 × 16).

## Propriétés

| Propriété | Type | Défaut | Rôle |
|---|---|---|---|
| `Status` | Variant | `Info` | Couleurs et pictogramme |
| `Form` | Variant | `Inline` | Forme (voir ci-dessus) |
| `Message` | Text | — | Message court, une à deux lignes |
| `Show-icon` | Boolean | true | Affiche `Status-icon` |
| `Show-action-1` | Boolean | true | Affiche `Action-1` |
| `Show-action-2` | Boolean | false | Affiche `Action-2` |
| `Show-close` | Boolean | true | Affiche `Close-icon` |

`Action-1` est une instance de `Button` `Type=Outlined` (action principale) ; `Action-2` une instance de `Button` `Type=Ghost` (action secondaire). Libellé et icône modifiables par instance. `Action-2` ne s'affiche jamais sans `Action-1`.

## Tokens

| Élément | Token |
|---|---|
| Fond | `Feedback/{Status}/background` |
| Bordure | `Feedback/{Status}/border` |
| Message | `Feedback/{Status}/text` |
| Icône de statut, icône de fermeture | `Feedback/{Status}/icon` |
| Rayon (`Inline`) | `Radius/control` |
| Padding | 12 (`Spacing/component-sm`), gap 8 |

Aucun token créé.

## Hauteur

Les actions sont des `Button` de 44 px : avec au moins une action, le Banner mesure 68 à 70 px (44 + padding 24 + bordure). Sans action, il se réduit à la hauteur du message (hug).

## Règles d'usage

- Un seul `Banner/Page` visible à la fois ; en cas de messages multiples, afficher le plus sévère (Danger > Warning > Info > Success).
- `Banner/Page` : directement sous la barre du haut, sous les zones fixes. Il défile avec la page, sauf décision contraire du produit.
- Message court et actionnable ; jamais de lien ou d'information critique uniquement dans le Banner.
- `Success` : fermable et temporaire de préférence. `Danger` : ne se ferme que lorsque la condition est résolue (`Show-close` = false).
- Mobile : le message passe sur plusieurs lignes ; les actions passent sous le message (retour à la ligne, en code).

## Accessibilité

- `role="status"` (`aria-live="polite"`) pour `Info` et `Success` ; `role="alert"` pour `Warning` et `Danger`.
- Le pictogramme est décoratif (`aria-hidden="true"`) : le statut est porté par le texte du message, jamais par la couleur seule.
- Bouton fermer : `<button>` avec `aria-label="Fermer"`, zone cliquable **44 × 44** (le pictogramme reste à 16 px), focus visible.
- Contrastes : mêmes paires `Feedback/{Status}/text` sur `Feedback/{Status}/background` qu'Alert.
- Apparition : pas de déplacement de focus automatique ; le lecteur d'écran l'annonce via le rôle.
