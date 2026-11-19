# Pattern Confirmation

> **Statut** : spec seule (2026-11-19), pas encore de page Figma. Formalise la confirmation déjà exigée par `BulkActions` et `Dialog-toolbar`. Aucun composant nouveau. Les choix marqués « proposé » sont à valider.

## Purpose

Faire confirmer une fois une action destructive ou irréversible, en énonçant la conséquence exacte, puis donner un retour.

## Use when

- Suppression définitive, perte de données, action qui touche d'autres personnes.
- Une action groupée (une seule confirmation pour tout le lot).

## Do not use when

- Une action réversible : l'exécuter et proposer Annuler dans un `Toast` plutôt que demander avant.
- Une information non destructive → `Banner` ou `Toast`.

## Components

- `Dialog` (`Dialog-header`, `Dialog-body`, `Dialog-footer`) — la confirmation.
- `Button` — `Destructive` (type de Button ; voir `components/button/`) pour l'action qui confirme, `Ghost`/`Outlined` pour Annuler.
- `Toast` — le résultat, avec Annuler/Restaurer quand c'est possible.

## Structure

En-tête : la question nommant l'objet et le nombre (« Supprimer 5 entreprises ? »). Corps : les conséquences en une ou deux phrases. Pied : Annuler (à gauche de l'action qui confirme) et l'action destructive libellée par le verbe, jamais « OK ».

## Interaction flow

1. L'utilisateur déclenche l'action ; le `Dialog` s'ouvre ; le focus va sur Annuler (l'action sûre).
2. Confirmer exécute l'action une fois ; Échap ou Annuler ferme sans effet.
3. Un seul `Toast` rend compte du résultat pour tout le lot, avec Annuler/Restaurer si l'action est réversible côté serveur.

## States

Ouvert, en cours de confirmation (action en cours, boutons désactivés), succès, erreur (`Toast` d'erreur, rien n'est modifié).

## Validation/errors

Pour les suppressions à très fort impact, exiger la saisie du nom de l'objet (proposé, seulement là où le produit en a besoin).

## Accessibility

`role="alertdialog"` avec le titre et les conséquences comme nom et description ; focus piégé puis rendu au déclencheur à la fermeture ; le bouton d'action nomme le verbe et l'objet.

## Responsive behavior

`Dialog` sur desktop ; en mobile, le même contenu dans un conteneur ancré en bas (proposé).

## Tokens

Aucun propre.

## Related components/patterns

`Dialog`, `Button`, `Toast` ; patterns `BulkActions`, `Form`, `DataTable`.
