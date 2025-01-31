with open("./1/data/data.txt") as file:
    lines = [line.rstrip() for line in file]

a = list()
b = list()

for line in lines:
    pair = [int(word) for word in line.split() if word.isdigit()]
    a.append(pair[0])
    b.append(pair[1])

result = list()

for x in a:
    result.append(x * b.count(x))

print(f'The sum is {sum(result)}')