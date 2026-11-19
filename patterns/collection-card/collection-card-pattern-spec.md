# Pattern Collection card

> **Statut** : reclassé le 2026-11-19 depuis les composants `Card-collection`, `Block-header` et `Card-item` (promus depuis ASMA OS le 2026-11-07). Le pattern est « une carte qui liste un groupe d'entrées liées, plafonné à cinq, avec un lien vers la liste complète ». Les trois briques restent des composants Figma. Page Figma : `↳ Collection card` (section `💻 PATTERNS`, anciennement `↳ Card-collection`). Aucun token créé.

## Purpose

Présenter une collection ou un groupe d'informations sur une page de détail ou un écran d'accueil : en-tête, liste libre de lignes (une par entité), pied optionnel.

## Use when

- Collection liée ou groupe d'informations sur une page de détail (contacts d'une entreprise, tâches d'un projet, informations) et sur les écrans d'accueil (aujourd'hui, agenda, notes, ressources favorites).
- La liste est courte (5 éléments maximum).

## Do not use when

- Un simple conteneur titre / texte / actions → `Card`.
- Une liste longue ou des colonnes comparables → `Table` (pattern `DataTable`).
- Des éléments déplacés entre statuts → pattern `Kanban`.
- Imbriquée dans une autre carte : jamais.

## Components

- `Card-collection` (brique, ComponentSet) — le conteneur.
- `Block-header` (brique, ComponentSet) — en-tête : pictogramme, titre, compteur, filtre, actions.
- `Card-item / Note | Tâche | Contact | Relation | Information | Projet` (briques) — une ligne par entité.
- `Button` (`Neutral`, `Outlined`) dans le pied ; `Select`, `Count`, `Icon` dans l'en-tête ; `Tag`, `Checkbox`, `Avatar` dans les lignes.

## Structure

`Card-collection` → `Block-header` → **Slot** libre recevant des lignes `Card-item` → `cardFooter` optionnel. Le dernier `Card-item` n'a pas de séparateur (`Show-divider=false`).

## Interaction flow

1. Les lignes ouvrent l'entité (lien ou bouton englobant).
2. Au-delà de 5 éléments, le pied propose « Tous les … (N) » vers la liste complète.
3. Mobile : l'en-tête replie la carte (`State=Collapsed`).

## States

`Expanded`, `Collapsed` (mobile), vide (proposé : `Empty-state` Compact dans le slot), chargement (lignes `Skeleton`).

## Validation/errors

Aucune (liste en lecture seule) ; les actions des lignes suivent leur composant.

## Accessibility

Voir les sections des briques : région avec `aria-labelledby`, `aria-expanded` sur la bascule mobile, lignes en éléments de liste.

## Responsive behavior

`Device` = `Desktop` (752), `Desktop-sidebar` (360), `Mobile` (393, repliable).

## Tokens

Voir les sections des briques. Aucun token créé.

## Related components/patterns

`Card`, `List-group-header` (en-tête de groupe dans une liste, pas un titre de section), `Search-results` (réutilise les lignes `Card-item`) ; patterns `Search`, `Kanban`.

---

## Brique : Card-collection

Carte qui présente une **collection ou un groupe d'informations** : un en-tête de bloc (`Block-header`), un contenu libre (**Slot**) qui reçoit des `Card-item`, et un pied optionnel. **Distincte de `Card`** (conteneur générique titre / corps / actions, `components/card/`) : `Card-collection` sert à lister des éléments liés et se replie en mobile. Décision du 2026-11-07 : composant séparé, `Card` n'est pas modifié.

ComponentSet, 4 variantes :

| Device | State | Largeur | Notes |
|---|---|---|---|
| `Desktop` | `Expanded` | 752 | padding `Spacing/component-md`, gap `Spacing/component-sm`, sans pied |
| `Desktop-sidebar` | `Expanded` | 360 | colonne latérale, avec `cardFooter` |
| `Mobile` | `Expanded` | 393 | padding `Spacing/component-xs`, gap `Spacing/component-2xs`, avec `cardFooter` |
| `Mobile` | `Collapsed` | 393 | en-tête seul (60 px), repli |

- Propriétés : `Show-footer` (Boolean, `true`), `content` (Slot).
- `cardFooter` : `Secondary-action` (`Button` `Neutral`) et `Action` (`Button` `Outlined`).
- Fond `Background/elevated`.
- Accessibilité : région (`role="region"`, `aria-labelledby` sur le titre du `Block-header`) ; le repli mobile est un bouton avec `aria-expanded` ; chaque `Card-item` est un élément de liste, un item cliquable est un lien ou un bouton englobant, jamais un `div`.

## Brique : Block-header

En-tête d'un bloc de contenu (une `Card-collection` ou une section de page de détail) : pictogramme, titre, compteur, filtre et actions. Équivalent de `PageHeader` au niveau section. Ajouté à la promotion parce que `Card-collection` en dépend.

- ComponentSet, `Device` = `Desktop` | `Mobile`.
- Propriétés : `Title`, `Description` (Text) ; `Show-icon` (true), `Show-count` (true), `Show-filter` (true), `Show-action` (true), `Show-secondary-action` (true), `Show-toggle` (false), `Show-description` (true) — les valeurs par défaut sont celles du composant d'origine.
- `Title` : `Heading/SM`, `Text/primary`. `Description` : `Body/SM`, `Text/tertiary`. Gap `Spacing/component-xs`. Instances : `Icon`, `Count`, `Select`, `Button` (`Neutral` et `Outlined`).

## Brique : Card-item (patron de ligne)

Six composants, un par entité, nommés `Card-item / Note`, `/ Tâche`, `/ Contact`, `/ Relation`, `/ Information`, `/ Projet`. Une ligne : `row` (rangée horizontale, padding `Spacing/component-sm` en vertical, gap `Spacing/component-sm`) puis `divider` (`Border/subtle`).

| Patron | Contenu | Propriétés |
|---|---|---|
| `Note` | titre, entités liées, date, épingle | `Primary`, `Secondary`, `Date`, `Show-secondary`, `Show-pin`, `Show-divider` |
| `Tâche` | `Checkbox` (libellé de la tâche), `Tag`, échéance | `Échéance`, `Show-tag`, `Show-due`, `Show-divider` |
| `Contact` | `Avatar` (`Initials`, `Small`), nom, poste, e-mail ou téléphone | `Primary`, `Secondary`, `Meta`, `Show-leading`, `Show-secondary`, `Show-meta`, `Show-divider` |
| `Relation` | type, depuis, `Tag` | `Primary`, `Secondary`, `Show-tag`, `Show-divider` |
| `Information` | label, valeur — **sans séparateur** | `Label`, `Value` |
| `Projet` | nom, période, `Tag` | `Primary`, `Secondary`, `Show-tag`, `Show-divider` |

Tokens : `Primary` `Misc/Label` + `Text/primary` ; `Secondary` et `Date` `Body/SM` (`Text/secondary` ; `Text/tertiary` pour la date d'une note) ; `Information` : `Label` `Body/SM` + `Text/tertiary`, `Value` `Body/MD` + `Text/primary`, padding `Spacing/component-xs`, gap `Spacing/component-2xs`.

Règle : le dernier `Card-item` d'une carte n'a pas de séparateur (`Show-divider=false`). Ces patrons sont aussi les lignes de `Search-results`.
