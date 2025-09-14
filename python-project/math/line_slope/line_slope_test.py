###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '____tools____'))

try:
    import pyskillz_tools

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the “____tools____” folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """

Did you hear about the two parallel lines that had so much in common? It's a shame they'll never meet.

"""

success_message += 'The slope of a line measures how steep it is. '
success_message += 'It is calculated as (y₂ - y₁) / (x₂ - x₁) for two points on the line. '
success_message += 'Fun fact: positive slopes rise from left to right, '
success_message += 'negative slopes fall from left to right, and zero slope is perfectly flat!'


class LineSlope(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.num_random_test_cases = 100

        # Optional Exercise Constraints
        # self.max_statement_count =                 # Default is 10_000_000
        # self.max_lines_of_code =                   # Default is 10_000_000

        # Additional PrintBasedExercise Option
        # self.strict_print_usage = True             # Default is False

        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            [3, 4, 5, 6]
        ]


    def test_case_to_string(self, test_case) -> str:
        x1, y1, x2, y2 = test_case
        return f'(x1, y1) = ({x1}, {y1})\n(x2, y2) = ({x2}, {y2})'


    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]
    

    def check_additonal_solution_criteria(self) -> bool:
        return True


if __name__ == "__main__":
    exercise = LineSlope()
    exercise.run()
