import math

def pythagorean_theorem(a: int, b: int) -> float:
    return math.sqrt(a ** 2 + b ** 2)


# Alternate solution using math.hypot.
def pythagorean_theorem_alt(a: int, b: int) -> float:
    return math.hypot(a, b)
