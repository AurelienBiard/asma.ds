# Composant KPI

> Ce fichier est la **source de vérité** du composant. Toute modification (anatomie, variants, tokens) se fait ici en premier, puis est répercutée dans Figma. Ne pas modifier le composant Figma directement sans reporter le changement dans ce fichier ensuite.

> **Statut** : composant créé le 2026-10-28 (page Figma `↳ KPI`) à partir du design dessiné par l'utilisateur (frames `KPI / Desktop` et `KPI / Mobile`, converties en ComponentSet). Une première version avec pastille d'icône et delta en texte a été remplacée.

Affiche **un indicateur clé** d'un coup d'œil : un libellé, une valeur dominante, une variation et son repère de comparaison. Sert à surveiller un chiffre, pas à l'explorer (→ `Table`, graphique). Non interactif.

## Pourquoi un composant (`new_component_gate`)

- **Concept propre** : la hiérarchie libellé / valeur / variation / repère, avec une tendance.
- **Pourquoi pas `Card`** : `Card` est un conteneur libre (Title / Subtitle / Body / Footer). Le KPI impose une structure et deux gabarits (Desktop / Mobile).
- **Composition** : la variation réutilise `Tag` (Small) et le pictogramme réutilise `Icon` — aucune brique nouvelle.
- **Réutilisation** : tableaux de bord, en-têtes de page de liste, écrans de synthèse.

## Propriétés du composant Figma

Variants (12 = 2 Device × 3 Trend × 2 State) :

- **Device** : `Desktop` / `Mobile`. Fixe le mode de la collection **Responsive** (Desktop / Mobile).
- **Trend** : `Neutral` / `Positive` / `Negative` — `Type` du `Tag` (`Neutral` / `Success` / `Danger`), flèche de tête (`ArrowRight` / `ArrowUp` / `ArrowDown`) et couleur de la minicourbe. Exprime le **jugement** (bon / mauvais), pas la direction : une baisse du taux d'erreur est `Positive`.
- **State** : `Default` / `Loading` (voir « Chargement »). `Trend` est sans effet en `Loading` : les 3 variantes sont identiques, gardées pour que la matrice reste complète.

Propriétés :

