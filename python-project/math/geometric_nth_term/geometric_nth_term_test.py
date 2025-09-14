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

success_message += 'In a geometric sequence, each term is obtained by multiplying the previous term by a constant called the common ratio. '
success_message += 'The nth term of a geometric sequence can be calculated as: '
success_message += 'aₙ = a₁ x r^(n - 1), where a₁ is the first term, r is the common ratio, and n is the term number. '
success_message += '\n\n'
success_message += 'Fun fact: geometric sequences appear in finance, population growth, and computer science, '
success_message += 'because they model exponential growth or decay. '
success_message += 'Recognizing the pattern allows us to predict future terms efficiently.'


class GeometricNthTerm(pyskillz_tools.Exercise):
    
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
    exercise = GeometricNthTerm()
    exercise.run()
