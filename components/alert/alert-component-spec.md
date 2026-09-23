# Composants Alert et Toast

## Alert (page `↳ Alert`)

Feedback **persistant**, intégré au flux de la page — reste visible jusqu'à fermeture ou résolution de la condition.

`Status` = `Info`/`Success`/`Warning`/`Danger`, 4 variantes. Fond/bordure/texte/icône = tokens `Feedback/{status}` correspondants. `Status-icon`, `Description` et `Close-icon` indépendamment affichables (`Show-icon`/`Show-description`/`Show-close`, Boolean). Propriétés `Title`, `Description` (Text).

**Bug corrigé** : la coloration des icônes utilisait un mauvais ID de vecteur (fallback générique au lieu du vecteur réel du pictogramme swappé), donnant `Icon/primary` partout au lieu de la couleur du statut — corrigé en récupérant le vrai vecteur de chaque pictogramme (`CheckCircle`, `Warning`, `WarningCircle`, `Info`) individuellement.

## Toast (page `↳ Toast`, dédiée séparément d'Alert)

Feedback **éphémère**, flottant en superposition — disparaît automatiquement après un délai (4-6s typique, plus long si une Action est présente).

Mêmes 4 `Status` et tokens Feedback qu'Alert, mais plus compact (une seule ligne, pas de `Description`). `Action` textuelle optionnelle (`Show-action`, Semi Bold souligné, ex. "Annuler"/"Voir") en plus de `Show-close`. Propriétés `Title`, `Action-label` (Text).

## Leçons de construction

- Une propriété texte liée via `componentPropertyReferences` peut réinitialiser le `fontName`/`textDecoration` local du calque au moment du binding — toujours réappliquer le style visuel personnalisé (gras, souligné) **après** avoir terminé tous les bindings de propriétés, jamais avant.
- Toujours utiliser le bon ID de vecteur interne par pictogramme — ne jamais réutiliser un seul ID en dur pour plusieurs pictogrammes différents (cause du bug de couleur ci-dessus).
