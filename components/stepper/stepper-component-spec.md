# Composant Stepper

Sélecteur numérique incrémentable (± discret). À ne pas confondre avec **Step Indicator** (progression multi-étapes d'un formulaire), nom proche mais concept différent.

## Propriétés

`Interaction` = `Default`/`Focus`/`Disabled`, **3 variantes** — pas de `Hover` au niveau du conteneur : un survol ne concerne jamais les deux boutons à la fois (incohérent), le Hover est déjà porté individuellement par chaque instance de Button.

Boutons `Decrement`/`Increment` = **vraies instances de Button** (`Type=Ghost`, `Icon-only=true`), icônes `Minus`/`Plus` colorées en `Icon/primary`. Valeur centrée entre les deux (`Misc/Label`). Propriété texte `Value`.

## Note d'interactivité

Le `State` de chaque bouton `Decrement`/`Increment` reste **indépendamment modifiable** (ce sont des instances normales de Button, chacune garde sa propre propriété `State`) — pas besoin d'une variante `Hover` dédiée sur Stepper pour démontrer le survol d'un seul bouton.

Doc complète : guidelines Figma page `↳ Numeric inputs`.
