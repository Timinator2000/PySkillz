###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '____tools____'))

try:
    import pyskillz_tools

except ImportError:
    print(f'Import Error: pyskillz_tools.py needs to be in the ____tools____ folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


# Enter a funciton signaure for the new exercise and run this script. A full set of 
# template files will be created in the '____new_exercises____' folder.

###########################

function_signature = "def hello_world_3x_restricted_loc() -> None:"

###########################

print()

# There shouldn't be any newlines in the function definition, but just in case...
for line in function_signature.split('\n'):
    if line.startswith('def'):
        template = pyskillz_tools.ExerciseTemplate(function_signature=line)
        error = template.check_function_definition()
    else:
        error = 'No function definition found.'

if error:
    print(error)
    quit()

destination_path = os.path.normpath(os.path.join(dir_path, '..', '____new_exercises____'))
exercise_folder_path = os.path.join(destination_path, template.exercise_name)

if os.path.exists(exercise_folder_path):
    print(f"Aborted: The folder '{template.exercise_name}' already exists at {destination_path}.")
    quit()

os.makedirs(exercise_folder_path)
print(f"Folder '{template.exercise_name}' created successfully at {destination_path}")


source_path = os.path.normpath(os.path.join(dir_path, '..', '____new_exercises____', '____exercise_template____'))

text = []
filepath = os.path.join(source_path, 'exercise_name.md')
text.append(template.markdown_file(filepath))

filepath = os.path.join(source_path, 'exercise_name.py')
text.append(template.retrieve_text(filepath))

filepath = os.path.join(source_path, 'exercise_name_solution.py')
text.append(template.retrieve_text(filepath))

filepath = os.path.join(source_path, 'exercise_name_test.py')
text.append(template.retrieve_test_file(filepath))

destination_path = os.path.normpath(os.path.join(dir_path, '..', '____new_exercises____', template.exercise_name))

for file_text, filename in zip(text, [f'{template.exercise_name}' + ext for ext in ['.md', '.py', '_solution.py', '_test.py']]):
    if filename.endswith('.md'):
        continue

    filepath = os.path.join(destination_path, filename)
    with open(filepath, 'w') as f:
        f.write('\n'.join(file_text))
