def under_1800(vehicle_weights: dict[str, int]) -> list:
    return sorted(v.upper() for v, w in vehicle_weights.items() if w < 1800)
