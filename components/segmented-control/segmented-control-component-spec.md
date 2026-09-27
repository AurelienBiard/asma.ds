# Composants Segment et Segmented-control

> Ce fichier est la **source de vérité** des deux composants (le second assemble le premier). Toute modification se fait ici en premier, puis est répercutée dans Figma.

## Composant atomique : Segment

Onglet individuel, réutilisé par Segmented-control.

- **Propriétés** : `Selected` (False/True) × `Interaction` (Default/Hover/Focus/Disabled), 8 variantes. Propriété texte `Label`.
- Selected=True : fond `Background/elevated` (se détache du conteneur neutre), texte `Text/primary`.
- Selected=False : transparent, texte `Text/tertiary` (Hover : fond `Action/ghost-hover`).
- Focus : bordure `Border/focus` + `Primitive/Border/medium`, `strokeAlign: OUTSIDE`.
- Disabled : texte `Text/disabled`, fond `Background/disabled` si Selected=True sinon transparent.
- Padding : `Spacing/component-sm` (horizontal) / `Spacing/component-xs` (vertical), radius `Radius/control`.

## Segmented-control (assemblage)

Conteneur `Action/neutral`, padding `Primitive/Spacing/2xs`, radius `Radius/control`, contenant 3 instances de `Segment` avec un gap de 4px. Exemple construit avec le 2ᵉ segment sélectionné. Propriété **Motion** (variant) : `Static` (défaut) / `Tension` — voir ci-dessous.

## Usage

Réserver à un petit nombre d'options (2 à 5) toutes visibles sans défilement. Au-delà, utiliser un Select ou des Tabs.

## Guidelines Figma

Page `↳ Selection inputs`, section "Segment" et section "Segmented-control" + section "Guidelines" complète (couvre Checkbox/Radio/Switch/Segmented Control ensemble).

## Variante Motion=Tension (ajoutée le 2026-09-27)

Propriété **Motion** (variant) : `Static` (défaut) / `Tension`. Même concept, même comportement, même anatomie — seule la façon dont l'état sélectionné se déplace change (règle `decisions.yaml` → `variant.motion_note`).

### Anatomie

- **Tension-layer** : couche `aria-hidden`, placée **sous** les Segments, en retrait `Primitive/Spacing/2xs` (le padding du conteneur), filtre SVG `asma-tension` (`foundations.yaml` → `motion.tension`).
- **Indicator** : forme opaque `Background/elevated`, radius `Radius/control`, de la taille du Segment sélectionné. C'est elle qui porte le fond « Selected=True » : les Segments deviennent transparents dans cette variante (texte `Text/primary` si sélectionné, `Text/tertiary` sinon, inchangé).
- **Drop** : copie de l'Indicator posée sur l'ancienne position, visible uniquement pendant la transition.

### Comportement

Au changement de sélection :
1. le bord d'attaque de l'Indicator (côté de la nouvelle option) part en `Motion/Duration/sm` + `Motion/Easing/spring` (léger rebond) ; le bord de fuite suit en `Motion/Duration/md` + `Motion/Easing/standard` → la forme s'étire puis se rétracte ;
2. le Drop se contracte sur l'ancienne position en `Motion/Duration/md` + `Motion/Easing/accelerate` ; le filtre le fait se détacher de l'Indicator comme une gouttelette.

Plus l'écart entre deux options est grand, plus l'étirement est visible.

### Règle d'usage

- Autorisée ici parce que l'Indicator est **opaque**, **unique** et porte un **changement d'état**. Voir la liste complète dans `foundations.yaml` → `motion.usage_rules`.
- Ne jamais filtrer les Segments eux-mêmes (texte, focus) : uniquement la Tension-layer.
- L'ombre portée du Segment sélectionné (Static) est absente en Tension (le filtre ne la conserve pas) ; les angles de l'Indicator sont légèrement adoucis par le flou — écart accepté.

### Accessibilité

Inchangée par rapport à `Static` : `role="radiogroup"`, Segments `role="radio"` + `aria-checked`, sélection lisible sans animation (couleur du texte + position de l'Indicator). `prefers-reduced-motion: reduce` → ni transition ni Drop.

### Implémentation de référence

```html
<!-- Filtre partagé, une fois par page (valeurs = Motion/Tension/*) -->
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <filter id="asma-tension" x="-20%" y="-60%" width="140%" height="220%" color-interpolation-filters="sRGB">
    <feGaussianBlur in="SourceGraphic" stdDeviation="4"/>
    <feColorMatrix mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7"/>
  </filter>
</svg>
```

```css
.tension-layer { position: absolute; inset: var(--spacing-scale-2xs); pointer-events: none; filter: url(#asma-tension); }
.tension-indicator, .tension-drop { position: absolute; top: 0; bottom: 0; background: var(--color-background-elevated); border-radius: var(--radius-control); }
/* Déplacement vers la droite : bord droit = bord d'attaque. Inverser left/right vers la gauche. */
.tension-indicator { transition:
  left  var(--motion-duration-scale-md) var(--motion-easing-scale-standard),
  right var(--motion-duration-scale-sm) var(--motion-easing-scale-spring); }
.tension-drop { animation: tension-drop var(--motion-duration-scale-md) var(--motion-easing-scale-accelerate) forwards; }
@keyframes tension-drop { 0% { transform: scale(1); } 55% { transform: scale(.55, .7); } 100% { transform: scale(0); } }
@media (prefers-reduced-motion: reduce) { .tension-indicator { transition: none; } .tension-drop { display: none; } }
```

Positions (N options, gap `Spacing/component-2xs`) : `left: calc(i × ((100% − (N−1)×4px) / N + 4px))`, `right` symétrique avec `N−1−i`.

