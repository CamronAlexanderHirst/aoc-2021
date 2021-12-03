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
