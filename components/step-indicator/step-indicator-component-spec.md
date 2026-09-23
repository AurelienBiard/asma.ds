# Composant Step Indicator

Affiche la progression dans un parcours multi-étapes (formulaire long, onboarding, checkout). **Distinct du Stepper** (Numeric inputs, incrément/décrément numérique) malgré le nom proche.

## Step-item (atomique)

`State` = `Completed` (cercle plein `Action/primary` + coche en **`Icon/inverse`**) / `Current` (cercle `Action/neutral` + bordure `Action/primary` + numéro coloré, label en gras) / `Upcoming` (cercle `Action/neutral` + numéro `Text/tertiary`, label atténué), 3 variantes.

Propriétés : `Label` (Text), `Show-label` (Boolean, défaut `true` — permet une version compacte sans label, voir Step-indicator-mobile).

## Step-indicator (assemblage)

Instances de `Step-item` reliées par des `Connector` (piste + fill, remplissage progressif de gauche à droite plutôt qu'un changement de couleur binaire) : `Action/primary` si l'étape précédente est `Completed`, sinon `Border/strong`.

## Step-indicator-mobile (version compacte)

`Show-label=false` sur toutes les instances, connecteurs resserrés à 16px (au lieu de 32px), label de l'étape courante affiché séparément en dessous ("Étape X sur Y — Nom").

## Interaction (prototype Figma)

5 frames `Progress-0` à `Progress-4` avec interactions de clic **Smart Animate** configurées (`node.setReactionsAsync`) — cliquer en mode Présentation anime la transition de couleur d'une étape à l'autre. Pas de changement de taille (`transform: scale`) sur le cercle — retiré sur demande, seule la couleur/bordure transitionne.

Doc complète : guidelines Figma page `↳ Step Indicator`.
