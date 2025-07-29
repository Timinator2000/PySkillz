# Last Edited: July 29, 2025 Afternoon

import random
import re
from copy import deepcopy
import builtins
import sys


CONGRATS = ['Kudos!',
            'Well Done!',
            'Bravo!',
            'Perfect!',
            'Nice Job!',
            'Keep It Up!',
            'Attaboy!',
            'Nice Work!',
            'Excellent My Friend!',
            'Excelente Mi Amigo!',
            'Awesome!',
            'Hooray!',
            'Way To Go!',
            'Encore!',
            'Great Effort!',
            'Top Notch!',
            'There You Go!',
            'Take a Bow!',
            'Great Work!',
            'Outstanding!',
            'Exceptional Work!',
            'Superb!',
            'First-Class Effort!',
            'Brilliant!',
            'You are a Champion!',
            'Stellar!',
            'Magnificent Job!',
            'Dazzling Work!',
            'Stupendous!',
            'Marvelous!',
            'B-E-A-UTIFUL!',
            'Congratulations!']

CONGRATS_EMOJIS = '🌟🔥👏💥🎆🎉🥳💓💖💗🤟💯😀🤩😍'

BUG = ['Oops!',
       'Uh-oh!',
       'Oh no!',
       'Hmmm?',
       'Might have to try again!',
       'Ugh!',
       'Egad!']

BUG_EMOJIS = '🐞🐛🪲🦗😔😢😧'


def get_section_and_exercise_names(file):
    m = re.search(r"(?P<section>[\w\-]+/)(?P<exercise>\w+)_test.py", file)
    if m is not None:
        return m.group('section'), m.group('exercise')

            
class Exercise():
    
    PRINT_TEST_CASES = False
    CONTAINERS = ['list', 'tuple', 'set']
    
    def __init__(self, user_solution, suggested_solution, solution_path):
        self.fixed_test_cases = []
        self.num_random_test_cases = 0
        self.user_solution = user_solution
        self.suggested_solution = suggested_solution
        self.success_message = ''

        with open(solution_path, 'r') as f:
            self.suggested_solution_text = f.read()

        self.success_channel = f'{random.choice(CONGRATS)} {random.choice(CONGRATS_EMOJIS)}'
        self.bug_channel = f'{random.choice(BUG)} {random.choice(BUG_EMOJIS)}'


    def send_multiline_text(self, channel, msg):
        for line in msg.strip().split('\n'):
            self.send_msg(channel, line)

        
    def send_msg(self, channel, msg):
        print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

            
    def success(self):
        print("TECHIO> success true")

            
    def fail(self):
        print("TECHIO> success false")

            
    def container_element_types(self, container) -> str:
        element_types = {self.data_type(element) for element in container}
        
        if len(element_types) > 1:
            return '[multiple types]'
        
        if len(element_types) == 1:
            return f'[{element_types.pop()}]'
        
        return ''
    
    
    def data_type(self, data) -> str:
        string = str(type(data)).split("'")[-2]
        
        if string in Exercise.CONTAINERS:
            string += self.container_element_types(data)
        
        if string == 'dict':
            key_types = self.container_element_types(data.keys())
            value_types = self.container_element_types(data.values())
            
            if key_types and value_types:
                string += f'[{key_types[1: -1]}, {value_types[1: -1]}]'
            
        return string
    
    
    def display_test_case(self, test_case):
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None


    def generate_random_test_case(self):
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None


    def check_answer_format(self, test_case):
        expected_answer = self.suggested_solution(*deepcopy(test_case))
        user_answer = self.user_solution(*deepcopy(test_case))

        expected_answer_format = self.data_type(expected_answer)
        user_answer_format = self.data_type(user_answer)

        if expected_answer_format == user_answer_format:
            return True

        self.fail()
        self.send_msg(self.bug_channel, 'Incorrect Data Types:')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'   Expected answer format = {expected_answer_format}')
        self.send_msg(self.bug_channel, f'   Expected answer        = {expected_answer}')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'   Your answer format = {user_answer_format}')
        self.send_msg(self.bug_channel, f'   Your answer        = {user_answer}')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, 'Input:')
        self.send_msg(self.bug_channel, '')
        self.display_test_case(test_case)
            
        return False

        
    def check_answer(self, test_case):
        expected_answer = self.suggested_solution(*deepcopy(test_case))
        user_answer = self.user_solution(*deepcopy(test_case))

        if expected_answer == user_answer:
            return True

        self.fail()
        self.send_msg(self.bug_channel, f'Incorrect Answer:')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'   Expected answer = {expected_answer}')
        self.send_msg(self.bug_channel, f'   Your answer     = {user_answer}')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'Input:')
        self.send_msg(self.bug_channel, '')
        self.display_test_case(test_case)
            
        return False


    def run_test_case(self, test_case):
        if Exercise.PRINT_TEST_CASES:
            print(test_case)

        if not self.check_answer_format(test_case):
               return False

        return self.check_answer(test_case)

        
    def run(self):
        
        count = 0
        for test_case in self.fixed_test_cases:
            if not self.run_test_case(test_case):
                break
                
            count += 1

        word = 'case' if count == 1 else 'cases'
        self.send_msg('Standard Output', f'{count} fixed test {word} solved correctly.')
        
        if count != len(self.fixed_test_cases):
            self.send_msg('Standard Output', f'FAILURE on fixed test case {count + 1}.')
            return
        
        count = 0
        for _ in range(self.num_random_test_cases):
            if not self.run_test_case(self.generate_random_test_case()):
                break
                
            count += 1

        word = 'case' if count == 1 else 'cases'
        self.send_msg('Standard Output', f'{count} random test {word} solved correctly.')

        if count != self.num_random_test_cases:
            self.send_msg('Standard Output', f'FAILURE on random test case {count + 1}.')
            return

        self.success()
        self.send_multiline_text(self.success_channel, self.success_message)
        self.send_multiline_text(f'Suggested Solution ✅', self.suggested_solution_text)



