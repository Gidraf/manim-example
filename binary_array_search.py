from manim import *

class SortingAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Step 1: Sorting the Array", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Unsorted Array
        unsorted_array = [7, 2, 9, 4, 6, 3, 8, 5, 1]
        blocks = [Square().set_fill(BLUE, opacity=0.5).set_stroke(WHITE).scale(0.8) for _ in unsorted_array]
        numbers = [Text(str(num), font_size=24) for num in unsorted_array]
        unsorted_group = VGroup(*[VGroup(block, num).arrange(ORI) for block, num in zip(blocks, numbers)]).arrange(RIGHT, buff=0.5).shift(UP)

        unsorted_label = Text("Unsorted Array", font_size=24).next_to(unsorted_group, DOWN)
        self.play(FadeIn(unsorted_group), Write(unsorted_label))
        self.wait(1)

        # Sorting Animation
        sorting_label = Text("Sorting using Bubble Sort...", font_size=24).to_edge(DOWN)
        self.play(Write(sorting_label))

        for i in range(len(unsorted_array) - 1):
            for j in range(len(unsorted_array) - i - 1):
                current_block = unsorted_group[j]
                next_block = unsorted_group[j + 1]
                self.play(Indicate(current_block), Indicate(next_block))

                # Swap if needed
                if unsorted_array[j] > unsorted_array[j + 1]:
                    unsorted_array[j], unsorted_array[j + 1] = unsorted_array[j + 1], unsorted_array[j]
                    self.play(
                        current_block.animate.shift(RIGHT * 1.5),
                        next_block.animate.shift(LEFT * 1.5),
                    )
                    unsorted_group[j], unsorted_group[j + 1] = unsorted_group[j + 1], unsorted_group[j]

        self.wait(1)
        self.play(FadeOut(sorting_label), Transform(unsorted_label, Text("Sorted Array", font_size=24).move_to(unsorted_label.get_center())))
        self.wait(1)


class BinarySearchAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Step 2: Binary Search", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Sorted Array
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        blocks = [Square().set_fill(BLUE, opacity=0.5).set_stroke(WHITE).scale(0.8) for _ in sorted_array]
        numbers = [Text(str(num), font_size=24) for num in sorted_array]
        sorted_group = VGroup(*[VGroup(block, num).arrange(direction=ORIGIN) for block, num in zip(blocks, numbers)]).arrange(RIGHT, buff=0.5).shift(UP)

        sorted_label = Text("Sorted Array", font_size=24).next_to(sorted_group, DOWN)
        self.play(FadeIn(sorted_group), Write(sorted_label))
        self.wait(1)

        # Binary Search Process
        target = 5
        target_label = Text(f"Searching for Target: {target}", font_size=24).to_edge(DOWN)
        self.play(Write(target_label))

        low_idx = 0
        high_idx = len(sorted_array) - 1
        mid_idx = (low_idx + high_idx) // 2

        low_marker = Triangle().rotate(-PI / 2).set_fill(YELLOW, opacity=1).scale(0.5).next_to(sorted_group[low_idx], DOWN)
        high_marker = Triangle().rotate(-PI / 2).set_fill(RED, opacity=1).scale(0.5).next_to(sorted_group[high_idx], DOWN)
        mid_marker = Triangle().rotate(-PI / 2).set_fill(GREEN, opacity=1).scale(0.5).next_to(sorted_group[mid_idx], UP)

        self.play(FadeIn(low_marker), FadeIn(high_marker), FadeIn(mid_marker))

        while low_idx <= high_idx:
            self.play(Indicate(sorted_group[mid_idx]))

            if sorted_array[mid_idx] == target:
                self.play(sorted_group[mid_idx].animate.set_fill(GREEN, opacity=0.8))
                self.play(Write(Text("Target Found!", font_size=30).next_to(sorted_group[mid_idx], UP)))
                break
            elif sorted_array[mid_idx] < target:
                self.play(FadeOut(VGroup(*sorted_group[low_idx:mid_idx + 1]), low_marker))
                low_idx = mid_idx + 1
                mid_idx = (low_idx + high_idx) // 2
                low_marker.next_to(sorted_group[low_idx], DOWN)
                mid_marker.next_to(sorted_group[mid_idx], UP)
                self.play(FadeIn(low_marker), Transform(mid_marker, mid_marker.copy()))
            else:
                self.play(FadeOut(VGroup(*sorted_group[mid_idx:high_idx + 1]), high_marker))
                high_idx = mid_idx - 1
                mid_idx = (low_idx + high_idx) // 2
                high_marker.next_to(sorted_group[high_idx], DOWN)
                mid_marker.next_to(sorted_group[mid_idx], UP)
                self.play(FadeIn(high_marker), Transform(mid_marker, mid_marker.copy()))

        self.wait(2)


class SortingAndBinarySearch(Scene):
    def construct(self):
        # Scene transitions
        self.play(Write(Text("Sorting and Binary Search Combined", font_size=36).to_edge(UP)))
        self.wait(1)
        self.add(SortingAnimation(), BinarySearchAnimation())
