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

My favorite exercise is a cross between a lunge and a crunch.

    -- It's called lunch.

"""


class AddTwoNumbers(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [0, 4],
            [1, 1],
            [-4, 4],
            [5, 10],
            [542, 800]
        ]


    def test_case_to_string(self, test_case) -> str:
        a, b = test_case
        return f'{a = }\n{b = }'


    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100), random.randint(-100, 100)]


if __name__ == "__main__":
    exercise = AddTwoNumbers()
    exercise.run()
