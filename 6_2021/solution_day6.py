import numpy as np

# Read the input to list of boards and numbers
with open('input.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

# Part 1: find number of fish after 80 days
fish_file = [int(x) for x in lines[0].split(',')]
for i in range(80):
    for j in range(len(fish_file)):
        if fish_file[j] == 0:
            fish_file[j] = 6
            fish_file.append(8)
        else:
            fish_file[j] -= 1

print('Solution part 1: ', len(fish_file))


# Part 2: find number of fish after 256 days
fish_file = [int(x) for x in lines[0].split(',')]

# Count the number of fish in each day
fish_count = np.zeros(9)
for i in fish_file:
    fish_count[i] += 1

for i in range(256):
    # find number of new fish
    new_fish = fish_count[0]
    new_fish_count = np.zeros(9)

    for i in range(8):
        new_fish_count[i] += fish_count[i+1]
    
    new_fish_count[6] += new_fish
    new_fish_count[8] += new_fish
    
    fish_count = new_fish_count

print('Solution part 2: ', sum(fish_count))