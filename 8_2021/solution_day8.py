import numpy as np

# Read the input
with open('short_test.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

dict_list = []
for line in lines:
    signal_pattern = line.split(' | ')[0]
    output = line.split(' | ')[1]
    line_dict = {
        'signal_pattern_strings': signal_pattern.split(),
        'output_strings': output.split()
    }
    dict_list.append(line_dict)

### Part 1: count the number of unique numbers in output (1, 4, 7 ,8)

# count number of strings of length 2, 4, 3, or 7
count = 0
for x in dict_list:
    for output in x['output_strings']:
        if len(output) in [2, 4, 3, 7]:
            count += 1
print('Solution Part 1: ', count)


### Part 2: get confused then decode each output

for x in dict_list:
    # get the correct pattern - number combinations
    truth_dict = {}
    for pattern in x['signal_pattern_strings']:
        if len(pattern) == 2:
            truth_dict[a] = pattern
        elif len(pattern) == 4:
            truth_dict[4] = pattern
        elif len(pattern) == 3:
            truth_dict[7] = pattern
        elif len(pattern) == 7:
            truth_dict[8] = pattern
        else:
            truth_dict[pattern] = None 
    
    signal_to_segment_dict = {}

    # get signal to segment A (top) by comparing 1 and 7:
    signal_to_segment_dict[set(truth_dict[7]).difference(set(truth_dict[1]))] = 'a'

    # get signal to segment D (middle) by comparing 0 and 8:







    


