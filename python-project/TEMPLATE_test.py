# -------------------------------------------------------------
# All code must remain unchanged, except where specified.
# -------------------------------------------------------------

import random
import timinator

section, exercise_name = timinator.get_section_and_exercise_names(__file__)
exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')

# -------------------------------------------------------------
# Changes may be made below to create a custom success message.
# -------------------------------------------------------------

success_message = """

You message can go here. A multi-line string will be printed line by line.

"""

# -------------------------------------------------------------
# To add a paragraph to your success message, use the following 
# format to keep the text easy to read here in the script.
# -------------------------------------------------------------

success_message += ''
success_message += ''
success_message += ''
success_message += ''


class {{Exercise Name Goes Here}}(timinator.Exercise):
    
    def __init__(self):
        
        super().__init__(user_solution, suggested_solution, f'{section}{exercise_name}_solution.py')
        self.success_message = success_message
        self.num_random_test_cases = 10
        
        # -------------------------------------------------------------
        # Each test case is a list of inputs. Even if there is only one 
        # input, it needs to be inside a list. If the only input for a
        # test case is a list of elements, that list must be put inside
        # the test case list.
        # -------------------------------------------------------------
        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            []
        ]
    
    
    # -------------------------------------------------------------
    # When a user makes a mistake, the superclass will display an 
    # error message, including the test case. This method must be
    # used to define what a printed test case looks like.
    # -------------------------------------------------------------
    def display_test_case(self, test_case) -> None:

        # In this example, the test case is a single string of characters.
        data = f'{[test_case[0]]}'[1:-1]
        self.send_msg(self.bug_channel, f'   a_string = {data}')
        
    # -------------------------------------------------------------
    # This method must be defined to generate a random test case. 
    # -------------------------------------------------------------
    def generate_random_test_case(self):
        return [''.join([random.choice('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(random.randint(0, 50))])]


if __name__ == "__main__":
    exercise = {{Exercise Name Goes Here}}()
    exercise.run()
