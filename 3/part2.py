import re

with open("./3/data/data.txt") as file:
    input = file.read()

# PRE-PROCESSING

inputs = re.split(r"do\(\)", input)

processed_items = []

for item in inputs:
    print(f'pre: {len(item)}')
    processed_items.append(item.split(r"don't")[0])
    print(f' post: {len(item)}')

print(processed_items)

# COMPUTE

pattern = re.compile(r"mul\(\d+,\d+\)")
pattern_tuples = re.compile(r"\d+")

# expressions = pattern.findall(input)

result = 0

for item in processed_items:
    expressions = pattern.findall(item)

    for expression in expressions:
        tuple = pattern_tuples.findall(expression)
        result += int(tuple[0]) * int(tuple[1])

print(f'Result: {result}')