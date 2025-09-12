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

Did you fix the quote in the previous question and identify who said it?

"""

success_message += '“This is not the end. It is not even the beginning of the end. '
success_message += 'But it is, perhaps, the end of the beginning.”'
success_message += '\n\n'
success_message += '     —— Winston Churchill'


class StartToFinishOneLine(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):
        
        super().__init__(__file__, success_message)
        self.parameter_names = ['start', 'finish']
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [1, 5],
            [-3, 0],
            [-4, 4],
            [5, -1],
            [0, 9],
            [4, 4]
        ]


    def generate_random_test_case(self) -> list:
        return [random.randint(-20, 10), random.randint(0, 30)]


if __name__ == "__main__":
    exercise = StartToFinishOneLine()
    exercise.run()
