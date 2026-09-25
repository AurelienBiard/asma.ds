# Composant Popover

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : composant construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Contenu/contrôle flottant contextuel, non modal (`decisions.yaml` → `Popover`).

## Propriétés du composant Figma

- **Position** (variant) : `Top` / `Bottom` / `Left` / `Right` — détermine le bord où pointe la flèche. Le placement réel à l'écran (au-dessus/en-dessous du déclencheur) est géré par la logique de positionnement de l'app (Floating UI, Popper...), pas par Figma.
- **Title**, **Description** (Text)
- **Show-close** (Boolean, défaut `true`)

## Tokens

Fond `Background/elevated` · Bordure `Border/default` · Radius `Radius/md` · Ombre `Shadow/lg`
Title : `Heading/SM` · Description : `Body/SM` + `Text/secondary`

## Popover vs Card vs Dialog

- Popover : transitoire, ancré à un déclencheur, non modal (fermeture au clic extérieur).
- Dialog : modal (fond assombri, focus piégé) — utiliser Popover seulement si le reste de la page doit rester interactif.
- Card : conteneur statique in-flow, pas de comportement de superposition/positionnement.

## Guidelines Figma

Page dédiée `↳ Popover`.
