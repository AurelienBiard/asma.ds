---
version: alpha
name: asma.ds
description: Design system produit — architecture à 3 niveaux (Primitive/Semantic/Responsive), mobile-first, thème Light/Dark.
colors:
  primary: "#152ad3"
  primary-hover: "#1123b5"
  secondary: "#ffffff"
  neutral: "#f1f5f9"
  background: "#ffffff"
  background-elevated: "#ffffff"
  background-subtle: "#f8fafc"
  text-primary: "#0f172a"
  text-secondary: "#334155"
  text-disabled: "#475569"
  border-default: "#64748b"
  border-strong: "#475569"
  border-focus: "#152ad3"
  info: "#0891b2"
  success: "#16a34a"
  warning: "#d97706"
  danger: "#dc2626"
typography:
  # Valeurs Mobile (base mobile-first) — Desktop : display-sm 3rem/3rem, heading-md 1.75rem/2rem ; body, label, caption fixes
  display-sm:
    fontFamily: Inter
    fontSize: 2rem
    lineHeight: 3rem
    fontWeight: 700
  heading-md:
    fontFamily: Inter
    fontSize: 1.5rem
    lineHeight: 2rem
    fontWeight: 700
  body-md:
    fontFamily: Inter
    fontSize: 0.875rem
    lineHeight: 1.25rem
    fontWeight: 400
  body-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    lineHeight: 1rem
    fontWeight: 400
  label:
    fontFamily: Inter
    fontSize: 0.875rem
    lineHeight: 1.25rem
    fontWeight: 600
  caption:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    lineHeight: 1rem
rounded:
  control: 4px
spacing:
  2xs: 4px
  xs: 8px
  sm: 12px
  md: 16px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.control}"
    height: 40px
  button-outlined:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.control}"
  input:
    backgroundColor: "{colors.background-elevated}"
    borderColor: "{colors.border-default}"
    rounded: "{rounded.control}"
    height: 40px
  checkbox:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.control}"
    size: 20px
---

## Overview

asma.ds est un design system produit, mobile-first, construit avec une architecture à 3 niveaux : **Primitive** (valeurs brutes, échelle Tailwind pour les couleurs, t-shirt sizing pour le reste), **Semantic** (rôles contextuels, Light/Dark), **Responsive** (Mobile/Desktop). Ton visuel neutre et fonctionnel — priorité à la clarté et à l'accessibilité (contraste WCAG vérifié) sur l'expressivité décorative.

## Colors

La couleur de marque (`primary`, bleu) porte les actions principales et les états sélectionnés/actifs (boutons, cases cochées, radios, curseurs de switch). Texte et icônes posés sur un fond de marque utilisent `Text/on-brand` / `Icon/on-brand` (blanc dans les deux thèmes), jamais `Text/inverse` qui devient quasi noir en Dark. Les fonds Feedback sont au grade 100 (Light) / 900 (Dark). Les 4 couleurs de statut (`info`/`success`/`warning`/`danger`) sont volontairement saturées — alignées sur la couleur des icônes de statut pour un contraste suffisant en bordure de champ (correction récente : les bordures de validation étaient trop pâles).

En Dark, les surfaces Background suivent une échelle d'élévation : `sunken` (Neutral/950) < `default` (900) < `subtle` (850) < `elevated` (800) — plus c'est élevé, plus c'est clair. `disabled` (800) coïncide volontairement avec `elevated`.

`text-disabled` est identique en apparence des deux côtés du thème mais résulte de deux valeurs Primitive différentes (`Neutral/600` en Light, `Neutral/400` en Dark) — nécessaire après correction d'un bug de contraste où ces valeurs étaient quasiment inversées entre les deux modes.

## Typography

Police **Inter** pour le texte d'interface. **JetBrains Mono** (famille Alternate) est réservée au code, au contenu technique et au style `caption` (métadonnées d'appoint, libellés de section en capitales comme ceux de la Sidebar) — jamais pour le texte courant ni les contrôles. `label` (14px/20px, Semi Bold) est le style standard pour tout contrôle de formulaire (bouton, champ, case à cocher) — jamais `body-md`, qui est réservé au contenu éditorial ; les deux partagent taille et hauteur de ligne, seule la graisse les distingue.

## Layout & Spacing

Échelle en t-shirt sizing (2xs → 9xl), pas numérique. Les composants interactifs (bouton, champ, case à cocher) utilisent presque exclusivement `xs`, `sm` et `md` — les échelles plus grandes (`lg` et au-delà) sont réservées à la mise en page, pas aux composants eux-mêmes.

## Shapes

Un seul rayon de coin pour tous les contrôles interactifs (`rounded.control`, 4px) — pas de variation par composant. Les indicateurs ronds (Dot Indicator, Radio) utilisent un rayon à 50% de leur propre taille plutôt que ce token, puisqu'ils doivent rester des cercles parfaits quelle que soit leur taille.

## Motion

Le mouvement porte un changement d'état, jamais de la décoration. Fondation Primitive uniquement (`Motion/Duration/sm` 240ms, `md` 440ms ; `Motion/Easing/spring`, `standard`, `accelerate` ; `Motion/Tension/*`). Seul traitement signature : la **tension de surface** — l'indicateur de sélection s'étire vers sa nouvelle position et laisse une gouttelette qui se détache — réservée aux indicateurs opaques de `SegmentedControl` et `ThemeSwitcher` (variante `Motion=Tension`), jamais sur un Chip ni un élément en contour. `prefers-reduced-motion` coupe toute animation.

## Components

Référence rapide seulement — chaque composant a sa propre spec détaillée dans `components/<nom>/`, qui fait autorité en cas de divergence avec ce fichier.

Hauteur standard des contrôles de saisie sur une ligne (bouton, champ texte) : **40px**, obtenue par `spacing.sm` (padding vertical) + la hauteur de ligne du style `label`. Ne jamais fixer cette hauteur en dur — elle doit rester le résultat du padding + du texte, pas une valeur imposée (un stroke en alignement `INSIDE` combiné à un hug peut fausser ce calcul de 1-2px selon le contexte — vérifier visuellement après toute modification de bordure).

## Do's and Don'ts

**Do :**
- Utiliser les tokens Semantic (jamais les valeurs Primitive brutes) dans tout composant.
- Utiliser Warning pour une information non bloquante, Danger quand elle empêche la validation.
- Garder un seul bouton Primary par écran/section pour l'action principale.

**Don't :**
- Ne jamais coder une couleur, un espacement ou un rayon en valeur littérale — toujours passer par une variable liée.
- Ne jamais utiliser Checkbox pour un choix exclusif (→ Radio) ni Radio pour une bascule instantanée (→ Switch).
- Ne jamais afficher une icône de statut sans message associé, ou l'inverse.

---

*Ce fichier est généré depuis `tokens/*.json` et l'état live de Figma — ne pas éditer les valeurs de tokens ici directement, les corriger à la source (Figma) puis régénérer.*
