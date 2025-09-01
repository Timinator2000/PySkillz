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

Q: Why did the triangle player quit the orchestra?
A: It was just one ting after another!

Q: Why couldn't the triangle get a bank loan?
A: Its parents wouldn't cosine.

I heard some gossip about the hypotenuse of a triangle, but I only know one side of the story.

"""


class NumberTriangle(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):
        
        super().__init__(user_solution, suggested_solution, solution_filename, success_message)
        self.num_random_test_cases = 0

        self.fixed_test_cases = [[i] for i in range(1, 10)] + [[0], [-1]]


    def test_case_to_string(self, test_case) -> str:
        return f'number = {test_case[0]}'
        
        
    def generate_random_test_case(self) -> list:
        return [random.randint(-9, 9)]


if __name__ == "__main__":
    exercise = NumberTriangle()
    exercise.run()
