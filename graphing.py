from manim import *

myAxes = Axes(x_range=[-5, 5], y_range=[-5, 5],
              x_length=12, y_length=12, tips=False, axis_config={"stroke_width": 5}, color=WHITE)


class Odd(Scene):
    def construct(self):
        odd = myAxes.get_graph(lambda x: x, color=GREEN_C, stroke_width=10)
        self.add(myAxes, odd)


class Even(Scene):
    def construct(self):
        odd = myAxes.get_graph(
            lambda x: x**2, color=DARK_BLUE, stroke_width=10)
        self.add(myAxes, odd)


class NumberLineNotation(Scene):
    def construct(self):
        axis = NumberLine(x_range=[-5, 8], length=12,
                          numbers_to_include=[-4, 0, 7], stroke_width=5, font_size=56, color=WHITE)
        # eDot = Circle(0.1, color=WHITE)
        # iDot = Circle(0.1, color=WHITE).set_fill(WHITE)
        iDot = Dot(radius=0.1, point=[5.08, 0.5, 0], color=DARK_BLUE)
        eDot = Dot(radius=0.1, point=[-5.08, 0.5, 0], stroke_width=5,
                   fill_opacity=0, color=DARK_BLUE)
        nline = Line(eDot, iDot, color=DARK_BLUE, stroke_width=5)
        self.add(axis, eDot, iDot, nline)


class Secant(Scene):
    def construct(self):
        def func(x):
            return 0.3*(x-1) ** 2 + 1
        delta = myAxes.get_graph(func, color=YELLOW_D, stroke_width=10)
        dot1 = Dot(myAxes.coords_to_point(-1, func(-1)), stroke_width=5)
        dot1Label = MathTex("P_1", font_size=72).next_to(
            dot1, DOWN).shift(LEFT/2)
        dot2 = Dot(myAxes.coords_to_point(4, func(4)), stroke_width=5)
        dot2Label = MathTex("P_2", font_size=72).next_to(
            dot2, DOWN).shift(RIGHT/2)
        secant = Line(dot1, dot2, stroke_width=5)
        self.add(myAxes, delta, dot1, dot1Label, dot2, dot2Label, secant)


class Tangent(Scene):
    def construct(self):
        a = ValueTracker(-3)
        def func(x):
            return 0.3*(x-1)**2 + 1
        epsilon = myAxes.get_graph(func, color=YELLOW_D, stroke_width=10)
        tangentDot = always_redraw(lambda: Dot(stroke_width=15).move_to(myAxes.c2p(a.get_value(), func(a.get_value()))))
        movingTangent = always_redraw(lambda: myAxes.get_secant_slope_group(x=a.get_value(), graph=epsilon, dx=0.01, secant_line_color=WHITE, secant_line_length=50))
        self.add(myAxes, epsilon, movingTangent, tangentDot)
        self.play(a.animate.set_value(5),run_time=5, rate_func=linear)
        self.play(a.animate.set_value(-3),run_time=5, rate_func=linear)
