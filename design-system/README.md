# Design System

Source de vérité : Figma (fichier `asma.ds`, 3 collections de variables — *Primitive*, *Semantic*, *Responsive*). Ce repo garde une copie synchronisée de ces tokens pour le code (CSS) et pour la documentation lue par un agent IA.

## Structure

```
design-system/
├── tokens/
│   ├── primitive.json    # Couleurs (échelle Tailwind), typo, spacing, radius, border, opacity, grid — mode unique
│   ├── semantic.json     # Couleurs contextuelles — modes Light/Dark
│   └── responsive.json   # Typo, spacing, radius, grid — modes Mobile/Desktop
├── guidelines/
│   └── design-system-ai-guidelines.yaml   # Règles d'usage, architecture, scopes Figma
├── scripts/
│   └── build_css.py      # Génère dist/tokens.css depuis les 3 fichiers tokens/
└── dist/
    └── tokens.css         # Custom properties CSS, prêt à inclure
```

## Utiliser les tokens dans le portfolio

Inclure `dist/tokens.css` avant ton propre CSS :

```html
<link rel="stylesheet" href="tokens.css">
```

- **Thème sombre** : ajoute `data-theme="dark"` sur `<html>` (ou `<body>`) pour basculer les couleurs Semantic.
- **Responsive** : les valeurs Mobile sont la base (`:root`), le `@media (min-width: 768px)` surcharge automatiquement vers les valeurs Desktop — rien à faire côté HTML.

```css
.button {
  background: var(--color-action-primary);
  padding: var(--spacing-component-md) var(--spacing-component-lg);
  border-radius: var(--radius-control);
  font-size: var(--font-size-body-md);
}
```

## Régénérer le CSS après un changement de tokens

1. Modifier les variables dans Figma.
2. Mettre à jour `tokens/*.json` (export live depuis Figma, ou export du plugin *Export/Import Variables*).
3. `python3 scripts/build_css.py`

## Conventions de nommage CSS

| Source | Exemple Figma | Variable CSS |
|---|---|---|
| Primitive Color | `Color/Blue/600` | `--color-blue-600` |
| Primitive (autres, suffixe `-scale-` pour éviter les collisions avec Responsive) | `Radius/pill` | `--radius-scale-pill` |
| Semantic | `Action/primary` | `--color-action-primary` |
| Semantic (Feedback, imbriqué) | `Feedback/Danger/text` | `--color-feedback-danger-text` |
| Responsive | `Spacing/component-md` | `--spacing-component-md` |
| Responsive Typography | `Typography/body-md/Font-size` | `--font-size-body-md` |

Le détail complet des règles (architecture, quand utiliser primitive vs semantic vs responsive, scopes Figma) est dans `guidelines/design-system-ai-guidelines.yaml`.
