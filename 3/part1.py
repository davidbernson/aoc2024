import re

with open("./3/data/testdata.txt") as file:
    input = [line.rstrip() for line in file]

print(input)

pattern = re.compile("mul\([0-9]+,[0-9]+\)")

print(pattern.match(input[0]))

