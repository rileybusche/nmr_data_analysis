import math
import matplotlib.pyplot as plt
import functions
from decimal import Decimal
import glob

size = ''
left = ''
right = ''

frequencies = [1.1969]

debug = False
graph_debug = True

search_range = 100
peak_search = True

y_values = []


graphs = glob.glob()
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
print(f'Index Input Point: {indices}')

if debug:
    print(f'Interval: {interval}')
    print(f'Left: {left}')
    print(f'Right: {right}')

    print(f'Length of y_values: {len(y_values)}')
    print(f'Length of x_values: {len(x_values)}')

# plot
fig, ax = plt.subplots()
ax.plot(x_values, y_values)
ax.set(xlabel='Frequency (ppm)', ylabel='')
ax.set_title('Test Title')

for index in indices:
    point = (frequencies[0], y_values[index])

    ax.annotate(
        text =          f'Input Point (red):\n({point[0]} ppm, {"%.4E" % Decimal(point[1])})', 
        xy =            (point[0], point[1]),
        xytext =        (-50,10),
        textcoords =    'offset points'
        # arrowprops =    {'arrowstyle' : 'simple'}
    )

    # This is the point defined by the input frequency - before adjust to be the local maximum
    input_point = (x_values[index], y_values[index])
    ax.plot(input_point[0], input_point[1], marker='.', c='red')
    # Build left and right bounds of search area
    if graph_debug:
        ax.plot(x_values[index-search_range], y_values[index-search_range], marker='.', c='green')
        ax.plot(x_values[index+search_range], y_values[index+search_range], marker='.', c='green')

    print(f'Y_value at {index}: {y_values[index]}')
    print(f'Input Point: ({point[0]} ppm, {"%.4E" % Decimal(point[1])})')

    # Finds the true max point in search range
    if peak_search:
        # Take subset of data to search for peak
        y_subset = y_values[index-search_range : index+search_range]
        x_subset = x_values[index-search_range : index+search_range]
        
        # Find Max_y
        max_y = max(y_subset)
        max_y_index = y_subset.index(max_y)

        # Build max point (x,y) in subset
        max_point = (x_subset[max_y_index], max_y)
        print(f'Index Max Point: {index-(search_range-max_y_index)}')
        print(f'Max Point: ({max_point[0]:.4f} ppm, {"%.4E" % Decimal(max_point[1])})')

        if debug:
            print(f'index: {index}')
            print(f'max_x: {x_subset[max_y_index]}')
            print(f'max_x: {x_values[index-(search_range-max_y_index)]}')
            print(f'max_y: {max_y}')
            print(f'max_index: {max_y_index}')

        # Graphing the max in the search range
        ax.plot(max_point[0], max_point[1], marker='.', c='orange')

        # location for the zoomed portion 
        sub_axes = plt.axes([.2, .6, .25, .25])
        # plot the zoomed portion
        sub_axes.plot(x_subset, y_subset)
        # Plot input point
        sub_axes.plot(input_point[0], input_point[1], marker='.', c='red')
        # Plot max point
        sub_axes.plot(max_point[0], max_point[1], marker='.', c='orange')

        sub_axes.annotate(
            text =          f'Max Point (orange):\n({max_point[0]:.4f} ppm, {"%.4E" % Decimal(max_point[1])})', 
            xy =            (point[0], point[1]),
            xytext =        (-50,-50),
            textcoords =    'offset points'
            # arrowprops =    {'arrowstyle' : 'simple'}
        )
        
        # insert the zoomed figure
        sub_axes.invert_xaxis()
        # plt.setp(sub_axes)

ax.invert_xaxis()

plt.show()