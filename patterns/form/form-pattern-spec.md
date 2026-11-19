# Pattern Form

> **Statut** : spec seule (2026-11-19), pas encore de page Figma. Généralise la composition de `patterns/authentication/login-pattern-spec.md` à tout formulaire labellisé. Aucun composant nouveau. Les choix marqués « proposé » sont à valider.

## Purpose

Collecter une saisie structurée : champs labellisés, validation, retour d'information, action de soumission. Définit l'empilement des champs, l'affichage des erreurs et l'emplacement des actions.

## Use when

- Création ou édition d'un enregistrement, réglages, inscription, toute saisie multi-champs.

## Do not use when

- Un seul champ → le composant d'entrée directement.
- Connexion → pattern `Login` (un formulaire spécialisé).
- Envoi de fichier seul → pattern `FileUpload`.
- Requête à nombreux critères → `QueryBuilder` (candidat).

## Components

- `Field` (choix par défaut pour un input labellisé ; `Label` seulement quand la mise en page fixe de `Field` ne convient pas — voir `components/label/`) avec `TextInput`, `Textarea`, `Select`, `Checkbox`, `Radio`, `Switch`, `DateTimePicker`, etc. échangés dedans.
- `Banner` (Inline) ou `Alert` — erreur ou information au niveau du formulaire.
- `Button` — `Primary` pour valider, `Ghost`/`Outlined` pour annuler.
- Dans un `Dialog` ou un `Drawer` : `Dialog-header`, `Dialog-body`, `Dialog-footer`.

## Structure

Pile verticale de `Field` (espacement entre champs : proposé `Spacing/component-md`), actions à la fin. Dans un `Dialog`/`Drawer`, les champs sont dans le corps et les actions (Annuler / Créer) dans le pied. **Pas de `Dialog-toolbar` dans les formulaires de création** : il n'y a encore rien à terminer ni à supprimer (voir la spec `Drawer`) ; la barre est réservée à un élément existant.

## Interaction flow

1. L'utilisateur remplit les champs ; la validation s'exécute à la sortie d'un champ et à la soumission pour l'ensemble (proposé).
2. Soumission avec erreurs : les champs affichent leur état d'erreur, le focus va au premier champ invalide, et un `Banner` de formulaire résume s'il y en a plusieurs.
3. Succès : fermer le conteneur ou naviguer, et confirmer par un `Toast`.
4. Fermer avec des modifications non enregistrées demande confirmation (pattern `Confirmation`).

## States

Intact, en saisie, erreur de champ, erreur de formulaire, envoi en cours (`Button` principal en chargement, champs désactivés), succès, désactivé.

## Validation/errors

Texte d'erreur sous le champ, en toutes lettres, disant comment corriger ; champs obligatoires signalés dans le label ; jamais la couleur seule. Les erreurs serveur non liées à un champ vont dans le `Banner`.

## Accessibility

Chaque input a un label programmatique ; erreurs reliées par `aria-describedby` et `aria-invalid` ; la première erreur reçoit le focus à la soumission ; erreurs de formulaire dans une région live. Le focus des inputs est dessiné hors du champ : ne jamais rogner les conteneurs d'inputs (`clipsContent` à false).

## Responsive behavior

Colonne unique à toutes les tailles ; actions pleine largeur en mobile (proposé).

## Tokens

Aucun propre ; hérités des composants assemblés.

## Related components/patterns

`Field`, `Label`, `TextInput`, `Select`, `Banner`, `Alert`, `Dialog`, `Drawer` ; patterns `Login`, `FileUpload`, `Confirmation`.
