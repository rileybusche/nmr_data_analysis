# Program to sort through NMR text files and pull out the Intensities associated with given Frequencys
# Riley Busche 2019
import matplotlib.pyplot as plt
import functions as fl
import glob
import argparse

# Command Line Arguments
parser = argparse.ArgumentParser(description='Options.')
parser.add_argument('--path', help='Full Path to folder contianing files', required=True)
parser.add_argument('--freq', metavar='N', type=float, nargs='+',
                    help='frequency(s)', required=True)

args = vars(parser.parse_args())

# Path will be parameter from user
# path = "/Users/rileybusche/Research/LVR_DIFFUSION_pH10.10_Trial_1/*.txt"
files = glob.glob(args["path"])

# User inputed
frequencies = []
for frequency in args['freq']:
    frequencies.append(frequency)
# frequencies.append(-.1202)
# frequencies.append(3.1225)

outputs = {}
trial_number = 1

for name in files:

    file_object = open(name, "r")

    # Parsing for LEFT and RIGHT and SIZE of spectrum
    for line in file_object:
        if line.find("LEFT") != -1:
            tokens = line.split()
            left_bound = float(tokens[3])
            right_bound = float(tokens[7])
        elif line.find("SIZE") != -1:
            tokens = line.split()
            size = int(tokens[3])-1
            break

    step_size = (left_bound+abs(right_bound))/size

    # Build list of INTENSITIES
    intensity_list = []

    for line in file_object:
        if line.find("#") == -1:
            # Build List
            intensity_list.append(float(line))

    indices = fl.calculateIndexs(left_bound, right_bound, size, frequencies)

    frequency_intensity_dict = fl.findIntensities(intensity_list, indices, frequencies)

    outputs[trial_number] = frequency_intensity_dict
    trial_number += 1


for inner_dict in outputs:
    peaks_dict = outputs.get(inner_dict)
    print(peaks_dict)

print(len(files))

