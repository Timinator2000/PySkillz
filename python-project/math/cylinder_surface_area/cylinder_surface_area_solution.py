import math

def cylinder_surface_area(radius: int, height: int) -> float:
    return 2 * math.pi * radius * height + 2 *math.pi * radius ** 2
