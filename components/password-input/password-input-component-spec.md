# Composant PasswordInput

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Champ de saisie mot de passe — même anatomie et mêmes tokens que `TextInput`, plus un toggle de visibilité (œil / œil barré). Anciennement nommé `Password`, renommé `PasswordInput`.

## Différences avec TextInput

- **Visibility-icon** : instance du composant `Icon`, propriété Instance-swap `Visibility-icon` (défaut = `EyeSlash`, alternative = `Eye`), couleur `Icon/primary`.
- Quand Validation ≠ None, `Status-icon` et `Visibility-icon` sont regroupés dans un sous-frame **Icons** (auto-layout horizontal, gap 8px) — **Visibility-icon toujours en dernier** (à droite) : c'est un contrôle interactif dont la position doit rester stable indépendamment de l'état de validation (l'icône de statut, informative, n'a pas cette contrainte).
- **Placeholder** par défaut : `••••••••` (points de masquage). **Value** par défaut : `Ryk!k4h$@ySex6SA` (exemple de mot de passe réel).
- Propriétés texte propres à ce composant (pas partagées avec TextInput) : `Placeholder`, `Value`, `Message` — chaque ComponentSet a ses propres clés de propriété même si cloné depuis TextInput à l'origine.

## Propriétés du composant Figma

Mêmes axes que TextInput : **Interaction** (Default/Hover/Focus/Disabled) × **Content** (Empty/Filled) × **Validation** (None/Error/Warning/Success) = 32 variantes, plus **Visibility-icon** (Instance-swap, propriété partagée — un seul état visuel possible à la fois pour tout le ComponentSet, cohérent puisque toutes les variantes doivent démarrer masquées par défaut).

## Limitation connue

La propriété `preferredValues` de `Visibility-icon` n'a pas pu être mise à jour vers des clones colorés localement (erreur de validation Figma : "Default value for instance swap component property is invalid" — un clone local n'a pas de `key` publiable). Sans impact fonctionnel : chaque instance affiche correctement l'icône colorée voulue, seule la métadonnée de suggestion du sélecteur reste sur les composants Phosphor bruts non colorés.

## Guidelines Figma

Page `↳ Text inputs`, section "PasswordInput". Partage les guidelines génériques du composant `Input` de base avec TextInput.
