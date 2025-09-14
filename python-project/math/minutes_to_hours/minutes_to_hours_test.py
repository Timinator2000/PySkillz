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

Q: Why did the man get fired from the watch factory?
A: He just stood around all day making faces.

"""

success_message += 'Before clocks, people used sundials to tell time using the sun\'s shadow. '
success_message += 'A stick called a gnomon casts a shadow on a marked surface to show the hour. '
success_message += 'Because the sun\'s path changes with the seasons, sundials were adjusted '
success_message += 'to account for longer summer days and shorter winter days. '
success_message += 'Some ancient sundials were even angled to match the latitude of the location!'


class MinutesToHours(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['minutes']
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
    exercise = MinutesToHours()
    exercise.run()
