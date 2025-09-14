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

Q: Why don’t Americans ever understand Celsius?
A: Because when they try, things just heat up too quickly.

Q: Why was Celsius jealous of Fahrenheit?
A: Because Fahrenheit was getting all the hot dates.

"""

success_message += 'The Celsius to Fahrenheit formula is F = (C x 9/5) + 32. '
success_message += 'This means water freezes at 0°C (32°F) and boils at 100°C (212°F). '
success_message += 'Interestingly, -40° is the same in both scales!'


class CelciusToFahrenheit(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['celcius']
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
    exercise = CelciusToFahrenheit()
    exercise.run()
