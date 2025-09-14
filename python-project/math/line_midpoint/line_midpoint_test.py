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

Q: Why did the point sit in the middle of the line?
A: Because it wanted to be fair to both ends!

"""

success_message += 'The midpoint of a line segment is the point exactly halfway between the endpoints. '
success_message += 'If the endpoints are (x₁, y₁) and (x₂, y₂), the midpoint is ((x₁ + x₂)/2, (y₁ + y₂)/2). '
success_message += 'Finding the midpoint is like finding balance — it\'s the center of the line!'


class LineMidpoint(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.num_random_test_cases = 100

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
    exercise = LineMidpoint()
    exercise.run()
