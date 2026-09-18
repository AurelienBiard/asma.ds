# Composants Code-OTP et PIN

> Ce fichier est la **source de vérité** des deux composants (partagent la même brique atomique). Toute modification se fait ici en premier, puis est répercutée dans Figma.

Saisie de code à cases multiples — anatomie différente des autres champs texte (plusieurs cases individuelles plutôt qu'un seul champ continu).

## Composant atomique : OTP-cell

Case unique, réutilisée par Code-OTP et PIN.

- **Anatomie** : `Field` carré 40×40 (padding retiré, `primaryAxisAlignItems`/`counterAxisAlignItems: CENTER`), un seul caractère (Text Style `Heading/SM`, centré). Pas de Status-icon (pas de place, la validation est portée par le groupe, pas par case).
- **Propriétés** : Interaction (Default/Hover/Focus/Disabled) × Content (Empty/Filled) × Validation (None/Error/Warning/Success), 32 variantes. Propriété texte `Value` (uniquement sur Content=Filled).

## Code-OTP (assemblage, 6 cases, chiffre visible)

- Rangée de 6 instances `OTP-cell` (gap 8px), variante `Content=Filled` avec chiffres d'exemple.
- **Propriété de variante** : `Validation` (None/Error/Warning/Success) — colore les 6 cases uniformément et affiche un `Message` en dessous. Pas de propriété par case individuelle : la validation s'applique au groupe entier.
- Propriété texte `Message`.

## PIN (assemblage, 4 cases, contenu masqué)

- Identique à Code-OTP mais : **4 cases** (convention PIN standard, vs 6 pour OTP) et contenu **masqué** (`•` au lieu du chiffre réel) — sécurité, pas de révélation temporaire dans cette version (à ajouter si besoin confirmé, sur le modèle du toggle œil de PasswordInput).

## Leçons de construction

- Pour insérer une instance d'un ComponentSet existant (ex. `OTP-cell`) dans un nouveau composant, utiliser `variant.createInstance()` sur la variante ciblée du set source, puis `setProperties()` avec la clé complète de la propriété (ex. `Value#xxx:yy`, pas juste `"Value"`) — récupérable via `Object.keys(instance.componentProperties)`.
- Le champ `description` échappe automatiquement les apostrophes en `&#39;` (rappel déjà documenté sur Tooltip) — vérifié absent sur ces descriptions.

## Guidelines Figma

Page `↳ Text inputs`, section "Code/OTP et PIN" (partagée avec les guidelines génériques de la page).
