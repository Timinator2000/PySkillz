import random

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

class Exercise():
    
    CONTAINERS = ['list', 'tuple', 'set']
    
    def __init__(self, user_solution):
        self.fixed_test_cases = []
        self.num_random_test_cases = 0
        self.user_solution = user_solution

        self.suggested_solution_text = ''
        self.success_message = ''

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
    
    
    def solution(self):
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None


    def display_test_case(self, test_case):
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None


    def generate_random_test_case(self):
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None
        
        
    def run_test_case(self, test_case):
        expected_answer = self.solution(*test_case)
        user_answer =self.user_solution(*test_case)

        expected_answer_format = self.data_type(expected_answer)
        user_answer_format = self.data_type(user_answer)

        if expected_answer_format != user_answer_format:

            self.fail()
            self.send_msg(self.bug_channel, 'Incorrect Data Types:')
            self.display_test_case(test_case)
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'   Expected answer format = {expected_answer_format}')
            self.send_msg(self.bug_channel, f'   Expected answer        = {expected_answer}')
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'   Your answer format = {user_answer_format}')
            self.send_msg(self.bug_channel, f'   Your answer        = {user_answer}')
            
            return False
        
        if expected_answer != user_answer:
            self.send_msg(self.bug_channel, f'Incorrect Answer:')
            self.display_test_case(test_case)
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'   Expected answer = {expected_answer}')
            self.send_msg(self.bug_channel, f'   Your answer     = {user_answer}')
            
            return False

        return True

        
    def run(self):
        
        count = 0
        for test_case in self.fixed_test_cases:
            if not self.run_test_case(test_case):
                break
                
            count += 1
            
        print(f'{count} of {len(self.fixed_test_cases)} fixed test cases solved correctly.')
        
        if count != len(self.fixed_test_cases):
            return
        
        count = 0
        for _ in range(self.num_random_test_cases):
            if not self.run_test_case(self.generate_random_test_case()):
                break
                
            count += 1

        print(f'{count} of {self.num_random_test_cases} random test cases solved correctly.')

        if count != self.num_random_test_cases:
            return

        self.success()
        self.send_multiline_text(self.success_channel, self.success_message)
        self.send_multiline_text(f'Suggested Solution', self.suggested_solution_text)

