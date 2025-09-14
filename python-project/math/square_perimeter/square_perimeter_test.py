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
    print(f"Import Error: pyskillz_tools.py needs to be in the '____tools____' folder, one level deep from python-project.")

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """

Q: Why did the square go to therapy?
A: Because it felt a little boxed in.

"""

success_message += 'The perimeter of a square is the total distance around it. '
success_message += 'The formula is 4 x side. Fun fact: knowing the '
success_message += 'perimeter helps in fencing, framing, or designing any square-shaped area.'


class SquarePerimeter(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['side']
        self.num_random_test_cases = 1000

        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            []
        ]


    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100)]
    

if __name__ == "__main__":
    exercise = SquarePerimeter()
    exercise.run()
