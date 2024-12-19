from manim import *

class ArrayExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Arrays With Gidraf").scale(1).center()

        # Text explaining Array
        description = Text(
            text="""An Array is a data structure used to store a collection of items,
            It allows efficient storage and manipulation of elements of the same type.
            Using indexing, elements can be accessed individually.""",
            font_size=25,
        ).scale(1).center()

        # Example Array
        array_example = Text("Example: [1, 2, 3, 4]", font_size=20).scale(1).center()

        # Element Access
        index_explanation = Text(
            """Elements are accessed using indices starting from 0.,
            e.g., Element at index 0 is 1, Element at index 1 is 2, etc.""",
            font_size=20
        ).scale(1).center()

        # Applications
        applications = Text(
            """Applications of Arrays include:,
            1. Storing lists of data (e.g., numbers, strings),
            2. Implementing mathematical operations,
            3. Sorting and searching algorithms.
            4. Memory-efficient data handling."""
            ,font_size=25
        ).scale(1).center()

        # Grouping everything
        group = VGroup(title, description, array_example, index_explanation, applications).arrange(DOWN).center()

        # Animation
        self.play(Write(title))
        self.wait(1)
        self.remove(title)

        self.play(Write(description), run_time=5)
        self.wait(7)
        self.remove(description)

        self.play(Write(array_example), run_time=5)
        self.wait(5)
        self.remove(array_example)

        self.play(Write(index_explanation), run_time=5)
        self.wait(5)
        self.remove(index_explanation)

        self.play(Write(applications), run_time=5)
        self.wait(5)
        self.remove(applications)

        # Fade out
        self.play(FadeOut(group))
