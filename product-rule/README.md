# Product Rule — Definition, Statement & Proof

Animated explainer video for the product rule of differentiation, created with [Manim Community Edition](https://www.manim.community/) and narrated with gTTS.

## Scenes

1. **The Derivative** — Geometric definition: secant line → tangent line → limit formula
2. **The Product Rule Statement** — Statement: (fg)' = f'g + fg'
3. **The Proof** — Derivation from the limit definition using the add/subtract trick
4. **Example** — f(x) = x², g(x) = sin(x) → 2x·sin(x) + x²·cos(x)

## Stack

- **Manim CE v0.20.1** — Animation engine
- **manim-voiceover + gTTS** — Narration
- **ffmpeg** — Scene stitching

## Usage

```bash
# Render all scenes (1080p60)
manim -qh script.py Scene1_DerivativeDefinition Scene2_ProductRuleStatement Scene3_Proof Scene4_Example

# Stitch
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4

# Draft render (480p15, fast iteration)
manim -ql script.py Scene1_DerivativeDefinition
```

Requires Python 3.10+, Manim CE, LaTeX, and ffmpeg.
