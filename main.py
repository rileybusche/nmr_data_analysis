# Program to sort through NMR text files and pull out the Intensities associated with given Frequencys
# Riley Busche 2019
import matplotlib.pyplot as plt
import functions as fl
import glob
import argparse

# Command Line Arguments
parser = argparse.ArgumentParser(description='Options.')
parser.add_argument('--path', help='Full Path to folder contianing files.', required=True)
parser.add_argument('--freq', metavar='N', type=float, nargs='+',
                    help='frequency(s)', required=True)
parser.add_argument('--output', help='Output CSV filename.', required=True)

args = vars(parser.parse_args())

# Path is a user parameter
try:
    trials = glob.glob(args["path"] + "/*")
except:
    print("ERROR : Could not access files. Check path to folder and try again.")

# User inputed
frequencies = []
for frequency in args['freq']:
    frequencies.append(frequency)

outputs = {}

trial_number = 1

for trial_path in trials:

    files = glob.glob(trial_path + "/*[0-99].txt")
    print(trial_path)
    for file_number in range(1, len(files) + 1):
        try:
            file_object = open(trial_path + "/" + str(file_number) + ".txt", "r")
        except:
            print("Error : Could not access files. Check if folder and naming structure is correct and try agian.")

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

        # Array of indecies for input frequencies
        indices = fl.calculateIndexs(left_bound, right_bound, size, frequencies)

        # Builds Dict {frequency : Intensity}
        frequency_intensity_dict = fl.findIntensities(intensity_list, indices, frequencies)

        outputs[file_number] = frequency_intensity_dict

    fl.create_rawdata_csv(args['output'], outputs, trial_number)
    fl.create_table_csv(args['output'], outputs, trial_number)
    trial_number += 1

