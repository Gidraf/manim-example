from manim import *

class ArrayFormation(Scene):
    def construct(self):
        # Title
        title = Text("Array Formation and Creation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Array elements
        elements = ["1", "2", "3", "4", "5"]
        
        # Table to represent array
        array_table = MobjectTable(
            [[Text(el)] for el in elements],  # Rows with elements
            col_labels=None,                # No column labels
            include_outer_lines=True        # Include borders
        )
        
        # Position the table on the screen
        array_table.scale(1.2).shift(DOWN)
        
        # Step 1: Show empty array creation
        empty_array_table = MobjectTable(
            [[Text("")]] * len(elements),
            col_labels=None,
            include_outer_lines=True
        ).scale(1.2).shift(DOWN)
        
        self.play(FadeIn(empty_array_table))
        self.wait(1)

        # Step 2: Animate filling of array
        for i, el in enumerate(elements):
            # Highlight the current cell
            current_cell = empty_array_table.get_cell((i + 1, 1))
            self.play(
                current_cell.animate.set_fill(YELLOW, opacity=0.5),
                run_time=0.5
            )
            
            # Check if the cell has content and update it
            if current_cell.submobjects:
                cell_content = current_cell.submobjects[0]  # Get the current Text object
                new_text = Text(el).move_to(cell_content.get_center())  # Align new text
                self.play(Transform(cell_content, new_text), run_time=0.5)
            else:
                new_text = Text(el).move_to(current_cell.get_center())  # Create new text
                self.play(FadeIn(new_text), run_time=0.5)
                current_cell.add(new_text)
            
            # Reset cell color
            self.play(current_cell.animate.set_fill(WHITE, opacity=0), run_time=0.3)
        
        # Step 3: Show completed array
        
        self.play(ReplacementTransform(empty_array_table, array_table))
        self.remove(empty_array_table)
        self.wait(2)

        # Step 4: Add final label
        array_label = Text("Array: [1, 2, 3, 4, 5]", font_size=24)
        array_label.next_to(array_table, DOWN)
        self.play(Write(array_label))
        self.wait(2)
