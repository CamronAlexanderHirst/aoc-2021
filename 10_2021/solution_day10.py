import numpy as np

# Read the input
with open('input.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

points_dict = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}