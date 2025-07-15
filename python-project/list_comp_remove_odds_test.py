import random
import timinator
from list_comp_remove_odds import remove_odds


suggested_solution_text = """

def remove_odds(a_list: list[int]) -> list[int]:
    return [i for i in a_list if i % 2 == 0]

"""


success_message = """

Q: Why was 5 afraid of 7?
A: Becuase 7 ate 9.

Q: Do you know what's really odd?
A: Numbers not divisible by two.

"""

success_message += 'Fun fact about odd numbers: When you add all the odd numbers from 1 to any number, '
success_message += 'the sum that you get will always be a perfect square. For instance, the sum of odd '
success_message += 'numbers from 1 to 10 is 25, which is a perfect square!'



class RemoveOdds(timinator.Exercise):
    
    def __init__(self):
        
        super().__init__(remove_odds)
        self.suggested_solution_text = suggested_solution_text
        self.success_message = success_message
        self.num_random_test_cases = 10
        
        self.fixed_test_cases = [
            [[1, 3, 5, 7, 9]],
            [[2, 4, 6, 8, 10]],
            [[]],
            [[1, 2, 3, 4, 5, 6]],
            [[25678, 435, 24, 999]]
        ]
        
        
    def solution(self, a_list: list[int]) -> list:
        return [i for i in a_list if i % 2 == 0]
    
    
    def display_test_case(self, test_case) -> None:
        self.send_msg(self.bug_channel, f'   a_list = {test_case[0]}')
        
        
    def generate_random_test_case(self):
        return [[random.randint(0, 1000000) for _ in range(random.randint(0, 100))]]


if __name__ == "__main__":
    exercise = RemoveOdds()
    exercise.run()







# suggested_solution = """

# def remove_odds(a_list: list[int]) -> list[int]:
#     return [i for i in a_list if i % 2 == 0]

# """



# def test_remove_odds():
#     try:
#         answer = remove_odds([1, 3, 5, 7, 9])
#         assert answer == [], f'Trying remove_odds([1, 3, 5, 7, 9])... Expected [], got {answer}'
#         answer = remove_odds([2, 4, 6, 8, 10])
#         assert answer == [2, 4, 6, 8, 10], f'Trying remove_odds([2, 4, 6, 8, 10])... Expected [2, 4, 6, 8, 10], got {answer}'
#         answer = remove_odds([])
#         assert answer == [], f'Trying remove_odds([])... Expected [], got {answer}'
#         answer = remove_odds([1, 2, 3, 4, 5, 6])
#         assert answer == [2, 4, 6], f'Trying remove_odds([1, 2, 3, 4, 5, 6])... Expected [2, 4, 6], got {answer}'
#         answer = remove_odds([25678, 435, 24, 999])
#         assert answer == [25678, 24], f'Trying remove_odds([25678, 435, 24, 999])... Expected [[25678, 24]], got {answer}'
     
#         timinator.success()
#         timinator.send_msg(f'{random.choice(timinator.CONGRATS)} 🌟', "Back to boring me to death...and I had so much hope for you.  Sigh.")

#         for line in suggested_solution.strip().split('\n'):
#             timinator.send_msg(f'Suggested Solution', line)

#     except AssertionError as e:
#         timinator.fail()
#         timinator.send_msg("Oops! 🐞", e)
#         timinator.send_msg("Hint 💡", "Does your list expression have a condition that acts as a filter? 🤔")


# if __name__ == "__main__":
#     test_remove_odds()
