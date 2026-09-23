# Composant Tabs

Navigation entre plusieurs vues d'un même contexte (pas entre pages différentes).

## Tab-item

`State` = `Default`/`Hover`/`Active`/`Disabled`, 4 variantes. Hauteur fixe 40px, label centré verticalement.

**Indicateur = bordure basse individuelle** portée par chaque Tab-item lui-même (`strokeBottomWeight`), **pas** un calque `Underline` séparé ni une bordure au niveau de l'assemblage `Tabs` (double emploi retiré suite à retour) : `Border/default` 1px par défaut, `Action/primary` 2px si `Active`. Propriété texte `Label`.

## Tabs (assemblage)

Rangée d'instances `Tab-item`, **`gap: 0`** — les bordures basses de tous les onglets juxtaposés se touchent et forment une ligne séparatrice continue avec le contenu affiché en dessous, sans espace ni bordure dédiée supplémentaire sur le conteneur.

## Usage

2-6 onglets maximum, tous visibles sans défilement.

Doc complète : guidelines Figma page `↳ Tabs`.
