# Composant TextInput

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Champ de saisie texte de base — fondation des autres champs texte du système (Email, URL, Username, Phone, Number, Currency, Percentage, Decimal en héritent sans redéfinir de composant séparé). Anciennement nommé `Input`, renommé `TextInput` pour cohérence avec `PasswordInput`.

## Anatomie

- **field** : conteneur (fond, bordure, radius, padding), hauteur fixe 44px, `layoutSizingHorizontal: FILL` (s'adapte à son conteneur).
- **Placeholder / Value** : texte affiché — propriétés texte dédiées, éditables indépendamment.
- **Status-icon** : icône de statut, visible uniquement si Validation ≠ None.
- **Message** : texte d'aide/erreur sous le champ, visible uniquement si Validation ≠ None — propriété texte dédiée.

## Propriétés du composant Figma

- **Interaction** (variant) : `Default` / `Hover` / `Focus` / `Disabled`
- **Content** (variant) : `Empty` / `Filled`
- **Validation** (variant) : `None` / `Error` / `Warning` / `Success`
- **Placeholder** (Text) : liée aux 16 variantes `Content=Empty`.
- **Value** (Text) : liée aux 16 variantes `Content=Filled`.
- **Message** (Text) : liée aux 24 variantes `Validation≠None` — texte de validation, éditable.

32 variantes (4 Interaction × 2 Content × 4 Validation).

## Règles de couleur

| Interaction | Bordure |
|---|---|
| Default | `Border/subtle` (depuis le 2026-10-29 ; `Border/default` auparavant) — bordure surtout cosmétique, contraste faible assumé (décision 2026-11-02) ; utiliser `Border/default` quand la bordure doit rester bien visible |
| Hover | `Border/strong` |
| Focus | `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE` |
| Disabled | `Border/disabled`, fond `Background/disabled`, texte `Text/disabled` |

Cette règle vaut pour tous les champs de saisie en `Interaction=Default` et `Validation=None` : `TextInput`, `PasswordInput`, `Search`, `Textarea`, `Select`, `TagInput`, `OTP-cell` / `Code-OTP`, `Duration-segment` et `Stepper` (Numeric inputs). Hover reste `Border/strong`. Bordure discrète : le champ se distingue par son fond `Background/elevated` ; à vérifier au regard du contraste des composants d'interface (3:1) avant de généraliser sur fond clair.

**Validation prioritaire sur Interaction** pour la bordure — un champ Error en Hover garde la bordure `Feedback/Danger/border`, pas `Border/strong`. Exception documentée : en Disabled, la bordure de validation reste visible même si le champ n'est plus interactif (choix volontaire).

- Fond (hors Disabled) : `Background/elevated`.
- Texte Empty (placeholder) : `Text/tertiary`. Texte Filled (value) : `Text/primary`. Voir « Règle : couleur du texte d'un champ » ci-dessous.
- Icône de statut + message : `Feedback/{Error|Warning|Success}/icon` et `/text`.

## Règle : couleur du texte d'un champ (2026-11-09)

Règle commune à `TextInput`, `PasswordInput`, `Search`, `Textarea`, `Select` et `TagInput`.

| Situation | Couleur du texte |
|---|---|
| Champ vide (`Content=Empty`), `Interaction` Default, Hover ou Focus | `Text/tertiary` (placeholder) |
| Texte saisi ou valeur choisie (`Content=Filled`) | `Text/primary` |
| `Interaction=Disabled` (placeholder comme valeur) | `Text/disabled` |

- La validation (`Error`, `Warning`, `Success`) **ne change jamais** la couleur du texte du champ : seuls le message et l'icône de statut prennent la couleur `Feedback/{statut}/…`.
- `Select` : « Sélectionner une option » en `Text/tertiary`, l'option choisie en `Text/primary`. `TagInput` : le texte d'ajout (`Input-placeholder`) en `Text/tertiary` ; les tags saisis sont des `Chip`, qui gardent leurs couleurs.
- Le placeholder n'est jamais un libellé (voir `guidelines/accessibility.yaml`) et ne porte pas d'information indispensable.
- Contraste sur le fond du champ (`Background/elevated`) : `Text/tertiary` 7,58:1 en Light, 5,71:1 en Dark ; `Text/primary` 17,85:1 et 13,98:1.

**Code**

```css
.field { color: var(--color-text-primary); }
.field::placeholder { color: var(--color-text-tertiary); opacity: 1; }   /* opacity: 1 pour Firefox */
.field:disabled,
.field:disabled::placeholder { color: var(--color-text-disabled); }
/* Select personnalisé : valeur vide */
.select__value[data-empty] { color: var(--color-text-tertiary); }
```

## Dimensions et comportement

- **Décision (2026-11-02)** : 44 px est la hauteur définitive de tous les champs de saisie ; le 40 px est abandonné, aucune variante à 40 px.
- Hauteur du Field fixée à 44px (padding vertical `Spacing/component-sm` moins la bordure de 1px, + ligne de 20px ; la spec disait 40px par erreur jusqu'au 2026-10-29) — atteinte en évitant `strokeAlign: INSIDE` combiné à un stroke sur un frame en hug (ajoute mystérieusement 2px de hauteur, cause exacte non identifiée malgré investigation ; contournement : construire avec `strokeAlign: OUTSIDE` pour Focus, sinon reconstruire proprement sans jamais appeler `resize()` sur la hauteur si le problème persiste).
- Padding horizontal du Field : `Spacing/component-xs`. Padding vertical : `Spacing/component-sm`.
- Radius : `Radius/control`.
- Placeholder/Value : Text Style `Misc/Label`, troncature 1 ligne avec ellipse (`textTruncation: ENDING`, `maxLines: 1`, `layoutSizingHorizontal: FILL`).
- `clipsContent: false` sur Field et sur le composant global.
- **Conteneurs parents** : la bordure Focus est dessinée à l'extérieur du champ (`strokeAlign: OUTSIDE`) ; les cadres qui contiennent un champ (formulaires, rangées, cartes) ne doivent pas rogner leur contenu (`clipsContent: false`), sinon l'anneau de focus est coupé. Vaut pour tous les champs de saisie.

## Icônes de statut

Construites selon la méthode standard du DS (voir spec Button) : cloner une instance déjà matérialisée, colorer avant de swapper le pictogramme. Pictogrammes : `WarningCircle` (Error), `Warning` (Warning), `CheckCircle` (Success), tous en `Format=Outline`.

## Guidelines Figma

Page `↳ Text inputs`, section "TextInput". Guidelines génériques du composant `Input` de base partagées avec `PasswordInput` (section "Guidelines" commune sur la page).
