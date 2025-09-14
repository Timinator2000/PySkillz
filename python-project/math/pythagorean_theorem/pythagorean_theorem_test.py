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

success_message += 'The Pythagorean theorem applies to right triangles. '
success_message += 'If the legs are a and b, and the hypotenuse is c, '
success_message += 'then a² + b² = c². '
success_message += 'Example: a 3-4-5 triangle satisfies 3² + 4² = 5² (9 + 16 = 25). '
success_message += 'Fun fact: the Babylonians knew this relationship around 1800 BCE, '
success_message += 'long before Pythagoras. '
success_message += 'There are infinitely many integer solutions called Pythagorean triples. '
success_message += 'Bonus: the distance formula in coordinate geometry comes from this theorem.'


class PythagoreanTheorem(pyskillz_tools.Exercise):
    
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
        return [random.randint(1, 1000), random.randint(1, 1000)]
    

if __name__ == "__main__":
    exercise = PythagoreanTheorem()
    exercise.run()
