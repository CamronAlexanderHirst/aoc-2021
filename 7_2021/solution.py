import numpy as np

# Read the input
with open('input.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

### Part 1: find the min fuel location

crab_loc = np.array([int(x) for x in lines[0].split(',')])
min_loc = np.min(crab_loc)
max_loc = np.max(crab_loc)
opt_loc, opt_fuel = None, np.inf

# brute force search
for i in range(min_loc, max_loc+1):
    total_fuel_cost = np.sum(np.abs(crab_loc-i))

    if total_fuel_cost < opt_fuel:
        opt_loc = i
        opt_fuel = total_fuel_cost
    
print('solution: ', opt_fuel)


### Part 2: Find the min fuel location, more expensive fuel

crab_loc = np.array([int(x) for x in lines[0].split(',')])
min_loc = np.min(crab_loc)
max_loc = np.max(crab_loc)
opt_loc, opt_fuel = None, np.inf

# brute force search
for i in range(min_loc, max_loc+1):

    # calculate total fuel cost
    total_fuel_cost = np.abs(crab_loc-i)
    total_fuel_cost = np.sum(np.array([n*(n+1)/2 for n in total_fuel_cost]))

    if total_fuel_cost < opt_fuel:
        opt_loc = i
        opt_fuel = total_fuel_cost
    
print('solution: ', opt_fuel)