###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS and split the path into directory and filename
dir_path, filename = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '----tools----'))

try:
    import timinator_tools

except ImportError:
    print(f'Import Error: timinator_tools.py needs to be in the tools folder, one level deep from python-project.')

exercise_name = filename[:filename.find('_test.py')]
solution_filename = os.path.join(dir_path, f'{exercise_name}_solution.py')

exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """

Q: Why was 5 afraid of 7?
A: Becuase 7 ate 9.

Q: Do you know what's really odd?
A: Numbers not divisible by two.

"""

success_message += 'Fun fact about odd numbers: When you add all the odd numbers from 1 to any number, '
success_message += 'the sum that you get will always be a perfect square. For instance, the sum of odd '
success_message += 'numbers from 1 to 10 is 25, which is a perfect square!'



class RemoveOdds(timinator_tools.Exercise):
    
    def __init__(self):
        
        super().__init__(user_solution, suggested_solution, solution_filename)
        self.success_message = success_message
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [[1, 3, 5, 7, 9]],
            [[2, 4, 6, 8, 10]],
            [[]],
            [[1, 2, 3, 4, 5, 6]],
            [[25678, 435, 24, 999]]
        ]
        
        
    def test_case_to_string(self, test_case) -> str:
        return f'a_list = {test_case[0]}'
        
        
    def generate_random_test_case(self) -> list:
        return [[random.randint(0, 1000000) for _ in range(random.randint(0, 100))]]


if __name__ == "__main__":
    exercise = RemoveOdds()
    exercise.run()
