def start_to_finish_one_line(start: int, finish: int) -> None:
    for i in range(start, finish + 1):
        print(i, end='\n' if i == finish else ' ')


# alternate solution using str.join()
def start_to_finish_one_line_alt(start: int, finish: int) -> None:
    if finish >= start:
        print(' '.join(str(i) for i in range(start, finish + 1)))