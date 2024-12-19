from manim import *

class ArraySortingAnimation(Scene):
    def construct(self):
        # Define the array of 5 elements
        array = [5, 3, 8, 6, 2]

        # Create rectangles for each element in the array
        rectangles = VGroup(*[
            Square(side_length=0.5, fill_color=BLUE, fill_opacity=1).shift(LEFT * (4 - i) * 1.5)
            for i in range(len(array))
        ])

        # Adding the values to the rectangles
        for i, rect in enumerate(rectangles):
            rect_value = Integer(array[i], font_size=24).scale(0.5)
            rect_value.move_to(rect)
            rect.add(rect_value)

        # Create an array for colors
        colors = [BLUE, GREEN, ORANGE, RED, PURPLE]

        # Perform bubble sort step-by-step with color animation
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                self.play(
                    rectangles[j].animate.set_color(RED),  # Highlight the first element
                    rectangles[j + 1].animate.set_color(RED),  # Highlight the second element
                    run_time=0.5
                )

                # Swap and animate
                self.play(
                    rectangles[j].animate.move_to(rectangles[j + 1].get_center()),
                    rectangles[j + 1].animate.move_to(rectangles[j].get_center()),
                    run_time=0.5
                )

                # Swap the values
                array[j], array[j + 1] = array[j + 1], array[j]

                # Animate values with different colors
                self.play(
                    rectangles[j].animate.set_fill(colors[j % len(colors)], opacity=1),
                    rectangles[j + 1].animate.set_fill(colors[(j + 1) % len(colors)], opacity=1),
                    run_time=0.5
                )

            # Reset colors after each iteration
            for rect in rectangles:
                rect.set_color(WHITE)

        # Final sorted array
        final_array = [2, 3, 5, 6, 8]
        for i, rect in enumerate(rectangles):
            self.play(
                rect.animate.move_to(Square(side_length=0.5, fill_color=WHITE, fill_opacity=1)
                                     .shift(LEFT * (4 - i) * 1.5)),
                run_time=0.5
            )
            rect_value = Integer(final_array[i], font_size=24).scale(0.5)
            rect_value.move_to(rect)
            rect.add(rect_value)

        # Display final sorted array
        self.wait(1)
