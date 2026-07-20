# Ilustraciones con Manim CE

Animated mathematical explainer videos created with [Manim Community Edition](https://www.manim.community/) and narrated with [gTTS](https://pypi.org/project/gTTS/).

---

## What

A collection of short, animated math videos in the style of [3Blue1Brown](https://www.3blue1brown.com/). Each video walks through a mathematical concept — definition, statement, proof, example — with smooth transitions, geometric intuition, and voiceover narration.

## Why

Visual memory encodes faster than symbolic memory. When the viewer sees the shape before the equation, the formula feels earned. This project exists to turn abstract math into something you can *see*.

## When

Use this project when you need:

- Animated explanations of calculus, algebra, or analysis topics
- Step-by-step equation derivations with visual flow
- Educational content that combines geometry and formalism
- 3Blue1Brown-style videos generated from code, not hand-drawn

## Where

Source: [github.com/ErChulo/ilustraciones-manimce](https://github.com/ErChulo/ilustraciones-manimce)

Each subdirectory (e.g., `product-rule/`) is a self-contained video project with its own script, config, and render output.

## How

The production pipeline:

```
PLAN  -->  CODE  -->  RENDER  -->  STITCH  -->  VOICEOVER  -->  FINAL
```

1. **Plan** — Define the narrative arc, scenes, and visual elements
2. **Code** — Write `script.py` with one class per scene (each independently renderable)
3. **Render** — Draft at `-ql` (480p15) for iteration, production at `-qh` (1080p60)
4. **Stitch** — Concatenate scene clips into a single video with ffmpeg
5. **Voiceover** — Add narration via gTTS (or other TTS providers)
6. **Final** — Review, adjust timing, re-render as needed

---

## Prerequisites

| Requirement | Version | Install |
|-------------|---------|---------|
| Python | 3.10+ | [python.org](https://www.python.org/) |
| Manim CE | 0.20+ | `pip install manim` |
| LaTeX | texlive-full | `sudo apt install texlive-full` (Linux) / `brew install --cask mactex` (macOS) |
| ffmpeg | any recent | [ffmpeg.org](https://ffmpeg.org/) or static build |
| gTTS | any | `pip install manim-voiceover[gtts]` |
| MF-Tools | 1.4+ | `pip install MF-Tools` |

Run the setup check script to verify your environment:

```bash
bash scripts/setup.sh
```

---

## Project Structure

```
ilustraciones-manimce/
├── README.md
├── SKILL.md                    # Manim Video skill definition
├── scripts/
│   └── setup.sh                # Prerequisite checker
├── references/                 # Manim CE reference documentation
│   ├── animations.md
│   ├── animation-design-thinking.md
│   ├── camera-and-3d.md
│   ├── decorations.md
│   ├── equations.md
│   ├── graphs-and-data.md
│   ├── mobjects.md
│   ├── paper-explainer.md
│   ├── production-quality.md
│   ├── rendering.md
│   ├── scene-planning.md
│   ├── troubleshooting.md
│   ├── updaters-and-trackers.md
│   └── visual-design.md
└── product-rule/               # Video project
    ├── script.py               # 4 scenes (definition, statement, proof, example)
    ├── manim.cfg               # Manim config
    ├── concat.txt              # ffmpeg scene list
    └── final.mp4               # Stitched output (1920x1080)
```

---

## Build Instructions

### 1. Set up the environment

```bash
cd product-rule

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install manim manim-voiceover[gtts] MF-Tools
```

### 2. Draft render (fast iteration)

```bash
# Render a single scene at 480p15
manim -ql script.py Scene3_Proof

# Render all scenes
manim -ql script.py \
  Scene1_DerivativeDefinition \
  Scene2_ProductRuleStatement \
  Scene3_Proof \
  Scene4_Example
```

### 3. Production render (1080p60)

```bash
# Render each scene at full quality
manim -qh script.py Scene1_DerivativeDefinition
manim -qh script.py Scene2_ProductRuleStatement
manim -qh script.py Scene3_Proof
manim -qh script.py Scene4_Example
```

### 4. Stitch into final video

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
```

### 5. Preview a single frame

```bash
manim -ql --format=png -s script.py Scene3_Proof
```

---

## Scenes — Product Rule

| # | Scene | Description |
|---|-------|-------------|
| 1 | **The Derivative** | Geometric definition: secant line approaches tangent line, limit formula |
| 2 | **The Product Rule Statement** | Statement of the rule: (fg)' = f'g + fg' |
| 3 | **The Proof** | Derivation from the limit definition using the add/subtract trick; two-column layout with `TransformByGlyphMap` for glyph-level morphing |
| 4 | **Example** | Concrete application: f(x) = x^2, g(x) = sin(x) |

---

## Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Animation | [Manim CE](https://www.manim.community/) v0.20.1 | Scene rendering, animation engine |
| Math rendering | LaTeX (texlive) | Equations via `MathTex` |
| Glyph morphing | [MF-Tools](https://github.com/TheMathematicFanatic/MF_Tools) v1.4.9 | `TransformByGlyphMap` for smooth character-level transforms |
| Voiceover | [manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) + [gTTS](https://pypi.org/project/gTTS/) | Google Text-to-Speech narration |
| Video I/O | [ffmpeg](https://ffmpeg.org/) | Scene stitching, format conversion |

---

## Skills & Reference Material

### Skills

| Skill | Source | Description |
|-------|--------|-------------|
| **Manim Video** | [agentic-in/elephant-agent](https://github.com/agentic-in/elephant-agent) | Production pipeline for mathematical animations — planning, coding, rendering, and review workflow |

### Libraries

| Library | Author | URL |
|---------|--------|-----|
| Manim CE | Manim Community | [github.com/ManimCommunity/manim](https://github.com/ManimCommunity/manim) |
| MF-Tools | John Connell | [github.com/TheMathematicFanatic/MF_Tools](https://github.com/TheMathematicFanatic/MF_Tools) |
| manim-voiceover | Manim Community | [github.com/ManimCommunity/manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) |
| gTTS | pndurette | [github.com/pndurette/gTTS](https://github.com/pndurette/gTTS) |

### Reference Documentation (14 files)

Included in `references/` for offline use during development:

| File | Contents |
|------|----------|
| `animations.md` | Core animations, rate functions, composition, `.animate` syntax, timing patterns |
| `animation-design-thinking.md` | When to animate vs. show static, decomposition, pacing, narration sync |
| `camera-and-3d.md` | MovingCameraScene, ThreeDScene, 3D surfaces, camera control |
| `decorations.md` | SurroundingRectangle, Brace, arrows, DashedLine, Angle, annotation lifecycle |
| `equations.md` | LaTeX in Manim, TransformMatchingTex, derivation patterns |
| `graphs-and-data.md` | Axes, plotting, BarChart, animated data, algorithm visualization |
| `mobjects.md` | Text, shapes, VGroup/Group, positioning, styling, custom mobjects |
| `paper-explainer.md` | Turning research papers into animations — workflow, templates, domain patterns |
| `production-quality.md` | Pre-code, pre-render, post-render checklists, spatial layout, color, tempo |
| `rendering.md` | CLI reference, quality presets, ffmpeg, voiceover workflow, GIF export |
| `scene-planning.md` | Narrative arcs, layout templates, scene transitions, planning template |
| `troubleshooting.md` | LaTeX errors, animation errors, common mistakes, debugging |
| `updaters-and-trackers.md` | ValueTracker, add_updater, always_redraw, time-based updaters, patterns |
| `visual-design.md` | 12 design principles, opacity layering, layout templates, color palettes |

---

## Acknowledgements

- **[3Blue1Brown](https://www.3blue1brown.com/)** — Grant Sanderson's Manim library and the visual math community that inspired this project
- **[Manim CE Community](https://www.manim.community/)** — Maintainers and contributors of Manim Community Edition
- **[John Connell / The Mathematic Fanatic](https://github.com/TheMathematicFanatic)** — MF-Tools library and `TransformByGlyphMap` for glyph-level animation morphing
- **[agentic-in/elephant-agent](https://github.com/agentic-in/elephant-agent)** — Manim Video production pipeline skill
- **[pndurette](https://github.com/pndurette)** — gTTS library for text-to-speech narration
