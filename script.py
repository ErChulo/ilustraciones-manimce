from manim import *
from MF_Tools import *
import numpy as np

class CauchySchwarzTitle(Scene):
    """Scene 1: Title & Hook"""
    def construct(self):
        # Title
        title = Text("The Cauchy-Schwarz Inequality", font_size=48)
        title.to_edge(UP, buff=0.5)
        
        # Subtitle
        subtitle = Text("Proving |x·y| ≤ ||x|| ||y||", font_size=32)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        # Abstract vectors
        x_vec = Arrow(ORIGIN, 2*RIGHT + 1*UP, buff=0, color=BLUE, stroke_width=3)
        x_vec.shift(2*LEFT + 1*DOWN)
        x_label = MathTex("x", font_size=36, color=BLUE)
        x_label.next_to(x_vec.get_end(), RIGHT, buff=0.2)
        
        y_vec = Arrow(ORIGIN, 1.5*RIGHT + 1.5*UP, buff=0, color=GREEN, stroke_width=3)
        y_vec.shift(1*RIGHT + 1.5*DOWN)
        y_label = MathTex("y", font_size=36, color=GREEN)
        y_label.next_to(y_vec.get_end(), RIGHT, buff=0.2)
        
        # Inequality
        inequality = MathTex(r"|x \cdot y| \leq \|x\| \|y\|", font_size=48)
        inequality.to_edge(DOWN, buff=0.8)
        
        # Animations
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(Create(x_vec), Write(x_label))
        self.wait(0.5)
        self.play(Create(y_vec), Write(y_label))
        self.wait(1)
        self.play(Write(inequality))
        self.wait(2)
        
        # Transition out
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(x_vec),
            FadeOut(y_vec),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(inequality)
        )

class CauchySchwarzFundamental(Scene):
    """Scene 2: The Fundamental Fact"""
    def construct(self):
        # Fundamental inequality
        expr = MathTex(
            r"\|x - ty\|^2 \geq 0",
            font_size=48
        )
        expr.shift(1*UP)
        
        # Highlight zones
        norm_term = SurroundingRectangle(expr[0][:4], color=BLUE, buff=0.1)
        zero_part = SurroundingRectangle(expr[0][4:], color=GREEN, buff=0.1)
        
        # Explanation
        explanation = Text(
            "For any vector v, ||v||² ≥ 0",
            font_size=28,
            color=WHITE
        )
        explanation.next_to(expr, DOWN, buff=0.5)
        
        # t parameter
        t_line = NumberLine(
            x_range=[-3, 3, 1],
            length=6,
            include_numbers=True,
            font_size=24
        )
        t_line.to_edge(DOWN, buff=0.8)
        
        t_dot = Dot(t_line.number_to_point(0), color=YELLOW, radius=0.1)
        t_label = MathTex("t", font_size=32, color=YELLOW)
        t_label.next_to(t_dot, DOWN, buff=0.2)
        
        # Animations
        self.play(Write(expr))
        self.wait(1)
        self.play(Create(norm_term))
        self.wait(0.5)
        self.play(Create(zero_part))
        self.wait(1)
        self.play(FadeIn(explanation))
        self.wait(1)
        self.play(Create(t_line), Write(t_label), Create(t_dot))
        self.wait(2)
        
        # Move t parameter
        self.play(t_dot.animate.shift(2*RIGHT), run_time=2)
        self.wait(1)
        self.play(t_dot.animate.shift(4*LEFT), run_time=2)
        self.wait(1)
        self.play(
            FadeOut(expr),
            FadeOut(norm_term),
            FadeOut(zero_part),
            FadeOut(explanation),
            FadeOut(t_line),
            FadeOut(t_label),
            FadeOut(t_dot)
        )

