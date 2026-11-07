# Composants Card-collection, Block-header et Card-item (2026-11-07)

Page Figma : `↳ Card-collection`. **Promus depuis ASMA OS** (`OS / Card`, `OS / BlockHeader`, `OS / Card-item / …`) le 2026-11-07 ; les instances des maquettes OS suivent les composants.

## Card-collection

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

### Règles d'usage

- Collection liée ou groupe d'informations sur une page de détail (contacts d'une entreprise, tâches d'un projet, informations) et écrans d'accueil (aujourd'hui, agenda, notes, ressources favorites).
- **5 éléments maximum** dans la carte ; au-delà, le pied propose « Tous les … (N) ».
- Ne pas imbriquer une `Card-collection` dans une autre carte. Pour un simple conteneur titre / texte / actions : `Card`.

### Accessibilité

- Région (`role="region"`, `aria-labelledby` sur le titre du `Block-header`).
- Le repli mobile est un bouton avec `aria-expanded`.
- Chaque `Card-item` est un élément de liste ; un item cliquable est un lien ou un bouton englobant, jamais un `div`.

## Block-header

En-tête d'un bloc de contenu (une `Card-collection` ou une section de page de détail) : pictogramme, titre, compteur, filtre et actions. Équivalent de `PageHeader` au niveau section. Ajouté à la promotion parce que `Card-collection` en dépend.

- ComponentSet, `Device` = `Desktop` | `Mobile`.
- Propriétés : `Title`, `Description` (Text) ; `Show-icon` (true), `Show-count` (true), `Show-filter` (true), `Show-action` (true), `Show-secondary-action` (true), `Show-toggle` (false), `Show-description` (true) — les valeurs par défaut sont celles du composant d'origine.
- `Title` : `Heading/SM`, `Text/primary`. `Description` : `Body/SM`, `Text/tertiary`. Gap `Spacing/component-xs`. Instances : `Icon`, `Count`, `Select`, `Button` (`Neutral` et `Outlined`).

## Card-item (patron de ligne)

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

Aucun token créé.
