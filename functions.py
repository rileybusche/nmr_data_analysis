# Riley Busche 2019
# File containing functions used in main.py
import csv

def calculateIndexs(left_bound, right_bound, size, frequencies):
    indices = []
    # Calculating y = m x + b equation for finding index of intestity from given frequency
    
    slope = (0 - size)/(left_bound - right_bound)      # Point Slope form to find m
    y_int = 0 - (slope * left_bound)                  # Using line equaiton to find y-int

    # index = slope * (given frequency) + y_int
    # This index (frequency) will be truncated to get a valid whole number for the index
    for frequency in frequencies:
        indices.append(int((slope * frequency) + y_int))
    
    return indices

# Pulls the intensities out of intensity_list and stores in a dictionary
def findIntensities(intensity_list, indices, frequencies):
    frequency_intensity_dict = {}
    for index, frequency in map(None, indices, frequencies):
        frequency_intensity_dict[frequency] = findPeak(intensity_list, index)

    return frequency_intensity_dict

# Looks for peak closest to given intensity and return that intensity
def findPeak(intestity_list, index):
    peak_intensity = 0.00
    # Check frequecny at intensity_list[index] vs intensity_list[index--] and intensity_list[index++], take higher value
    search = True
    while(search):
        if abs(intestity_list[index]) <= abs(intestity_list[index + 1]):
            index += 1
        elif abs(intestity_list[index]) <= abs(intestity_list[index - 1]):
            index -= 1
        else:
            peak_intensity = intestity_list[index]
            search = False

    return abs(peak_intensity)

# Creates CSV file
def create_csv(file_name, values):

    with open(file_name, mode='w') as output_file:
        output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print(values)
        output_file.writerow(['Trial', ''])
        output_file.writerow(['Run' , 'Frequency', 'Intensity'])

        run = 1
        for item in values:
            print(item)
            peak_dict = values.get(item)
            for key in peak_dict:
                output_file.writerow([run, key, peak_dict.get(key)])
            run += 1
            