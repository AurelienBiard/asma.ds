# Composant Calendar

Composant unique couvrant tous les pickers de date (Date Picker, Date Range Picker, Month/Year/Week Picker) — un seul concept de grille, décliné par usage.

## Calendar-day (atomique)

`State` = `Default`/`Hover`/`Selected`/`Today`/`In-range`/`Outside-month`/`Disabled`, 7 variantes. Case 32×32.
- `Selected` : fond `Action/primary`, texte **`Text/on-brand`** (reste clair dans les 2 modes, cohérent avec la correction du bouton Primary — pas `Text/inverse`, qui change de polarité avec le thème).
- `Today` : pas de fond, anneau `Border/focus` + `Primitive/Border/medium` — distinct de `Selected` pour ne jamais confondre "jour actuel" et "jour choisi".
- `In-range` : fond `Action/secondary-active` (base du Date Range Picker).
- `Outside-month` : `Text/tertiary`.
- Propriété texte `Day-number`.

## Calendar (assemblage)

- `Header` : `Nav-prev`/`Nav-next` (CaretLeft/CaretRight) encadrant `Month-label`. **Largeur fixe 248px** (pas hug), alignée sur la grille.
- `Weekday-row` : 7 cases 32×20, `Text/tertiary`.
- `Days-grid` : 5-6 rangées `Week-N` de 7 instances `Calendar-day`. Rangées `Header` et `Week-N` en largeur **FIXE** pour un alignement constant des colonnes.
- `clipsContent: false` partout (outer, Header, Days-grid, chaque Week) — retiré pour cohérence après une modification manuelle.

## Usage

- **Date Range Picker** : 2 jours `Selected` (début/fin), jours intermédiaires en `In-range`.
- **Month/Year Picker** : réutiliser `Calendar-day` à l'identique (mêmes 7 states), seul le contenu texte change (mois/années au lieu de jours).
- **Week Picker** : mettre toute une rangée `Week-N` en `In-range`.

## Leçon de construction

Un arc partiel n'est pas utilisé ici, mais rappel pour la famille Progress : `ellipse.arcData = { startingAngle, endingAngle, innerRadius }` fonctionne directement via l'API Figma.

Doc complète : guidelines Figma page `↳ Calendar`.
