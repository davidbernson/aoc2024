def test_line(line, critical_dist):
    direction = "UP"
    
    for x in range(0, len(line)-1):
        dist = line[x] - line[x+1]
        if abs(dist) > critical_dist:
            return False
        
        if dist>0:
            direction = "UP"
        elif dist<0:
            direction = "DOWN"
        else:
            direction = "NONE"
            
        if x > 0:
            if direction != current_direction:
                return False
        
        current_direction = direction

    else:
        return True

def test_permuted_lines(line, critical_dist):
    direction = "UP"
    status = "UNSAFE"

    for permutation in range(0, len(line)):
        
        permuted_line = line[:permutation] + line[permutation +1:]

        for x in range(0, len(permuted_line)-1):
            dist = permuted_line[x] - permuted_line[x+1]

            if test_line(permuted_line, critical_dist):
                return True
    return False


with open("./2/data/data.txt") as file:
    lines = [line.rstrip() for line in file]

critical_dist = 3

total_safe_sequences = 0

for line in lines:
    line = [int(x) for x in line.split() if x.isdigit()]

    direction = "UP"
    status = "NORMAL"

    if test_line(line, critical_dist):
        print(f'Line {line} is a safe sequence')
        total_safe_sequences += 1
    elif test_permuted_lines(line, critical_dist):
        print(f'Line {line} is a safe sequence, due to Problem Dampener')
        total_safe_sequences += 1
    else:
        print(f'Line {line} is NOT a safe sequence.')

print(f"Total number of safe sequences: {total_safe_sequences}")
        