def number_triangle(number: int) -> None:
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            if j > 1:
                print(' ', end='')
            print(i, end = '')
        print()


# Alternate Solution #1
def number_triangle_alt1(number: int) -> None:
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(i, end = ' ' if j != i else '\n')


# Alternate Solution #2
def number_triangle_alt2(number: int) -> None:
    for i in range(1, number + 1):
        print(' '.join(str(i) for _ in range(1, i + 1)))


# Alternate Solution #3
def number_triangle_alt3(number: int) -> None:
    for i in range(1, number + 1):
        print(' '.join([str(i)] * i))


# Alternate Solution #4
def number_triangle_alt4(number: int) -> None:
    if number >= 1:
        print('\n'.join(' '.join(str(i) for _ in range(1, i + 1)) for i in range(1, number + 1)))