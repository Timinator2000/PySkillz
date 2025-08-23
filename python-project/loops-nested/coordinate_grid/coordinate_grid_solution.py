def coordinate_grid(n: int) -> None:
    for r in range(n + 1):
        string = f'({r},0)'
        for c in range(1, n + 1):
            string += f' ({r},{c})'

        print(string)


# Alternate solution using str.join()
def coordinate_grid_alt1(n: int) -> None:
    for r in range(n + 1):
        print(' '.join(f'({r},{c})' for c in range(n + 1)))
