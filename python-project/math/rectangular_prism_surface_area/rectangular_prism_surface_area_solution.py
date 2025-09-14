import math

def rectangular_prism_surface_area(length: int, width: int, height: int) -> int:
    return 2 * (length * width + width * height + length * height)
