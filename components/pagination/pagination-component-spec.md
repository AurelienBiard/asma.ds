# Composant Pagination

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : nouveau composant, créé le 2026-10-04. Composé d'une brique atomique (`Page-item`) et de deux instances du composant `Button` (`Prev`/`Next`, réutilisé tel quel, pas de nouveau composant de navigation) — même logique d'assemblage manuel que `Table` (voir `components/table/`) : le nombre de pages est arbitraire, donc pas de ComponentSet monolithique « Pagination », composition manuelle d'instances.

## Page-item

### Propriétés du composant Figma

- **State** (variant) : `Default` / `Hover` / `Current`.
- **Label** (Text) : le numéro de page.

3 variantes.

### Anatomie

Conteneur 32×32 — hauteur fixe 32px, largeur hug avec `minWidth: 32px` (accueille 2-3 chiffres sans déformer l'alignement sur les pages à un seul chiffre), `Radius/control`, contenu (`Label`) centré horizontalement et verticalement. Même gabarit que `Button` en `Icon-only=true` (32×32, voir `components/button/button-component-spec.md`) — alignement vertical exact avec `Prev`/`Next` dans l'assemblage.

### États et couleurs

- **Default** : fond transparent, `Label` en `Misc/Label` + `Text/secondary`.
- **Hover** : fond `Action/ghost-hover`, `Label` inchangé (`Text/secondary`) — cohérent avec `Header-cell`/`Row` : le survol change le fond, jamais la couleur du texte.
- **Current** : fond `Action/primary`, `Label` en `Text/on-brand` (même token que `Button` Type=Primary, corrigé pour le contraste le 2026-09-27 — voir `button-component-spec.md`). Page affichée, non cliquable (pas de `Hover` sur cet état).

## Ellipsis (non composant)

Nœud texte simple `…` (`Misc/Label` + `Text/tertiary`), posé dans une frame 32×32 centrée pour l'alignement avec les `Page-item` — **volontairement pas un ComponentSet dédié** : aucun état, aucun comportement propre, aucune réutilisation hors de ce seul point d'assemblage (gate `new_component_gate` de `decisions.yaml` : composition insuffisante ? non, un simple texte suffit). Non interactif, non focusable.

## Pagination (assemblage)

Pas de composant unique paramétrique, comme `Table`. Rangée horizontale, alignement vertical centré, `itemSpacing: Spacing/component-2xs` (4px) uniforme sur toute la largeur (`Prev`, `Page-item`, `Ellipsis`, `Next` — pas de regroupement visuel supplémentaire).

Deux structures d'assemblage selon le contexte :

- **Numbered** (par défaut) : `Prev` + séquence de `Page-item` (+ `Ellipsis` si besoin) + `Next`.
- **Simple** (espace contraint — ex. pied de `Table` en largeur réduite, mobile — ou total de pages inconnu/très grand) : `Prev` + texte `« Page {n} sur {N} »` (`Misc/Label` + `Text/primary`, non interactif) + `Next`. Variante de contenu `« Page {n} »` seule si `{N}` n'est pas encore connu (chargement progressif/infini).

### Prev / Next

Instance `Button` (`Type=Ghost`, `Icon-only=true`, padding `Spacing/component-xs` carré 32×32 — même convention que sur `Search-button`, voir `button-component-spec.md` ; `Pagination` en devient le **deuxième usage réel**). Icônes `ChevronLeft` / `ChevronRight` (Phosphor, `Outline`, `Regular`, 16×16). `Disabled` natif du composant `Button` (`Background/disabled` + `Text/disabled` + `Icon/disabled`) quand la page courante est la première (`Prev`) ou la dernière (`Next`) — aucune règle nouvelle, réutilisation directe de l'état existant du composant.

### Troncature (Numbered — comportement)

Règle de fenêtrage : toujours afficher la première page, la dernière page, la page courante et ses voisins immédiats (courante ± 1). Un seul `…` par écart quand il dépasse 1 page masquée (au plus 2 `Ellipsis` au total : un avant, un après la fenêtre courante). Exemple pour page courante = 6 sur 20 : `1 … 5 6 7 … 20`. Si le nombre total de pages est petit (≤ 7), toutes les pages sont affichées sans troncature — le gain de place ne justifie pas l'écart cognitif d'un `…` sur un si petit ensemble.

## Accessibilité

- Conteneur : `<nav aria-label="Pagination">`.
- `Page-item` : `<button aria-label="Page {n}">`, page courante avec `aria-current="page"`.
- `Prev`/`Next` : `aria-label="Page précédente"` / `"Page suivante"`, `disabled` natif aux bornes (hérité du composant `Button`).
- `Ellipsis` : `aria-hidden="true"`, jamais focusable — l'écart est visuellement évident, pas de texte alternatif énumérant les pages masquées (cohérent avec le choix déjà fait ailleurs de ne pas sur-décrire ce qui est visuellement clair, ex. `CaretUpDown` sur `Header-cell`).
- **Simple** : la zone `« Page {n} sur {N} »` en `aria-live="polite"` pour annoncer le changement de page aux lecteurs d'écran — contenu dynamique, aucun contrôle associé.
- Navigation clavier : `Tab` déplace le focus entre `Prev`, chaque `Page-item` visible et `Next` (`Ellipsis` jamais focusable) — cohérent avec le modèle de navigation déjà retenu pour `Table`.

## Guidelines Figma

Page dédiée `↳ Pagination`, section `Page-item` (ComponentSet) + section `Guidelines`. Exemple d'assemblage `Pagination (example)` montrant les deux structures (`Numbered` avec troncature, `Simple`) côte à côte.
