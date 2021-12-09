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

# Read the input
with open('riley-8-data.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

dict_list = []
for line in lines:
    signal_pattern = line.split(' | ')[0]
    output = line.split(' | ')[1]
    print(signal_pattern.split(' '))
    print(output.split(' '))
    line_dict = {
        'signal_pattern_strings': signal_pattern.split(' '),
        'output_strings': output.split(' ')
    }
    dict_list.append(line_dict)

total_list = [] 
for x in dict_list:
    # get the correct pattern - number combinations
    truth_dict = [None for _ in range(10)]
    remaining_list = []
    for pattern in x['signal_pattern_strings']:
        if len(pattern) == 2:
            truth_dict[1] = pattern
        elif len(pattern) == 4:
            truth_dict[4] = pattern
        elif len(pattern) == 3:
            truth_dict[7] = pattern
        elif len(pattern) == 7:
            truth_dict[8] = pattern
        else:
            remaining_list.append(pattern)
    
    # find 3:
    for p in remaining_list:
        if len(p) == 5 and set(p).intersection(set(truth_dict[1])) == set(truth_dict[1]):
            truth_dict[3] = p
            remaining_list.remove(p)
            #print('found 3!')
            break

    # find 9:
    for p in remaining_list:
        if len(p) == 6 and set(p).intersection(set(truth_dict[4])) == set(truth_dict[4]):
            truth_dict[9] = p
            remaining_list.remove(p)
            # print('found 9!')
            break 
    
    # find 6:
    for p in remaining_list:
        if len(p) == 6 and len((set(p).intersection(set(truth_dict[8]))).intersection(set(truth_dict[1]))) == 1 :
            truth_dict[6] = p
            remaining_list.remove(p)
            # print('found 6!')
            break 

    # find 0:
    for p in remaining_list:
        if len(p) == 6:
            truth_dict[0] = p
            remaining_list.remove(p)
            # print('found 0!')
            break 

    # find 5:
    for p in remaining_list:
        if len(p) == 5:
            truth_dict[5] = p 
            remaining_list.remove(p)
            # print('found 5!')
            break 

    # find 2:
    for p in remaining_list:
        if len(p) == 5:
            truth_dict[2] = p 
            remaining_list.remove(p)
            # print('found 2!')
            break 
    
    if len(remaining_list) != 0:
        raise ValueError('remaining list no length 0')

    
    number_list = []
    for o in x['output_strings']:
        for i in range(len(truth_dict)):
            if set(o) == set(truth_dict[i]):
                number_list.append(i)
                break
            else:
                pass

    # concatenate the integers
    if len(number_list) != 4:
        print(number_list)
        break
    else: print(number_list)

    number = int(''.join(map(str, number_list)))
    total_list.append(number)

print(total_list)
print(np.sum(np.array(total_list)))







    


