# Pattern BulkActions

> **Statut** : reclassé le 2026-11-19 depuis le composant `Bulk-action-bar` (créé le 2026-11-09). Le pattern est « sélectionner plusieurs éléments, agir sur tous » ; `Bulk-action-bar` en est la barre flottante (ComponentSet Figma conservé). Page Figma : `↳ Bulk-actions` (section `💻 PATTERNS`, anciennement `↳ Bulk-action-bar`). Aucun token créé.

## Purpose

Agir sur plusieurs éléments d'une même collection en une fois (supprimer, restaurer, archiver, ajouter un tag, changer un statut, reporter). Le pattern couvre la sélection, la barre flottante, les sélections mixtes, la confirmation et le retour d'information.

## Use when

- La collection permet la sélection (`Table` avec `Selectable=True`, ou liste avec un mode sélection).
- La même action s'applique à de nombreux éléments : supprimer, restaurer, archiver, ajouter un tag, changer un statut, reporter une échéance.

## Do not use when

- Action sur un seul élément → actions de la ligne, du menu contextuel ou de la page.
- Filtres, recherche, tri, bascule de vue (`SegmentedControl`), réglages d'affichage (`Switch` « Afficher les éléments archivés ») → pattern `Filter bar`, toujours accessible sans sélection. La barre ne porte **que** des actions sur la sélection.
- Actions d'un formulaire ou d'un panneau → pied de `Dialog` / `Drawer`, `Dialog-toolbar`.

## Components

- `Table` (`Selectable=True`) ou liste sélectionnable — la collection ; noms des cases : « Sélectionner la ligne {nom} », « Tout sélectionner » avec `aria-checked="mixed"`.
- `Bulk-action-bar` (brique, ComponentSet `Device=Desktop | Mobile`) — voir « Brique : Bulk-action-bar ».
- `Button` (`Ghost`, `Outlined`, `Destructive-ghost`), `Menu` (actions de `More`), `Tooltip` (raison d'une action désactivée).
- `Dialog` — une confirmation pour une action destructive. `Toast` — un résultat par lot.

## Structure

La barre est flottante, centrée en bas de la zone de contenu, et apparaît dès qu'au moins un élément est sélectionné. Elle ne pousse pas le contenu ; la page réserve en bas un espace égal à sa hauteur tant qu'elle est visible.

## Interaction flow

1. L'utilisateur coche une ligne ; la barre apparaît avec un compteur en direct.
2. « Tout sélectionner ({n}) » optionnel : prend les lignes **visibles avec les filtres en cours**, jamais des éléments masqués. Changer un filtre, la recherche, le tri ou la page vide la sélection.
3. L'utilisateur déclenche une action : trois actions visibles au plus sur desktop, puis `More` ; mobile : une action, puis `More` ; `Delete` toujours en dernier.
4. Action destructive : un seul `Dialog` donnant le nombre et les conséquences (« Supprimer 5 entreprises ? »), puis un seul `Toast` pour tout le lot avec *Annuler* / *Restaurer*.
5. La barre disparaît quand la sélection retombe à 0 et après l'exécution d'une action (sélection vidée). Le `Toast` de résultat prend sa place ; un toast visible pendant une sélection s'empile au-dessus de la barre.

## States

Masquée (0 sélectionné), visible (≥ 1), action désactivée (`State=Disabled`, raison en `Tooltip`), en cours d'exécution, succès (`Toast`), erreur (`Toast` d'erreur, sélection conservée).

## Validation/errors

- **Sélection mixte** : une action qui ne concerne qu'une partie de la sélection (ex. « Archiver » avec des éléments déjà archivés) s'exécute sur les éléments concernés et le dit dans le toast (« 3 sur 5 archivés ») ; si elle ne concerne aucun élément, elle est désactivée avec la raison en `Tooltip`.
- **Tout ou rien** : une action groupée réussit pour tout le lot ou échoue sans rien modifier ; en cas d'échec, `Toast` d'erreur et la sélection est conservée.

## Accessibility

Voir la section de la brique (`role="toolbar"`, compteur en direct, focus non déplacé).

## Responsive behavior

Desktop : largeur au contenu, centrée sur la zone de contenu (hors sidebar), à `Spacing/section-xs` du bas de la fenêtre. Mobile : 361 px (marges de 16), à 16 px du bas + `safe-area-inset-bottom`, au-dessus d'une éventuelle barre de retour.

## Tokens

Voir la section de la brique. Aucun token créé.

## Related components/patterns

`Table`, `Button`, `Menu`, `Dialog`, `Toast`, `Tooltip` ; patterns `Filter bar`, `DataTable`, `Confirmation`.

---

## Brique : Bulk-action-bar

ComponentSet Figma `Device=Desktop | Mobile`. Barre d'actions groupées : elle apparaît quand **au moins un élément d'une collection est sélectionné** et porte le nombre d'éléments sélectionnés et les actions qui s'appliquent à **toute la sélection**.

