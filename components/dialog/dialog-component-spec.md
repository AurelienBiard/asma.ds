# Composant Dialog

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : construit dans Figma avant que cette spec n'existe — rédigée le 2026-09-25 à partir d'une relecture de l'état Figma réel. À valider si un détail diverge de l'intention d'origine.

Tâche/décision modale focalisée (`decisions.yaml` → `Dialog`). Scindé en **3 composants indépendants** — `Dialog-header`, `Dialog-body`, `Dialog-footer` — composés manuellement selon le cas d'usage plutôt qu'un assemblage rigide unique. `Drawer` réutilise les 3 mêmes sous-composants dans un conteneur positionné différemment.

## Dialog-header

Composant unique (pas de variantes — piloté par propriétés) :
- **Title**, **Subtitle** (Text)
- **Show-subtitle** (Boolean, défaut `false`)
- **Show-back** (Boolean, défaut `false`) — chevron retour, pour dialogues multi-étapes
- **Show-close** (Boolean, défaut `true`)

Fond `Background/elevated` · Padding 16 px sur les 4 côtés (le padding bas a été ajusté le 2026-11-06 pour s'aligner sur les autres côtés, notamment au-dessus de la `Dialog-toolbar`) · Title `Heading/SM` · Subtitle `Misc/Caption` + `Text/secondary`.

## Dialog-toolbar (2026-11-06)

Barre d'actions **optionnelle**, propre au `Drawer` : elle s'affiche quand le contenu appelle des actions supplémentaires (terminer, éditer, supprimer…) qui ne relèvent ni du titre ni de la validation du pied. Même famille que `Dialog-header` / `Dialog-body` / `Dialog-footer` : composant indépendant, réutilisé par le `Drawer` (voir `components/drawer/`). Elle n'est pas affichée dans un `Dialog` centré.

- **Position** : entre `Dialog-header` et `Dialog-body`. **Zone fixe**, comme l'en-tête et le pied : elle ne défile jamais avec le corps.
- **Propriétés** (Boolean) : `Show-action-1` (défaut `false`), `Show-action-2` (défaut `true`), `Show-delete` (défaut `true`). Instances de `Button` exposées : `Action-1`, `Action-2`, `Delete`.
- **Anatomie** : rangée horizontale, gap 8, alignement vertical centré, padding 12 px vertical / 16 px horizontal. Un `spacer` en `FILL` pousse l'action de suppression à l'extrémité droite ; les autres actions s'alignent à gauche. Les boutons sans libellé suivent la règle 44×44 (`components/button/`). Hauteur : 68 px (44 + 2 × 12).
- **Tokens** : fond `Background/sunken` (modifié le 2026-11-07, `Background/subtle` auparavant : distingue la barre du corps et de l'en-tête en `Background/elevated`), **aucune bordure** (retirée le 2026-11-07 — le contraste de fond suffit à séparer la zone), aucun arrondi.
- **Clip** : `clipsContent: false`, comme les autres parties (voir « Champs dans un Dialog »).
- **Accessibilité** : `role="toolbar"` avec `aria-label`, navigation aux flèches, nom accessible (`aria-label`) sur chaque bouton sans libellé, dont la suppression. L'action destructive reste soumise à confirmation si elle est irréversible.

**Règles des actions (2026-11-07)**

| Action | Rôle | Button | Règle |
|---|---|---|---|
| `Action-1` | Action d'état (terminer, archiver, publier…) | `Type=Outlined`, **libellé + icône** | Seule action avec libellé : elle nomme l'état qu'elle fait changer. Masquée par défaut. |
| `Action-2` | Action secondaire (éditer, dupliquer, partager…) | `Type=Outlined`, **icône seule** (44×44) | Nom accessible obligatoire (`aria-label`). |
| `Delete` | Suppression | `Type=Destructive` (**plein**), icône seule (44×44) | **Toujours à droite**, isolé des autres actions par le `spacer` ; confirmation (`Dialog`) si irréversible. |

**Pas de barre dans les formulaires de création** : un `Drawer` ou un `Dialog` qui crée un élément n'a encore rien à terminer ni à supprimer. `Show-toolbar` reste à `false` ; seuls l'en-tête et le pied (Annuler / Créer) s'affichent. La barre est réservée à un élément **existant** (consultation, édition).

## Dialog-body

Composant unique avec une **vraie propriété Slot Figma** (`figma.createSlot()` n'existe pas via script — un Slot ne peut être créé que manuellement dans l'UI Figma — mais une fois créé ainsi, il est bien lisible/pilotable via l'API Plugin, confirmé sur ce composant).

Fond `Background/elevated` · Padding `Spacing/component-md` (Responsive). **`clipsContent: false`** sur le composant et sur le `slot` (2026-11-02) : le contenu du slot n'est jamais rogné, pour que la ligne de détourage Focus d'un champ (`strokeAlign: OUTSIDE`) reste visible. Le contenu glissé dans le slot (formulaire, groupe de champs) ne clippe pas non plus.

## Dialog-footer

Composant unique, **aucune propriété exposée** — placer des instances `Button` directement en enfants (typiquement un "Annuler" secondaire + une action primaire).

Fond `Background/elevated` · **aucune bordure** (décision 2026-11-06, conforme à Figma ; la bordure haute `Border/default` annoncée jusqu'ici n'a jamais existé dans le composant) · Padding 8 px en haut, 16 px (`Spacing/component-md`) sur les 3 autres côtés.

## Composition

Empiler header + body + footer dans un conteneur (radius `Radius/card`, aucune ombre tokenisée — l'architecture n'a pas de famille Shadow (Semantic = couleur uniquement), largeur fixe selon breakpoint) avec un fond assombri plein écran (voile plein écran sans token dédié — aucun token Overlay n'existe) derrière.

## Champs dans un Dialog (ligne de détourage et clip)

Un `Dialog` contient souvent des champs de saisie (`TextInput`, `Textarea`, `Select`, …) dont la bordure `Focus` est dessinée à l'extérieur (`strokeAlign: OUTSIDE`, voir `components/text-input/`). Règle : `Dialog-header`, `Dialog-body` et `Dialog-footer` ont `clipsContent: false`, et le conteneur de la composition aussi — un parent qui clippe coupe la ligne de détourage des champs en bordure du corps. Pour garder les coins arrondis (`Radius/card`) sans rogner : arrondir les coins hauts du `Dialog-header` et bas du `Dialog-footer` au lieu de clipper le conteneur. En code : pas de `overflow: hidden` sur le conteneur du dialogue ; le corps défile dans sa propre zone (`overflow: auto`) avec un padding qui laisse la place du trait (`Border/medium`). **Dans un `Drawer`, cet arrondi ne s'applique pas** (coins à 0 sur les instances, voir `components/drawer/`). **Validé et appliqué dans Figma (2026-11-02)** : `Dialog-header` (coins hauts) et `Dialog-footer` (coins bas) en `Radius/card` (variable liée), `clipsContent: false` conservé partout.

## Guidelines Figma

Page dédiée `↳ Dialog`.

> **Correction (2026-09-27)** : la spec citait des tokens inexistants (`Radius/lg`, `Spacing/lg`/`Spacing/md` en Responsive, `Shadow/*`, `Overlay/scrim`). Remappés sur l'existant (`Radius/card`, `Spacing/component-md` — valeur déjà utilisée dans Figma) ; ombre et voile documentés sans token, aucun token créé. À répercuter dans Figma.
