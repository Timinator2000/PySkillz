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

Q: What\'s it called when a King and Queen have no children?
A: A receding heir line...

Q: What do you call 100 rabbits walking backwards?
A: A receding hare line.

"""

success_message += 'The distance between two points in a plane can be found using the formula: '
success_message += '√((x₂ - x₁)² + (y₂ - y₁)²), where (x₁, y₁) and (x₂, y₂) are the points. '
success_message += 'Fun fact: this formula comes from the Pythagorean theorem, '
success_message += 'and it works in any number of dimensions!'


class LineDistance(pyskillz_tools.Exercise):
    
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
            []
        ]


    def test_case_to_string(self, test_case) -> str:
        x1, y1, x2, y2 = test_case
        return f'(x1, y1) = ({x1}, {y1})\n(x2, y2) = ({x2}, {y2})'


    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]
    

if __name__ == "__main__":
    exercise = LineDistance()
    exercise.run()