### Propriétés du composant Figma

- **Device** (variant) : `Desktop` / `Mobile`.
- **Selection-label** (Text, défaut « 3 sélectionnés ») : « 1 sélectionné », « 3 sélectionnés » ; au féminin selon l'entité si le produit le choisit (« 3 sélectionnées »).
- **Show-select-all** (Boolean, défaut `true`) : « Tout sélectionner ({n}) » et le séparateur — desktop seulement, quand la sélection ne couvre pas toutes les lignes visibles.
- **Show-action-2**, **Show-action-3** (Boolean, défaut `true` / `false`) — desktop ; sur mobile, ces actions passent dans `More`.
- **Show-more** (Boolean, défaut `true`) : bouton `More`, ouvre un `Menu` avec les actions suivantes.
- **Show-delete** (Boolean, défaut `true`) : action destructive, toujours en dernier.
- Instances exposées : `Action-1`, `Action-2`, `Action-3`, `More`, `Delete`, `Select-all` (libellé et icône réglables depuis l'instance de la barre).

### Anatomie

Rangée horizontale, alignement centré, padding et gap `Spacing/component-xs`, hauteur 60 (bouton 44 + 2 × 8).

1. **Clear** — `Button` `Ghost`, icône `X`, sans libellé 44×44 ; nom accessible « Désélectionner tout ».
2. **Selection-label** — texte `Misc/Label`, `Text/primary` ; mobile : `FILL`, une ligne, ellipse.
3. **Select-all** — `Button` `Ghost` « Tout sélectionner ({n}) » (desktop).
4. **Divider** — rectangle 1 × 24, `Border/subtle` (desktop, avec `Select-all`).
5. **Action-1 … Action-3** — `Button` `Outlined`, icône + libellé (desktop) ; mobile : `Action-1` seule, icône seule 44×44.
6. **More** — `Button` `Outlined`, icône `DotsThree`, sans libellé 44×44.
7. **Delete** — `Button` `Destructive-ghost`, icône `Trash` + « Supprimer » (desktop), icône seule (mobile).

| Élément | Token |
|---|---|
| Fond | `Background/elevated` |
| Bordure | `Border/subtle`, 1 px |
| Rayon | `Radius/card` |
| Élévation | `Elevation/3` (barre flottante, comme une navigation collante — `foundations.yaml` → `elevation`) |
| Padding, gap | `Spacing/component-xs` |
| Libellé | `Misc/Label`, `Text/primary` |

### Position et mouvement

- Desktop : flottante, largeur au contenu, aucun décalage de mise en page à l'apparition. Mobile : voir le pattern.
- Apparition : glissement de 8 px vers le haut + fondu, `Motion/Duration/sm`, `Motion/Easing/standard` ; `prefers-reduced-motion` : fondu seul.
- **Clear** et **Échap** (focus dans la collection ou la barre) vident la sélection.

### Accessibilité

- `role="toolbar"`, `aria-label="Actions sur la sélection"` ; navigation entre les boutons avec ← → (roving tabindex), `Tab` sort de la barre.
- `Selection-label` en `aria-live="polite"` (annonce « 3 sélectionnés » à chaque changement).
- L'apparition de la barre **ne déplace pas le focus** (il reste sur la case cochée) ; dans le DOM, la barre suit la collection.
- Boutons sans libellé : `aria-label` (« Désélectionner tout », « Plus d'actions », « Supprimer la sélection », libellé de l'action).

### Code (référence)

```html
<div class="bulk-bar" role="toolbar" aria-label="Actions sur la sélection">
  <button class="btn btn--ghost btn--icon-only" aria-label="Désélectionner tout">…X…</button>
  <span class="bulk-bar__label" aria-live="polite">3 sélectionnés</span>
  <button class="btn btn--ghost">Tout sélectionner (12)</button>
  <span class="bulk-bar__divider" aria-hidden="true"></span>
  <button class="btn btn--outlined">…Archive… Archiver</button>
  <button class="btn btn--outlined btn--icon-only" aria-label="Plus d'actions" aria-haspopup="menu">…DotsThree…</button>
  <button class="btn btn--destructive-ghost">…Trash… Supprimer</button>
</div>
```

```css
.bulk-bar {
  position: fixed; left: 50%; bottom: var(--spacing-section-xs); transform: translateX(-50%);
  display: flex; align-items: center; gap: var(--spacing-component-xs); padding: var(--spacing-component-xs);
  background: var(--color-background-elevated); border: var(--border-scale-thin) solid var(--color-border-subtle);
  border-radius: var(--radius-card); box-shadow: 0 20px 50px 0 var(--color-shadow-subtle); /* Elevation/3 */
}
.bulk-bar__label { font-size: var(--font-size-label); font-weight: var(--font-weight-scale-semibold); color: var(--color-text-primary); }
.bulk-bar__divider { width: 1px; height: 24px; background: var(--color-border-subtle); }
```
