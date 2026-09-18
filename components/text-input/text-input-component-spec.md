# Composant TextInput

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Champ de saisie texte de base — fondation des autres champs texte du système (Email, URL, Username, Phone, Number, Currency, Percentage, Decimal en héritent sans redéfinir de composant séparé). Anciennement nommé `Input`, renommé `TextInput` pour cohérence avec `PasswordInput`.

## Anatomie

- **Field** : conteneur (fond, bordure, radius, padding), hauteur fixe 40px, `layoutSizingHorizontal: FILL` (s'adapte à son conteneur).
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
| Default | `Border/default` |
| Hover | `Border/strong` |
| Focus | `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE` |
| Disabled | `Border/disabled`, fond `Background/disabled`, texte `Text/disabled` |

**Validation prioritaire sur Interaction** pour la bordure — un champ Error en Hover garde la bordure `Feedback/Danger/border`, pas `Border/strong`. Exception documentée : en Disabled, la bordure de validation reste visible même si le champ n'est plus interactif (choix volontaire).

- Fond (hors Disabled) : `Background/elevated`.
- Texte Empty (placeholder) : `Text/tertiary`. Texte Filled (value) : `Text/primary`.
- Icône de statut + message : `Feedback/{Error|Warning|Success}/icon` et `/text`.

## Dimensions et comportement

- Hauteur du Field fixée à 40px — atteinte en évitant `strokeAlign: INSIDE` combiné à un stroke sur un frame en hug (ajoute mystérieusement 2px de hauteur, cause exacte non identifiée malgré investigation ; contournement : construire avec `strokeAlign: OUTSIDE` pour Focus, sinon reconstruire proprement sans jamais appeler `resize()` sur la hauteur si le problème persiste).
- Padding horizontal du Field : `Spacing/component-xs`. Padding vertical : `Spacing/component-sm`.
- Radius : `Radius/control`.
- Placeholder/Value : Text Style `Misc/Label`, troncature 1 ligne avec ellipse (`textTruncation: ENDING`, `maxLines: 1`, `layoutSizingHorizontal: FILL`).
- `clipsContent: false` sur Field et sur le composant global.

## Icônes de statut

Construites selon la méthode standard du DS (voir spec Button) : cloner une instance déjà matérialisée, colorer avant de swapper le pictogramme. Pictogrammes : `WarningCircle` (Error), `Warning` (Warning), `CheckCircle` (Success), tous en `Format=Outline`.

## Guidelines Figma

Page `↳ Text inputs`, section "TextInput". Guidelines génériques du composant `Input` de base partagées avec `PasswordInput` (section "Guidelines" commune sur la page).
