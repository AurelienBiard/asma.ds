# Pattern Node-graph

> **Statut** : spec seule (2026-11-19), pas encore de page Figma (une page d'exemple de graphe est prévue). Agencement de la famille `Node` sur `Canvas-dotted`. Les comportements de référence (React Flow, n8n) sont une source d'inspiration, pas des règles. Les choix marqués « proposé » sont à valider.

## Purpose

Afficher et éditer un graphe d'étapes connectées (workflow, pipeline, graphe d'agents) sur un canvas libre : placer des nœuds, relier des ports, inspecter, supprimer.

## Use when

- Étapes avec entrées et sorties étiquetées reliées par des liens.
- Disposition spatiale libre, avec zoom et déplacement.

## Do not use when

- Parcours linéaire à accomplir → `Step-indicator`.
- Données hiérarchiques ou tabulaires → `Table`.
- Dessin de diagrammes libres (non couvert).

## Components

- `Canvas-dotted` — la surface (`components/canvas-dotted/`).
- `Node` (carte), `Port` (ligne étiquetée), `Handle` (point de connexion), `Edge` (lien) — `components/node/`.
- `Menu` (actions d'un nœud), `Tooltip`, `Toast` (retour), `Empty-state` (canvas vide).

## Structure

`Canvas-dotted` remplit la zone d'édition ; les nœuds y sont placés librement ; les liens sont tracés entre les handles. Les quantités sont arbitraires, le graphe est donc assemblé à la main (comme `Table`) : la famille documente les briques, ce pattern l'agencement. Un graphe d'exemple est la composition de référence.

## Interaction flow

1. Glisser d'un `Handle` de sortie vers un `Handle` d'entrée crée une `Edge` ; les cibles compatibles affichent `Handle` `Hover`, les incompatibles `Invalid`.
2. Glisser un nœud le déplace ; le sélectionner affiche ses actions.
3. Alternative clavier (obligatoire) : sélectionner un nœud, ouvrir « Connecter à… » dans son menu, choisir le port cible ; les flèches déplacent un nœud sélectionné (proposé : pas de 8 px).
4. Supprimer un nœud supprime ses liens ; proposer Annuler dans un `Toast`.

## States

Nœud : voir les états de `Node` (défaut, sélectionné, erreur…). Handle : `Default`, `Hover`, `Connected`, `Invalid`, `Disabled`. Canvas : vide (`Empty-state`), rempli.

## Validation/errors

Une connexion refusée (types incompatibles, cycle) affiche `Handle` `Invalid` pendant le glissement et un `Tooltip` avec la raison ; rien n'est créé.

## Accessibility

Le graphe doit être utilisable sans pointeur : nœuds focusables, ports listés dans la description accessible du nœud, connexions accessibles par le flux clavier ci-dessus, liste des connexions exposée en texte (proposé : panneau « Connexions »). Le fond à points est décoratif (voir `Canvas-dotted`).

## Responsive behavior

Desktop d'abord. Mobile : consultation seule avec déplacement/zoom (proposé) ; l'édition n'est pas prise en charge.

## Tokens

Aucun propre (voir `Node` et `Canvas-dotted`).

## Related components/patterns

`Node`, `Port`, `Handle`, `Edge`, `Canvas-dotted`, `Menu`, `Tooltip`, `Toast` ; patterns `Confirmation`, `States`.
