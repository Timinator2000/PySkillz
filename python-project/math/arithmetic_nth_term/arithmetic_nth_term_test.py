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

success_message += 'In an arithmetic sequence, each term differs from the previous one by a constant '
success_message += 'amount, called the common difference. '
success_message += '\n\n'
success_message += 'Fun fact: arithmetic sequences appear in real life in situations like '
success_message += 'arranging seats, scheduling, or even saving money regularly. '
success_message += 'Recognizing patterns and calculating the nth term helps predict future values efficiently.'


class ArithmeticNthTerm(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['a1', 'd', 'n']
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
    exercise = ArithmeticNthTerm()
    exercise.run()