- **Label**, **Value**, **Caption** (Text) — défauts : `Commandes`, `1 284`, `vs mois dernier`.
- **Show-icon**, **Show-delta**, **Show-caption** (Boolean, défaut `true`) ; **Show-chart** (Boolean, défaut `false`) : affiche la minicourbe.
- **Icon** (Instance-swap, exposée depuis l'instance `Icon` du Header) — `Size=Small`, `Weight=Light`.
- **Tag** (instance exposée) : son `Label` porte la variation (défaut `+8,2 %`), `Show-icon-leading` affiche la flèche.

`Show-delta` et `Show-caption` ne sont **pas** liés : si les deux sont à `false`, le `Footer` est vide mais garde sa hauteur de ligne (pas de logique conditionnelle entre propriétés dans Figma).

## Anatomie

- **Header** : `Icon` (16 px) puis `Label`, gap `Spacing/component-2xs`.
- **Value-row** : `Value` (la valeur, toujours l'élément le plus grand du bloc) et, si `Show-chart`, la `Sparkline`. Gap `Spacing/component-sm` (Desktop) / `Spacing/component-2xs` (Mobile).
- **Footer** : `Tag` (variation) puis `Caption`, gap `Spacing/component-2xs`.

## Minicourbe (`Sparkline`)

Sous-composant du KPI (ComponentSet `Sparkline`, variant `Trend` = `Neutral` / `Positive` / `Negative` / `Stagnant`, page Figma `↳ KPI`, section `Sparkline`). Une **pastille** contenant une ligne seule, sans axe, sans valeur, sans infobulle.

- **Pastille** : fond `Background/subtle`, radius `Radius/card`, padding `Spacing/component-sm` (12), auto-layout vertical, hauteur hug.
- **Tracé** : 72 × 32 dans la pastille, épaisseur `Border/medium`, extrémités et jonctions arrondies, pas de remplissage. Couleur : `Feedback/Success/icon` (Positive), `Feedback/Danger/icon` (Negative), `Icon/secondary` (Neutral et Stagnant).
- **Position** : Desktop — à droite de `Value`, 96 × 56. Mobile — sous `Value`, pleine largeur × 56 (le tracé suit la largeur). La `Value-row` passe de 48 à 56 de haut quand la minicourbe est affichée : prévoir ce décalage (le KPI avec minicourbe est plus haut que sans).
- **Stagnant** : courbe quasi plate (écart de 2,6 px sur 32, centrée dans la boîte) pour une valeur qui ne bouge pas sur la période. À distinguer de `Neutral`, qui est irrégulier (monte et descend sans tendance, sans jugement). Même couleur `Icon/secondary`, pastille 96 × 56 inchangée.
- **Forme indicative** : le tracé du composant Figma est un placeholder (montée, descente, irrégulier, plat selon `Trend`). En code, tracer les vraies données en SVG (une `polyline`, points normalisés sur la boîte 72 × 32) — le composant ne définit que la pastille, le trait et la couleur.
- **Pourquoi pas un composant « Chart »** : aucune interaction, aucune donnée affichée ; c'est un habillage visuel de la valeur. Un vrai graphique (axes, survol) serait un autre composant.
- **Accessibilité** : décorative (`aria-hidden="true"`) quand la variation est affichée, car elle dit déjà le sens. Sans variation (`Show-delta=false`), lui donner `role="img"` et un `aria-label` qui résume période et sens (« Commandes sur 30 jours, en hausse »).

## Chargement (`State=Loading`)

Chaque élément est remplacé par une instance `Skeleton` (`components/skeleton/`) : icône (`Circle` 16), libellé (`Text`), valeur (`Rectangle`), tag (`Rectangle` en pilule) et repère (`Text`). Les trois zones (`Header`, `Value-row`, `Footer`) gardent la **hauteur exacte** de l'état `Default` — le KPI ne change pas de taille quand les données arrivent. Pas de minicourbe en `Loading`.

- Les propriétés `Label`, `Value`, `Caption` et `Show-*` n'agissent pas dans cet état.
- En code : `aria-busy="true"` sur le KPI, animation de pulsation/shimmer sur les squelettes (un squelette statique se lit comme une erreur de rendu). Ne jamais afficher une valeur `0` provisoire.

## Gabarits

| | Desktop | Mobile |
|---|---|---|
| Largeur par défaut | 280 | 160 (grille 2 colonnes d'un écran 360 : marges 12, gouttière 16) |
| Header | horizontal, aligné au centre | vertical, centré : icône au-dessus du libellé |
| Value | `Display/SM` — 48 px | `Display/SM` — 32 px |
| Minicourbe | à droite de `Value`, 96 × 56 | sous `Value`, pleine largeur × 56 |
| Footer | horizontal : `Tag` puis `Caption` | vertical : `Tag` au-dessus de `Caption` |
| Gap principal | `Spacing/component-xs` | `Spacing/component-2xs` |
| Padding | `Spacing/component-md` | `Spacing/component-md` |

La largeur est un défaut de prévisualisation : dans une grille, le KPI se met en FILL (`Grid/columns`, `Grid/gutter`).

## Tokens

- Fond `Background/elevated` · bordure `Border/subtle` (épaisseur `Border/thin`) · radius `Radius/card` · padding `Spacing/component-md`.
- `Label` : `Body/MD` + `Text/secondary`. `Value` : `Display/SM` + `Text/primary`. `Caption` : `Body/SM` + `Text/secondary`.
- `Sparkline` : fond `Background/subtle`, radius `Radius/card`, padding `Spacing/component-sm`, trait `Border/medium` (voir « Minicourbe »). `Skeleton` : fond `Background/disabled` (voir sa spec).
- `Tag` : voir `components/tag/tag-component-spec.md` (`Type=Success` / `Danger` / `Neutral`, `Size=Small`).
- Aucun token créé ; aucune ombre (niveau d'élévation 0, comme `Card`).

## Comportement

- Statique. Si le KPI mène à un détail, c'est le **conteneur** qui devient cliquable (lien ou `Card` cliquable), pas le KPI.
- `Value` ne se tronque pas : en cas de dépassement elle passe à la ligne. Préférer la **notation compacte** (`12,4 k`, `1,2 M€`), surtout en Mobile (zone utile 128 px).
- Les chiffres sont formatés par l'application (séparateur de milliers, devise, signe) ; le composant n'impose aucun format.

## Accessibilité

- Le **signe de la variation est écrit** (`+` / `−`) dans le `Tag` : la couleur, la flèche et la minicourbe ne portent jamais seules l'information.
- Ordre de lecture : libellé → valeur → variation → repère (« Commandes, 1 284, +8,2 % vs mois dernier »), sans `aria-label` redondant.
- L'icône, la flèche et la minicourbe sont décoratives : `aria-hidden="true"` (voir « Minicourbe » pour le cas sans variation). En `Loading` : `aria-busy="true"`.
- Le trait de la minicourbe est un élément graphique (≥ 3:1 attendu, tous respectés — le plus bas : `Feedback/Success/icon` en Light). Contrastes sur `Background/subtle` (fond de la pastille, calculés le 2026-10-28), Light / Dark : `Feedback/Success/icon` 3,15 / 9,34 · `Feedback/Danger/icon` 4,62 / 5,88 · `Icon/secondary` 7,24 / 6,34.
- Contrastes de `Text/primary` et `Text/secondary` sur `Background/elevated` (calculés le 2026-10-28), Light / Dark : 17,85 / 13,98 et 10,35 / 9,85 — ≥ 4,5:1 (AA). Les contrastes du `Tag` sont documentés dans sa spec.

## Do / Don't

**Do** : 2 colonnes en Mobile, 3 à 4 en Desktop · un libellé court (1 à 3 mots) · un repère de comparaison explicite · `Trend` selon le jugement.

**Don't** : afficher un état (→ `Tag`) ou une progression (→ `Progress`) · utiliser `Positive` / `Negative` pour une hausse / baisse neutre (→ `Neutral`) · multiplier les icônes décoratives sans sens.

## Guidelines Figma

Page dédiée `↳ KPI` : section `KPI` (ComponentSet + exemples `Exemple — Desktop`, `Exemple — Mobile` et `Exemple — Chargement`), section `Sparkline` et section `Guidelines`.

## À valider

- Forme du tracé placeholder.
- Hauteur du KPI avec minicourbe (+8 en Desktop, +32 en Mobile) : acceptée telle quelle dans le design actuel.
