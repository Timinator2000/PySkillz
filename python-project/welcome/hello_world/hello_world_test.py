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
    print(f'Import Error: pyskillz_tools.py needs to be in the tools folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = 'The “Hello, World” program is such a fixture in computer '
success_message += 'science that it\'s practically the rite of passage for learning '
success_message += 'any new language — but it has a very specific origin.\n\n'

success_message += 'Somewhere between 1972 and 1974, the phrase first appeared in '
success_message += 'connection with the C programming language at Bell Labs. '
success_message += 'Brian Kernighan, one of C\'s co-creators, used it in an internal '
success_message += 'Bell Labs memo titled “A Tutorial Introduction to the Language B” '
success_message += '(B was C\'s predecessor). In 1978, it was made famous by “The C '
success_message += 'Programming Language” (the original K&R book by Kernighan and Ritchie).'


class HelloWorld(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):
        
        super().__init__(__file__, success_message)
        self.fixed_test_cases = [[]]

        
    def test_case_to_string(self, test_case) -> str:
        return 'There is no input to this test case. You just need to print \'Hello, World!\''
        
        
if __name__ == "__main__":
    exercise = HelloWorld()
    exercise.run()
