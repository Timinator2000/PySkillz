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

success_message += 'Density is defined as mass divided by volume. '
success_message += 'It tells us how compact matter is in an object. '
success_message += 'Fun fact: metals like gold are dense, '
success_message += 'while substances like cork are much less dense.'
success_message += '\n\n'
success_message += 'Saturn is significantly less dense than Earth; Saturn\'s '
success_message += 'density is about 0.687 g/cm³, while Earth\'s is 5.52 g/cm³. '
success_message += 'This makes Saturn the least dense planet in our solar system, '
success_message += 'with a density lower than water, which means it would float '
success_message += 'in a large enough body of water. Earth, being rocky and metallic, '
success_message += 'is the densest planet, while Saturn is a gas giant composed '
success_message += 'primarily of hydrogen and helium.'



class Density(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['mass', 'volume']
        self.num_random_test_cases = 1000

        self.fixed_test_cases = [
            [1000, 10],
            [250, 1],
            [90, 2000],
            [100, 10_000],
            [1, 1]
        ]


    def generate_random_test_case(self) -> list:
        return [random.randint(100, 100_000), random.randint(100, 100_000)]
    

if __name__ == "__main__":
    exercise = Density()
    exercise.run()
