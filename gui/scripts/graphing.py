import math
import matplotlib.pyplot as plt
import functions
from decimal import Decimal
import glob
import os
import json 

size = ''
left = ''
right = ''

frequencies = [1.1969]

debug = False
graph_debug = False

search_range = 100
peak_search = True

data = {}

# graphs = sorted(glob.glob(os.path.join('/Users/rileybusche/Development/nmr_data_analysis/SULVdiamine/ph8.50/Trial1', '*.txt')))
for number in range(1,19):
    y_values = []
    graph_path = f'/Users/rileybusche/Development/nmr_data_analysis/SULVdiamine/ph8.50/Trial1/{number}.txt'
    print(graph_path)
    with open(graph_path) as file_object:
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
    fig.set_size_inches(16, 9)
    ax.plot(x_values, y_values)
    ax.set(xlabel='Frequency (ppm)', ylabel='')
    ax.set_title(' '.join(graph_path.split(os.sep)[-4:]))

    for count, index in enumerate(indices):

        point = (frequencies[count], y_values[index])

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
            if point[1] > 0:
                max_y = max(y_subset)
                max_y_index = y_subset.index(max_y)
            # Handles the case where peak is inverted
            elif point[1] < 0:
                max_y = min(y_subset)
                max_y_index = y_subset.index(max_y)

            # Build max point (x,y) in subset
            max_point = (x_subset[max_y_index], max_y)

            data[graph_path] = {
                f'{frequencies[count]:.4f}'  : "%.4E" % Decimal(y_values[index]),
                f'{max_point[0]:.4f}'        : "%.4E" % Decimal(max_point[1])
            }

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
            sub_axes = plt.axes([.15, .6, .25, .25])
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

    plt.savefig(f'./{"_".join(graph_path.split(os.sep)[-4:])}.jpeg', bbox_inches='tight', dpi=200)
    if graph_debug:
        plt.show()

if debug:
    with open('./logged_data.json', 'w') as output_file:
        json.dump(data, output_file, indent=4)