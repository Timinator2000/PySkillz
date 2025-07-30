import random 
import timinator_tools

section, exercise_name = timinator_tools.get_section_and_exercise_names(__file__)
exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')


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
        
        super().__init__(user_solution, suggested_solution, f'{section}{exercise_name}_solution.py')
        self.success_message = success_message
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [[1, 3, 5, 7, 9]],
            [[2, 4, 6, 8, 10]],
            [[]],
            [[1, 2, 3, 4, 5, 6]],
            [[25678, 435, 24, 999]]
        ]
        
        
    def display_test_case(self, test_case) -> None:
        self.send_msg(self.bug_channel, f'   a_list = {test_case[0]}')
        
        
    def generate_random_test_case(self):
        return [[random.randint(0, 1000000) for _ in range(random.randint(0, 100))]]


if __name__ == "__main__":
    exercise = RemoveOdds()
    exercise.run()
