# Composant Count

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveau composant, créé le 2026-10-29 (page Figma `↳ Count`). Il remplace le « Badge » cité dans les specs `Dot Indicator` et `Icon`.

Le Count est un petit repère chiffré qui affiche **une quantité** : éléments non lus, résultats d'un filtre, tâches ouvertes, éléments sélectionnés. Il accompagne un libellé ou une icône et ne porte jamais d'action.

## Pourquoi un composant (`new_component_gate`)

- **Concept propre** : une quantité, sous forme d'un nombre court.
- **Pourquoi pas `Tag`** : `Tag` est un libellé (catégorie, statut), au minimum 24 px de haut, avec icônes et texte libre. Le Count est un nombre seul, plus compact (20 ou 16 px), circulaire pour un chiffre, et se superpose à une icône.
- **Pourquoi pas `Dot Indicator`** : le Dot signale une présence, pas une quantité (voir sa spec).
- **Réutilisation** : onglets, entrées de menu, filtres (`Filter bar`), icône de notifications.

## Anatomie

- **Container** : pastille `Radius/pill`, hauteur fixe (20 px Medium, 16 px Small, 12 px ExtraSmall), largeur minimale égale à la hauteur, hug horizontal, padding horizontal `Spacing/component-2xs`.
- **Value** : le nombre, centré.
- **Anchor** : élément auquel le Count est rattaché (hors composant). Sur une icône, le Count prend la place du `Dot Indicator` : composant `Icon`, `Bullet=Count`, mêmes quatre positions (débordement de 4 px du coin).

## Propriétés du composant Figma

- **Type** (variant) : `Neutral` / `Brand` / `Info` / `Success` / `Warning` / `Danger`.
- **Size** (variant) : `Medium` / `Small` / `ExtraSmall`.
- **Value** (Text) : le nombre, défaut `8`.

18 variantes (6 Type × 3 Size).

## Règles de couleur et de texte

| Type | Fond | Texte |
|---|---|---|
| Neutral | `Background/strong` | `Text/primary` |
| Brand | `Action/primary` | `Text/on-brand` |
| Info | `Feedback/Info/background` | `Feedback/Info/text` |
| Success | `Feedback/Success/background` | `Feedback/Success/text` |
| Warning | `Feedback/Warning/background` | `Feedback/Warning/text` |
| Danger | `Feedback/Danger/background` | `Feedback/Danger/text` |

Même mapping que `Tag`. Aucun nouveau token.

| Size | Hauteur | Text Style |
|---|---|---|
| Medium | 20 px | `Body/SM` |
| Small | 16 px | `Body/XS` |
| ExtraSmall | 12 px (padding horizontal 3 px) | `Body/2XS` (8/12, nouveau style) |

Les hauteurs sont des valeurs littérales (aucun token de taille dédié).

## Usage

- **Medium** : à côté d'un libellé (onglet, entrée de menu, filtre), séparé par `Spacing/component-xs`.
- **Small** : uniquement en superposition sur une icône Large ou XLarge, en haut à droite, débordant d'environ un quart de sa taille. Réservé au cas où le nom accessible du parent exprime déjà la quantité.
- **ExtraSmall** : superposition sur une icône `Small` (16 px) ou `Medium` (20 px), où un Count de 16 px couvrirait presque tout le pictogramme. Un seul chiffre tient dans un rond de 12 px ; `99+` s'étire en pastille. Mêmes règles que Small.
- **Valeur** : entier positif. Au-delà de 99, afficher `99+`. À 0, ne pas afficher le Count, sauf si zéro est une information (ex. « Résultats 0 »). Jamais « 0 » en superposition sur une icône.
- **Contenu** : un nombre uniquement, pas d'unité, de texte ni d'icône. Une présence sans quantité → `Dot Indicator` ; un libellé ou un statut → `Tag` ; une valeur à surveiller avec sa variation → `KPI` ; une progression → `Progress`.

## Remplacement du Dot Indicator

Quand une quantité est pertinente, le Count prend la place du Dot Indicator, au même emplacement. Dans `Icon`, c'est la valeur `Bullet=Count` (Count Danger Small par défaut ; `Value` et `Type` se règlent via l'instance imbriquée exposée). Dot ou Count, jamais les deux sur le même élément.

## Comportement

Statique, sans états propres. Visibilité et valeur relèvent du composant qui l'instancie. Non interactif : l'interaction est portée par le parent.

## Accessibilité

- Le Count n'est jamais la seule source d'information : le parent porte un nom accessible qui contient la quantité (« Notifications, 3 non lues »). Le Count est alors masqué aux lecteurs d'écran (`aria-hidden`).
- Un changement de valeur (nouvelles notifications) est annoncé par une région `aria-live` du parent, pas par le Count.
- La couleur ne porte pas seule l'information : le nombre est toujours affiché.
- Contraste : mêmes couples fond/texte que `Tag`.

## Do / Don't

**Do** : afficher une quantité réelle et à jour ; le rattacher à l'élément quantifié ; plafonner à `99+` ; choisir le Type selon la signification (Neutral par défaut).

**Don't** : utiliser un Count pour un libellé ou un statut ; y mettre du texte, une unité ou une icône ; en faire un élément interactif indépendant ; empiler plusieurs Count sur un même élément ; afficher « 0 » en superposition sur une icône.

## Guidelines Figma

Page `↳ Count` (entre `↳ Command` et `↳ Dot indicator`) : section `Guidelines`, section `Count` (le ComponentSet) et section `Exemples` (icône avec Count Danger Small, onglet avec Count Neutral Medium, plafond `99+` Brand Medium).

## À valider

- Hauteurs 20 / 16 / 12 px en valeurs littérales : à rattacher à un token si une échelle de tailles de composants est introduite.
- `Body/XS` (10 px) pour Small et `Body/2XS` (8 px) pour ExtraSmall : lisibilité limitée, d'où la restriction à la superposition sur icône. `Body/2XS` n'a pas de pas Primitive (2xs=6, xs=9) : valeur directe, comme `Body/XS`.
- Cas non couverts : Count dans un `Button` avec libellé, dans un `Tab-item` (propriété dédiée), dans la `Sidebar`.
