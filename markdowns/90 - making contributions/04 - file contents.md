# Template Files



# exercise_name.py

```python
# Format for a normal exercise.
def exercise(a: int, b: int) -> int:
    return # Your code goes here.

# Format for a print-based exercise.
def exercise() -> None:
    # Your code goes here.
    
    # Write an answer using print
    # To debug: import sys at the top of this script
    #           print("Debug messages...", file=sys.stderr, flush=True)
```

# exercise_name_solution.py

```python
# Format of a normal exercise.
def exercise(a: int, b: int) -> int:
    return a + b

# Format of a print-based exercise.
def exercise(a: int, b: int) -> None:
    print(a + b)
```

# exercise_name_test.py

```python
###############################################################################################################
# Environment Setup - Everything in this section must not be changed.
###############################################################################################################

import os
import sys
import random

timinator_tools_directory = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.insert(0, timinator_tools_directory)

try:
    import timinator_tools

except ImportError as e:
    print(f'Import Error: timinator_tools.py needs to be located in the root python-project directory.')

section, exercise_name = timinator_tools.get_section_and_exercise_names(__file__)
solution_filename = f'{section}{exercise_name}_solution.py'

exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """


"""

success_message += ''
success_message += ''
success_message += ''


class ExerciseName(timinator_tools.Exercise):
class ExerciseName(timinator_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(user_solution, suggested_solution, solution_filename)
        self.success_message = success_message
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            []
        ]


    def display_test_case(self, test_case) -> None:
        a, b = test_case
        self.send_msg(self.bug_channel, f'   a = {a}     b = {b}')


    def generate_random_test_case(self):
        return [random.randint(-100, 100), random.randint(-100, 100)]


if __name__ == "__main__":
    exercise = ExerciseName()
    exercise.run()
```


************

[![Skillz Catalog](../../graphics/PySkillzFooter.png)](skillz-catalog)
