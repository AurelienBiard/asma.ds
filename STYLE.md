---
name: asma.ds — style graphique
version: alpha
description: Identité graphique globale d'asma.ds et de ses supports (portfolio « Dossier de compétences », cover). À lire par tout agent avant de produire un écran, une slide ou une illustration.
references:
  figma_pages: ["✨ COVER", "↳ Doodles", "↳ Dossier de compétences (PROTOTYPES)"]
  complements: ["DESIGN.md (tokens et règles composants)", "guidelines/*.yaml"]
---

# STYLE.md — identité graphique asma.ds

`DESIGN.md` dit **comment l'interface fonctionne** (tokens, composants). `STYLE.md` dit **à quoi elle ressemble** : le parti pris visuel à reproduire sur les supports éditoriaux (slides, cover, portfolio, pages de présentation). En cas de conflit sur une valeur de token, `DESIGN.md` et `tokens/*.json` font foi ; ce fichier ne définit aucune valeur nouvelle.

## 1. Principes (dans l'ordre de priorité)

1. **Clarté avant décoration.** Rien qui ne porte une information ou une structure.
2. **Éditorial technique.** Ton sobre d'un document d'ingénierie : filets fins, libellés mono, beaucoup d'air.
3. **Un seul accent fort.** Le bleu `Action/primary` signale l'important ; tout le reste est neutre.
4. **Illustration géométrique au trait.** Tracé fin sur fond clair ; la seule teinte autorisée derrière un doodle est la dalle cyan clair de la cover (§6). Pas d'ombre portée, de flou, de dégradé ni de grain/mezzotint.
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
| Traits des doodles | `Icon/primary` |
| Dalle des doodles (cover) | cyan clair `#cffafe` à 20 % + cadre intérieur `#18fefe` à 8 % (valeurs littérales à tokeniser, voir §9) |

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

## 6. Doodles (illustrations des 5 pôles)

Composant `Doodle` (page `↳ Doodles`), propriété `Pole`, 100×100 (400×400 sur la cover). Tracés convertis en formes remplies `Icon/primary` (aucun contour résiduel).

| Variante | Pôle | Motif |
|---|---|---|
| `Pole=ProductDesign` | Product Design | triangle plein au trait + triangle pointillé, cercle central |
| `Pole=DesignSystem` | Design Systems | cercles concentriques, arcs épais, point central |
| `Pole=UX/UI` | UX/UI | cercles, croisillon et repères |
| `Pole=Tech` | Design × Tech | anneaux avec arcs de largeurs inégales |
| `Pole=IA` | Design × IA | cercle central, quatre points en orbite sur arcs |

**Dalle.** Chaque doodle est posé sur une dalle carrée : remplissage cyan clair `#cffafe` à 20 % et quatre ombres intérieures `#18fefe` à 8 % (rayon 0, décalage 16px en haut, bas, gauche et droite) qui dessinent un cadre doux intérieur. C'est le seul usage d'ombre autorisé dans le style, et il est réservé aux doodles.

**Grammaire du trait.**
- Toujours cercle(s) + un élément distinctif ; deux épaisseurs (fin ≈ 1px structurel, épais ≈ 4px pour l'accent) ; pointillé pour le « possible / hypothétique ».
- Un seul accent épais par doodle. Pas de couleur supplémentaire.
- Un nouveau doodle garde cette grammaire et la même dalle.

## 7. Cover (✨ COVER, `Slide 16:9 - 1`)

Format 1920×1080, fond `Background/subtle`. Deux plans :

**Plan 1 — bandes de doodles (gauche et centre).**
- Deux bandes verticales de 400×2000 (5 doodles de 400×400 chacune, empilés sans espace), dans l'ordre ProductDesign → DesignSystem → UX/UI → Tech → IA.
- Rotation de −12,14° sur les deux bandes ; elles se décalent horizontalement d'environ 110px et verticalement pour que les dalles se chevauchent en quinconce.
- Les bandes débordent du cadre (haut, bas, gauche) : seuls des fragments de doodles sont visibles, la cover est rognée par le cadre.
- La zone de droite reste vide : rien ne chevauche le bloc titre.

**Plan 2 — bloc titre (bas droite).**
- Cadre `section` : auto-layout vertical, marges 128px ; `title_content` 1664×824, gap 32, aligné en bas et à droite (`MAX/MAX`), tout le texte aligné à droite.
- Titre « DESIGN SYSTEM » : style `Display/LG` (Inter Bold 48), `Text/primary`, en capitales.
- Sous-titre « Asma, AI driven Design System » : `Body/MD`, `Text/primary`.
- Métadonnées en bas : « Design system » puis « V 1.0, 2026 » en `Body/MD`, `Text/primary`, alignées à droite, séparées du sous-titre par un grand espace.
- Une ligne de sommaire (Lignes directrices, Fondations, Composants, Typographies, Icônes, Élevation, Animation — Inter Bold 24, interlettrage −2 %) existe dans le fichier mais n'est pas affichée dans le rendu actuel : ne pas la réafficher sans demande.

**Règles de la cover.**
- Pas de cadre « blueprint » (rail, nav, pagination) : ils appartiennent aux slides de contenu (§4), jamais à la cover.
- Pas d'autre illustration que les doodles ; pas de photo, de logo décoratif ni de dégradé.
- Hiérarchie : doodles (texture) → titre (information) ; le texte ne passe jamais au-dessus d'une dalle.

## 8. Do / Don't

**Do** : filets 1px, beaucoup de blanc, libellés mono capitales, un seul accent bleu, doodles au trait, texte en Text Styles, tokens Semantic.

**Don't** : ombre, flou, dégradé, grain ou effet de trame hors dalle des doodles (mezzotint abandonné) · texte posé sur une dalle de doodle · nouvelle teinte non tokenisée · texte courant en mono · information portée par la couleur seule · plus d'un accent fort par vue.

## 9. Ambiguïtés à signaler (ne pas trancher seul)

- Teinte exacte du niveau intermédiaire (échelle Cyan à confirmer côté Figma).
- Dalle des doodles : `#cffafe` @20 % et `#18fefe` @8 % sont des valeurs littérales, pas des variables ; à rattacher à une primitive `Color/Cyan` ou à documenter comme exception.
- Ligne de sommaire de la cover : masquée, statut à confirmer (supprimer ou conserver).
- Cadre de page hors format 1920×1080 (mobile, web) : non spécifié.
- Dossier de compétences : slides non encore spécifiées une par une (Expériences, Contact).
