# Composant Icon

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

L'Icon est un symbole graphique représentant une fonctionnalité, une action ou un contenu de façon visuellement expressive. Les icônes rendent l'interface plus intuitive en offrant des repères visuels pour des actions (enregistrer, supprimer, partager) ou des éléments (utilisateur, panier, etc.). Selon le contexte, une icône peut être utilisée seule ou accompagnée de texte pour renforcer la compréhension.

## Anatomie

- **Icon** — le pictogramme lui-même (source : bibliothèque Phosphor, page Foundation/Icons).
- **Bullet** — indicateur optionnel sur l'icône : instance du composant [Dot Indicator](../dot-indicator/dot-indicator-component-spec.md) (nouveauté, attention requise) ou, quand une quantité est pertinente, du composant [Count](../count/count-component-spec.md) qui prend alors la place du Dot.
- **BulletPosition** — position du Bullet par rapport à l'icône : top-right, top-left, bottom-right, bottom-left, ou none.

## Variants

- **Size** — Small / Medium / Large / XLarge.
- **Bullet** — False / True / Count — rien, le Dot Indicator, ou le Count (Type Danger, Size Small par défaut). Avec `Count`, l'instance imbriquée `Count` est exposée : sa valeur (`Value`) et son Type se règlent depuis l'instance d'Icon.
- **BulletPosition** — n'a d'effet que lorsque Bullet = True ou Count. Avec Count, le badge déborde de 4 px du coin de l'icône.

36 variantes (4 Size × [1 sans Bullet + 4 positions × 2 types de Bullet]).

L'icône elle-même est un slot d'échange (Instance-swap) : n'importe quel composant de la bibliothèque Phosphor locale (page Foundation/Icons) peut être inséré à sa place.

## Usage du Bullet

Le Bullet reprend les règles du composant Dot Indicator : signaler une présence ou une nouveauté, jamais une quantité. Quand une quantité est pertinente, `Bullet=Count` : le Count prend la place du Dot, aux mêmes quatre positions ; Dot ou Count, jamais les deux. Un Count Small de 16 px couvre l'essentiel d'une icône Small : préférer Medium ou plus. Ne pas l'activer sur toutes les icônes « importantes » : son usage doit rester significatif et rare.

## Accessibilité

- **Icône décorative** (accompagnée d'un texte visible) : masquer l'icône aux technologies d'assistance (`aria-hidden`).
- **Icône seule et actionnable** (bouton icon-only, lien) : porter un nom accessible explicite sur l'élément parent (`aria-label`), pas sur l'icône elle-même.

Si un Bullet est affiché, l'information qu'il représente (nouveauté, notification) doit être disponible dans le nom accessible ou le contexte du composant parent — jamais uniquement via la présence visuelle du point.

## Do / Don't

**Do :**
- Utiliser un seul et même format/graisse Phosphor dans toute l'interface (Format=Outline, Weight=Light par convention).
- Réserver le Bullet aux cas où une vraie nouveauté/attention existe.
- Choisir la taille d'icône cohérente avec le texte ou le composant qui l'entoure.

**Don't :**
- Mélanger plusieurs graisses Phosphor (Regular et Bold) dans une même interface.
- Utiliser `Bullet=True` (Dot) pour afficher une quantité (→ `Bullet=Count`).
- Ajouter un Bullet par défaut sur toutes les icônes.

## Spécifications techniques

- **Composant Figma** : `Icon` (ComponentSet)
- **Propriétés de variante** :
  - `Size` = `Small` | `Medium` | `Large` | `XLarge`
  - `Bullet` = `False` | `True`
  - `BulletPosition` = `bottom-right` | `bottom-left` | `top-left` | `top-right` | `none`
- **Propriété Instance-swap** (icône) : défaut = `Acorn` (Phosphor, `Format=Outline`, `Weight=Light`) — source = composants locaux de la page `🎨 FOUNDATION / ↳ Icons`, aucune restriction technique à `Acorn`, n'importe quel Phosphor local convient.
- **Composant nested (Bullet)** : instance du composant local `Dot Indicator`, `Color=Brand` sur les 4 positions (harmonisé — voir historique ci-dessous).

**Corrections effectuées lors de la construction** : les composants `Add` (icône), `Type=Brand` et `Form=Bullet, Type=Success, Variant=Opacity` (indicateurs) provenaient initialement d'une bibliothèque Figma externe (`remote: true`). Ils ont été remplacés par des composants 100% locaux : icône Phosphor (Foundation/Icons) et instances du composant `Dot Indicator` du design system. Toute icône ou indicateur ajouté à ce composant DOIT provenir des composants locaux du fichier — jamais d'une bibliothèque externe/remote.

Référence complète des tokens Primitive/Semantic/Responsive : `guidelines/design-system-ai-guidelines.yaml`.
