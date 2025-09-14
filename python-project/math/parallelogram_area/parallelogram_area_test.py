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

Q: What do you call a parallelogram who can't stop laughing?
A: A para-LOL-ogram.

"""

success_message += 'A parallelogram is a four-sided figure with opposite sides parallel and equal. '
success_message += 'The area is calculated as base x height. '
success_message += 'You can think of a parallelogram as a rectangle that has been slanted — '
success_message += 'just slide one side over without changing the area, and you have a new shape!'



class ParallelogramArea(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['base', 'height']
        self.num_random_test_cases = 1000

        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            []
        ]


    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100), random.randint(-100, 100)]
    

if __name__ == "__main__":
    exercise = ParallelogramArea()
    exercise.run()
