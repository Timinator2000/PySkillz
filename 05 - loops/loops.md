# Exercise #1: Start to Finish

Create a function that prints all numbers between, and including the two numbers given.

[Start to Finish]({"stubs": ["loops/start_to_finish.py"], "command": "python3 loops/start_to_finish_test.py"})


# Exercise #2: Start to Finish on One Line

Create a function that prints all numbers between, and including the two numbers given, on a single line.

[Start to Finish on One Line]({"stubs": ["loops/start_to_finish_one_line.py"], "command": "python3 loops/start_to_finish_one_line_test.py"})


# Exercise #3: Number Triangle


[Number Triangle]({"stubs": ["loops/number_triangle.py"], "command": "python3 loops/number_triangle_test.py"})


# Exercise #4: Sum Numbers from Start to Finish


[Start to Finish Sum]({"stubs": ["loops/start_to_finish_sum.py"], "command": "python3 loops/start_to_finish_sum_test.py"})


# Exercise #5: Divisible by 5

 Given a list of integers, iterate over the list and display the numbers which are divisible by 5. If you find a number greater than 150, stop the loop iteration immediately before printing anything more.

[Divisible by 5]({"stubs": ["loops/divisible_by_5.py"], "command": "python3 loops/divisible_by_5_test.py"})

# NESTED LOOPS

# Coordinate Grid

Given a number `n`. Print all (row, col) coordinate pairs in a grid from (0, 0) to (`n`, `n`).

__Example:__

`n` = 2

Expected Output:

```
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

[Coordinate Grid({"stubs": ["loops/coordinate_grid.py"], "command": "python3 loops/coordinate_grid_test.py"})

*************

1. Multiplication Table (Basic)
Print a multiplication table from 1 to 10 in a neatly aligned format.

python
Copy
Edit
# Example output (first few rows):
#  1   2   3   4   5 ...
#  2   4   6   8  10 ...
# ...
2. Right-Angled Triangle of Stars
Print a triangle of stars using nested loops.

python
Copy
Edit
# For n = 5
# *
# **
# ***
# ****
# *****
Challenge: Make the triangle right-aligned instead of left-aligned.



4. Chessboard Pattern
Generate an 8×8 grid where cells alternate between "B" (black) and "W" (white).

python
Copy
Edit
# Example output:
# B W B W B W B W
# W B W B W B W B
# ...
Hint: Use (row + col) % 2 to decide colors.

5. Pascal’s Triangle (First 6 Rows)
Use nested loops to build and print Pascal’s Triangle up to row 6.

python
Copy
Edit
# Example output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# ...
Extension: Center-align the numbers to make the triangle look neat.
