# Patterns ASMA

Un pattern est un workflow récurrent ou un modèle d'interaction composé de plusieurs composants. Ce n'est pas une composition d'écran ponctuelle.

## Où trouver un pattern (source de vérité unique)

**La liste des patterns vit dans `guidelines/decisions.yaml` → `pattern_selection`.** Chaque entrée donne le besoin en une phrase, des synonymes d'intention (anglais et français), les composants, le chemin de la spec, un statut et un pointeur `not_for`. Ce README ne décrit que le format des specs et l'organisation ; il ne duplique pas la liste.

Ordre de recherche pour un agent : **besoin → pattern (`pattern_selection`) → composant (`component_selection`) → token.**

Valeurs de statut : `built` (page Figma + spec) · `spec` (spec seule, pas de page Figma) · `candidate` (besoin identifié, pas de spec).

## Organisation

- Un dossier par pattern : `patterns/<nom>/<nom>-pattern-spec.md` (Login : `patterns/authentication/login-pattern-spec.md` ; Topbar et Site-nav sont documentés dans `patterns/navigation/sidebar-pattern-spec.md`).
- Figma : une page par pattern construit dans la section `💻 PATTERNS`.
- Briques : un composant qui n'existe que pour servir un pattern (par exemple `Kanban-card`) reste un composant Figma, mais sa spec est une section du pattern et son entrée `component_selection` renvoie vers le pattern.

## Pattern ou composant ?

C'est un pattern si au moins deux de ces critères sont vrais : il est surtout fait d'instances d'autres composants ASMA ; sa valeur est un workflow ou un agencement ; il s'assemble à la main avec un nombre arbitraire de parties. Il reste un composant s'il a une anatomie atomique propre réutilisée comme brique, ou une responsabilité unique.

## Format d'une spec

Purpose, Use when, Do not use when, Components, Structure, Interaction flow, States, Validation/errors, Accessibility, Responsive behavior, Tokens, Related components/patterns. Les specs de patterns sont rédigées en français, comme celles des composants ; les noms de sections restent en anglais (ils sont vérifiés par le script).

## Contrôle

`python3 scripts/check_patterns.py` vérifie que les dossiers de specs et les entrées `pattern_selection` correspondent, que les chemins existent, que les sections requises sont présentes et que les briques référencées dans `component_selection` pointent vers un vrai pattern.
