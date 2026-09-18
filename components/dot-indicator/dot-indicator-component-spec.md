# Composant Dot Indicator

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

Le Dot Indicator est un petit indicateur visuel, généralement circulaire, utilisé pour signaler un état, une nouveauté ou une action nécessitant l'attention de l'utilisateur. Il est généralement associé à une icône, un élément de navigation ou un composant interactif.

## Anatomie

- **Dot** — élément circulaire indiquant l'état ou l'attention requise.
- **Anchor** — élément auquel le dot est rattaché : icône, bouton, élément de navigation, etc.
- **Position** — position du dot par rapport à l'élément parent, généralement en haut à droite.

## Variants

- **Default** — indique une nouveauté ou une information non consultée. Utilise le token `Feedback/Success/icon` (changé depuis `Icon/primary` sur demande explicite — même couleur que la variante Success).
- **Semantic** — Info / Success / Warning / Danger : la couleur communique une signification spécifique définie par le Design System.
- **Brand** — couleur primaire, sans signification sémantique particulière.

La couleur ne doit pas être l'unique moyen de communiquer une information importante.

Lorsque le nombre d'éléments est pertinent, utiliser un Badge plutôt qu'un Dot Indicator — le Dot signale une présence/absence d'information, le Badge une quantité.

## États

- **Visible** — une information ou une action nécessite l'attention de l'utilisateur.
- **Hidden** — aucun élément ne nécessite d'attention.
- **Dismissed / Read** — l'information a été consultée ou l'action effectuée ; le dot disparaît.

Le Dot Indicator ne devrait généralement pas être interactif lui-même. L'interaction doit être portée par son élément parent.

## Positionnement

- Le dot est généralement positionné en overlay sur l'élément qu'il représente.
- Il doit rester suffisamment proche de l'élément associé pour que la relation visuelle soit évidente.
- Le positionnement doit rester cohérent entre les composants utilisant le Dot Indicator.

## Contenu

Le Dot Indicator ne contient normalement aucun texte. Si une information doit être exprimée sous forme de :
- nombre → Badge
- texte court → Badge
- état explicite → Status / Status Indicator
- notification non lue → Dot Indicator

## Accessibilité

Le Dot Indicator ne doit pas être la seule source d'information.

À éviter : 🔴 = "Votre compte nécessite une action", sans autre indication accessible.

À privilégier : "Paramètres — Action requise", avec le dot comme renforcement visuel.

Si le dot représente une notification ou un état, cette information doit être disponible dans le nom accessible ou le contexte du composant parent.

## Do / Don't

**Do :**
- Utiliser le dot pour signaler une présence ou une nouveauté.
- Le rattacher visuellement à l'élément concerné.
- Le faire disparaître lorsque l'état n'est plus pertinent.
- Utiliser les couleurs sémantiques de manière cohérente avec le Design System.

**Don't :**
- Utiliser un dot pour afficher une quantité.
- Utiliser plusieurs dots pour représenter plusieurs informations.
- Utiliser uniquement la couleur pour communiquer une information critique.
- Faire du dot un élément interactif indépendant.
- Ajouter un dot à tous les éléments « importants » : son usage doit rester significatif.

## Spécifications techniques

- **Composant Figma** : `Dot Indicator` (ComponentSet)
- **Propriété de variante** : `Color` = `Default` | `Info` | `Success` | `Warning` | `Danger` | `Brand` (valeurs exactes, sensibles à la casse — relues en direct sur le composant Figma)
- **Taille** : 8×8 px — valeur littérale, non liée à une variable (aucun token de taille dédié dans le système actuel)

**Correspondance `Color` → token Semantic :**

| Color | Token |
|---|---|
| Default | `Feedback/Success/icon` |
| Info | `Feedback/Info/icon` |
| Success | `Feedback/Success/icon` |
| Warning | `Feedback/Warning/icon` |
| Danger | `Feedback/Danger/icon` |
| Brand | `Action/primary` |

Pas de propriété `Visible`/`Hidden` sur ce composant : la visibilité est de la responsabilité du composant qui l'instancie (ex. futur composant Icon avec un booléen dédié), pas une variante propre au Dot Indicator.

Référence complète des tokens Primitive/Semantic/Responsive : `guidelines/design-system-ai-guidelines.yaml`.
