from manim import *
import pygments.styles as code_styles


code_style = code_styles.get_style_by_name("one-dark")

class CreateCircle(Scene):
    def construct(self):
        demo_code = Code(
            code='''tracker = self.add_voiceover_text(
    """AI generated voices have become realistic
        enough for use in most content. Using neural
        text-to-speech frees you from the painstaking
        process of recording and manually syncing
        audio to your video."""
)
self.play(Write(demo_code), run_time=tracker.duration)''',
            insert_line_no=False,
            style=code_style,
            background="window",
            font="Consolas",
            language="python",
        ).rescale_to_fit(12, 0)
        self.play(Write(demo_code), run_time=30)
        self.play(FadeOut(demo_code))
      
    

# class SquareToCircle(Scene):
    # def construct(self):
    #     circle = Circle()  # create a circle
    #     circle.set_fill(PINK, opacity=0.5)  # set color and transparency

    #     square = Square()  # create a square
    #     square.rotate(PI / 4)  # rotate a certain amount

    #     self.play(Create(square))  # animate the creation of the square
    #     self.play(Transform(square, circle))  # interpolate the square into the circle
    #     self.play(FadeOut(square))  # fade out animation