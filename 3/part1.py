import re

with open("./3/data/data.txt") as file:
    input = file.read()

print(input)

pattern = re.compile(r"mul\(\d+,\d+\)")
pattern_tuples = re.compile(r"\d+")

expressions = pattern.findall(input)

result = 0

for expression in expressions:
    tuple = pattern_tuples.findall(expression)
    result += int(tuple[0]) * int(tuple[1])

print(result)

