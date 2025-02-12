import re

with open("./3/data/data.txt") as file:
    input = file.read()

pattern = re.compile(r"(.*)(don\'t\(\))(.*)(do\(\))(.*)")
pattern_expr = re.compile(r"mul\(\d+,\d+\)")
pattern_tuples = re.compile(r"\d+")

first_parse = pattern.findall(input)

print(first_parse[0])

expressions = pattern_expr.findall(first_parse)[0]

print(expressions)

result = 0

for expression in expressions:
    tuple = pattern_tuples.findall(expression)
    result += int(tuple[0]) * int(tuple[1])

print(result)

