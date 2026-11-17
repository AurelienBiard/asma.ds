# Composant Card

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : composant construit dans Figma (page `↳ Card`) avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel, pas d'une notre de conception préalable. À valider/corriger si un détail ne correspond pas à l'intention d'origine.

Conteneur borné pour du contenu/action cohérent (`decisions.yaml` → `Card`).

## Propriétés du composant Figma

- **Interactive** (variant) : `True` (défaut) / `False`. **Survol et élévation n'existent que sur une carte cliquable dans son ensemble** (carte-lien vers un détail). `Interactive=False` n'a qu'une variante (`Interaction=Default`) : pas de hover, pas d'ombre, pas de focus. Côté code : `Interactive=True` ⇒ la carte est un vrai `<a>`/`<button>` englobant (voir Accessibilité) ; `Interactive=False` ⇒ conteneur statique (`<div>`/`<article>`), aucun style `:hover`/`:focus-visible`.
- **Style** (variant) : `Outlined` (défaut) / `Subtle`.
  - `Outlined` : fond `Background/elevated` + bordure 1 px `Border/default`.
  - `Subtle` : fond `Background/subtle`, **sans bordure** (Default et Hover).
- **Interaction** (variant) : `Default` / `Hover` / `Focus` — état visuel de prévisualisation uniquement, ne pilote pas le vrai hover/focus applicatif (géré côté app). Hover = élévation (style d'effet `Elevation`, ombre `0 10 25` à 10 %) + bordure `Border/strong` (Outlined uniquement) ; Focus = bordure `Border/focus` 2 px (Outlined et Subtle). Le fond ne change pas au survol.
- Combinaisons existantes : 8 variantes = `Interactive=True` × `Style` × `Interaction` (6) + `Interactive=False` × `Style` en `Default` (2).
- **Title**, **Subtitle**, **Body** (Text)
- **Show-header**, **Show-subtitle**, **Show-footer** (Boolean, défaut `true`)
- **Show-icon** (Boolean, défaut **`false`**) — affiche une icône `Icon` **XLarge** (32 px) en **premier enfant** de la carte, **avant `header`** (espacement vertical de 12 px hérité du layout de la carte, soit +44 px de hauteur quand l'icône est affichée). Nom du calque : `Card-icon`. Couleur de l'icône : `Icon/brand` (changé de `Icon/tertiary` le 2026-11-16) ; l'icône se change via l'instance (Instance swap de l'`Icon` imbriqué). Utilisée pour illustrer le type de contenu (ex. carte de sélection, carte d'information) ; elle est décorative → `aria-hidden="true"` côté code, sauf si elle est seule porteuse de sens.
- **Show-tag** (Boolean, défaut **`false`**) — affiche une instance `Tag` (Type `Neutral`, Size `Small`, sans icônes ; calque `Card-tag`) **dans `header`, à droite du titre**. Le `header` est horizontal : `title-group` (Title + Subtitle, remplit la largeur) puis le Tag, aligné en haut, espacement `Spacing/component-sm`. Le titre se rétrécit et passe à la ligne si besoin ; la hauteur de la carte ne change pas pour un titre d'une ligne. Libellé et `Type` du Tag se modifient sur l'instance (statut, catégorie : texte court). Masqué avec le `header` (`Show-header=false`).

## Composition — pas de Slot scriptable

Body/Footer sont de simples frames, **pas** de propriété Slot Figma sur ce composant (`figma.createSlot()` n'existe pas dans l'API Plugin — testé et confirmé). Contenu réel à placer manuellement en dupliquant l'instance, ou en la détachant pour un usage ponctuel.

## Tokens

- Fond : `Background/elevated` (Outlined) ou `Background/subtle` (Subtle) · Bordure : `Border/default` (Outlined uniquement) · Icône : `Icon/brand` · Radius : `Radius/card` (Responsive) · Padding : `Spacing/component-md` (Responsive)
- Title : Text Style `Heading/SM` · Subtitle : `Misc/Caption` + `Text/secondary` · Body : `Body/MD`

## Guidelines Figma

Page dédiée `↳ Card`.

> **Correction (2026-09-27)** : la spec citait des tokens inexistants (`Radius/lg`, `Spacing/lg`/`Spacing/md` en Responsive, `Shadow/*`, `Overlay/scrim`). Remappés sur l'existant (`Radius/card`, `Spacing/component-md` — valeur déjà utilisée dans Figma) ; ombre et voile documentés sans token, aucun token créé. À répercuter dans Figma.

> **Note (2026-11-16)** : les variantes `Style=Subtle` sont 2 px moins hautes que `Outlined` (pas de bordure comptée dans le layout) — sans incidence quand les cartes s'étirent en hauteur dans une rangée.
