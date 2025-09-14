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

success_message += 'Unit price is the cost per single unit of a product, like per item, per kilogram, '
success_message += 'or per liter. It helps compare prices between different sizes or brands. '
success_message += '\n\n'
success_message += 'Fun fact: savvy shoppers use unit price to find the best deal, '
success_message += 'even if a larger package looks cheaper upfront. '
success_message += 'Understanding unit price is also important in business, manufacturing, and budgeting, '
success_message += 'because it allows accurate cost comparisons and resource planning.'


class UnitPrice(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['number_of_items', 'total_cost']
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
    exercise = UnitPrice()
    exercise.run()