class CauchySchwarzSetup(Scene):
    """Scene 3: Setting Up the Expansion"""
    def construct(self):
        # Initial expression
        initial = MathTex(
            r"\|x - ty\|^2",
            font_size=48
        )
        initial.shift(2*UP)
        
        # Dot product form
        dot_form = MathTex(
            r"(x - ty) \cdot (x - ty)",
            font_size=48
        )
        dot_form.next_to(initial, DOWN, buff=1)
        
        # Arrow
        arrow = Arrow(initial.get_bottom(), dot_form.get_top(), buff=0.2, color=YELLOW)
        
        # Highlight
        highlight = SurroundingRectangle(dot_form, color=YELLOW, buff=0.1)
        
        # Animations
        self.play(Write(initial))
        self.wait(1)
        self.play(Create(arrow))
        self.wait(0.5)
        self.play(
            TransformByGlyphMap(
                initial,
                dot_form,
                path_arc=PI/2,
                run_time=2
            )
        )
        self.wait(1)
        self.play(Create(highlight))
        self.wait(2)
        
        self.play(
            FadeOut(initial),
            FadeOut(dot_form),
            FadeOut(arrow),
            FadeOut(highlight)
        )

class CauchySchwarzExpansion1(Scene):
    """Scene 4: Expanding Step 1"""
    def construct(self):
        # Initial
        initial = MathTex(
            r"(x - ty) \cdot (x - ty)",
            font_size=48
        )
        initial.shift(3*UP)
        
        # Expanded form
        expanded = MathTex(
            r"x \cdot x - t(x \cdot y) - t(y \cdot x) + t^2(y \cdot y)",
            font_size=48
        )
        expanded.next_to(initial, DOWN, buff=1.5)
        
        # Terms
        term1 = SurroundingRectangle(expanded[0][:3], color=BLUE, buff=0.1)  # x·x
        term2 = SurroundingRectangle(expanded[0][3:8], color=YELLOW, buff=0.1)  # -t(x·y)
        term3 = SurroundingRectangle(expanded[0][8:13], color=YELLOW, buff=0.1)  # -t(y·x)
        term4 = SurroundingRectangle(expanded[0][13:], color=GREEN, buff=0.1)  # +t²(y·y)
        
        # Animations
        self.play(Write(initial))
        self.wait(1)
        
        # Transform with varying arc angles
        self.play(
            TransformByGlyphMap(
                initial,
                expanded,
                path_arc=PI/2,  # Main transform
                run_time=3
            )
        )
        self.wait(1)
        
        # Highlight each term
        self.play(Create(term1))
        self.wait(0.5)
        self.play(Create(term2))
        self.wait(0.5)
        self.play(Create(term3))
        self.wait(0.5)
        self.play(Create(term4))
        self.wait(2)
        
        self.play(
            FadeOut(initial),
            FadeOut(expanded),
            FadeOut(term1),
            FadeOut(term2),
            FadeOut(term3),
            FadeOut(term4)
        )

class CauchySchwarzExpansion2(Scene):
    """Scene 5: Expanding Step 2"""
    def construct(self):
        # Previous
        prev = MathTex(
            r"x \cdot x - t(x \cdot y) - t(y \cdot x) + t^2(y \cdot y)",
            font_size=48
        )
        prev.shift(2*UP)
        
        # Simplified
        simplified = MathTex(
            r"\|x\|^2 - 2t(x \cdot y) + t^2\|y\|^2",
            font_size=48
        )
        simplified.next_to(prev, DOWN, buff=1.5)
        
        # Highlight symmetry
        symmetry_text = Text(
            "Symmetry: x·y = y·x",
            font_size=28,
            color=YELLOW
        )
        symmetry_text.next_to(simplified, DOWN, buff=0.5)
        
        # Animations
        self.play(Write(prev))
        self.wait(1)
        
        # Highlight middle terms
        middle1 = SurroundingRectangle(prev[0][3:8], color=YELLOW, buff=0.1)
        middle2 = SurroundingRectangle(prev[0][8:13], color=YELLOW, buff=0.1)
        
        self.play(Create(middle1), Create(middle2))
        self.wait(1)
        
        # Combine
        self.play(
            TransformByGlyphMap(
                prev,
                simplified,
                path_arc=PI/2,
                run_time=2.5
            )
        )
        self.wait(1)
        
        self.play(FadeIn(symmetry_text))
        self.wait(2)
        
        self.play(
            FadeOut(prev),
            FadeOut(simplified),
            FadeOut(middle1),
            FadeOut(middle2),
            FadeOut(symmetry_text)
        )

