# Riley Busche 2019
# File containing functions used to generate csv
import csv
import math

# Creates CSV of raw data
def create_rawdata_csv(file_name, values, trial_number):
    file_name += "_raw_data.csv"
    if trial_number == 1:
        mode = 'w'
    else:
        mode = 'a'
    print(file_name)
    with open(file_name, mode=mode) as output_file:
        
        output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        output_file.writerow([''])
        output_file.writerow(['Trial', trial_number])
        output_file.writerow([''])
        
        # Looping through runs and printing out raw data
        run = 1
        for item in values:
            output_file.writerow(['Run', run])
            output_file.writerow(['Frequency', 'Intensity'])
            peak_dict = values.get(item)
            for key in peak_dict:
                output_file.writerow([key, peak_dict.get(key)])
            run += 1
            output_file.writerow([''])

# Creates CSV with table of data, %G and ln(freq)
def create_table_csv(file_name, values, trial_number, diffusion_values):
    file_name += ".csv"
    if trial_number == 1:
        mode = 'w'
    else:
        mode = 'a'
    
    # Build Dictionary for Table
    table_dict = build_table_dictionary(values, diffusion_values)
    # Build Frequencies
    field_names = build_field_names(table_dict)
    
    list_dicts_in_table = []

    for number in table_dict:
        list_dicts_in_table.append(table_dict[number])

    with open(file_name, mode=mode) as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([''])
        writer.writerow(['Trail',trial_number])
        writer.writerow([''])

        # Build Fieldnames from dictionary keys
        writer = csv.DictWriter(output_file, fieldnames=field_names)
        writer.writeheader()
        # Prints out table
        
        for item in list_dicts_in_table:
            writer.writerow(item)

# Takes in values, adds ln() key and associated value to the dictionary
def build_table_dictionary(d, diffusion_values):
    key_list = []
    value_list = []

    for number in d:
            values = d[number]
            
            for freq in values:
                    key_list.append("ln(" + str(freq) + ")")
                    value_list.append(math.log(values[freq], math.e))
    key_list.reverse()
    value_list.reverse()
    
    for diff_number, number in enumerate(d):
            values = d[number]
            for _ in range(len(values)):
                    values[key_list.pop()] = value_list.pop()
            values["G"] = diffusion_values[diff_number]
    return d

# Builds a list of the keys in dictionary to use in csv writer
def build_field_names(table_dict):
    field_names = []
    copy_dict = table_dict.copy()
    try:
        dict_entry_for_names = copy_dict.pop(1)
    except:
        print("ERROR : No data exists in dicitonary entry") 

    # Pulls key from dictionary and appends key to field_names
    for key in dict_entry_for_names:
        field_names.append(key)

    return field_names

# Reads in the values from Difframp into diffusion_values[]
def read_diffusion_ramp(path):
    path += "/Difframp"
    try:
        file_object = open(path, "r")
    except:
        print("ERROR : Could not access 'Difframp' file. Check that it is in the proper folder and try again.")

    diffusion_values = []
    for line in file_object:
            if line.find("#") == -1:
                # Converting values from Scientific to Standard for proper input into CSV
                pos = line.find("e")
                number = float(line[0 : pos])
                power = int(line[pos + 1 : len(line)])

                diffusion_values.append(number * pow(10, power))

    return diffusion_values