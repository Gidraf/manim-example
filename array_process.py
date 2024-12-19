from manim import *

class ArrayAnimation(Scene):
    def construct(self):
        # Define array
        array = [1, 2, 3, 4, 5]

        # Title
        title = Text("Practical Examples").to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.remove(title)

        # First Scene: Initial Array
        array_rects = VGroup(*[Square(side_length=0.5).shift(LEFT * (5 - i)) for i in range(5)])
        array_labels = VGroup(*[Text(str(num), color=BLUE).next_to(rect, DOWN) for num, rect in zip(array, array_rects)])
        initial_group = VGroup(array_rects, array_labels).center()

        self.play(Create(initial_group))
        self.wait(2)

        # Adding an element
        added_array = array + [6]
        added_rects = VGroup(*[Square(side_length=0.5).shift(LEFT * (len(added_array) - i)) for i in range(len(added_array))])
        added_labels = VGroup(*[Text(str(num), color=BLUE).next_to(rect, DOWN) for num, rect in zip(added_array, added_rects)])
        added_group = VGroup(added_rects, added_labels).center()
        title = Text("We can add an element to an array").next_to(added_group, DOWN)
        self.play(Write(title))
        self.wait(2)
        self.remove(title)
        self.play(Transform(initial_group, added_group))
        self.wait(5)

        # Removing an element
        removed_array = array[:-1]
        removed_rects = VGroup(*[Square(side_length=0.5).shift(LEFT * (len(removed_array) - i)) for i in range(len(removed_array))])
        removed_labels = VGroup(*[Text(str(num), color=BLUE).next_to(rect, DOWN) for num, rect in zip(removed_array, removed_rects)])
        removed_group = VGroup(removed_rects, removed_labels).center()
        
        title = Text("We can also remove an element from an array").next_to(removed_group, DOWN)
        self.play(Write(title))
        self.wait(2)
        self.remove(title)
        self.play(Transform(initial_group, removed_group))
        self.wait(2)

        # Sorting
        sorted_array = sorted(array)
        sorted_rects = VGroup(*[Square(side_length=0.5).shift(LEFT * (5 - i)) for i in range(5)])
        sorted_labels = VGroup(*[Text(str(num), color=BLUE).next_to(rect, DOWN) for num, rect in zip(sorted_array, sorted_rects)])
        sorted_group = VGroup(sorted_rects, sorted_labels).center()
        title = Text("An array can also be sorted").next_to(sorted_group, DOWN)
        self.play(Write(title))
        self.wait(2)
        self.remove(title)
        self.play(Transform(initial_group, sorted_group))
        self.wait(2)

        # Finding an element
        

        target = 3
        target_index = sorted_array.index(target)
        target_rect = sorted_rects[target_index]
        target_label = sorted_labels[target_index]
        target_highlight = VGroup(target_rect, target_label).center()
        
        title = Text("We can also search through an array").next_to(sorted_group, DOWN)
        self.play(Write(title))
        self.wait(2)
        self.remove(title)
        self.play(Create(target_highlight))
        self.wait(2)

        # Filtering elements
        title = Text("We can also filter through an array").to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.remove(title)

        filtered_array = [num for num in sorted_array if num > 2]
        filtered_rects = VGroup(*[Square(side_length=0.5).shift(LEFT * (len(filtered_array) - i)) for i in range(len(filtered_array))])
        filtered_labels = VGroup(*[Text(str(num), color=BLUE).next_to(rect, DOWN) for num, rect in zip(filtered_array, filtered_rects)])
        filtered_group = VGroup(filtered_rects, filtered_labels).center()

        self.play(Transform(initial_group, filtered_group))
        self.wait(2)

        # Combine all scenes and save the video
        final_scene = VGroup(initial_group, filtered_group, target_highlight, title).center()
        self.play(FadeOut(final_scene))
        self.wait(2)
