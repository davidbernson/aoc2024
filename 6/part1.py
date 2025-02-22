import numpy as np

with open("./6/data/testdata.txt") as file:
    input = [line.rstrip() for line in file]

# print(input)

class Board():
    def __init__(self, N):
        self.size = N
        
        self.board = np.full((N, N), None)

    def populateBoard(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                self.board[row][col] = Cell([row, col], None)

    def changeCellValue(self, position, value):
        self.board[position[0]][position[1]].value = value

    def getCellValue(self, position):
        if position[0] >= board.size or position[1] >= board.size:
            return "outOfBounds"
        return self.board[position[0]][position[1]].value

    def printBoard(self):
        for row in range(0, self.size):
            rowString = ''
            for item in self.board[row]:
                if isinstance(item.value, str):
                    rowString += item.value
                else:
                    rowString += 'p'
            rowString += '\n'
            print(rowString)

class Cell():
    def __init__(self, position, value):
        self.value = value
        self.position = position

    def getValue(self):
        return self.value

class Player():
    def __init__(self, position):
        self.direction = [-1, 0]
        self.position = position

    def checkIfClear(self, board):
        nextCell = (self.position[0]+self.direction[0], self.position[1]+self.direction[1])
        if board.getCellValue(nextCell) == "outOfBounds":
            return "outOfBounds"
        if not board.getCellValue(nextCell) == '#':
            return board.getCellValue(nextCell)
        else:
            return False
        
    def move(self, board):
        if board.getCellValue(self.position) != "O":
            board.changeCellValue(self.position, 'X')
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]

    def rotate(self):
        if self.direction == [-1, 0]:
            self.direction = [0, 1]
        elif self.direction == [0, 1]:
            self.direction = [1, 0]
        elif self.direction == [1, 0]:
            self.direction = [0, -1]
        elif self.direction == [0, -1]:
            self.direction = [-1, 0]

    def lookRight(self, board):       
        if self.direction == [-1, 0]:
            rightCell = [self.position[0]+1, self.position[1]+1]
        elif self.direction == [0, 1]:
            rightCell = [self.position[0]+1, self.position[1]-1]
        elif self.direction == [1, 0]:
            rightCell = [self.position[0]-1, self.position[1]-1]
        elif self.direction == [0, -1]:
            rightCell = [self.position[0]-1, self.position[1]+1]
        
        return board.getCellValue(rightCell)
    
board = Board(len(input))
board.populateBoard()
board.changeCellValue([1, 1], "p")

for i, row in enumerate(input):
    for j, cell in enumerate(row):
        board.changeCellValue([i, j], input[i][j])

for i, row in enumerate(input):
    for j, cell in enumerate(row):
        if cell == '^':
            player = Player([i, j])

i = 0

while not player.checkIfClear(board) == "outOfBounds":
    i += 1

    if player.lookRight(board) == "X":

    if player.checkIfClear(board) in [".", "X"]:
        player.move(board)
    elif player.checkIfClear(board) == False:
        player.rotate()
    
    if i % 2000 == 0:
        board.printBoard()

    result = 0

for row in range(0, board.size):
    for col in range(0, board.size):
        if board.board[row, col].getValue() == "X":
            result +=1

print(result+1)






