import math

def seconds_to_hours_mins_secs(seconds: int) -> tuple[int]:
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    return hours, minutes, seconds


# Alternate solution using divmod
def seconds_to_hours_mins_secs_alt(seconds: int) -> tuple[int]:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds