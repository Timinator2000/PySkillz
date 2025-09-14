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

success_message += 'The sum of the first n terms of a geometric sequence is called a geometric sum. '
success_message += 'It can be calculated using the formula: Sₙ = a₁ × (1 - rⁿ) ÷ (1 - r), '
success_message += 'where a₁ is the first term, r is the common ratio, and n is the number of terms (r ≠ 1).'
success_message += '\n\n'
success_message += 'Fun fact: geometric sums are used in finance to calculate things like loan payments, '
success_message += 'compound interest, and investment growth over time. '
success_message += 'They are also useful in computer science, physics, and population modeling.'


class GeometricSum(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['a1', 'r', 'n']
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
    exercise = GeometricSum()
    exercise.run()
