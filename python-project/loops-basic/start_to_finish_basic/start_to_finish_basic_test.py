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
    import pyskillz_tools
    pyskillz_tools.check_for_tech_io(dir_path)

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the tools folder, one level deep from python-project.')

exercise_name = filename[:filename.find('_test.py')]
solution_filename = os.path.join(dir_path, f'{exercise_name}_solution.py')

exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """

Can you correct the follow quote and identify who said it?

"""

success_message += '"This is not the [finish]. It is not even the [start] of the [finish]. '
success_message += 'But it is, perhaps, the [finish] of the [start]."'


class StartToFinishBasic(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):
        
        super().__init__(user_solution, suggested_solution, solution_filename, success_message)
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [1, 5],
            [-3, 0],
            [-4, 4],
            [5, -1],
            [0, 9]
        ]

        
    def test_case_to_string(self, test_case) -> str:
        start, finish = test_case
        return f'start = {start}\nfinish = {finish}'
        
        
    def generate_random_test_case(self) -> list:
        return [random.randint(-20, 10), random.randint(0, 30)]


if __name__ == "__main__":
    exercise = StartToFinishBasic()
    exercise.run()
