from manim import *


class VerticalTransformation(Scene):
    def construct(self):

        axes = Axes(x_range=[-5, 5], y_range=[-10, 10],
                    x_length=12, y_length=10, tips=False, axis_config={"stroke_width": 5, "color": WHITE})

        tValue = ValueTracker(1)
        alpha = axes.get_graph(lambda x: tValue.get_value()
                               * (0.1*x**3-2.5*x), color=DARK_BROWN, stroke_width=10)
        alpha.add_updater(lambda func: func.become(axes.get_graph(
            lambda x: tValue.get_value() * (0.1*x**3-2.5*x), color=DARK_BROWN, stroke_width=10)))
        alphaBase = DashedVMobject(axes.get_graph(lambda x: tValue.get_value()
                                                  * (0.1*x**3-2.5*x), color=GRAY_BROWN, stroke_width=10))

        text = MathTex(r"a = 2", font_size=72).next_to(axes, DOWN)
        alphaLabel = MathTex(
            r"f(x)=0.1x^3-2.5x", font_size=72).next_to(axes, UP)

        self.add(axes, alphaBase, alpha, alphaLabel)
        self.wait(1)
        self.play(Write(text),
                  tValue.animate.set_value(2), runtime=2)
        self.wait(1)
        self.play(Transform(text, MathTex(r"a = \frac{1}{2}", font_size=72).next_to(axes, DOWN)),
                  tValue.animate.set_value(0.5), runtime=2)
        self.wait(1)
        self.play(Transform(text, MathTex(r"a = -2", font_size=72).next_to(axes, DOWN)),
                  tValue.animate.set_value(-2), runtime=2)
        self.wait(1)
        self.play(Unwrite(text), tValue.animate.set_value(1), runtime=2)


class HorizontalTransformation(Scene):
    def construct(self):

        axes = Axes(x_range=[-5, 5], y_range=[-10, 10],
                    x_length=12, y_length=10, tips=False, axis_config={"stroke_width": 5, "color": WHITE})

        tValue = ValueTracker(1)
        beta = axes.get_graph(lambda x: (
            0.1*(tValue.get_value() * x)**3-2.5*(tValue.get_value() * x)), color=DARK_BROWN, stroke_width=10)
        beta.add_updater(lambda func: func.become(axes.get_graph(
            lambda x: (0.1*(tValue.get_value() * x)**3-2.5*(tValue.get_value() * x)), color=DARK_BROWN, stroke_width=10)))
        betaBase = DashedVMobject(axes.get_graph(lambda x: (
            0.1*(tValue.get_value() * x)**3-2.5*(tValue.get_value() * x)), color=GRAY_BROWN, stroke_width=10))

        text = MathTex(r"k = 2", font_size=72).next_to(axes, DOWN)
        betaLabel = MathTex(
            r"f(x)=0.1x^3-2.5x", font_size=72,).next_to(axes, UP)

        self.add(axes, betaBase, beta, betaLabel)
        self.wait(1)
        self.play(Write(text),
                  tValue.animate.set_value(4), runtime=2)
        self.wait(1)
        self.play(Transform(text, MathTex(r"k = \frac{1}{2}", font_size=72,).next_to(axes, DOWN)),
                  tValue.animate.set_value(0.5), runtime=2)
        self.wait(1)
        self.play(Transform(text, MathTex(r"k = -2", font_size=72,).next_to(axes, DOWN)),
                  tValue.animate.set_value(-2), runtime=2)
        self.wait(1)
        self.play(Unwrite(text), tValue.animate.set_value(1), runtime=2)

       # ! OBSOLETE, VERY SHIT CODE
       # class VerticalTransformation(Scene):
       #     def construct(self):
       #         # Graph
       #         axes = Axes(x_range=[-5, 5], y_range=[-10, 10],
       #                     x_length=12, y_length=10, tips=False)

       #         # Base function
       #         def alpha(x):
       #             return 0.25*x**3-2*x

       #         alphaBase = axes.get_graph(alpha, color=DARK_BROWN)
       #         alphaLabel = MathTex("f(x) = x^3", font_size=72).next_to(axes, DOWN)

       #         # Transformed function
       #         alphaStretched = axes.get_graph(alpha(1, 4), color=DARK_BROWN)
       #         alphaStretchedLabel = MathTex(
       #             "a = 4", font_size=72).next_to(axes, DOWN)

       #         alphaCompressed = axes.get_graph(alpha, color=DARK_BROWN)
       #         alphaCompressedLabel = MathTex(
       #             r"a = \frac{1}{2}", font_size=72).next_to(axes, DOWN)

       #         alphaReflected = axes.get_graph(alpha, color=DARK_BROWN)
       #         alphaReflectedLabel = MathTex(
       #             "a = -2", font_size=72).next_to(axes, DOWN)

       #         # Displayed function
       #         displayFunction = assimilate(alphaBase)

       #         # Rendering
       #         self.add(axes, displayFunction)
       #         self.add(alphaLabel.next_to(axes, UP))
       #         self.wait(1)
       #         self.play(Transform(displayFunction, alphaStretched),
       #                   Write(alphaStretchedLabel))
       #         self.wait(1)
       #         self.play(Transform(alphaStretchedLabel, alphaCompressedLabel),
       #                   Transform(displayFunction, alphaCompressed))
       #         self.wait(1)
       #         self.play(Transform(alphaStretchedLabel, alphaReflectedLabel),
       #                   Transform(displayFunction, alphaReflected))
       #         self.wait(1)
       #         self.play(Unwrite(alphaStretchedLabel),
       #                   Transform(displayFunction, alphaBase))
