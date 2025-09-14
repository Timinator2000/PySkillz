import math

def line_slope(x1: int, y1: int, x2: int, y2: int) -> float:
    if x2 == x1:
        return None  # vertical line

    return (y2 - y1) / (x2 - x1)