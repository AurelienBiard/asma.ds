# Design System

Source de vérité : les 5 fichiers `guidelines/*.yaml` (architecture v5 — core/foundations/agent/decisions/accessibility) et `components/<nom>/<nom>-component-spec.md` de ce repo. Figma (fichier `asma.ds`) et ce repo GitHub sont synchronisés à partir de ces fichiers — jamais l'inverse.

## Structure

```
design-system/
├── tokens/
│   ├── primitive.json    # Couleurs (échelle Tailwind), typo, spacing, radius, border, opacity, grid — mode unique
│   ├── semantic.json     # Couleurs contextuelles — modes Light/Dark
│   └── responsive.json   # Typo, spacing, radius, grid — modes Mobile/Desktop
├── guidelines/
│   ├── core.yaml           # Philosophie, arbre de décision component/variant/slot/pattern
│   ├── foundations.yaml    # Architecture des tokens (Primitive/Semantic/Responsive), scopes Figma
│   ├── agent.yaml          # Comment un agent IA doit lire/appliquer ce repo, contraintes Figma connues
│   ├── decisions.yaml      # Guide de sélection de composant (quel composant pour quel besoin)
│   └── accessibility.yaml  # Règles a11y (contraste, clavier, focus, formulaires)
├── patterns/
│   └── README.md           # Patterns candidats (workflows recurrents multi-composants)
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

Construits dans Figma à partir des specs du repo — voir la source de vérité en tête de ce README.

### Text & Selection inputs (12/12)
| Composant | Statut | Spec |
|---|---|---|
| TextInput | ✅ 32 variantes | `components/text-input/` |
| PasswordInput | ✅ 32 variantes | `components/password-input/` |
| Search | ✅ 32 variantes | `components/search-input/` |
| Textarea | ✅ 32 variantes | `components/textarea/` |
| Code-OTP / PIN | ✅ OTP-cell (32) + 2 assemblages | `components/code-otp/`, `components/pin/` |
| TagInput | ✅ 32 variantes | `components/tag-input/` |
| Checkbox | ✅ 24 variantes | `components/checkbox/` |
| Radio | ✅ 16 variantes | `components/radio/` |
| Switch | ✅ 8 variantes | `components/switch/` |
| Segment / Segmented-control | ✅ 8 + 1 assemblage | `components/segmented-control/` |
| Select / Select-option | ✅ 32 + 4 variantes | `components/select/` |
| Tag | ✅ 18 variantes | `components/tag/` |
| Chip | ✅ 18 variantes | `components/chip/` |

### Date & time / Numeric / File & media (7/7)
| Composant | Statut | Spec |
|---|---|---|
| Calendar | ✅ Calendar-day (7) + assemblage | `components/calendar/` |
| Duration Input | ✅ Duration-segment (8) + assemblage | `components/duration-input/` |
| Stepper | ✅ 3 variantes | `components/stepper/` |
| Range Slider | ✅ 8 variantes | `components/range-slider/` |
| Dropzone | ✅ 5 variantes | `components/dropzone/` |
| Image Upload | ✅ 4 variantes | `components/image-upload/` |
| Color Picker | ✅ 4 variantes (déclencheur seul) | `components/color-picker/` |

### Feedback & navigation
| Composant | Statut | Spec |
|---|---|---|
| Button | ✅ 25 variantes | `components/button/` |
| Dot Indicator | ✅ 6 variantes | `components/dot-indicator/` |
| Icon | ✅ wrapper Phosphor | `components/icon/` |
| Tooltip | ✅ 36 variantes | `components/tooltip/` |
| Alert | ✅ 4 variantes | `components/alert/` |
| Toast | ✅ 4 variantes | `components/toast/` |
| Skeleton | ✅ 3 variantes | `components/skeleton/` |
| Progress (linear/circular) | ✅ 12+12 variantes | voir Figma page `↳ Progress` |
| Step Indicator | ✅ Step-item (3) + assemblages | `components/step-indicator/` |
| Tabs | ✅ Tab-item (4) + assemblage | `components/tabs/` |
| Menu-item | ✅ 8 variantes | `components/menu/` |
| Avatar | ✅ 9 variantes | `components/avatar/` |
| Theme switcher | ✅ 2 variantes, fonctionnel | voir Figma page `↳ Theme switcher` |

### Patterns (page Figma `↳ Navigation`)
| Pattern | Statut |
|---|---|
| Sidebar (Mode=Expanded/Collapsed) | ✅ |
| Topbar (SaaS) | ✅ |
| Site-nav (vitrine) | ✅ |

Text inputs (6/6) et une bonne partie des Selection inputs terminés. Restent : Select, Tag Input (Selection inputs), Calendar, Duration Input (Date & time), Stepper, Range Slider (Numeric inputs), Dropzone, Image Upload, Color Picker (File & media) — voir `guidelines/decisions.yaml` pour le guide de sélection de composant.

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

Le détail complet des règles est réparti sur les 5 fichiers `guidelines/*.yaml` : architecture des tokens et scopes Figma dans `foundations.yaml`, philosophie et arbre de décision dans `core.yaml`, guide de sélection de composant dans `decisions.yaml`, contraintes techniques Figma connues dans `agent.yaml`, règles a11y dans `accessibility.yaml`.
