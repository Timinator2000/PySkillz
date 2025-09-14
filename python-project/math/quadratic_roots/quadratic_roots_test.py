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

"""

success_message += 'A quadratic equation has the form ax² + bx + c = 0. '
success_message += 'Its solutions, called roots, are found with the quadratic formula: '
success_message += 'x = (-b ± √(b² - 4ac)) / (2a). '
success_message += 'The expression under the square root, b² - 4ac, is the discriminant. '
success_message += 'Fun fact: if the discriminant is positive, you get two real roots; '
success_message += 'if zero, one real root; if negative, two complex roots. '
success_message += 'Quadratic equations appear in physics, engineering, economics, and beyond.'


class QuadraticRoots(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['a', 'b', 'c']
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


    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]
    

if __name__ == "__main__":
    exercise = QuadraticRoots()
    exercise.run()
