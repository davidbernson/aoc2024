with open("./2/data/data.txt") as file:
    lines = [line.rstrip() for line in file]

critical_dist = 3

total_safe_sequences = 0

for line in lines:
    line = [int(x) for x in line.split() if x.isdigit()]

    direction = "UP"
    
    for x in range(0, len(line)-1):
        dist = line[x] - line[x+1]
        if abs(dist) > critical_dist:
            print(f"Sequence {line} is not safe. Distance increased by {abs(dist)}.")
            break
        
        if dist>0:
            direction = "UP"
        elif dist<0:
            direction = "DOWN"
        else:
            direction = "NONE"
            
        if x > 0:
            if direction != current_direction:
                print(f"Sequence {line} is not safe. Direction changed from {current_direction} to {direction}.")
                break
        
        current_direction = direction

    else:
        print(f"Sequence {line} is safe.")
        total_safe_sequences += 1

print(f"Total number of safe sequences: {total_safe_sequences}")

        