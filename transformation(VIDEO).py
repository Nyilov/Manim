from manim import *

class aboutC(Scene):
    def construct(self):
        y = ValueTracker(5)
        yStep = ValueTracker(1)
        axes = Axes(
            x_range=[-5,5], 
            y_range=[-1*y.get_value(),y.get_value(), yStep.get_value()], 
            tips=False, 
            x_axis_config={
                "numbers_to_include": np.arange(-5, 6)
            },
            y_axis_config={
                "numbers_to_include": np.arange(-5, 5, yStep.get_value())
                # TODO why is it decimal?
            }
            )
        axes.add_updater(lambda func: func.become(Axes(
            x_range=[-5,5], 
            y_range=[-1*y.get_value(),y.get_value(), yStep.get_value()], 
            tips=False, 
            x_axis_config={
                "numbers_to_include": np.arange(-5, 6)
            },
            y_axis_config={
                "numbers_to_include": np.arange(-5, 5, yStep.get_value())
            }
            )))
        tForm = MathTex(r"y = af[k(x-c)]+h")
        alphaLabel = MathTex(r"\frac{1}{2}x(x-5)(x+5)")
        def func(x):
            return 0.5*x*(x-5)*(x+5)
        alpha = axes.get_graph(func, color=DARK_BROWN)
        self.add(axes, alpha)
    