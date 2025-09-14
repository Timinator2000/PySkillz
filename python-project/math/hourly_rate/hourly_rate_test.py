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


success_message = 'I was applying for a job last month and the manager said, '
success_message += '“You will start at $15 an hour, and later you could earn $20 an hour.” '
success_message += 'I replied, “Alright then... I will be back later!”'
success_message += '\n\n'
success_message += 'Hourly rate or hourly wage is the amount of money paid for one hour of work. '
success_message += 'It is commonly used to calculate pay for part-time or temporary jobs. '
success_message += 'Fun fact: working more hours increases total pay, but the hourly '
success_message += 'rate stays the same unless renegotiated. '
success_message += 'Overtime is often paid at a higher hourly rate, typically 1.5x the normal rate.'


class HourlyRate(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['hours', 'wages']
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
    exercise = HourlyRate()
    exercise.run()
