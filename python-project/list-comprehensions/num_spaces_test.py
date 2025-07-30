import random
import timinator_tools

section, exercise_name = timinator_tools.get_section_and_exercise_names(__file__)
exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')


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
        
        super().__init__(user_solution, suggested_solution, f'{section}{exercise_name}_solution.py')
        self.success_message = success_message
        self.num_random_test_cases = 10
        
        self.fixed_test_cases = [
            ['Rex and Blue need to go for a walk.'],
            [''],
            ['          '],
            ['This exercise is quite easy, right?'],
            ['abc']
        ]
    
    
    def display_test_case(self, test_case) -> None:
        data = f'{[test_case[0]]}'[1:-1]
        self.send_msg(self.bug_channel, f'   a_string = {data}')
        
        
    def generate_random_test_case(self):
        return [''.join([random.choice('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(random.randint(0, 50))])]


if __name__ == "__main__":
    exercise = NumSpaces()
    exercise.run()
