import math

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Alternate solution using math.hypot.
def distance_atl(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.hypot(x2 - x1, y2 - y1)