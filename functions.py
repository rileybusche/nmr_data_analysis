# Riley Busche 2019
# File containing functions used in main.py

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