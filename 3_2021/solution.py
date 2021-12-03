#%%
# Setup
import numpy as np

# import data
with open('input.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

#%%
# Part 1:
num_lines = len(lines)
sum = np.zeros(len(lines[0]))

for line in lines:
    line_split = np.array([int(num) for num in line])
    sum += line_split
print(sum, num_lines)

print('sum: {}'.format(sum))

gamma = [int(i > num_lines/2) for i in sum]
print('gamma: {}'.format(gamma))
epsilon = [int(not i) for i in gamma]
print('epsilon: {}'.format(epsilon))

gamma_binary = ''.join(map(str, gamma))
epsilon_binary = ''.join(map(str, epsilon))

gamma_dec = int(gamma_binary, base=2)
epsilon_dec = int(epsilon_binary, base=2)

print('solution: {}'.format(gamma_dec*epsilon_dec))


# convert gamma, epsilon strings to binary numbers

# %%
# Part 2:

# Oxygen generator rating:
ary = [[int(num) for num in line] for line in lines]
pos = 0
while len(ary) > 1:

    # sum of pos-ith index in ary
    sum = 0
    for line in ary:
        sum += int(line[pos])
    
    
    if len(ary)%2 == 0.0 and float(sum) == len(ary)/2:
        val = 1
    elif sum > len(ary)/2:
        val = 1
    else:
        val = 0

    # find all lines that don't meet bit criteria
    remove = []
    for i in range(len(ary)):
        line = ary[i]
        if line[pos] != val:
            remove.append(i)

    # remove all lines that don't meet bit criteria
    for i in sorted(remove, reverse=True):
        ary.pop(i)

    pos += 1
    if pos > len(ary[0])-1:
        break


oxy = ary[0]
oxy_bin = ''.join(map(str, oxy))
oxy_dec = int(oxy_bin, base=2)


# CO2 generator rating:
ary = [[int(num) for num in line] for line in lines]
pos = 0
while len(ary) > 1:
    # sum of pos-ith index in ary
    sum = 0
    for line in ary:
        sum += int(line[pos])
    
    
    if len(ary)%2 == 0.0 and float(sum) == len(ary)/2:
        val = 1
    elif sum > len(ary)/2:
        val = 1
    else:
        val = 0

    # find all lines that don't meet bit criteria
    remove = []
    for i in range(len(ary)):
        line = ary[i]
        if line[pos] == val:  # note changed logic
            remove.append(i)
    # remove all lines that don't meet bit criteria
    for i in sorted(remove, reverse=True):
        ary.pop(i)
    pos += 1
    if pos > len(ary[0])-1:
        break

co2 = ary[0]
co2_bin = ''.join(map(str, co2))
co2_dec = int(co2_bin, base=2)

print('oxy_dec: {}'.format(oxy_dec))
print('co2_dec: {}'.format(co2_dec))
print('solution: {}'.format(oxy_dec*co2_dec))


# %%

# %%
