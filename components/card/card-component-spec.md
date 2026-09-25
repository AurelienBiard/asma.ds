# Composant Card

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : composant construit dans Figma (page `↳ Card`) avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel, pas d'une notre de conception préalable. À valider/corriger si un détail ne correspond pas à l'intention d'origine.

Conteneur borné pour du contenu/action cohérent (`decisions.yaml` → `Card`).

## Propriétés du composant Figma

- **Interaction** (variant) : `Default` / `Hover` / `Focus` — état visuel de prévisualisation uniquement, ne pilote pas le vrai hover/focus applicatif (géré côté app).
- **Title**, **Subtitle**, **Body** (Text)
- **Show-header**, **Show-subtitle**, **Show-footer** (Boolean, défaut `true`)

## Composition — pas de Slot scriptable

Body/Footer sont de simples frames, **pas** de propriété Slot Figma sur ce composant (`figma.createSlot()` n'existe pas dans l'API Plugin — testé et confirmé). Contenu réel à placer manuellement en dupliquant l'instance, ou en la détachant pour un usage ponctuel.

## Tokens

- Fond : `Background/elevated` · Bordure : `Border/default` · Radius : `Radius/lg` (Responsive) · Padding : `Spacing/lg` (Responsive)
- Title : Text Style `Heading/SM` · Subtitle : `Misc/Caption` + `Text/secondary` · Body : `Body/MD`

## Guidelines Figma

Page dédiée `↳ Card`.
