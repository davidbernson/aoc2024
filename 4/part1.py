with open("./4/data/data.txt") as file:
    input = [line.rstrip() for line in file]

directions = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (-1, 1),
]

boardsize = len(input)
board = {}
result = 0

for i, line in enumerate(input):
    for j, letter in enumerate(line):
        board[(i, j)] = letter
    
for letter in board:
    if board[letter] == "X":
        # print(f'yipee! X @ {letter}')

        for direction in directions:
            letter2 = (letter[0] + direction[0], letter[1] + direction[1])
            if letter2 in board.keys():
                if board[letter2] == "M":
                    # print(f'M @ {letter2}, continuing in {direction}')
                    letter3 = (letter2[0] + direction[0], letter2[1] + direction[1])
                    if letter3 in board.keys():
                        if board[letter3] == "A":
                            # print(f'A @ {letter3}')
                            letter4 = (letter3[0] + direction[0], letter3[1] + direction[1])
                            if letter4 in board.keys():
                                if board[letter4] == "S":
                                    result += 1
                                    # print(f'yippeedoodle! full XMAS @ {letter}')
                        
print(f'Result: {result}')