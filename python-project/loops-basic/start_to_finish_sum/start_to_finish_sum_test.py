###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '----tools----'))

try:
    import pyskillz_tools

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the “----tools----” folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """

Q: What happens when you keep missing math class?
A: It really starts to add up!

Q: What did one math book say to the other?
A: Don't bother me. I've got my own problems.

There once was a hen who counted her own eggs. She was a mathemachicken! 🐔 🤣 🐔

"""


class StartToFinishSum(pyskillz_tools.Exercise):
    
    def __init__(self):
        
        super().__init__(__file__, success_message)
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [1, 5],
            [0, 4],
            [1, 1],
            [-4, 4],
            [5, 10],
            [542, 800]
        ]

        
    def test_case_to_string(self, test_case) -> str:
        start, finish = test_case
        return f'{start = }\n{finish = }'
        
        
    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 10), random.randint(-20, 300)]


if __name__ == "__main__":
    exercise = StartToFinishSum()
    exercise.run()
