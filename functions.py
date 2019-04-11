# Riley Busche 2019
# File containing functions used in main.py
import csv
import math

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

# Looks for peak closest to given intensity and return that intensity - "Search Algorithm"
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

def create_rawdata_csv(values, trial_number):
    file_name = "raw_data" + str(trial_number) + ".csv"
    with open(file_name, mode='w') as output_file:
        
        output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        output_file.writerow([''])
        output_file.writerow(['Trial', trial_number])
        output_file.writerow([''])
        
        run = 1
        for item in values:
            output_file.writerow(['Run', run])
            output_file.writerow(['Frequency', 'Intensity'])
            peak_dict = values.get(item)
            for key in peak_dict:
                output_file.writerow([key, peak_dict.get(key)])
            run += 1
            output_file.writerow([''])
# Creates CSV file
def create_table_csv(file_name, values, trial_number):
    file_name += str(trial_number) + ".csv"

    # Build Dictionary for Table
    table_dict = build_table_dictionary(values)
    # Build Frequencies
    field_names = build_field_names(table_dict)

    with open(file_name, mode='w') as output_file:
        # Build Fieldnames from dictionary keys
        writer = csv.DictWriter(output_file, fieldnames=field_names)
        writer.writeheader()
        counter = 1
        # Prints out table
        print(len(table_dict))
        for kvp in table_dict:
            #freq_inten in form of {-0.1202: 2578039.03125, 3.1225: 4778900.5}
            freq_inten = table_dict[kvp]
            writer.writerow(freq_inten)
            counter += 1
        
        # output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # output_file.writerow([''])
        # output_file.writerow([''])
        # output_file.writerow([''])
        # output_file.writerow(['Trial', trial_number])
        # output_file.writerow([''])
        # print(values)
        # run = 1
        # for item in values:
        #     output_file.writerow(['Run', run])
        #     output_file.writerow(['Frequency', 'Intensity'])
        #     peak_dict = values.get(item)
        #     for key in peak_dict:
        #         output_file.writerow([key, peak_dict.get(key)])
        #     run += 1
        #     output_file.writerow([''])

# Takes in values, adds ln() key and associated value to the dictionary
def build_table_dictionary(d):
    key_list = []
    value_list = []

    for number in d:
            values = d[number]
            
            for freq in values:
                    key_list.append("ln(" + str(freq) + ")")
                    value_list.append(math.log(values[freq], math.e))
    key_list.reverse()
    value_list.reverse()

    for number in d:
            values = d[number]
            for index in range(len(values)):
                    values[key_list.pop()] = value_list.pop()
            values["G"] = " "
    return d

def build_field_names(table_dict):
    field_names = []
    for key in table_dict:
        values = table_dict[key]
        for field_key in values:
            field_names.append(field_key)
    return field_names