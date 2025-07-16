import random
import timinator
from list_comp_under_1800 import under_1800


suggested_solution_text = """

def under_1800(vehicle_weights: dict) -> list:
    return sorted(vehicle.upper() for vehicle, weight in vehicle_weights if weight < 1800)

"""


success_message = """

Q: Why did the car go on a diet?
A: Becuase it was tired of being weighed down by all those extra pounds.

Q: Why did the truck blush at the weigh station?
A: It was caught carrying a ton of extra weight.

"""

success_message += 'Fun fact: The BelAZ 75710, made in Belarus, is the world\'s ' + \
                   'largest dump truck, with a gross weight of over 1.6 million pounds ' + \
                   '(800 tons) when fully loaded. That’s heavier than three Boeing 747s! ' + \
                   'Its tires alone are so pricey, each one costs more than a brand-new Tesla. ' + \
                   'Imagine changing a flat on that!'



class Under1800(timinator.Exercise):

    VEHICLES = {'Sedan': 1500,      'SUV': 2000,          'Pickup': 2500,              'Minivan': 1600, 
                'Van': 2400,        'Semi': 13600,        'Bicycle': 7,                'Motorcycle': 110, 
                'Sports Car': 1550, 'Electric SUV': 2300, 'Heavy-Duty Truck': 50000,   'Microcar': 990}
    
    def __init__(self):
        
        super().__init__(remove_odds)
        self.suggested_solution_text = suggested_solution_text
        self.success_message = success_message
        self.num_random_test_cases = 10
        
        self.fixed_test_cases = [
            [{}],
            [{v:Under1800.VEHICLES[v] for v, w in Under1800.VEHICLES if w < 1800}],
            [{v:Under1800.VEHICLES[v] for v, w in Under1800.VEHICLES if w > 1800}],
            [{v:Under1800.VEHICLES[v] for v, w in Under1800.VEHICLES if 1490 < w < 2210}]
        ]

        timinator.Exercise.PRINT_TEST_CASES = True
        
        
    def solution(self, vehicle_weights: dict) -> list:
        return sorted(vehicle.upper() for vehicle, weight in vehicle_weights if weight < 1800)
    
    
    def display_test_case(self, test_case) -> None:
        self.send_msg(self.bug_channel, f'   vehicle_weights = {test_case[0]}')
        
        
    def generate_random_test_case(self):
        return [{v:Under1800.VEHICLES[v]} for v in random.sample(Under1800.VEHICLES.keys(), random.randint(0, len(Under1800.VEHICLES))]


if __name__ == "__main__":
    exercise = Under1800()
    exercise.run()
