with open("./5/data/data.txt") as file:
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

def buildRuleSubset(instruction, rules):
    return [rule for rule in rules if rule[0] in list(instruction) and rule[1] in list(instruction)]

#SWAP
def swap(dict, a, b):
    
    stored_a = dict[a]
    stored_b = dict[b]

    dict[a] = stored_b
    dict[b] = stored_a

    return dict

#MANIPULATE ORDERING DICT
def orderDict(pageNumbersDict, rules):

    ruleSubset = buildRuleSubset(pageNumbersDict, rules)

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

#VALIDATE INSTRUCTION
def validateRule(instruction, rule):
    instruction = list(instruction)    
    a = rule[0]
    b = rule[1]
    
    if instruction.index(a) < instruction.index(b):
        return True
    else:
        return False

def validateInstruction(instruction, rules):
    ruleSubset = buildRuleSubset(instruction, rules)

    for rule in ruleSubset:
        if validateRule(instruction, rule):
            continue
        else:
            return False
    return True

def orderInstruction(instruction, rules):

    ruleSubset = buildRuleSubset(instruction, rules)
    
    instruction = list(instruction)

    for rule in ruleSubset:

        a = rule[0]
        b = rule[1]

        stored_a = instruction.index(a)
        stored_b = instruction.index(b)

        if not validateRule(instruction, rule):
            print(f'Rule {rule} broken. Changing order of {a} and {b} in {instruction}')
            instruction[stored_b], instruction[stored_a] = instruction[stored_a], instruction[stored_b]
            print(f'New instruction: {instruction}') 

    return instruction

#VALIDATING INSTRUCTIONS
resultValid = 0
resultInvalid = 0

for instruction in instructions:
    pageNumbersDict = buildDict(instruction)
    orderedPageNumbers = orderDict(pageNumbersDict, rules)

    if validateInstruction(instruction, rules):    
        print(f'{instruction} is a valid instruction')
        resultValid += instruction[len(instruction)//2]
    else:

        while not validateInstruction(instruction, rules):
            instruction = orderInstruction(instruction, rules)
            
        print(f'Ordered instruction: {instruction}')
        resultInvalid += instruction[len(instruction)//2]


print(resultValid, resultInvalid)

     
