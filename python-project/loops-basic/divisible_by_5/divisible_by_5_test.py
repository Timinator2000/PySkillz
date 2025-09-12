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

Do you find multiples of 5 somewhat more pleasing than other numbers?

"""

success_message += 'Multiples of 5 are often pleasing because they align with '
success_message += 'how humans naturally organize and process numbers, rooted '
success_message += 'in both cognitive and cultural factors. Our brains favor '
success_message += 'patterns, and multiples of 5 (5, 10, 15, 20, etc.) create a '
success_message += 'sense of rhythm and predictability. This stems from our base-10 number '
success_message += 'system, likely influenced by having ten fingers, which makes 5 and 10 '
success_message += 'intuitive benchmarks. Psychologically, numbers divisible by 5 feel “round” '
success_message += 'or complete, reducing cognitive load when counting or calculating.'


class DivisibleBy5(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):
        
        super().__init__(__file__, success_message)
        self.parameter_names = ['a_list']
        self.num_random_test_cases = 1000

        self.fixed_test_cases = [
                [[1, 2, 3, 4, 5, 6, 7, 145, 200, 300, 400]],
                [[5, 8, 10]],
                [[180, 200, 201]],
                [[35, 85, 150]],
                [[150]],
                [[155]],
                [[12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]]
        ]


    def generate_random_test_case(self) -> list:
        return [[random.randint(1, 170) for _ in range(random.randint(0, 100))]]


if __name__ == "__main__":
    exercise = DivisibleBy5()
    exercise.run()
