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
    timinator_tools.check_for_tech_io(dir_path)

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

Do you use 1 space or 2 spaces between sentences?

"""

success_message += 'The debate over one space versus two spaces after a period ' + \
                   'has been largely settled in favor of one space in modern writing, ' + \
                   'but the choice depends on context and style guidelines.\n' + \
                   '\n' + \
                   'However...\n' + \
                   '\n' + \
                   'Using two spaces after a period can hint at someone\'s age, as it was ' + \
                   'standard in the typewriter era, common among those born before the 1980s. ' + \
                   'Younger generations, trained on computers with modern fonts, typically use ' + \
                   'one space, making two spaces a giveaway of older typing habits.'



class NumSpaces(timinator_tools.Exercise):
    
    def __init__(self):
        
        super().__init__(user_solution, suggested_solution, solution_filename)
        self.success_message = success_message
        self.num_random_test_cases = 10
        
        self.fixed_test_cases = [
            ['Rex and Blue need to go for a walk.'],
            [''],
            ['          '],
            ['This exercise is quite easy, right?'],
            ['abc']
        ]
    
    
    def test_case_to_string(self, test_case) -> str:
        data = f'{[test_case[0]]}'[1:-1]
        return f'a_string = {data}'
        
        
    def generate_random_test_case(self) -> list:
        return [''.join([random.choice('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(random.randint(0, 50))])]


if __name__ == "__main__":
    exercise = NumSpaces()
    exercise.run()
