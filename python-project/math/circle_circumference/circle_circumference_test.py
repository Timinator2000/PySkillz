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

Q: Why did the circle go to school?
A: Because it wanted to be well-rounded.

Q: Why did the circle break up with the line?
A: It felt like the relationship was going nowhere.

"""

success_message += 'If you take the circumference of the Earth and divide it by its diameter, '
success_message += 'you still get π — the same ratio as a coffee cup, a hula hoop, or a cookie. '
success_message += 'Circles are the ultimate equalizers.'


class CircleCircumference(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['radius']
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
    exercise = CircleCircumference()
    exercise.run()
