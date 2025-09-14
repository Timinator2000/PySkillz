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

Q: Why did the second break up with the minute?
A: Because it felt like the relationship was moving too slowly.

"""

success_message += 'Hours, minutes, and seconds are units of time. '
success_message += 'One hour has 60 minutes, and one minute has 60 seconds. '
success_message += 'Fun fact: there are 86,400 seconds in a day, '
success_message += 'about 31.5 million seconds in a year, and roughly 2.5 billion '
success_message += 'seconds in an average human life. '
success_message += 'So don\'t tell me you don\'t have time to practice Python!'


class HoursAndMinutesToSeconds(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['hours', 'minutes']
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
    exercise = HoursAndMinutesToSeconds()
    exercise.run()
