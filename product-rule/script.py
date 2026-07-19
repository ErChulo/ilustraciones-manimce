from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

BG = "#1C1C1C"
BLUE = "#58C4DD"
GREEN = "#83C167"
YELLOW = "#FFFF00"
RED = "#FF6B6B"
MONO = "Menlo"


class Scene1_DerivativeDefinition(VoiceoverScene):
    def construct(self):
        self.camera.background_color = BG
        self.set_speech_service(GTTSService(lang="en"))

        # --- Axes ---
        axes = Axes(
            x_range=[-1, 6, 1], y_range=[-1, 6, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False, "stroke_color": GRAY, "stroke_width": 1.5},
        ).set_opacity(0.15).shift(DOWN * 0.3)
        x_label = axes.get_x_axis_label("x", direction=RIGHT).set_opacity(0.3)
        y_label = axes.get_y_axis_label("y", direction=UP).set_opacity(0.3)

        # --- Curve f ---
        f_curve = axes.plot(lambda x: 0.12 * (x - 1) ** 2 + 0.8, x_range=[-0.5, 5.5], color=BLUE, stroke_width=3)
        f_label = MathTex(r"f(x)", font_size=30, color=BLUE).next_to(f_curve, UR, buff=0.2).set_opacity(0.8)

        # --- Points ---
        x_p = 2.0
        x_q = 3.5
        h_tracker = ValueTracker(x_q - x_p)

        def get_f(x):
            return 0.12 * (x - 1) ** 2 + 0.8

        P = always_redraw(lambda: Dot(axes.c2p(x_p, get_f(x_p)), color=WHITE, radius=0.07))
        Q = always_redraw(lambda: Dot(
            axes.c2p(x_p + h_tracker.get_value(), get_f(x_p + h_tracker.get_value())),
            color=RED, radius=0.07
        ))

        p_label = always_redraw(lambda: MathTex("P", font_size=24, color=WHITE)
                                .next_to(P, DOWN, buff=0.2))
        q_label = always_redraw(lambda: MathTex("Q", font_size=24, color=RED)
                                .next_to(Q, UP, buff=0.2))

        # --- Secant line ---
        def get_secant():
            h = h_tracker.get_value()
            if abs(h) < 0.01:
                h = 0.01
            slope = (get_f(x_p + h) - get_f(x_p)) / h
            x0 = x_p + h_tracker.get_value() / 2
            y0 = get_f(x_p) + slope * (x0 - x_p)
            dx = 2.5
            return Line(
                axes.c2p(x0 - dx, y0 - slope * dx),
                axes.c2p(x0 + dx, y0 + slope * dx),
                color=RED, stroke_width=2
            ).set_opacity(0.7)

        secant = always_redraw(get_secant)

        # --- Title ---
        title = Text("The Derivative", font_size=42, color=WHITE, font=MONO, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # --- Difference quotient formula ---
        quotient = MathTex(
            r"\frac{f(x+h) - f(x)}{h}",
            font_size=36
        )
        quotient[0][0:8].set_color(BLUE)   # f(x+h)
        quotient[0][9:16].set_color(WHITE)  # - f(x)
        quotient.to_edge(DOWN, buff=0.8)

        # --- Limit formula ---
        limit_def = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            font_size=36
        )
        limit_def.to_edge(DOWN, buff=0.8)

        # ========================
        # ANIMATION SEQUENCE
        # ========================

        # Beat 1: Axes + curve appear
        with self.voiceover("Consider a continuous function f from R to R.") as tracker:
            self.play(Create(axes), run_time=1.0)
            self.play(Create(f_curve), Write(f_label), run_time=2.0)
            self.wait(0.5)

        # Beat 2: Point P
        with self.voiceover("Pick a point P on the curve.") as tracker:
            self.play(GrowFromCenter(P), Write(p_label), run_time=1.0)
            self.wait(0.5)

        # Beat 3: Point Q + secant
        with self.voiceover(
            "Place a second point Q nearby. "
            "The secant line through P and Q has a slope given by the difference quotient."
        ) as tracker:
            self.play(GrowFromCenter(Q), Write(q_label), run_time=1.0)
            self.play(Create(secant), run_time=1.0)
            self.play(Write(quotient), run_time=1.5)
            self.wait(1.0)

        # Beat 4: Q slides toward P
        with self.voiceover(
            "Now watch what happens as Q approaches P. "
            "As h shrinks toward zero, the secant line rotates."
        ) as tracker:
            self.play(h_tracker.animate.set_value(0.05), run_time=tracker.duration - 0.5, rate_func=smooth)

        # Beat 5: Secant becomes tangent, formula transforms
        with self.voiceover(
            "The secant line becomes the tangent line, "
            "and we obtain the definition of the derivative."
        ) as tracker:
            tangent = axes.plot(lambda x: get_f(x_p) + (0.12 * 2 * (x_p - 1)) * (x - x_p),
                                x_range=[x_p - 2, x_p + 2], color=WHITE, stroke_width=3)
            self.play(FadeOut(secant), Create(tangent), run_time=1.5)
            self.play(
                ReplacementTransform(quotient, limit_def),
                run_time=2.0
            )
            self.wait(3.0)

        # Clean exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.3)


