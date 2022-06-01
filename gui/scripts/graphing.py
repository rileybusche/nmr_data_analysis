import math
import matplotlib.pyplot as plt
import functions
from decimal import Decimal
import glob
import os
import json 

def build_graph(file_path:str, frequencies:[], graph_output_path:str, logging_path:str, run_number:str, sample:str, trial_number:str) -> dict:

    size = ''
    left = ''
    right = ''

    debug = False
    graph_debug = False

    search_range = 100
    peak_search = True

    # Contains the input freqs. as well as the actual highest value for logging
    data = {}
    # Peak data returned to main - has the highest intensity replacing the intensity at the point if peak_search 
    return_data = {}

    y_values = []
    
    # graph_path = f'/Users/rileybusche/Development/nmr_data_analysis/SULVdiamine/ph8.50/Trial1/{number}.txt'
    # /Users/rileybusche/Development/nmr_data_analysis/SULVdiamine/ph8.50/Trial1/17.txt
    print(f'file_path: {file_path}')
    with open(file_path) as file_object:
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
    
    if debug:
        print(f'Index Input Point: {indices}')
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
    ax.set_title(f'{file_path.split(os.sep)[-4]} ' + sample + f' Trial{trial_number} ' + run_number )

    for count, index in enumerate(indices):

        point = (frequencies[count], y_values[index])
        
        # If peak is inverted, value will be negative - need to take abs value for later calculation (math.e)
        return_data[frequencies[count]] = abs(float(y_values[index]))

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

            # Return Data with adjusted peak intensity
            return_data[frequencies[count]] = abs(float(max_y))


            data[file_path] = {
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

    # ~/graphing/{ph}/Trial1/...
    graph_output_path = os.path.join(graph_output_path, sample, f'Trial{trial_number}', f'{run_number}.jpeg')
    plt.savefig(graph_output_path, bbox_inches='tight', dpi=200)

    # Show Graphs if debug is on
    if graph_debug:
        plt.show()

    # Log input peak and actual peak to file
    logging_path = os.path.join(logging_path, 'raw', sample, f'Trial{trial_number}', f'{run_number}.json')
    with open(logging_path, 'w') as output_file:
        json.dump(data, output_file, indent=4)

    print(f'return_data: {return_data}')
    return return_data