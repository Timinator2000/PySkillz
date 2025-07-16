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
                   'but the choice depends on context and style guidelines.\n\n' + \

                   'However...\n\n' + \

                   'Using two spaces after a period can hint at someone's age, as it was ' + \
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





# import builtins


# sum_builtin_used = False


# def new_sum(x):
#     global sum_builtin_used
#     sum_builtin_used = True
#     return orig_sum(x)


# orig_sum = builtins.sum
# builtins.sum = new_sum


# def send_msg(channel, msg):
#     print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


# def success():
#     print("TECHIO> success true")


# def fail():
#     print("TECHIO> success false")
    

# def test_num_spaces():
#     try:
#         spaces = num_spaces('Barkley and Lulu need to go for a walk.')
#         assert spaces == 8, f"Trying num_spaces('Barkley and Lulu need to go for a walk.')... Expected 8, got {spaces}"
#         spaces = num_spaces('          ')
#         assert spaces == 10, f"Trying num_spaces('          ')... Expected 10, got {spaces}"
     
#         success()

#         if sum_builtin_used:
#             send_msg("My personal Yoda, you are. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
#             send_msg("My personal Yoda, you are. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
#             send_msg("My personal Yoda, you are. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
#             send_msg("My personal Yoda, you are. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
#             send_msg("My personal Yoda, you are. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
#             send_msg("My personal Yoda, you are. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
#             send_msg("My personal Yoda, you are. 🙏", "_)_/LI")
#         else:
#             send_msg("Kudos 🌟", "Back to boring me to death...and I had so much hope for you.  Sigh.")

#     except AssertionError as e:
#         fail()
#         send_msg("Oops! 🐞", e)
#         send_msg("Hint 💡", "Are you only counting the spaces? 🤔")


# if __name__ == "__main__":
#     test_num_spaces()
