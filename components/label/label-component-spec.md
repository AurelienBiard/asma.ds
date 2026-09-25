# Composant Label & Field

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Décision (2026-09-25)** : le slot d'input de `Field` était passé, directement dans Figma et sans documentation préalable, à une vraie propriété Slot Figma (`Input-placeholder`). Décision confirmée : on **revient au `swapComponent()`**, pas de Slot. Cette spec documente la décision retenue ; le retrait du Slot dans Figma (remplacement par une instance simple swappable) est une modification manuelle à faire côté Figma, hors de cette session.

Deux composants liés, pour le même problème ("comment ajouter un label à un input") — à choisir selon le contexte.

## Label

ComponentSet, pour un placement manuel avec contrôle total du layout.
- **State** (variant) : `Default` / `Disabled`
- **Label-text** (Text), **Show-required** (Boolean, défaut `false`)
- Typo : Text Style `Misc/Label` — **14px/20px** (line-height révisé du 16 au 20, 2026-09-25 — s'aligne désormais exactement sur `Body/MD`), **Semi Bold**. Même taille que `Body/MD`, volontairement non réduite — la distinction label/corps de texte passe entièrement par la graisse, pas la taille ni le line-height.

## Field

Composant unique — composition Label + un input, avec un gap garanti de 8px.
- L'input est une **instance simple, remplaçable via `instance.swapComponent(nouveauComposant)`** — pas un Slot Figma. Fonctionne même entre deux ComponentSets différents (ex. `TextInput` → `PasswordInput`), un enfant d'instance ne pouvant être `.remove()`, seulement swappé.
- L'instance par défaut posée dans le composant n'est qu'un exemple à remplacer — ne pas la traiter comme la seule option valide.

## Quand utiliser quoi

- **Field** : choix par défaut pour un input de formulaire labellisé — garantit l'espacement, le plus rapide à poser.
- **Label** : uniquement si le layout fixe de Field ne convient pas (label à côté d'un contrôle inline, label partagé par plusieurs inputs, espacement personnalisé).

## Référence d'usage

Voir `patterns/authentication/login-pattern-spec.md` — composition avec de vraies instances `Field`, input remplacé via `swapComponent()` par `TextInput`/`PasswordInput`.

## Guidelines Figma

Page dédiée `↳ Label` (sections Label et Field).
