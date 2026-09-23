# Composants Select et Select-option

## Select (déclencheur)

Base identique à TextInput (32 variantes Interaction × Content × Validation), icône trailing = `CaretDown` (fixe, non interactif) au lieu/en plus d'une icône de statut — les deux coexistent (`Status-icon` puis `Caret-icon`) si `Validation≠None`. Propriétés `Placeholder`, `Value`, `Message`.

## Select-option (item de liste)

État = `Default`/`Hover`/`Selected`/`Disabled`, 4 variantes (pas d'axe `Indent` — retiré sur demande, une hiérarchie de menu profonde n'a pas sa place ici).

**Structure `Left`** (FILL, texte tronqué proprement) :
- `Checkbox-slot`, `Radio-slot`, `Switch-slot` : **vraies instances imbriquées** de nos composants Checkbox/Radio/Switch (pas de simples icônes) — chacune synchronisée automatiquement avec le `State` de l'option (`Selected` → `Checked`/`Selected`/`On`=`True`), Boolean `Show-checkbox`/`Show-radio`/`Show-switch`.
- `Leading-icon` : icône de contenu indépendante (drapeau, avatar…), Boolean `Show-icon` (défaut `true`).
- `Label` (FILL, `Show-icon-leading`... texte tronqué en fin de ligne).

**Expand-icon** (chevron) : enfant direct de l'item (pas dans `Left`), `Show-expand` (Boolean) — toujours justifié à droite via `primaryAxisAlignItems: SPACE_BETWEEN` sur l'item.

## Leçons de construction

- Pour insérer une instance d'un ComponentSet existant dans un nouveau composant : `variant.createInstance()` sur la variante ciblée, puis `setProperties()` avec la clé complète (`Object.keys(instance.componentProperties)`).
- `Left` doit être en `layoutSizingHorizontal: FILL` pour que `Label` (également FILL) profite de l'espace disponible et tronque correctement un texte long.

Doc complète : voir aussi `components/checkbox/`, `components/radio/`, `components/switch/` pour les sous-composants réutilisés.
