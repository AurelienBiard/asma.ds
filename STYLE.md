---
name: asma.ds — style graphique
version: alpha
revision: "2026-10-28 — nouvelle DA : pictogrammes et logos remplacent les doodles sur la cover"
description: Identité graphique globale d'asma.ds et de ses supports (portfolio « Dossier de compétences », cover, pictogrammes et logos). À lire par tout agent avant de produire un écran, une slide, un pictogramme ou un logo.
references:
  figma_pages: ["✨ COVER", "↳ Logos", "↳ Doodles (historique)", "↳ Dossier de compétences (PROTOTYPES)"]
  complements: ["DESIGN.md (tokens et règles composants)", "guidelines/*.yaml"]
---

# STYLE.md — identité graphique asma.ds

`DESIGN.md` dit **comment l'interface fonctionne** (tokens, composants). `STYLE.md` dit **à quoi elle ressemble** : le parti pris visuel à reproduire sur les supports éditoriaux (slides, cover, portfolio, pages de présentation). En cas de conflit sur une valeur de token, `DESIGN.md` et `tokens/*.json` font foi ; ce fichier ne définit aucune valeur nouvelle.

## 1. Principes (dans l'ordre de priorité)

1. **Clarté avant décoration.** Rien qui ne porte une information ou une structure.
2. **Éditorial technique.** Ton sobre d'un document d'ingénierie : filets fins, libellés mono, beaucoup d'air.
3. **Un seul accent fort.** Le bleu `Action/primary` signale l'important ; tout le reste est neutre.
4. **Pictogramme géométrique plein.** Une forme simple par pictogramme, en `Icon/primary`, sur une tuile `Feedback/Info/background` aux coins `Radius/card` (§6). Pas d'ombre portée, de flou, de dégradé ni de grain/mezzotint sur les supports éditoriaux.
5. **Tokens uniquement.** Aucune couleur, espacement ou rayon littéral : toujours une variable liée.

## 2. Couleur

| Rôle | Token |
|---|---|
| Fond de page | `Background/subtle` (zones panneau : `Background/subtle`, page : fond clair) |
| Texte principal / titres | `Text/primary` |
| Libellés mono, texte secondaire | `Text/secondary` ; mono de rail : `Text/disabled` |
| Filets, contours | `Border/default` (1px) |
| Accent fort (barres de niveau, pastille « centrale », actions) | `Action/primary` |
| Niveau intermédiaire (pastille « forte ») | primitive `Color/Cyan` clair (fond) + texte foncé |
| Niveau neutre (pastille « appliquée ») | `Background/subtle` + `Text/primary` |
| Statut positif (ex. « Ouvert à discussion ») | famille `Feedback/Success` |
| Glyphe des pictogrammes | `Icon/primary` |
| Tuile des pictogrammes | `Feedback/Info/background` (liée à la variable, aucune valeur littérale) |
| Wordmark des logos | `Text/primary` |
| *Historique* — dalle des doodles | cyan clair `#cffafe` à 20 % + cadre intérieur `#18fefe` à 8 % (valeurs littérales, doodles masqués sur la cover, voir §6 bis) |

Règles : un seul niveau d'accent par vue ; le cyan ne s'utilise jamais seul comme fond de grande surface ; ne jamais introduire une nouvelle teinte pour distinguer un niveau — utiliser l'échelle ci-dessus.

## 3. Typographie

- **Inter** : titres (Bold), corps (Regular 14px), valeurs clés (Bold 14px).
- **JetBrains Mono** : eyebrows et libellés de champ **en capitales** (FOCUS, LOCATION, EXPERIENCE, STATUT, ÉCHELLE), rail latéral, métadonnées. Jamais pour le texte courant.
- Échelle observée sur les slides 1920×1080 : titre 48px Bold · nom de section 24–32px Bold · corps 14px · libellé mono 12–16px.
- Tout texte passe par un Text Style (`H1`, `H2`, `Body/MD`, `Body/SM`, `Misc/Label`, `Misc/Caption`). Aucun texte sans Text Style.

## 4. Cadre de page (slides et supports « portfolio »)

