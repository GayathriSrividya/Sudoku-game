# Sudoku

This repository implements Sudoku solver and creator using backtracking algorithm with other helper methods to improve solving speed.

algorithm:
---------
backtracking is a recursive approach where we try placing a number and move forward, if we get stuck we undo our step and try a different number. this way we explore all possible solutions until we find the right one.

steps:
- tries numbers 1-9 sequentially in each empty cell
- validates against sudoku rules (row, column, 3x3 box)
- if current number creates invalid state, go to previous cell
- maintains history of attempts to efficiently try next possible number
- process continues until solution is found or all possibilities are exhausted

puzzle creation:
--------------
generates new sudoku puzzles with different difficulty levels:
- creates a full solution by:
    - placing few random valid numbers
    - using solver to complete the board

- ensures puzzle remains solvable

code features:
----------------------
1. early validation:
    - checks if puzzle follows sudoku rules before attempting to solve
    - validates no duplicate numbers in rows, columns, and 3x3 boxes
    - returns early if puzzle is invalid, saving processing time

2. possibility reduction:
    - analyzes each empty cell to find all possible valid numbers
    - prioritizes cells with fewer possibilities first
    - reduces unnecessary backtracking significantly
    - maintains history of attempts for efficient backtracking

3. initial optimization:
    - before main algorithm starts, fills cells with only one possible value
    - reduces the search space for backtracking
    - handles many simple puzzles without full backtracking

input/output:
------------
input format (in markdown):
```
8 3 x | 4 6 9 | 5 x 7
x 6 x | x 7 3 | x x 9
x x x | 1 8 x | x x 3
------+------+------
3 x x | 6 x 2 | 9 7 x
6 x x | 7 9 x | 3 x 4
9 x 4 | x 5 x | 1 x x
------+------+------
1 5 x | 8 3 7 | x x 2
x 4 x | 9 1 x | x x x
x 8 9 | 5 x x | x 3 x
```

output:
```
8 3 2 | 4 6 9 | 5 1 7
5 6 1 | 2 7 3 | 8 4 9
4 9 7 | 1 8 5 | 2 6 3
------+------+------
3 1 5 | 6 4 2 | 9 7 8
6 2 8 | 7 9 1 | 3 5 4
9 7 4 | 3 5 8 | 1 2 6
------+------+------
1 5 6 | 8 3 7 | 4 9 2
2 4 3 | 9 1 6 | 7 8 5
7 8 9 | 5 2 4 | 6 3 1
```

usage:
------
Python version used - 3.11.11

to solve a puzzle:
1. place puzzle in question.md
2. run: "cd src && python3 sudoku_solver.py"
3. get solution in answer.md

to create a new puzzle:
1. run: "cd src && python3 sudoku_creator.py"
2. choose difficulty (0:easy, 1:medium, 2:hard)
3. get puzzle in question.md


reference:
---------
for more sudoku solving techniques:
https://en.wikipedia.org/wiki/Sudoku_solving_algorithms