class CauchySchwarzQuadratic(Scene):
    """Scene 6: Quadratic Form"""
    def construct(self):
        # Quadratic function
        func = MathTex(
            r"f(t) = \|y\|^2 t^2 - 2(x \cdot y)t + \|x\|^2",
            font_size=48
        )
        func.to_edge(UP, buff=0.5)
        
        # Axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 4, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        axes.shift(1*DOWN)
        
        # Parabola (always positive)
        parabola = axes.plot(
            lambda t: 0.5*t**2 + 1,
            color=YELLOW,
            x_range=[-2.5, 2.5]
        )
        
        # Shaded region
        shaded = axes.get_area(
            parabola,
            x_range=[-2.5, 2.5],
            color=BLUE,
            opacity=0.3
        )
        
        # Coefficients
        a = MathTex(r"a = \|y\|^2", font_size=36, color=BLUE)
        b = MathTex(r"b = -2(x \cdot y)", font_size=36, color=YELLOW)
        c = MathTex(r"c = \|x\|^2", font_size=36, color=GREEN)
        
        coeffs = VGroup(a, b, c).arrange(RIGHT, buff=1)
        coeffs.to_edge(DOWN, buff=0.5)
        
        # Animations
        self.play(Write(func))
        self.wait(1)
        self.play(Create(axes))
        self.wait(0.5)
        self.play(Create(parabola), Create(shaded))
        self.wait(1)
        self.play(
            FadeIn(a, shift=LEFT),
            FadeIn(b, shift=UP),
            FadeIn(c, shift=RIGHT)
        )
        self.wait(2)
        
        self.play(
            FadeOut(func),
            FadeOut(axes),
            FadeOut(parabola),
            FadeOut(shaded),
            FadeOut(a),
            FadeOut(b),
            FadeOut(c)
        )

class CauchySchwarzDiscriminant(Scene):
    """Scene 7: Discriminant Argument"""
    def construct(self):
        # Discriminant condition
        condition = MathTex(
            r"b^2 - 4ac \leq 0",
            font_size=48
        )
        condition.shift(2*UP)
        
        # Calculation
        calc = MathTex(
            r"4(x \cdot y)^2 - 4\|x\|^2\|y\|^2 \leq 0",
            font_size=48
        )
        calc.next_to(condition, DOWN, buff=1.5)
        
        # Arrow
        arrow = Arrow(condition.get_bottom(), calc.get_top(), buff=0.2, color=YELLOW)
        
        # Highlight
        highlight = SurroundingRectangle(calc, color=RED, buff=0.1)
        
        # Animations
        self.play(Write(condition))
        self.wait(1)
        self.play(Create(arrow))
        self.wait(0.5)
        
        self.play(
            TransformByGlyphMap(
                condition,
                calc,
                path_arc=PI/4,
                run_time=3
            )
        )
        self.wait(1)
        self.play(Create(highlight))
        self.wait(2)
        
        self.play(
            FadeOut(condition),
            FadeOut(calc),
            FadeOut(arrow),
            FadeOut(highlight)
        )

class CauchySchwarzFinal(Scene):
    """Scene 8: Final Result"""
    def construct(self):
        # Intermediate result
        intermediate = MathTex(
            r"(x \cdot y)^2 \leq \|x\|^2 \|y\|^2",
            font_size=48
        )
        intermediate.shift(1*UP)
        
        # Final inequality
        final = MathTex(
            r"|x \cdot y| \leq \|x\| \cdot \|y\|",
            font_size=56
        )
        final.next_to(intermediate, DOWN, buff=1.5)
        
        # Glow effect
        glow = final.copy().set_color(YELLOW).set_opacity(0.5)
        
        # Title
        title = Text("Cauchy-Schwarz Inequality", font_size=36, color=WHITE)
        title.to_edge(UP, buff=0.5)
        
        # Animations
        self.play(Write(intermediate))
        self.wait(1)
        
        self.play(
            TransformByGlyphMap(
                intermediate,
                final,
                path_arc=PI/6,
                run_time=2.5
            )
        )
        self.wait(1)
        
        # Glow effect
        self.play(
            FadeIn(glow),
            run_time=1
        )
        self.play(
            FadeOut(glow),
            run_time=1
        )
        
        self.play(FadeIn(title))
        self.wait(2)
        
        self.play(
            FadeOut(intermediate),
            FadeOut(final),
            FadeOut(title)
        )