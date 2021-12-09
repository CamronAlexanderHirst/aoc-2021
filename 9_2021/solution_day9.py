
import numpy as np

# Read the input
with open('input.txt') as f:
    lines = f.read().splitlines()  # read lines without /n

height_map = []
for line in lines:
    height_map.append([int(x) for x in line])

height_map = np.array(height_map)
print(height_map)


## Part 1:
# Find all low points and danger score

rows, columns = np.shape(height_map)

print(rows, columns)

vertical_mins = []
horizontal_mins = []
for x in range(rows):
    for y in range(columns):
        if y == 0:
            if height_map[x,y] < height_map[x,y+1]:
                horizontal_mins.append([x,y])
        elif y == columns - 1:
            if height_map[x,y] < height_map[x,y-1]:
                horizontal_mins.append([x,y])
        else:
            if height_map[x,y] < height_map[x,y-1] and height_map[x,y] < height_map[x,y+1]:
                horizontal_mins.append([x,y]) 

for y in range(columns):
    for x in range(rows):
        if x == 0:
            if height_map[x,y] < height_map[x+1,y]:
                vertical_mins.append([x,y])
        elif x == rows - 1:
            if height_map[x,y] < height_map[x-1,y]:
                vertical_mins.append([x,y])
        else:
            if height_map[x,y] < height_map[x-1,y] and height_map[x,y] < height_map[x+1,y]:
                vertical_mins.append([x,y]) 

low_points = []
for v in vertical_mins:
    if v in horizontal_mins:
        low_points.append(v)

print(low_points)

total_sum = 0
for p in low_points:
    total_sum += height_map[p[0], p[1]] +1

print('Solution part 1: ', total_sum)


## Part 2: Find basins of attraction for each low point, sum the sizes of three largest

def check_neighbors(point, h_map, rows, columns):
    points = []
    x = point[0]
    y = point[1]

    if x-1 >= 0:
        if h_map[x,y] < h_map[x-1,y] and h_map[x-1,y] < 9:
            points.append([x-1,y])
    if y-1 >= 0:
        if h_map[x,y] < h_map[x,y-1] and h_map[x,y-1] < 9:
            points.append([x,y-1])
    if x+1 <= rows - 1:
        if h_map[x,y] < h_map[x+1,y] and h_map[x+1,y] < 9:
            points.append([x+1,y]) 
    if y+1 <= columns - 1:
        if h_map[x,y] < h_map[x,y+1] and h_map[x,y+1] < 9:
            points.append([x,y+1]) 
    return points

# find basin of attraction around each low point
basin_len_list = []
#low_points = [low_points[0]]
for p in low_points:
    print(p)
    basin = [p]
    new_points = True
    while new_points:
        new_points = False
        potential_pts = []
        for b in basin:
            ayes = check_neighbors(b, height_map, rows, columns)
            for a in ayes:
                if a in basin:
                    pass 
                else:
                    basin.append(a)
                    new_points = True

    #print(basin)
    #toggle_map = np.zeros(np.shape(height_map))
    #for b in basin:
    #    toggle_map[b[0],b[1]] = 1
    #print(toggle_map)
    basin_len_list.append(len(basin))

sorted_list = sorted(basin_len_list)
solution_list = sorted_list[-3:]
solution_p2 = solution_list[0] * solution_list[1] * solution_list[2]
print('Solution Part 2: ', sorted_list, solution_list, solution_p2)
