#!/usr/bin/env python3
"""
Génère dist/tokens.css à partir de tokens/primitive.json, semantic.json, responsive.json.

- Primitive  -> :root (valeurs brutes, mode unique "Value")
- Semantic   -> :root (Light, valeurs par défaut) + [data-theme="dark"] (Dark)
- Responsive -> :root (Mobile, base mobile-first) + @media (min-width: 768px) (Desktop)

Nommage (voir guidelines/design-system-ai-guidelines.yaml pour le détail) :
- Primitive Color            -> --color-{family}-{step}
- Primitive Typography       -> --font-family-scale-{role} / --font-size-scale-{step} / etc.
- Primitive Spacing/Radius/Border/Opacity/Grid -> --{cat}-scale-{step}
  (le suffixe "-scale-" évite toute collision avec les rôles Semantic/Responsive,
   ex. Primitive Radius/pill vs Responsive Radius/pill)
- Semantic Color              -> --color-{group}-{role}  (ex: --color-action-primary)
- Responsive Typography       -> --font-size-{role} / --line-height-{role}
- Responsive Spacing/Radius/Grid -> --spacing-{role} / --radius-{role} / --grid-{role}
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "tokens"
DIST = ROOT / "dist"
BREAKPOINT = "768px"  # ajuster ici si besoin


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load(name):
    with open(TOKENS / name, encoding="utf-8") as f:
        return json.load(f)


def primitive_var_name(name):
    parts = name.split("/")
    if parts[0] == "Color":
        # Color/Blue/600 -> --color-blue-600
        return f"--color-{slug(parts[1])}-{slug(parts[2])}"
    if parts[0] == "Typography":
        # Typography/Family/Title -> --font-family-scale-title
        # Typography/Font-size/md -> --font-size-scale-md
        # Typography/Font-weight/regular -> --font-weight-scale-regular
        # Typography/Line-Height/md -> --line-height-scale-md
        sub = slug(parts[1])
        return f"--{sub}-scale-{slug(parts[2])}"
    if parts[0] == "Grid":
        # Grid/columns/4 -> --grid-columns-scale-4
        return f"--grid-{slug(parts[1])}-scale-{slug(parts[2])}"
    # Spacing/md, Radius/pill, Border/thin, Opacity/40 -> --spacing-scale-md, etc.
    return f"--{slug(parts[0])}-scale-{slug(parts[1])}"


def semantic_var_name(name):
    parts = name.split("/")
    if parts[0] == "Feedback":
        # Feedback/Danger/text -> --color-feedback-danger-text
        return f"--color-feedback-{slug(parts[1])}-{slug(parts[2])}"
    # Background/default -> --color-background-default
    # Action/primary-hover -> --color-action-primary-hover
    return f"--color-{slug(parts[0])}-{slug(parts[1])}"


def responsive_var_name(name):
    parts = name.split("/")
    if parts[0] == "Typography":
        # Typography/body-md/Font-size -> --font-size-body-md
        # Typography/body-md/Line-Height -> --line-height-body-md
        prop = "font-size" if parts[2] == "Font-size" else "line-height"
        return f"--{prop}-{slug(parts[1])}"
    if parts[0] == "Grid":
        # Grid/columns -> --grid-columns ; Grid/gutter -> --grid-gutter
        return f"--grid-{slug(parts[1])}"
    # Spacing/component-md -> --spacing-component-md
    # Radius/control -> --radius-control
    return f"--{slug(parts[0])}-{slug(parts[1])}"


def css_value(v, vtype):
    if vtype == "COLOR":
        return v
    if vtype == "STRING":
        return f'"{v}"'
    # FLOAT: font-size/line-height/spacing/radius/border/grid -> px ; font-weight -> nombre nu ; opacity -> %
    return v  # unit added by caller when relevant


def build():
    primitive = load("primitive.json")
    semantic = load("semantic.json")
    responsive = load("responsive.json")

    lines_root = ["/* Auto-généré par scripts/build_css.py — ne pas éditer à la main */", ":root {"]
    lines_dark = ['[data-theme="dark"] {']
    lines_desktop = [f"@media (min-width: {BREAKPOINT}) {{", "  :root {"]

    # --- Primitive -> :root ---
    lines_root.append("  /* Primitive */")
    for tok in primitive:
        name = primitive_var_name(tok["name"])
        val = tok["byMode"]["Value"]
        if tok["type"] == "COLOR":
            lines_root.append(f"  {name}: {val};")
        elif tok["type"] == "STRING":
            lines_root.append(f'  {name}: "{val}";')
        else:
            unit = "" if "Font-weight" in tok["name"] or "Opacity" in tok["name"] or "Grid" in tok["name"] else "px"
            lines_root.append(f"  {name}: {val}{unit};")

    # --- Semantic -> :root (Light) + [data-theme="dark"] ---
    lines_root.append("")
    lines_root.append("  /* Semantic — Light (défaut) */")
    for tok in semantic:
        name = semantic_var_name(tok["name"])
        lines_root.append(f"  {name}: {tok['byMode']['Light']};")
        lines_dark.append(f"  {name}: {tok['byMode']['Dark']};")

    # --- Responsive -> :root (Mobile, base) + @media desktop ---
    lines_root.append("")
    lines_root.append("  /* Responsive — Mobile (base, mobile-first) */")
    for tok in responsive:
        name = responsive_var_name(tok["name"])
        mobile_val = tok["byMode"]["Mobile"]
        desktop_val = tok["byMode"]["Desktop"]
        unit = "" if "Grid/columns" == tok["name"] else "px"
        lines_root.append(f"  {name}: {mobile_val}{unit};")
        if desktop_val != mobile_val:
            lines_desktop.append(f"    {name}: {desktop_val}{unit};")

    lines_root.append("}")
    lines_dark.append("}")
    lines_desktop.append("  }")
    lines_desktop.append("}")

    DIST.mkdir(exist_ok=True)
    out = "\n".join(lines_root) + "\n\n" + "\n".join(lines_dark) + "\n\n" + "\n".join(lines_desktop) + "\n"
    (DIST / "tokens.css").write_text(out, encoding="utf-8")
    print(f"OK — {DIST / 'tokens.css'} généré "
          f"({len(primitive)} primitives, {len(semantic)} semantic, {len(responsive)} responsive)")


if __name__ == "__main__":
    build()
