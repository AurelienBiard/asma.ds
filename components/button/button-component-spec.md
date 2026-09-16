# Composant Bouton — Spec de construction (v2)

Une seule taille pour l'instant (MD) — pas de variant Size à prévoir.

## Propriétés de variante (Figma Component Properties)

- **Type**: `Primary` / `Outlined` / `Neutral` / `Ghost` / `Link`
- **State**: `Default` / `Hover` / `Active` / `Disabled` / `Focus`
- **Icon-only**: `Boolean` — modificateur de forme combinable avec n'importe quel Type (carré, label masqué visuellement mais gardé pour l'accessibilité)

## Structure (auto-layout horizontal, hug contents, centré)

```
Button
 ├─ Icon (slot, optionnel, leading)
 ├─ Label
 └─ Icon (slot, optionnel, trailing)
```

- Gap : `Responsive → Spacing/component-xs`
- Padding X : `Spacing/component-md` — Padding Y : `Spacing/component-sm`
- Radius : `Responsive → Radius/control`
- Text style : **Label**

## Tokens par type × état

### Primary (filled, brand)
| État | Background | Texte |
|---|---|---|
| Default | `Action/primary` | `Text/inverse` |
| Hover | `Action/primary-hover` | `Text/inverse` |
| Active | `Action/primary-active` | `Text/inverse` |

### Outlined (fond plein neutre + bordure)
| État | Background | Texte | Border |
|---|---|---|---|
| Default | `Action/secondary` | `Text/primary` | `Border/default` |
| Hover | `Action/secondary-hover` | `Text/primary` | `Border/default` |
| Active | `Action/secondary-active` **(nouveau token)** | `Text/primary` | `Border/strong` |

### Neutral (filled, gris) — **nouveaux tokens**
| État | Background | Texte |
|---|---|---|
| Default | `Action/neutral` | `Text/primary` |
| Hover | `Action/neutral-hover` | `Text/primary` |
| Active | `Action/neutral-active` | `Text/primary` |

### Ghost (transparent par défaut) — **nouveaux tokens**
| État | Background | Texte |
|---|---|---|
| Default | transparent (pas de token) | `Text/primary` |
| Hover | `Action/ghost-hover` | `Text/primary` |
| Active | `Action/ghost-active` | `Text/primary` |

### Link (texte seul, pas de fond/bordure/padding) — **aucun nouveau token, réutilise Text/link**
| État | Background | Texte | Décoration |
|---|---|---|---|
| Default | transparent | `Text/link` | aucune |
| Hover | transparent | `Text/link` | souligné |
| Active | transparent | `Text/link` | souligné + légèrement plus sombre (opacité, pas de nouveau token) |

⚠️ Link n'a pas de padding, radius ni Focus-ring identique aux autres types (à traiter au cas par cas — souligné au focus suffit généralement).

## Icon-only (modificateur de forme)

S'applique à n'importe quel Type ci-dessus. Devient carré (padding égal sur les 4 côtés, `Spacing/component-sm`), le label reste dans la structure pour l'accessibilité (`aria-label` en Figma / attribut HTML) mais n'est pas affiché visuellement. Ne s'applique pas à Link (pas de padding à carrer).

## Icônes — bibliothèque et convention

- **Source** : Phosphor Icons, copié-collé en composants réels (pas une Team Library externe — voir `icon_library` dans les guidelines pour le raisonnement).
- **Emplacement dans Figma** : page `🎨 FOUNDATION / ↳ Icons`, sections organisées par catégorie (Weather & Nature, Communication, Maps & Travel, Media, Time, Games, Design, etc. — même taxonomie que Phosphor).
- **Structure** : chaque icône est un `COMPONENT_SET` avec deux propriétés de variante : `Format` (Stroke / Outline) et `Weight` (Regular / Thin / Light / Bold / Fill / Duotone).
- **Propriété `Weight`** : toujours **Regular** pour les icônes de bouton (convention documentée, pas une Variable — les propriétés de variante d'un composant ne sont pas bindables sur nos tokens).
- **Propriété `Format`** : Stroke (cohérent avec le style filaire des icônes de démo).
- **Pas de mise à jour automatique** : ces composants sont une copie figée au moment du copier-coller — une future mise à jour de Phosphor ne se répercutera pas ici (limite acceptée, commune à toute méthode d'import Phosphor dans Figma).

## États communs à tous les types

### Disabled
- Background : `Background/disabled`
- Texte : `Text/disabled`
- Border (si applicable, Outlined) : `Border/disabled`
- Opacité : `Primitive → Opacity/40` (0.4 — pas bindable nativement sur `opacity` du node en Figma, valeur littérale)

### Focus (accessibilité)
- Anneau externe : `Semantic → Border/focus`, épaisseur `Primitive → Border/medium`
- Identique pour les 4 types — se combine visuellement avec l'état Default de chaque type

## Nouveaux tokens Semantic à créer dans Figma (Light/Dark)

| Token | Light | Dark |
|---|---|---|
| `Action/secondary-active` | `#e2e8f0` | `#334155` |
| `Action/neutral` | `#f1f5f9` | `#1e293b` |
| `Action/neutral-hover` | `#e2e8f0` | `#334155` |
| `Action/neutral-active` | `#cbd5e1` | `#475569` |
| `Action/ghost-hover` | `#f1f5f9` | `#1e293b` |
| `Action/ghost-active` | `#e2e8f0` | `#334155` |

## Résumé des tokens utilisés

- **Semantic** : Action/primary(-hover/-active), Action/secondary(-hover/-active), Action/neutral(-hover/-active), Action/ghost-hover/-active, Text/inverse, Text/primary, Text/disabled, Background/disabled, Border/default, Border/strong, Border/disabled, Border/focus
- **Responsive** : Spacing/component-xs, component-sm, component-md, Radius/control
- **Primitive** : Border/thin, Border/medium, Opacity/40
