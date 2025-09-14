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

Q: Why was the math book always calm?
A: Because it knew how to deal with its mean problems.

"""

success_message += 'The average (mean) of a list is like the balance point: '
success_message += 'if each number were a weight on a seesaw, the average is where the seesaw would balance. '
success_message += 'That’s why the mean is sometimes called the “balance point” of data.'


class Average(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['numbers']
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
    exercise = Average()
    exercise.run()
