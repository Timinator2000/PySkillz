import timinator
import random
from list_comp_remove_odds import remove_odds


suggested_solution = """

def remove_odds(a_list: list[int]) -> list[int]:
    return [i for i in a_list if i % 2 == 0]

"""

def test_remove_odds():
    try:
        answer = remove_odds([1, 3, 5, 7, 9])
        assert answer == [], f'Trying remove_odds([1, 3, 5, 7, 9])... Expected [], got {answer}'
        answer = remove_odds([2, 4, 6, 8, 10])
        assert answer == [2, 4, 6, 8, 10], f'Trying remove_odds([2, 4, 6, 8, 10])... Expected [2, 4, 6, 8, 10], got {answer}'
        answer = remove_odds([])
        assert answer == [], f'Trying remove_odds([])... Expected [], got {answer}'
        answer = remove_odds([1, 2, 3, 4, 5, 6])
        assert answer == [2, 4, 6], f'Trying remove_odds([1, 2, 3, 4, 5, 6])... Expected [2, 4, 6], got {answer}'
        answer = remove_odds([25678, 435, 24, 999])
        assert answer == [25678, 24], f'Trying remove_odds([25678, 435, 24, 999])... Expected [[25678, 24]], got {answer}'
     
        timinator.success()
        timinator.send_msg(f'{random.choice(timinator.CONGRATS)} 🌟', "Back to boring me to death...and I had so much hope for you.  Sigh.")
        timinator.send_msg(f'Suggested Solution', suggested_solution)

    except AssertionError as e:
        timinator.fail()
        timinator.send_msg("Oops! 🐞", e)
        timinator.send_msg("Hint 💡", "Does your list expression have a condition that acts as a filter? 🤔")


if __name__ == "__main__":
    test_remove_odds()