Format 1920×1080. Structure fixe :
- **Rail gauche** `SlideSidebar` : 60px de large, pleine hauteur, séparé du contenu par un filet 1px. Contient la date (`JJ/MM/AAAA`, Inter 12px) et le mot « portfolio » (mono 12px), tous deux pivotés à la verticale.
- **Barre de navigation haute** : liens Inter 14px (l'actif en pastille `Background/subtle`), sélecteur de thème à droite, filet 1px dessous.
- **Pied de page** : pagination « Page X sur XX » à droite (Inter 14px Bold), filet 1px dessus.
- **Filets de cadre** : 1px `Border/default`. À chaque croisement de filets, un point de 5px (fond `Icon/inverse`, contour `Border/default` 1px) — signature « blueprint ».
- **Contenu** : zone centrale, deux colonnes maximum ; panneaux sur `Background/subtle`, sans contour, coins `Radius/card`.

## 5. Composants éditoriaux

- **Pastille / Tag** : pill (`Radius/pill`), Inter 14px ; utilisée pour les domaines (B2B SaaS, Data intensive…) et les niveaux d'expertise.
- **Barre de niveau** : trait fin 6–8px, piste `Background/subtle`, remplissage `Action/primary` ; la longueur encode le niveau (5 = pleine). Une pastille de libellé à droite redit le niveau — l'information ne repose jamais sur la couleur seule.
- **Échelle de niveaux** : 5 Expertise centrale · 4 Compétence forte · 3 Compétence appliquée · 2 Culture / exposition.
- **Bloc champ** : eyebrow mono capitales (`Text/secondary`) puis valeur Inter Bold 14px.
- **Statut** : pastille verte avec point plein + libellé.
- **Captures produit** : posées sur fond neutre, sans cadre décoratif ; mockup laptop acceptable pour les cas d'étude ; logos clients en monochrome.

## 6. Pictogrammes et logos (DA actuelle)

Page Figma `↳ Logos` (section Foundation). Trois objets, du plus petit au plus grand :

**`picto`** — ComponentSet, 80×80, une variante par pictogramme (propriété `Property 1`). Tuile `Feedback/Info/background`, coins `Radius/card` (8), aucun contour, aucun effet ; un seul glyphe plein en `Icon/primary`, centré. Sur la cover les instances sont agrandies à 160×160.

| Variante | Rôle | Forme (telle que construite dans Figma) |
|---|---|---|
| `concatenation` | marque du portfolio | cercle plein |
| `asma-ds` | marque du design system | polygone |
| `asma-os` | marque de l'application | étoile |
| `productDesign` | pôle Product Design | polygone |
| `designSystem` | pôle Design Systems | union de trois cercles |
| `uxUi` | pôle UX/UI | étoile |
| `tech` | pôle Design × Tech | forme vectorielle unique |
| `AI` | pôle Design × IA | union de formes (étoile) |

**`logo / <nom>`** — lockups horizontaux (`logo / concatenation`, `logo / asma-ds`, `logo / asma-os`) : instance `picto` 32×32 puis wordmark en minuscules, `Text/primary`, séparés de 8. Hauteur 32. Le wordmark est **tracé en vecteurs** (texte converti) : il ne se modifie pas comme du texte ; pour un nouveau logo, reconvertir le texte en vecteurs et conserver gap et hauteur. Le lockup de `concatenation` s'écrit `concatenation.fr`.

**`Logos`** — ComponentSet des logos clients (OuestFrance, Innlog, Ynov, Frinergy, CHStudio), 40×40, utilisé par `Timeline` (`Show-logo`). Inchangé par cette DA ; il n'est pas un logo de la marque.

**Règles.**
- Un pictogramme = une forme pleine, sans contour résiduel, en `Icon/primary` sur sa tuile ; pas de deuxième teinte, pas de trait fin ni de pointillé.
- Un nouveau pictogramme garde la tuile, la taille 80×80 et le rayon `Radius/card` ; il s'ajoute comme variante de `picto`.
- Un lockup n'est jamais redessiné à la main : il se compose d'une instance de `picto` et d'un wordmark vectoriel.
- Marges de protection d'un logo : non spécifiées (voir §9).

## 6 bis. Doodles (historique)

Composant `Doodle` (page `↳ Doodles`), propriété `Pole`, 100×100, cinq illustrations au trait (cercles concentriques, arcs épais, triangle pointillé, points en orbite) sur dalle cyan clair. **Ils ne sont plus affichés sur la cover** depuis la nouvelle DA : les pictogrammes des pôles (`productDesign`, `designSystem`, `uxUi`, `tech`, `AI`) les remplacent. La page et les deux bandes de la cover sont conservées dans le fichier, bandes masquées. Ne plus utiliser les doodles sur un nouveau support sans demande. Leur grammaire (cercle + un élément distinctif, deux épaisseurs, pointillé pour l'hypothétique) n'est plus une règle de la DA.

## 7. Cover (✨ COVER, `Slide 16:9 - 1`)

Format 1920×1080, fond `Background/subtle`, `clipsContent` actif. Deux plans :

**Plan 1 — grille de pictogrammes (centre).**
- Cadre `Frame 2608834` : auto-layout horizontal à retour, 793×379, pivoté de **5°**, positionné vers le centre (x 548, y 386).
- 8 instances de `picto` de 160×160, en 2 rangées de 4, pas d'environ 205 px (écart ≈ 45 px). Ordre : `concatenation`, `asma-ds`, `asma-os`, `productDesign` puis `designSystem`, `uxUi`, `tech`, `AI` — les trois marques d'abord, les cinq pôles ensuite.
- Aucune bande de doodles : les deux cadres `Frame 2608832` et `Frame 2608833` (400×2000, −12,14°) sont conservés mais **masqués**.

**Plan 2 — bloc titre (bas droite)** — inchangé.
- Cadre `section` : auto-layout vertical, marges 128px ; `title_content` 1664×824, gap 32, aligné en bas et à droite (`MAX/MAX`), tout le texte aligné à droite.
- Titre « DESIGN SYSTEM » : style `Heading/LG` (Inter Bold, 28 px dans l'état Figma actuel — l'ancienne spec indiquait `Display/LG` 48), `Text/primary`, en capitales.
- Sous-titre « Asma, AI driven Design System » : `Body/MD`, `Text/primary`.
- Métadonnées en bas : « Design system » puis « V 1.0, 2026 » en `Body/MD`, `Text/primary`, alignées à droite, séparées du sous-titre par un grand espace.
- Une ligne de sommaire (Lignes directrices, Fondations, Composants, Typographies, Icônes, Élévation, Animation — Inter Bold 24, interlettrage −2 %) existe dans le fichier mais n'est pas affichée : ne pas la réafficher sans demande.

**Règles de la cover.**
- Pas de cadre « blueprint » (rail, nav, pagination) : ils appartiennent aux slides de contenu (§4), jamais à la cover.
- Pas d'autre visuel que la grille de pictogrammes ; pas de photo ni de dégradé ; pas de doodles.
- Hiérarchie : pictogrammes (texture) → titre (information) ; le texte ne passe jamais au-dessus d'une tuile.
- Les tuiles sont des instances de `picto` : on ne les redessine pas sur la cover.

## 8. Do / Don't

**Do** : filets 1px, beaucoup de blanc, libellés mono capitales, un seul accent bleu, pictogrammes pleins sur tuile `Feedback/Info/background`, logos composés d'une instance `picto` et d'un wordmark vectoriel, texte en Text Styles, tokens Semantic.

**Don't** : ombre, flou, dégradé, grain ou effet de trame sur les supports éditoriaux (mezzotint abandonné) · doodles sur un nouveau support · texte posé sur une tuile de pictogramme · logo redessiné à la main · nouvelle teinte non tokenisée · texte courant en mono · information portée par la couleur seule · plus d'un accent fort par vue.

## 9. Ambiguïtés à signaler (ne pas trancher seul)

- Teinte exacte du niveau intermédiaire (échelle Cyan à confirmer côté Figma).
- **Doodles** : page `↳ Doodles` et bandes de la cover conservées mais masquées — à supprimer ou à garder comme archive ?
- Propriété de `picto` nommée `Property 1` (valeurs `concatenation`, `asma-ds`, `asma-os`, `productDesign`…) : à renommer (ex. `Name`) ; idem pour `Logos` (`Property 1`, déjà signalé dans la spec Timeline).
- Wordmark des logos tracé en vecteurs : la police d'origine n'est pas documentée ; marges de protection et taille minimale d'un logo non spécifiées.
- Grille de la cover : rotation 5° et position tirées de l'état Figma, pas d'une règle ; ne pas les généraliser aux slides de contenu.
- Cadre de page hors format 1920×1080 (mobile, web) : non spécifié.
- Dossier de compétences : slides non encore spécifiées une par une (Expériences, Contact) ; leur usage éventuel des doodles n'a pas été relu.
- Ligne de sommaire de la cover : masquée, statut à confirmer (supprimer ou conserver).

## 10. Entête de l'artefact asma.ds (`Cover/preview.html`)

Déclinaison de la cover (§7) pour l'entête de l'artefact, 960×288 (échelle ½ de la cover), publiée dans l'artefact (page Cover) ; le repo n'en contient pas de copie. Elle reproduit la DA actuelle : fond `Background/subtle`, grille de 8 pictogrammes (`picto`, tuile `Feedback/Info/background`, forme `Icon/primary`) pivotée de 5°, bloc titre en bas à droite aligné à droite. Mêmes règles que la cover : pas de filets ni de cadre blueprint, texte jamais sur une tuile.
