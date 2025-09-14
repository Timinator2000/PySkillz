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

"""

success_message += 'A trapezoid has four sides, but only one pair of opposite sides is parallel. '
success_message += 'Squares have all sides equal and opposite sides parallel, making them a special case of rectangles. '
success_message += '\n\n'
success_message += 'Fun fact: trapezoids are common in roof designs, bridges, and ramps. '
success_message += 'Their slanted sides allow forces to be distributed more efficiently, '
success_message += 'reducing stress at key points and allowing structures to bear heavier loads. '
success_message += 'This makes trapezoidal shapes ideal in engineering, where both stability and '
success_message += 'material efficiency are crucial.'


class TrapezoidArea(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['base_1', 'base_2', 'height']
        self.num_random_test_cases = 1000

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
    exercise = TrapezoidArea()
    exercise.run()
