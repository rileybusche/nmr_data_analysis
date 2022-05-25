import math
import matplotlib.pyplot as plt
import functions
from decimal import Decimal

size = ''
left = ''
right = ''
search_range = 50
frequencies = [1.1950]

debug = True

peak_search = True

y_values = []
with open('/Users/rileybusche/Development/nmr_data_analysis/SULV_1,2-diamine/ph8.5/Trial1/1.txt') as file_object:
    for line in file_object.readlines():

        if 'SIZE' in line:
            size = int(line.strip().split()[3])
            print(size)
        if 'LEFT' in line:
            tokens = line.strip().split()
            left = float(tokens[3])
            right = float(tokens[7])
        if '#' not in line:
            y_values.append(float(line.strip()))

interval = (left + abs(right)) / size

x_values = [left]
previous_value = left
for _ in range(size-1):
    previous_value -= interval
    x_values.append(previous_value)

# data_points = {}
# for (x,y) in zip(x_values, y_values):
#     data_points[x] = y
indices = functions.calculateIndexs(left_bound=left, right_bound=right, size=size, frequencies=frequencies)
print(f'Index: {indices}')

if debug:
    print(f'Interval: {interval}')
    print(f'Left: {left}')
    print(f'Right: {right}')

    print(f'Length of y_values: {len(y_values)}')
    print(f'Length of x_values: {len(x_values)}')

# plot
fig, ax = plt.subplots()
ax.plot(x_values, y_values)

for index in indices:
    point = (frequencies[0], y_values[index])

    ax.annotate(
        text =          f'point: ({point[0]} ppm, {"%.3E" % Decimal(point[1])})', 
        xy =            (point[0], point[1]),
        xytext =        (-100,10),
        textcoords =    'offset points'
        # arrowprops =    {'arrowstyle' : 'simple'}
    )

    
    ax.plot(x_values[index], y_values[index], marker='.', c='red')
    if debug:
        ax.plot(x_values[index-search_range], y_values[index-search_range], marker='.', c='green')
        ax.plot(x_values[index+search_range], y_values[index+search_range], marker='.', c='yellow')

    print(f'Y_value at {index}: {y_values[index]}')
    print(f'Point: ({point[0]} ppm, {"%.3E" % Decimal(point[1])})')


if peak_search:
    for index in indices:
        y_subset = y_values[index-search_range : index+search_range]
        x_subset = x_values[index-search_range : index+search_range]
        
        max_y = max(y_subset)
        max_y_index = y_subset.index(max_y)

        max_point = (x_subset[max_y_index], max_y)

        print(f'index: {index}')
        print(f'max_x: {x_subset[max_y_index]}')
        print(f'max_x: {x_values[index-(search_range-max_y_index)]}')
        print(f'max_y: {max_y}')
        print(f'max_index: {max_y_index}')

        # Graphing the max in the search range
        ax.plot(max_point[0], max_point[1], marker='.', c='orange')

        # location for the zoomed portion 
        sub_axes = plt.axes([.6, .6, .25, .25])
        # plot the zoomed portion
        sub_axes.plot(x_subset, y_subset, c = 'k')
        # insert the zoomed figure
        plt.setp(sub_axes)

ax.invert_xaxis()
plt.show()