with open("./4/data/data.txt") as file:
    input = [line.rstrip() for line in file]

directions = [
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1),
]

boardsize = len(input)
board = {}
result = 0

x_dict = {(1, 1) : "",
          (1, -1) : "",
          (-1, -1) : "",
          (-1, 1) : ""}

for i, line in enumerate(input):
    for j, letter in enumerate(line):
        board[(i, j)] = letter
    
for letter in board:
    if board[letter] == "A":
        # print(f'Current letter: "A" @ {letter}')
        for direction in directions:
            new_letter = (letter[0] + direction[0], letter[1] + direction[1])
            # print(new_letter)
            if new_letter not in board.keys():
                break
            x_dict[direction] = board[new_letter]
            # print(f'A @ {letter}: neighbours - {x_dict}')
            values = list(x_dict.values())
        if values.count("M") == 2 and values.count("S") == 2:
            if x_dict[(-1, -1)] != x_dict[(1, 1)]:
                # print(x_dict)
                result += 1

        x_dict = {(1, 1) : "",
          (1, -1) : "",
          (-1, -1) : "",
          (-1, 1) : ""}
                        
print(f'Result: {result}')