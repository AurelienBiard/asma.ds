# Audit — Button (skill `improve-ui`)

## Design language

- **Audited surface** : composant `Button` (Figma, ComponentSet `34:41`), et son usage réel comme bouton attaché dans `Search` (`Search-button`, instance `Icon-only=true`).
- **Design sources** : `components/button/button-component-spec.md` (source de vérité déclarée), `components/search-input/search-input-component-spec.md`, état live du composant Figma.
- **Documented decisions** : `Icon-only` (Boolean) "non lié automatiquement à `Show-label`" et nécessite d'"ajuster le padding à la main pour un rendu carré (limitation Figma documentée)" — `button-component-spec.md`, section Icon-only.
- **Governing owners and consumers** : `Button` est le owner (composant source). Consommateur vérifié : `Search-button` (composant `Search`), seul usage réel actuel d'`Icon-only=true` trouvé dans le système.
- **Explicit exceptions** : `search-input-component-spec.md` documente déjà que le pictogramme du bouton attaché de Search hérite d'Acorn (Primary par défaut) plutôt que de la loupe, et que ceci doit être changé manuellement (Swap instance). Exception connue, non traitée dans cet audit — pas une régression, une décision déjà actée et journalisée.

## Findings

| # | Problem | Evidence | Proposed change | Scope | Confidence |
|---|---|---|---|---|---|
| 1 | `Icon-only=true` ne produit pas de padding symétrique — l'instance réelle `Search-button` (40×40) porte le padding par défaut de Button (`16/16/12/12`), donnant une zone de contenu 8×16 au lieu d'un carré centré. | Lu en direct sur l'instance : `paddingLeft/Right=16, paddingTop/Bottom=12`, taille du frame `40×40`. Le spec documente la limitation en général mais ne fixe pas de valeur cible. | Fixer une convention explicite dans le spec (ex. padding égal `Spacing/component-xs` sur les 4 côtés quand `Icon-only=true`) + l'appliquer manuellement à `Search-button` et tout futur bouton icon-only. | Localisé — 1 instance actuellement affectée, mais la convention manquante affecterait tout futur bouton icon-only. | Haute — mesuré directement sur le composant, pas une supposition. |

## Improve first

**Finding #1** — c'est la seule instance réelle d'`Icon-only` dans le système à ce jour, donc l'effort de correction est minimal (une instance), mais laisser la limitation sans valeur cible documentée garantit que chaque futur bouton icon-only répétera le même écart visuel. Fixer la convention maintenant, pendant qu'il n'y a qu'un seul cas à corriger rétroactivement, coûte moins cher que de le découvrir sur plusieurs instances plus tard.

---

*Ce plan ne modifie pas le produit — décisions à valider par l'utilisateur avant exécution par un autre agent (ou moi, sur confirmation explicite).*
