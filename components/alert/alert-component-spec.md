# Composants Alert et Toast

## Alert (page `↳ Alert`)

Feedback **persistant**, intégré au flux de la page — reste visible jusqu'à fermeture ou résolution de la condition.

`Status` = `Info`/`Success`/`Warning`/`Danger`, 4 variantes. Fond/bordure/texte/icône = tokens `Feedback/{status}` correspondants. `Status-icon`, `Description` et `Close-icon` indépendamment affichables (`Show-icon`/`Show-description`/`Show-close`, Boolean). Propriétés `Title`, `Description` (Text).

**Bug corrigé** : la coloration des icônes utilisait un mauvais ID de vecteur (fallback générique au lieu du vecteur réel du pictogramme swappé), donnant `Icon/primary` partout au lieu de la couleur du statut — corrigé en récupérant le vrai vecteur de chaque pictogramme (`CheckCircle`, `Warning`, `WarningCircle`, `Info`) individuellement.

## Toast (page `↳ Toast`, dédiée séparément d'Alert)

Feedback **éphémère**, flottant en superposition — disparaît automatiquement après un délai (4-6s typique, plus long si une Action est présente).

Mêmes 4 `Status` et tokens Feedback qu'Alert, mais plus compact (une seule ligne, pas de `Description`). `Action` textuelle optionnelle (`Show-action`, Semi Bold souligné, ex. "Annuler"/"Voir") en plus de `Show-close`. Propriétés `Title`, `Action-label` (Text).

**Text Styles du Toast (2026-11-01)** : `Title` en `Body/MD` (14/20, Regular) — auparavant `Body/SM` (12/16) ; `Action-label` reste en `Misc/Label` (14/20, Semi Bold). Le Toast passe de 274 à 297 px de large (largeur hug), hauteur inchangée (46 px).

**Placement du Toast (2026-11-02)** :

- **Desktop** : ancré au viewport (`position: fixed`), coin droit, à **40 px** des bords — en bas (`bottom: 40px`, placement par défaut) ou en haut (`top: 40px`).
- **Mobile** : **centré horizontalement**, ancré en bas.
- **Zones fixes** (barre de navigation, en-tête, pied collant, barre de retour mobile `OS / BreadCrumbMobile` de 60 px dans ASMA OS…) : le toast ne doit **jamais être masqué ni se superposer** à une zone fixe. Le placement s'adapte : le décalage de 40 px se mesure depuis le bord libre de la zone fixe, pas depuis le bord de l'écran. Sur mobile, prendre aussi en compte la zone de sécurité (`env(safe-area-inset-bottom)`).
- Plusieurs toasts simultanés : empilés, convention (plus récent en haut ou en bas) à fixer une fois pour toutes par produit.

**Espacement du Toast (2026-10-13)** : padding de `Spacing/component-sm` (12px) sur les 4 côtés (le vertical était de 10px en dur) ; gap de `Spacing/component-xs`. Hauteur passée de 42 à 46px.

## Leçons de construction

- Une propriété texte liée via `componentPropertyReferences` peut réinitialiser le `fontName`/`textDecoration` local du calque au moment du binding — toujours réappliquer le style visuel personnalisé (gras, souligné) **après** avoir terminé tous les bindings de propriétés, jamais avant.
- Toujours utiliser le bon ID de vecteur interne par pictogramme — ne jamais réutiliser un seul ID en dur pour plusieurs pictogrammes différents (cause du bug de couleur ci-dessus).
