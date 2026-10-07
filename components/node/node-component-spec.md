# Composants Node, Port, Handle et Edge

> Ce fichier est la **source de vérité** des composants. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveaux composants, créés le 2026-10-06. Famille « graphe de nœuds » (éditeurs de workflow, pipelines, agents : références de comportement React Flow / Svelte Flow, n8n, Figma Weave). Quatre briques : `Handle` (point de connexion), `Port` (ligne étiquetée portant un `Handle`), `Node` (carte), `Edge` (liaison). Pas de composant monolithique « Graph » : nombre de nœuds, de ports et de liaisons arbitraire → assemblage manuel, comme `Table` et `Pagination`.

## Handle

Point de connexion d'un port — la « prise » où une `Edge` s'accroche.

- **State** (variant) : `Default` / `Hover` / `Connected` / `Invalid` / `Disabled`. 5 variantes.
- Cercle 12×12 (valeur littérale, pas de token de taille), bordure 2px, `Radius/pill`.
- `Default` : fond `Background/elevated`, bordure `Border/strong`. `Hover` : bordure `Action/primary`, fond `Action/secondary` (cible de connexion prête). `Connected` : fond et bordure `Action/primary` (au moins une `Edge` attachée). `Invalid` : bordure `Feedback/Danger/border`, fond `Background/elevated` (connexion refusée pendant un glisser). `Disabled` : bordure `Border/disabled`, fond `Background/disabled`.
- **Zone d'interaction** : le visuel fait 12px mais la cible cliquable/tactile est de **24×24 minimum** (zone transparente autour du cercle en code). Non représentée dans Figma.

## Port

Ligne d'un nœud portant un `Handle` et une étiquette. Un `Node` contient autant de `Port` que nécessaire.

- **Side** (variant) : `Input` (handle à gauche, étiquette alignée à gauche) / `Output` (handle à droite, étiquette alignée à droite). 2 variantes.
- **Label** (Text) : nom du port, `Body/SM` + `Text/secondary`.
- **Show-label** (Boolean, défaut `true`) : affiche l'étiquette. **Show-handle** (Boolean, défaut `true`) : affiche la prise (`Handle`) — à masquer sur un port purement informatif.
- Le `Handle` est une instance de `Handle`, positionnée en absolu (`layoutPositioning: ABSOLUTE`) à cheval sur le bord du `Node` : centre du cercle exactement sur la bordure (décalage −6px à gauche, +6px à droite via contraintes). Le `Port` occupe toute la largeur du nœud (`FILL`), hauteur 24px.
- L'état du `Handle` se règle par instance (propriété exposée) ; `Port` n'a pas d'état propre.

## Node

Carte représentant une étape du graphe (déclencheur, action, condition, transformation…).

