# Template Files

Creating a new exercise from scratch is quick and easy, especially with the template files provided in the `python-project` folder.

📂 python-project<BR>
&nbsp;&nbsp;&nbsp;&nbsp;📂 ----exercise_template----<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_solution.py<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 exercise_name_test.py<BR>

<BR>

Let’s take a look at the contents of each file so we can pinpoint exactly what needs to be changed to get your new exercise up and running.

# exercise_name.py

```python
def exercise_name(a: int, b: int) -> int:
    return # Your code goes here.
```

```python
def exercise_name(a: int, b: int) -> None:
    # Your code goes here.
    
    # Write an answer using print
    # To debug: import sys at the top of this script
    #           print("Debug messages...", file=sys.stderr, flush=True)
```

# exercise_name_solution.py

```python
def exercise_name(a: int, b: int) -> int:
    return a + b
```

```python
def exercise_name(a: int, b: int) -> None:
    print(a + b)
```

# exercise_name_test.py

```python
###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS and split the path into directory and filename
dir_path, filename = os.path.split(os.path.normpath(__file__))

# Add tools directory to the operating system PATH
python_project_path = dir_path[:dir_path.find('python-project') + len('python-project')]
sys.path.insert(0, os.path.join(python_project_path, 'tools'))

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
###############################################################################################################```
```

```python
success_message = """


"""

success_message += ''
success_message += ''
success_message += ''
```

```python
class ExerciseName(timinator_tools.Exercise):
class ExerciseName(timinator_tools.PrintBasedExercise):
```
    
```python
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
```

```python
    def display_test_case(self, test_case) -> None:
        a, b = test_case
        self.send_msg(self.bug_channel, f'   a = {a}     b = {b}')
```

```python
    def generate_random_test_case(self):
        return [random.randint(-100, 100), random.randint(-100, 100)]
```

```python
if __name__ == "__main__":
    exercise = ExerciseName()
    exercise.run()
```


************

[![Skillz Catalog](../../graphics/PySkillzFooter.png)](skillz-catalog)
