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

They say 88 percent people are bad at math. Luckily, I am among the remaining 22 percent.

"""

success_message += 'A percent is a way of expressing a number as a fraction of 100. '
success_message += 'It is used in finance, statistics, and everyday life to compare quantities. '
success_message += 'Fun fact: a 50% increase followed by a 50% decrease does not return you to the original number! '
success_message += 'Percentages help us understand growth, discounts, and proportions in a clear way.'


class PercentIncrease(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['original', 'new']
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
    exercise = PercentIncrease()
    exercise.run()
