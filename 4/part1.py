def checkNeighbours(puzzle, a, b, checkValue):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if (a+i < 0 or b+j <0) or (a+i > len(puzzle)-1 or b+j > len(puzzle)-1):
                continue
            print(f'Checking at {a+i}, {b+j}')

            currentValue = puzzle[a+i][b+j]
            if currentValue == checkValue:
                return True

with open("./4/data/testdata.txt") as file:
    input = [line.rstrip() for line in file]

import numpy as np

n = len(input)

puzzle = np.empty((n, n), dtype=str)

for i in range(0, n):
    for j in range(0, n):
        puzzle[i][j] = input[i][j]

for i in range(0, n):
    for j in range(0, n): 
        if puzzle[i][j] == "X":
            print(f'Here\'s an X! @ {i} ; {j}')
            checkNeighbours(puzzle, i, j, "M")