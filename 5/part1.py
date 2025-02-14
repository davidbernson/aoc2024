with open("./5/data/testdata.txt") as file:
    input = [line for line in file]

#PRE-PROCESSING

#RULES
rules = [line.rstrip() for line in input if '|' in line]
rules = [tuple(map(int, pair.split(sep='|'))) for pair in rules]

#INSTRUCTIONS
instructions = [line.rstrip() for line in input if ',' in line]
instructions = [tuple(map(int, instruction.split(sep=','))) for instruction in instructions]

#BUILD ORDERING DICT

def buildDict(instruction):

    pageNumbersDict = {key: value for value, key in enumerate(instruction)}

    return pageNumbersDict

#SWAP
def swap(dict, a, b):
    
    stored_a = dict[a]
    stored_b = dict[b]

    dict[a] = stored_b
    dict[b] = stored_a

    return dict

#MANIPULATE ORDERING DICT
def orderDict(pageNumbersDict, rules):

    ruleSubset = [rule for rule in rules if rule[0] in list(pageNumbersDict.keys()) and rule[1] in list(pageNumbersDict.keys())]

    for rule in ruleSubset:
        
        a = rule[0]
        b = rule[1]

        stored_a = pageNumbersDict[a]
        stored_b = pageNumbersDict[b]

        # print(f'Evaluating rule {rule}. {a} : {pageNumbersDict[a]} vs {b} : {pageNumbersDict[b]}')
        if stored_a > stored_b:
            
            pageNumbersDict = swap(pageNumbersDict, a, b)

    # print(pageNumbersDict)
    return pageNumbersDict

def orderInstruction(instruction, rules):
    ruleSubset = [rule for rule in rules if rule[0] in list(pageNumbersDict.keys()) and rule[1] in list(pageNumbersDict.keys())]
    
    instruction = list(instruction)

    for rule in ruleSubset:

        a = rule[0]
        b = rule[1]

        if instruction.index(a) > instruction.index(b):
            print(f'{a} is after {b}, thus violating rule {rule}.')

            a, b = instruction.index(a), instruction.index(b)
            instruction[b], instruction[a] = instruction[a], instruction[b]

    return instruction
            

#VALIDATING INSTRUCTIONS
resultValid = 0
resultInvalid = 0

for instruction in instructions:
    pageNumbersDict = buildDict(instruction)
    orderedPageNumbers = orderDict(pageNumbersDict, rules)

    isValidInstruction = False
    prev_value = -1

    for page in instruction:
        if orderedPageNumbers[page] > prev_value:
            prev_value = orderedPageNumbers[page]
            isValidInstruction = True
            continue
        else:
            isValidInstruction = False
            break

    if isValidInstruction:    
        print(f'{instruction} is a valid instruction')
        resultValid += instruction[len(instruction)//2]
    else:
        print(f'{instruction} is an invalid instruction')
        instruction = orderInstruction(instruction, rules)
        print(f'Ordered instruction: {instruction}')
        resultInvalid += instruction[len(instruction)//2]

print(resultValid, resultInvalid)

    
