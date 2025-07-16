import random
import timinator
from list_comprehension_ex_09 import num_spaces


suggested_solution_text = """

def num_spaces(a_string: str) -> int:
    return sum(c == ' ' for c in a_string)

"""


success_message = """

Do you use 1 space or 2 spaces between sentences?

"""

success_message += 'The debate over one space versus two spaces after a period ' + \
                   'has been largely settled in favor of one space in modern writing, ' + \
                   'but the choice depends on context and style guidelines.\n' + \
                   '\n' + \
                   'However, if you prefer to hid your age...' + \
                   '\n' + \
                   'Using two spaces after a period can hint at someone\'s age, as it was ' + \
                   'standard in the typewriter era, common among those born before the 1980s. ' + \
                   'Younger generations, trained on computers with modern fonts, typically use ' + \
                   'one space, making two spaces a giveaway of older typing habits.'



class NumSpaces(timinator.Exercise):
    
    def __init__(self):
        
        super().__init__(num_spaces)
        self.suggested_solution_text = suggested_solution_text
        self.success_message = success_message
        self.num_random_test_cases = 10
        
        self.fixed_test_cases = [
            ['Rex and Blue need to go for a walk.'],
            [''],
            ['          '],
            ['This exercise is quite easy, right?'],
            ['abc']
        ]
        
        
    def solution(self, a_string: str) -> int:
        return sum(c == ' ' for c in a_string)
    
    
    def display_test_case(self, test_case) -> None:
        self.send_msg(self.bug_channel, f'   a_string = {test_case[0]}')
        
        
    def generate_random_test_case(self):
        return [''.join([random.choice('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(random.randint(0, 50))])]


if __name__ == "__main__":
    exercise = NumSpaces()
    exercise.run()
