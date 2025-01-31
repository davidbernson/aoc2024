with open("./data/data.txt") as file:
    lines = [line.rstrip() for line in file]

a = list()
b = list()

for line in lines:
    pair = [int(word) for word in line.split() if word.isdigit()]
    a.append(pair[0])
    b.append(pair[1])

a.sort()
b.sort()

result = list()

for x, y in zip(a, b):
    result.append(abs(x - y))

print(f'The sum is {sum(result)}')