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

Q: Why did the cylinder open a dance studio?
A: To show everyone how to roll with style.

"""

success_message += 'The surface area of a cylinder is 2 x π x radius x height '
success_message += '+ 2 x π x radius². '
success_message += 'The first term is the lateral area, and the second term '
success_message += 'covers the top and bottom circles. '
success_message += 'Fun fact: doubling the radius quadruples the surface area, '
success_message += 'and doubling the height doubles the lateral area.'


class CylinderSurfaceArea(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['radius', 'height']
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
    exercise = CylinderSurfaceArea()
    exercise.run()
