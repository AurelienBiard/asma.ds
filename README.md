# Design System

Source de vérité : les fichiers `guidelines/design-system-ai-guidelines.yaml` et `components/<nom>/<nom>-component-spec.md` de ce repo. Figma (fichier `asma.ds`) et ce repo GitHub sont synchronisés à partir de ces fichiers — jamais l'inverse.

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

## Microcopy (tokens/content.json)

Textes UI réutilisables (labels de boutons, messages de feedback, placeholders), séparés du design (couleurs/spacing/typo) qui reste dans les tokens Figma. Structure par langue (`fr` pour l'instant, prêt à accueillir `en` plus tard sans tout restructurer).

```js
const copy = await fetch('tokens/content.json').then(r => r.json());
button.textContent = copy.fr.actions.save; // "Enregistrer"
```

## Composants

Composants (Bouton, Dot Indicator, etc.) construits dans Figma à partir des specs du repo — voir la source de vérité en tête de ce README.

Flux de travail :
1. Toute décision (nouveau token, nouveau composant, nouvel état/variant) est écrite ou modifiée dans le `.yaml`/`.md` correspondant, dans le repo.
2. Cette spec est ensuite poussée vers Figma (construction/mise à jour du composant via l'API du plugin Figma, ou du token via les Variables).
3. Si un ajustement est fait directement dans Figma (itération manuelle par le designer), il doit être reporté dans le `.md`/`.yaml` correspondant pour rester la référence — Figma ne doit jamais diverger silencieusement de la spec écrite.

**Priorité du projet** : ce design system doit être lisible par un agent IA pour permettre un prototypage rapide. Chaque page Guidelines Figma suit une structure homogène reflétant son `.md` source : titres de section préfixés `H2:`, et un bloc final "Spécifications techniques" listant la propriété de variante exacte et sa correspondance avec les tokens Primitive/Semantic/Responsive.

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
