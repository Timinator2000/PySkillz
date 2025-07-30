import random
import timinator_tools

section, exercise_name = timinator_tools.get_section_and_exercise_names(__file__)
exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')


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


class Under1800(timinator_tools.Exercise):

    VEHICLES = {'Sedan': 1500,      'SUV': 2000,          'Pickup': 2500,              'Minivan': 1600, 
                'Van': 2400,        'Semi': 13600,        'Bicycle': 7,                'Motorcycle': 110, 
                'Sports Car': 1550, 'Electric SUV': 2300, 'Heavy-Duty Truck': 50000,   'Microcar': 990}
    
    def __init__(self):
        
        super().__init__(user_solution, suggested_solution, f'{section}{exercise_name}_solution.py')
        self.success_message = success_message
        self.num_random_test_cases = 10
        
        self.fixed_test_cases = [
            [{}],
            [{v:w for v, w in Under1800.VEHICLES.items() if w < 1800}],
            [{v:w for v, w in Under1800.VEHICLES.items() if w > 1800}],
            [{v:w for v, w in Under1800.VEHICLES.items() if 1490 < w < 2210}],
            [{v:w for v, w in Under1800.VEHICLES.items() if 1490 > w or w > 2210}]
        ]

  
    def display_test_case(self, test_case) -> None:
        self.send_msg(self.bug_channel, f'   vehicle_weights = {test_case[0]}')
        
        
    def generate_random_test_case(self):
        sample = {v:Under1800.VEHICLES[v] for v in random.sample(sorted(Under1800.VEHICLES), random.randint(0, len(Under1800.VEHICLES)))}
        return [sample]


if __name__ == "__main__":
    exercise = Under1800()
    exercise.run()
