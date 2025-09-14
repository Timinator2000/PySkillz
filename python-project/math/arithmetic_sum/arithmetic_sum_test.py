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

success_message += 'The sum of the first n terms of an arithmetic sequence is called an arithmetic sum. '
success_message += 'It can be calculated using the formula: Sₙ = n x (a₁ + aₙ) ÷ 2, '
success_message += 'where a₁ is the first term, aₙ is the nth term, and n is the number of terms. '
success_message += '\n\n'
success_message += 'Fun fact: the formula was famously discovered by the mathematician Carl Gauss as a child, '
success_message += 'when he quickly summed the numbers from 1 to 100 by pairing terms efficiently. '
success_message += 'Arithmetic sums are useful in budgeting, planning, and analyzing regularly increasing quantities.'


class ArithmeticSum(pyskillz_tools.Exercise):
    
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
    exercise = ArithmeticSum()
    exercise.run()
