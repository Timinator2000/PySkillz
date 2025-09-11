import math

def quadratic_roots(a: int, b: int, c: int) -> tuple[float]:
    disc = b**2 - 4*a*c
    if disc < 0:
        return None  # no real roots
    sqrt_disc = math.sqrt(disc)
    x1 = (-b + sqrt_disc) / (2*a)
    x2 = (-b - sqrt_disc) / (2*a)

    return (x1, x2)