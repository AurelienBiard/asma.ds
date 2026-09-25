# Pattern Login

> **Statut** : construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel.

Page de référence `💻 PATTERNS / ↳ Authentication`. Démontre la bonne façon de composer un formulaire labellisé à partir de vraies instances de composants plutôt que d'un layout reconstruit à la main.

## Composition

- Instance `Field` — Email — slot rempli par une instance `TextInput`.
- Instance `Field` — Password — slot rempli par une instance `PasswordInput`.
- `Button` (Type=Primary) — action de soumission.
- `Link` — actions secondaires ("mot de passe oublié", "créer un compte").

## Pourquoi cette référence compte

Une première version avait reconstruit à la main la structure label+gap+input au lieu d'utiliser `Field` — corrigé une fois l'erreur repérée. La version actuelle dans Figma est la version corrigée. **Toujours composer les formulaires à partir de vraies instances `Field`**, jamais reconstruire label/gap/input manuellement.
