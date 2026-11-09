# Composant Bulk-action-bar (2026-11-09)

> Ce fichier est la **source de vérité** du composant. Toute modification se fait ici en premier, puis est répercutée dans Figma.

Page Figma : `↳ Bulk-action-bar`. ComponentSet `Device=Desktop | Mobile`. Aucun token créé.

Barre d'actions groupées : elle apparaît quand **au moins un élément d'une collection est sélectionné** (`Table` avec `Selectable=True`, ou liste en mode sélection) et porte le nombre d'éléments sélectionnés et les actions qui s'appliquent à **toute la sélection**. Elle disparaît quand la sélection retombe à 0 et après l'exécution d'une action (la sélection est vidée).

## Use when

- Agir sur plusieurs éléments d'une même collection en une fois : supprimer, restaurer, archiver, ajouter un tag, changer un statut, reporter une échéance…
- La collection permet la sélection (`Table` `Selectable=True`, liste avec un mode sélection).

## Do not use when

- Action sur un seul élément → actions de la ligne, du menu contextuel ou de la page.
- Filtres, recherche, tri, bascule de vue (`SegmentedControl`), réglages d'affichage (`Switch` « Afficher les éléments archivés ») → barre de filtres (`patterns/filter-bar/`), toujours accessible sans sélection. La barre ne porte **que** des actions sur la sélection.
- Actions d'un formulaire ou d'un panneau → pied de `Dialog` / `Drawer`, `Dialog-toolbar`.

## Propriétés du composant Figma

- **Device** (variant) : `Desktop` / `Mobile`.
- **Selection-label** (Text, défaut « 3 sélectionnés ») : « 1 sélectionné », « 3 sélectionnés » ; au féminin selon l'entité si le produit le choisit (« 3 sélectionnées »).
- **Show-select-all** (Boolean, défaut `true`) : « Tout sélectionner ({n}) » et le séparateur — desktop seulement, quand la sélection ne couvre pas toutes les lignes visibles.
- **Show-action-2**, **Show-action-3** (Boolean, défaut `true` / `false`) — desktop ; sur mobile, ces actions passent dans `More`.
- **Show-more** (Boolean, défaut `true`) : bouton `More`, ouvre un `Menu` avec les actions suivantes.
- **Show-delete** (Boolean, défaut `true`) : action destructive, toujours en dernier.
- Instances exposées : `Action-1`, `Action-2`, `Action-3`, `More`, `Delete`, `Select-all` (libellé et icône réglables depuis l'instance de la barre).

## Anatomie

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

## Position

- **Desktop** : flottante, largeur hug, centrée horizontalement sur la zone de contenu (hors sidebar), à `Spacing/section-xs` du bas de la fenêtre. Elle ne pousse pas le contenu (aucun décalage de mise en page à l'apparition) ; la page réserve en bas un espace égal à sa hauteur tant qu'elle est visible, pour que la dernière ligne reste atteignable.
- **Mobile** : 361 px (marges de 16), à 16 px du bas + `safe-area-inset-bottom`, au-dessus d'une éventuelle barre de retour.
- **Toasts** : la barre disparaît quand une action s'exécute, le `Toast` de résultat prend sa place ; si un toast est visible pendant une sélection, il s'empile au-dessus de la barre.
- **Apparition** : glissement de 8 px vers le haut + fondu, `Motion/Duration/sm`, `Motion/Easing/standard` ; `prefers-reduced-motion` : fondu seul.

## Comportement

- Apparaît dès 1 élément sélectionné ; le libellé suit le nombre en direct.
- **Clear** et **Échap** (focus dans la collection ou la barre) vident la sélection.
- **Tout sélectionner** prend les lignes **visibles avec les filtres en cours** (jamais des éléments masqués) ; changer un filtre, la recherche, le tri ou la page vide la sélection.
- **Trois actions visibles au plus** sur desktop, puis `More` ; mobile : une action, puis `More`.
- **Sélection mixte** : une action qui ne concerne qu'une partie de la sélection (ex. « Archiver » avec des éléments déjà archivés) s'exécute sur les éléments concernés et le dit dans le toast (« 3 sur 5 archivés ») ; si elle ne concerne aucun élément, elle est désactivée (`State=Disabled`) avec la raison en `Tooltip`.
- **Action destructive** : une seule confirmation (`Dialog`) qui donne le nombre et les conséquences (« Supprimer 5 entreprises ? »), puis un seul `Toast` pour tout le lot, avec *Annuler* / *Restaurer*.
- **Tout ou rien** : une action groupée réussit pour tout le lot ou échoue sans rien modifier ; en cas d'échec, `Toast` d'erreur et la sélection est conservée.

## Accessibilité

- `role="toolbar"`, `aria-label="Actions sur la sélection"` ; navigation entre les boutons avec ← → (roving tabindex), `Tab` sort de la barre.
- `Selection-label` en `aria-live="polite"` (annonce « 3 sélectionnés » à chaque changement).
- L'apparition de la barre **ne déplace pas le focus** (il reste sur la case cochée) ; dans le DOM, la barre suit la collection.
- Boutons sans libellé : `aria-label` (« Désélectionner tout », « Plus d'actions », « Supprimer la sélection », libellé de l'action).
- Cases de sélection : noms accessibles de `Table` (« Sélectionner la ligne {nom} », « Tout sélectionner » avec `aria-checked="mixed"`).

## Code (référence)

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
