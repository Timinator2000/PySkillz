import math

def geometric_sum(a1: int, r: int, n: int) -> int:
    if r == 1:
        return a1 * n
    return a1 * (1 - r**n) / (1 - r)