class Scene2_ProductRuleStatement(VoiceoverScene):
    def construct(self):
        self.camera.background_color = BG
        self.set_speech_service(GTTSService(lang="en"))

        # --- Two curves ---
        axes = Axes(
            x_range=[-1, 7, 1], y_range=[-2, 5, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False, "stroke_color": GRAY, "stroke_width": 1.5},
        ).set_opacity(0.15).shift(DOWN * 0.3)

        f_curve = axes.plot(lambda x: 0.4 * x + 0.5, x_range=[-0.5, 6], color=BLUE, stroke_width=3)
        g_curve = axes.plot(lambda x: 1.5 * np.sin(0.8 * x) + 2, x_range=[-0.5, 6], color=GREEN, stroke_width=3)

        f_label = MathTex(r"f(x)", font_size=28, color=BLUE).next_to(f_curve, UR, buff=0.15)
        g_label = MathTex(r"g(x)", font_size=28, color=GREEN).next_to(g_curve, UP, buff=0.15)

        # --- Product curve ---
        h_curve = axes.plot(
            lambda x: (0.4 * x + 0.5) * (1.5 * np.sin(0.8 * x) + 2),
            x_range=[-0.5, 6], color=YELLOW, stroke_width=3
        )
        h_label = MathTex(r"h(x) = f(x) \cdot g(x)", font_size=28, color=YELLOW)
        h_label.next_to(h_curve, UR, buff=0.15)

        # --- Product Rule Formula ---
        product_rule = MathTex(
            r"(f \cdot g)' = f' \cdot g + f \cdot g'",
            font_size=40
        )
        product_rule[0][0:6].set_color(WHITE)     # (f*g)'
        product_rule[0][7:10].set_color(BLUE)     # f'
        product_rule[0][11:14].set_color(GREEN)   # g
        product_rule[0][15:18].set_color(BLUE)    # f
        product_rule[19:22].set_color(GREEN)       # g'
        product_rule.to_edge(DOWN, buff=0.8)

        # --- Title ---
        title = Text("The Product Rule", font_size=42, color=WHITE, font=MONO, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # ========================
        # ANIMATION SEQUENCE
        # ========================

        # Beat 1: f and g appear
        with self.voiceover("Suppose we have two differentiable functions, f and g.") as tracker:
            self.play(Create(axes), run_time=0.5)
            self.play(Create(f_curve), Write(f_label), run_time=1.5)
            self.play(Create(g_curve), Write(g_label), run_time=1.5)
            self.wait(0.5)

        # Beat 2: Product h appears
        with self.voiceover("Their product, h equals f times g, is also a function.") as tracker:
            self.play(Create(h_curve), Write(h_label), run_time=2.0)
            self.wait(0.5)

        # Beat 3: Product rule formula
        with self.voiceover(
            "The product rule tells us how to differentiate it. "
            "The derivative of f times g equals f prime times g, plus f times g prime."
        ) as tracker:
            self.play(Write(product_rule), run_time=2.0)
            self.wait(1.0)

        # Beat 4: Why it works
        with self.voiceover(
            "Why? Because the product changes when either factor changes."
        ) as tracker:
            self.play(
                product_rule[7:14].animate.set_opacity(1.0),
                product_rule[15:22].animate.set_opacity(1.0),
                run_time=1.0
            )
            self.wait(2.0)

        # Clean exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.3)


class Scene3_Proof(VoiceoverScene):
    def construct(self):
        self.camera.background_color = BG
        self.set_speech_service(GTTSService(lang="en"))

        # --- Title ---
        title = Text("Proof of the Product Rule", font_size=38, color=WHITE, font=MONO, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # --- Step 1: Limit definition ---
        step1 = MathTex(
            r"(f \cdot g)'(x) = \lim_{h \to 0} \frac{f(x+h)\,g(x+h) - f(x)\,g(x)}{h}",
            font_size=30
        ).shift(UP * 1.5)

        # --- Step 2: Add and subtract f(x+h)g(x) ---
        step2 = MathTex(
            r"= \lim_{h \to 0} \frac{f(x+h)\,g(x+h) - f(x+h)\,g(x) + f(x+h)\,g(x) - f(x)\,g(x)}{h}",
            font_size=26
        ).shift(UP * 0.3)

        highlight_box = SurroundingRectangle(
            step2[0][37:72], color=YELLOW, buff=0.08, corner_radius=0.05, stroke_width=2
        )
        clever_note = Text("add and subtract", font_size=18, color=YELLOW)
        clever_note.next_to(highlight_box, UP, buff=0.15)

        # --- Step 3: Two fractions ---
        step3a = MathTex(
            r"= \lim_{h \to 0} \left[",
            font_size=30
        ).shift(UP * 1.8)
        step3b = MathTex(
            r"\frac{f(x+h)\,g(x+h) - f(x+h)\,g(x)}{h}",
            font_size=28, color=BLUE
        ).next_to(step3a, RIGHT, buff=0.15)
        step3c = MathTex(
            r"+ \frac{f(x+h)\,g(x) - f(x)\,g(x)}{h} \right]",
            font_size=28, color=GREEN
        ).next_to(step3b, DOWN, buff=0.3, aligned_edge=LEFT).shift(RIGHT * 0.5)

        # --- Step 4: Factor ---
        step4a = MathTex(
            r"= \lim_{h \to 0} \left[",
            font_size=30
        ).shift(UP * 1.8)
        step4b = MathTex(
            r"g(x) \cdot \frac{f(x+h) - f(x)}{h}",
            font_size=28, color=BLUE
        ).next_to(step4a, RIGHT, buff=0.15)
        step4c = MathTex(
            r"+ f(x+h) \cdot \frac{g(x+h) - g(x)}{h} \right]",
            font_size=28, color=GREEN
        ).next_to(step4b, DOWN, buff=0.3, aligned_edge=LEFT).shift(RIGHT * 0.5)

        # --- Step 5: Limit result ---
        step5 = MathTex(
            r"= g(x) \cdot f'(x) + f(x) \cdot g'(x)",
            font_size=34
        ).shift(DOWN * 0.5)
        step5[0][0:7].set_color(GREEN)    # g(x)
        step5[0][8:13].set_color(BLUE)    # f'(x)
        step5[0][14:19].set_color(BLUE)   # f(x)
        step5[0][20:25].set_color(GREEN)  # g'(x)

        # --- Final result ---
        final = MathTex(
            r"\boxed{(f \cdot g)' = f' \cdot g + f \cdot g'}",
            font_size=38
        ).shift(DOWN * 1.8)
        final[0][1:8].set_color(WHITE)
        final[0][9:12].set_color(BLUE)
        final[0][13:16].set_color(GREEN)
        final[0][17:20].set_color(BLUE)
        final[0][21:24].set_color(GREEN)

        qed = MathTex(r"\blacksquare", font_size=24, color=WHITE).next_to(final, RIGHT, buff=0.3)

        # ========================
        # ANIMATION SEQUENCE
        # ========================

        # Title
        with self.voiceover("Now let us prove the product rule from the limit definition.") as tracker:
            self.play(Write(title), run_time=1.5)
            self.wait(0.5)

        # Step 1
        with self.voiceover(
            "By definition, the derivative of f times g is the limit as h approaches zero of "
            "f of x plus h times g of x plus h, minus f of x times g of x, all over h."
        ) as tracker:
            self.play(Write(step1), run_time=2.5)
            self.wait(1.0)

        # Step 2: The clever zero
        with self.voiceover(
            "Here is the key trick. We add and subtract f of x plus h times g of x in the numerator."
        ) as tracker:
            self.play(Write(step2), run_time=2.0)
            self.play(Create(highlight_box), Write(clever_note), run_time=1.0)
            self.wait(2.0)

        # Step 3: Two fractions
        with self.voiceover(
            "Now we regroup. This single fraction splits into two."
        ) as tracker:
            self.play(
                FadeOut(step2), FadeOut(highlight_box), FadeOut(clever_note),
                run_time=0.5
            )
            self.play(Write(step3a), Write(step3b), run_time=1.5)
            self.play(Write(step3c), run_time=1.5)
            self.wait(1.0)

        # Step 4: Factor
        with self.voiceover(
            "In the first fraction, we factor out g of x. "
            "In the second fraction, we factor out f of x plus h."
        ) as tracker:
            self.play(
                ReplacementTransform(step3a, step4a),
                ReplacementTransform(step3b, step4b),
                ReplacementTransform(step3c, step4c),
                run_time=2.0
            )
            self.wait(2.0)

        # Step 5: Recognize the derivatives
        with self.voiceover(
            "As h approaches zero, the first fraction becomes f prime of x. "
            "The second fraction becomes g prime of x. "
            "And f of x plus h approaches f of x."
        ) as tracker:
            self.play(
                FadeOut(step4a), FadeOut(step4b), FadeOut(step4c),
                run_time=0.5
            )
            self.play(Write(step5), run_time=2.0)
            self.wait(2.0)

        # Final result
        with self.voiceover(
            "Therefore, the derivative of f times g is f prime times g, plus f times g prime."
        ) as tracker:
            self.play(Write(final), run_time=1.5)
            self.play(Write(qed), run_time=0.5)
            self.wait(3.0)

        # Clean exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.3)


class Scene4_Example(VoiceoverScene):
    def construct(self):
        self.camera.background_color = BG
        self.set_speech_service(GTTSService(lang="en"))

        # --- Title ---
        title = Text("Example", font_size=42, color=WHITE, font=MONO, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # --- Functions ---
        f_def = MathTex(r"f(x) = x^2", font_size=34, color=BLUE)
        g_def = MathTex(r"g(x) = \sin x", font_size=34, color=GREEN)
        defs = VGroup(f_def, g_def).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(UP * 2.0)

        # --- Derivatives ---
        f_prime = MathTex(r"f'(x) = 2x", font_size=34, color=BLUE)
        g_prime = MathTex(r"g'(x) = \cos x", font_size=34, color=GREEN)
        primes = VGroup(f_prime, g_prime).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(UP * 0.5)

        # --- Apply product rule ---
        rule_line = MathTex(
            r"(f \cdot g)' = f' \cdot g + f \cdot g'",
            font_size=30, color=WHITE
        ).shift(DOWN * 0.8)

        # --- Substitute ---
        substituted = MathTex(
            r"= 2x \cdot \sin x + x^2 \cdot \cos x",
            font_size=34
        ).shift(DOWN * 1.8)
        substituted[0][0:5].set_color(BLUE)    # 2x
        substituted[0][6:12].set_color(GREEN)   # sin x
        substituted[0][13:17].set_color(BLUE)   # x^2
        substituted[0][18:24].set_color(GREEN)  # cos x

        box = SurroundingRectangle(substituted, color=YELLOW, buff=0.2, corner_radius=0.1, stroke_width=2)

        # ========================
        # ANIMATION SEQUENCE
        # ========================

        # Beat 1: State the functions
        with self.voiceover(
            "Let us apply the product rule. "
            "Let f of x equal x squared, and g of x equal sine x."
        ) as tracker:
            self.play(Write(title), run_time=1.0)
            self.play(Write(f_def), run_time=1.0)
            self.play(Write(g_def), run_time=1.0)
            self.wait(1.0)

        # Beat 2: Compute derivatives
        with self.voiceover(
            "Then f prime is 2x, and g prime is cosine x."
        ) as tracker:
            self.play(Write(f_prime), run_time=1.0)
            self.play(Write(g_prime), run_time=1.0)
            self.wait(1.0)

        # Beat 3: Apply rule
        with self.voiceover(
            "By the product rule, the derivative of f times g is f prime times g plus f times g prime."
        ) as tracker:
            self.play(Write(rule_line), run_time=1.5)
            self.wait(1.0)

        # Beat 4: Substitute
        with self.voiceover(
            "Substituting, we get 2x times sine x, plus x squared times cosine x."
        ) as tracker:
            self.play(Write(substituted), run_time=2.0)
            self.wait(1.0)

        # Beat 5: Box
        with self.voiceover(
            "This is the derivative of x squared sine x."
        ) as tracker:
            self.play(Create(box), run_time=1.0)
            self.wait(3.0)

        # Clean exit
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.3)