class PrintBasedExercise(Exercise):

    def __init__(self, user_solution, suggested_solution, solution_path):
        super().__init__(user_solution, suggested_solution, solution_path)
        self.output_buffer = []
                
        self.normal_print = builtins.print
        self.test_case_printing = False


    def __del__(self):
        builtins.print = self.normal_print


    def swap_printer(self):
        self.test_case_printing = not self.test_case_printing
        if self.test_case_printing:
            builtins.print = self.new_print
        else:
            builtins.print = self.normal_print

            
    def new_print(self, *args, sep=' ', end='\n', file=sys.stdout, flush=False):
        if file==sys.stderr:
            self.normal_print(*args, sep=sep, end=end, file=file, flush=flush)
        else:
            string = end.join(str(arg for arg in args))
            self.output_buffer.extend(string.split('\n'))

            
    def check_answer_format(self, test_case):
        self.swap_printer()
                
        self.suggested_solution(*deepcopy(test_case))
        expected_answer = deepcopy(self.output_buffer)
        self.output_buffer.clear()
        
        user_answer = self.user_solution(*deepcopy(test_case))
        user_answer = deepcopy(self.output_buffer)
        self.output_buffer.clear()

        self.swap_printer()
                
        expected_answer_format = self.data_type(expected_answer)
        user_answer_format = self.data_type(user_answer)

        if len(expected_answer_format) == len(user_answer_format):
            return True

        self.fail()
        self.send_msg(self.bug_channel, 'Incorrect number of lines printed:')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'   Expected answer = {len(expected_answer_format)} lines printed.')
        self.send_msg(self.bug_channel, f'   Your answer     = {len(user_answer)} lines printed.')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, 'Input:')
        self.send_msg(self.bug_channel, '')
        self.display_test_case(test_case)
            
        return False

        
    def check_answer(self, test_case):
        self.swap_printer()

        self.suggested_solution(*deepcopy(test_case))
        expected_answer = deepcopy(self.output_buffer)
        self.output_buffer.clear()
        
        user_answer = self.user_solution(*deepcopy(test_case))
        user_answer = deepcopy(self.output_buffer)
        self.output_buffer.clear()

        self.swap_printer()

        if expected_answer == user_answer:
            return True

        self.fail()
        self.send_msg(self.bug_channel, f'Incorrect Answer:')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'   Expected answer = {expected_answer}')
        self.send_msg(self.bug_channel, f'   Your answer     = {user_answer}')
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'Input:')
        self.send_msg(self.bug_channel, '')
        self.display_test_case(test_case)
            
        return False
