import numpy as np

# Read the input
with open('input.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

markers = [['(', ')'], 
           ['[', ']'],
           ['{', '}'],
           ['<', '>']]

points_dict = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
match_dict = {'(':')', '[':']', '{':'}', '<':'>'}
count_dict = {}

def reset_count(c_dict, m_list):
    for mset in m_list:
        for s in mset:
            c_dict[s] = 0
    return c_dict


# Part 1: Find the first incorrect closing character in each line
list_openers = []
incorrect_chars = []
corrupted_lines = []
i = 0
for line in lines:
    stop_line = False
    for c in list(line):
        if stop_line: break
        if c in list(match_dict.keys()):
            list_openers.append(c)
        else:
            if c == match_dict[list_openers[-1]]:
                list_openers = list_openers[:-1]
            else:
                incorrect_chars.append(c)
                corrupted_lines.append(i)
                stop_line = True
    i += 1
sol = 0
for c in incorrect_chars:
    sol += points_dict[c]

print('Solution part 1: ', sol)
print(corrupted_lines)



## Part 2: 

closer_score_dict = {
    ')': 1, 
    ']': 2, 
    '}': 3, 
    '>': 4, 
}

 
# Discard all corrupted lines
for i in sorted(corrupted_lines, reverse=True):
    lines.pop(i)

score_list = []
for line in lines:
    openers = []
    for c in list(line):
        if c in list(match_dict.keys()):
            openers.append(c)
        else:
            if c == match_dict[openers[-1]]:
                openers = openers[:-1]
            else:
                raise ValueError('Corrupted line found')
    close_list = []
    openers.reverse()
    for o in openers:
        close_list.append(match_dict[o])
    
    score = 0 
    for c in close_list:
        score = 5 * score 
        score += closer_score_dict[c]
    score_list.append(score)

score_list = sorted(score_list)
sol = score_list[int(len(score_list)/2)]

print('Part 2 solution: ', sol)
    
    


    