- **State** (variant) : `Default` / `Hover` / `Selected` / `Disabled`.
- **Status** (variant) : `None` / `Success` / `Error` — résultat d'exécution ou de validation du nœud.
- **Title** (Text), **Description** (Text), **Show-body** (Boolean, défaut `true` — masque tout le `Body`, description comprise), **Show-input** / **Show-output** (Boolean, défaut `true` — masquent toute la ligne `Port` d'entrée / de sortie, ex. un déclencheur n'a pas d'entrée).
- Instances imbriquées **exposées** (leurs propriétés se règlent depuis l'instance de `Node`) : `Icon`, `Status-icon`, `Port-input`, `Port-output` (donc `Label`, `Show-label`, `Show-handle` et l'état du `Handle` par port).
- **Icon** : instance imbriquée du composant `Icon` (`Size=Medium`), exposée — le pictogramme se change par instance (`Lightning` par défaut), comme sur les autres composants. Pas de propriété Instance swap dédiée sur `Node` (un swap direct remplacerait le composant `Icon` par le glyphe brut).

12 variantes (4 State × 3 Status).

`Body` et `Ports` n'ont **aucun fond** (`fills = []`) : un auto-layout créé par script a un fond blanc par défaut qui recouvrirait la bordure du `Node` (côtés et bas).

### Anatomie

Conteneur vertical, largeur **240px** dans le composant (`clipsContent: false` — les `Handle` débordent volontairement), fond `Background/elevated`, bordure 1px, `Radius/card`.
- **Header** : horizontal, fond `Background/subtle`, padding `Spacing/component-sm` (horizontal) / `Spacing/component-xs` (vertical), gap `Spacing/component-xs`, coins supérieurs `Radius/card`. `Icon` (`Icon/primary`) + `Title` (`Misc/Label` + `Text/primary`, `FILL`, tronqué sur 1 ligne) + `Status-icon` (uniquement si `Status` ≠ `None` : `CheckCircle` en `Feedback/Success/icon`, `WarningCircle` en `Feedback/Danger/icon`).
- **Body** : vertical, padding `Spacing/component-sm`, gap `Spacing/component-xs`. `Description` (`Body/SM` + `Text/secondary`). Contenu libre possible en dessous (champ, valeur) par instances.
- **Ports** : zone sans padding horizontal contenant les `Port` — `Input` à gauche, `Output` à droite, en lignes de 24px. Par défaut 1 `Input` + 1 `Output`.

### États et couleurs (bordure)

Ordre de priorité, du plus fort au plus faible :
1. `Disabled` : bordure `Border/disabled`, fond `Background/disabled`, texte `Text/disabled`, icône `Icon/disabled` (pas de couleur de statut).
2. `Selected` : bordure **2px** `Border/focus` (même token que l'anneau de focus).
3. `Status` : `Success` → bordure `Feedback/Success/border` ; `Error` → `Feedback/Danger/border`.
4. `Hover` : bordure `Border/strong` (sans effet quand un `Status` est déjà affiché : la couleur de statut est conservée).
5. `Default` : bordure `Border/default`.

## Edge

Liaison entre deux `Handle` (sortie d'un nœud → entrée d'un autre). Représentée par un trait vectoriel, pas par un composant paramétrique : sa géométrie dépend des positions des nœuds. Le ComponentSet `Edge` n'est qu'un **gabarit de style** (courbe de référence 160×64) à copier et à dessiner entre les nœuds.

- **Shape** (variant) : `Curve-up` (bézier montante, de bas-gauche à haut-droite), `Curve-down` (bézier descendante, de haut-gauche à bas-droite), `Straight` (droite horizontale) ou `Vertical` (droite verticale, de haut en bas).
- **State** (variant) : `Default` / `Selected` / `Error` / `Disabled`.

16 variantes (4 Shape × 4 State). Le gabarit montre la forme de chaque tracé ; en usage réel, `Curve-up` / `Curve-down` se choisissent selon que la cible est plus haute ou plus basse que la source, `Straight` quand les deux `Handle` sont alignés sur une même ligne horizontale. `Vertical` pour une liaison verticale (graphe orienté de haut en bas, liaison entre un nœud et un élément placé au-dessus ou en dessous) ; les `Handle` de `Port` étant à gauche et à droite, un tracé vertical suppose des prises posées en haut ou en bas du nœud — non spécifié à ce jour (voir « Non spécifié »).
- Trait 2px en **tirets 10/10** (`dashPattern` [10, 10]) pour tous les états, extrémités arrondies (`strokeCap: ROUND`). `Default` : `Border/strong`. `Selected` : `Action/primary`. `Error` : `Feedback/Danger/border`. `Disabled` : `Border/disabled` (distingué par la couleur seule, les tirets étant communs).
- **Famille de tracé** (choix par graphe) : bézier (`Curve-up` / `Curve-down`, courbe en S, tangentes horizontales — flux gauche → droite) ou droit (`Straight` horizontal, `Vertical`) ; `Step` (angles droits arrondis) reste possible mais non gabarité. Un seul type de tracé par graphe : ne pas mélanger courbes et droites.
- Pas de pointe de flèche par défaut : le sens est porté par l'emplacement des ports (sortie à droite, entrée à gauche).
- Étiquette d'edge (condition, branche « oui/non ») : une instance de `Tag` (`Neutral`, `Small`) posée au milieu du tracé. Aucun composant dédié.

## Comportement

- **Connexion** : glisser depuis un `Handle` de sortie vers un `Handle` d'entrée. Pendant le glisser, les `Handle` compatibles passent en `Hover`, les incompatibles en `Invalid`. Une sortie peut alimenter plusieurs entrées ; une entrée n'accepte qu'une seule `Edge` par défaut (à préciser par produit).
- **Sélection** : clic sur un `Node` ou une `Edge` → `Selected`. Un seul élément sélectionné par défaut ; Maj+clic pour une sélection multiple.
- **Déplacement** : glisser l'en-tête déplace le nœud ; les `Edge` suivent. Aucun état visuel dédié au glissement n'est spécifié.
- **Non spécifié à ce jour** : `Handle` en haut / en bas d'un nœud (nécessaire pour un graphe vertical de bout en bout), bézier à tangentes verticales, animation de flux sur une `Edge` en cours d'exécution, mini-carte, zoom/pan, regroupement de nœuds, état `Running` d'un `Node`, comportement responsive (le graphe est un canvas : pas de réorganisation mobile).

## Usage

- Éditeur de workflow, pipeline de données, graphe d'agents, schéma relationnel. Pas pour un organigramme ou un simple parcours d'étapes (→ `Step-indicator`).
- Un `Node` ne contient pas d'autre `Node` ni de `Card` imbriquée.
- Nommer les ports par leur donnée (« Contexte », « Résultat »), jamais « Entrée 1 ».

## Accessibilité

- Le canvas est un `role="application"` avec description d'usage ; chaque `Node` est focusable (`Tab`), `Enter` entre dans ses ports, flèches pour naviguer entre nœuds proches.
- Toute opération faisable à la souris (créer / supprimer une liaison, déplacer un nœud) doit avoir un équivalent clavier : sélectionner un `Handle` de sortie, `Enter`, choisir la cible dans une liste, `Enter`.
- Chaque `Handle` a un nom accessible (« Sortie Résultat du nœud <Title> ») ; chaque `Edge` est exposée comme relation textuelle (« <Titre A> → <Titre B> »).
- Le statut ne repose jamais sur la couleur seule : l'icône `Status-icon` est toujours présente pour `Success` / `Error`.
- Contraste ≥ 3:1 de la bordure et des `Handle` contre le fond du canvas ; focus visible (`Border/focus`) sur nœud et handle.
- Annoncer par zone `aria-live` les créations/suppressions de liaison et les changements de statut.

## Tokens

`Background/elevated`, `Background/subtle`, `Background/disabled`, `Border/default`, `Border/strong`, `Border/focus`, `Border/disabled`, `Action/primary`, `Action/secondary`, `Feedback/Success/{border,icon}`, `Feedback/Danger/{border,icon}`, `Text/primary`, `Text/secondary`, `Text/disabled`, `Icon/primary`, `Icon/disabled`, `Radius/card`, `Radius/pill`, `Spacing/component-xs`, `Spacing/component-sm`. Text Styles : `Misc/Label`, `Body/SM`. Valeurs littérales assumées : largeur de nœud 240, `Handle` 12, ligne de `Port` 24, trait d'`Edge` 2, tirets 10/10.

## Guidelines Figma

Page dédiée `↳ Node` dans `❖ COMPONENTS` (entre `Menu` et `Numeric inputs`), sections `Node`, `Port & Handle`, `Edge`, `Exemple de graphe` (4 nœuds, 3 liaisons, `Handle` en `Connected`, nœud `Filtre` en `Selected`, `Envoyer l'e-mail` en `Error`) et `Guidelines`.

## Leçons de construction

- Un `Handle` à cheval sur le bord se fait par `layoutPositioning = "ABSOLUTE"` dans le `Port` + contraintes (`MIN` à gauche, `MAX` à droite) ; le `Node` doit avoir `clipsContent = false`, sinon les `Handle` sont rognés.
- Les `Edge` de l'exemple sont des vecteurs (`vectorPaths`, courbe cubique `M x1 y1 C x1+dx y1 x2-dx y2 x2 y2`, `dx = max(40, (x2-x1)/2)`) calés sur le centre des `Handle` (`absoluteBoundingBox`), placés sous les nœuds. Elles ne suivent pas les nœuds si on les déplace : à redessiner.
- Un `figma.createAutoLayout()` a un fond blanc par défaut : `fills = []` sur `Body` et `Ports`, sinon la bordure du `Node` est masquée (les enfants se dessinent au-dessus du trait de leur parent).
- Une propriété Instance swap liée à `mainComponent` sur une instance imbriquée remplace le composant lui-même (ici `Icon` par le glyphe Phosphor) et renomme l'instance : préférer une instance exposée et `setProperties({'Instance#…': id})`.
- `dashPattern` sur `findAll('VECTOR')` atteint aussi les glyphes d'icône des nœuds : cibler uniquement les `Edge`.
- Un cloneur de section par script laisse des clones orphelins sur la page : vérifier `page.children` après un test.
