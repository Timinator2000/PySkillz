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

success_message += 'In computing, we often measure time in milliseconds (ms) and microseconds (µs). '
success_message += '1 millisecond is 1/1,000 of a second, and 1 microsecond is 1/1,000,000 of a second. '
success_message += 'Fun fact: modern processors can execute billions of instructions per second, '
success_message += 'so measuring operations in seconds would be far too slow and imprecise! '
success_message += 'Milliseconds and microseconds help programmers optimize performance, '
success_message += 'handle real-time systems, and synchronize networks accurately.'


class SecondsToHoursMinsSecs(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['seconds']
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
    exercise = SecondsToHoursMinsSecs()
    exercise.run()
