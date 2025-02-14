import numpy as np

with open("./6/data/testdata.txt") as file:
    input = [line.rstrip() for line in file]

print(input)

class Board():
    def __init__(self, N):
        self.size = N
        
        self.board = np.full((N, N), Cell())

class Cell():
    def __init__(self):
        self.value = None
    
board = Board(10)

print(board.board[0][4].value)

