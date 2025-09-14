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

success_message += 'Triangles are a key shape in construction and engineering because they are inherently stable. '
success_message += 'Unlike rectangles or other polygons, a triangle cannot be deformed without changing the length '
success_message += 'of its sides. This makes them ideal for trusses, bridges, roofs, and scaffolding. '
success_message += '\n\n'
success_message += 'Fun fact: the famous Eiffel Tower relies heavily on triangular supports to maintain strength '
success_message += 'while minimizing material. Triangles distribute weight evenly and resist bending, '
success_message += 'which is why engineers use them extensively in both modern and historic architecture.'


class TriangleArea(pyskillz_tools.Exercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['base', 'height']
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
    exercise = TriangleArea()
    exercise.run()
