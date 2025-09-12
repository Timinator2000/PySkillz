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
    print(f'Import Error: pyskillz_tools.py needs to be in the “____tools____” folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """

Q: Why did the zero and the two break up?
A: Because some ONE came between them!

Q: What is x and y's favorite mode of transportation?
A: A coordinate plane.

"""

success_message += 'Coordinate grids are one of the most universal ways '
success_message += 'to represent space, and in computer science, “space” '
success_message += 'comes up in far more contexts than just maps. '
success_message += 'Grids are a concrete, visual sandbox for developing '
success_message += 'skills in indexing, algorithms, graph theory, and spatial '
success_message += 'reasoning—skills that carry over to almost every branch of '
success_message += 'computer science.'


class CoordinateGrid(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):
        
        super().__init__(__file__, success_message)

        self.fixed_test_cases = [[i] for i in range(10)]


    def test_case_to_string(self, test_case) -> str:
        return f'n = {test_case[0]}'
        
        
if __name__ == "__main__":
    exercise = CoordinateGrid()
    exercise.run()
