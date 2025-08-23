def start_to_finish_sum(start: int, finish: int) -> int:
    total = 0
    for i in range(start, finish + 1):
        total += i

    return total


# Alternate solution #1
def start_to_finish_sum_alt1(start: int, finish: int) -> int:
    return sum(i for i in range(start, finish + 1))


# Alternate solution #2
def start_to_finish_sum_alt2(start: int, finish: int) -> int:
    return sum(range(start, finish + 1))