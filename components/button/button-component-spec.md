# Composant Bouton — Spec de construction

## Propriétés de variante (Figma Component Properties)

- **Type**: `Primary` / `Secondary` / `Destructive`
- **Size**: `SM` / `MD` / `LG`
- **State**: `Default` / `Hover` / `Active` / `Disabled`

## Structure (auto-layout horizontal, hug contents, centré)

```
Button
 ├─ Icon (optionnel, leading)
 ├─ Label
 └─ Icon (optionnel, trailing)
```

- Gap entre icône et label : `Responsive → Spacing/component-xs`
- Text style du Label : **Label** (text style déjà créé) — cohérent avec la règle "Use Label for controls, fields, tabs"

## Tailles (padding, hauteur, radius — tous en Responsive)

| Size | Padding X | Padding Y | Radius | Icon size (px, hors token) |
|---|---|---|---|---|
| SM | `Spacing/component-sm` (12) | `Spacing/component-xs` (8) | `Radius/control` | 16 |
| MD | `Spacing/component-md` (16) | `Spacing/component-sm` (12) | `Radius/control` | 18 |
| LG | `Spacing/component-lg` (20→24) | `Spacing/component-md` (16) | `Radius/control` | 20 |

⚠️ Pas de token dédié à la taille d'icône dans le système actuel — valeurs en dur ici, à créer plus tard si besoin (`Responsive → Icon/size-*`).

## Couleurs par variante × état (tous Semantic, sauf mention)

### Primary
| État | Background | Label |
|---|---|---|
| Default | `Action/primary` | `Text/inverse` |
| Hover | `Action/primary-hover` | `Text/inverse` |
| Active | `Action/primary-active` | `Text/inverse` |
| Disabled | `Background/disabled` | `Text/disabled` |

### Secondary (bordé, fond transparent/neutre)
| État | Background | Label | Border |
|---|---|---|---|
| Default | `Action/secondary` | `Text/primary` | `Border/default` |
| Hover | `Action/secondary-hover` | `Text/primary` | `Border/default` |
| Active | `Action/secondary-hover` ⚠️ | `Text/primary` | `Border/strong` |
| Disabled | `Background/disabled` | `Text/disabled` | `Border/disabled` |

⚠️ Il n'existe pas de token `Action/secondary-active` dans le système actuel — j'ai réutilisé `secondary-hover`. Ajoute le token si tu veux un état actif distinct.

### Destructive
| État | Background | Label |
|---|---|---|
| Default | `Action/destructive` | `Text/inverse` |
| Hover | `Action/destructive-hover` | `Text/inverse` |
| Active | `Action/destructive-active` | `Text/inverse` |
| Disabled | `Background/disabled` | `Text/disabled` |

## Bordure (Secondary uniquement)

- Épaisseur : `Primitive → Border/thin` (pas de couche Semantic/Responsive pour Border, cf. guidelines — bind direct sur Primitive)
- Couleur : voir tableau ci-dessus (`Border/default`, `Border/strong`, `Border/disabled`)

## État Disabled (toutes variantes)

- En plus des couleurs du tableau, applique `Primitive → Opacity/40` sur le calque entier du bouton (pas de token Semantic/Responsive pour Opacity non plus — bind direct sur Primitive).

## Focus (accessibilité, toutes variantes)

- Anneau de focus : stroke externe
  - Couleur : `Semantic → Border/focus`
  - Épaisseur : `Primitive → Border/medium`

## Résumé des tokens utilisés

- **Semantic** : Action/primary(-hover/-active), Action/secondary(-hover), Action/destructive(-hover/-active), Text/inverse, Text/primary, Text/disabled, Background/disabled, Border/default, Border/strong, Border/disabled, Border/focus
- **Responsive** : Spacing/component-xs, component-sm, component-md, component-lg, Radius/control
- **Primitive** : Border/thin, Border/medium, Opacity/40
