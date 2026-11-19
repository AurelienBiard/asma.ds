# Pattern FileUpload

> **Statut** : spec seule (2026-11-19), pas encore de page Figma. Agencement de composants existants ; aucun composant nouveau. **Décision (2026-11-19)** : `Image-upload` reste documenté avec `Dropzone` et `Color Picker` sur la page `↳ File & media` (`components/dropzone/`) ; il n'est pas déplacé dans ce pattern. Les choix marqués « proposé » sont à valider.

## Purpose

Permettre d'ajouter un ou plusieurs fichiers par glisser-déposer ou parcours de fichiers, voir la progression et traiter les fichiers refusés ou en échec.

## Use when

- Import de documents ou d'images dans un formulaire ou une page.

## Do not use when

- Choix parmi des fichiers existants → `Select` ou `Command`.
- Photo de profil seule → `Avatar` avec `Image-upload` (image carrée unique, 96×96).

## Components

- `Dropzone` (`State` Default/Hover/Dragging/Error/Disabled) — zone multi-fichiers.
- `Image-upload` (`State` Empty/Filled/Hover/Disabled) — image carrée unique.
- `Progress` — progression par fichier.
- `Alert` ou texte d'erreur inline — fichiers refusés ; `Button` — retirer ou réessayer.

## Structure

`Dropzone` suivie d'une liste verticale des fichiers ajoutés (nom, taille, `Progress`, action de retrait) (disposition de ligne proposée).

## Interaction flow

1. Déposer des fichiers sur la zone (état `Dragging`) ou l'activer pour ouvrir le sélecteur de fichiers.
2. Chaque fichier est contrôlé (type, taille) avant l'envoi ; les fichiers refusés sont listés avec la raison.
3. Les fichiers acceptés sont envoyés avec un `Progress` déterminé ; un fichier peut être retiré ou réessayé.
4. À la fin, la liste montre le résultat ; un `Toast` est optionnel.

## States

Dropzone : Default, Hover, Dragging, Error, Disabled. Ligne de fichier : en attente, en cours (`Progress`), terminé, échec (réessayer), refusé.

## Validation/errors

Les contraintes (types, taille max, nombre max) sont énoncées dans la zone avant l'action. Un refus dit quelle règle échoue et ne bloque pas les autres fichiers.

## Accessibility

La zone est un vrai bouton / input fichier atteignable au clavier (le glisser-déposer n'est jamais le seul moyen) ; progression exposée avec `role="progressbar"` ou un texte équivalent ; fichiers ajoutés, retirés et en échec annoncés dans une région live.

## Responsive behavior

Sur écran tactile, la zone est une cible qui ouvre le sélecteur ; le libellé « déposez ici » est remplacé par une formulation neutre (proposé).

## Tokens

Aucun propre (voir `Dropzone`).

## Related components/patterns

`Dropzone`, `Image-upload`, `Progress`, `Alert`, `Button` ; patterns `Form`, `States`.
