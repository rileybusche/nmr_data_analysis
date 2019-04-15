# Riley Busche 2019
# Program to sort through NMR text files and pull out the Intensities associated with given Frequencys
import matplotlib.pyplot as plt
import functions as fl
import build_csv as bcsv
import glob
import argparse

# Command Line Arguments
parser = argparse.ArgumentParser(description='Options.')
parser.add_argument('--path', help='Full Path to folder contianing files.', required=True)
parser.add_argument('--freq', metavar='N', type=float, nargs='+',
                    help='frequency(s)', required=True)
parser.add_argument('--output', help='Output CSV filename.', required=True)

args = vars(parser.parse_args())

# Path from user arugument
try:
    trials = glob.glob(args["path"] + "/*/")
except:
    print("ERROR : Could not access files. Check path to folder and try again.")

# User inputed
frequencies = []
for frequency in args['freq']:
    frequencies.append(frequency)

# Storing Diffusion Gradient values into list
diffusion_values = fl.read_diffusion_ramp(args["path"])

outputs = {}

trial_number = 1

# Runs for the number of Trials 
for _ in range(len(trials)):
    trial_path = args["path"] + "/Trial_" + str(trial_number)
    # Getting number of files to be read in the folder
    files = glob.glob(trial_path + "/*[0-99].txt")
    print(trial_path)

    # looping through all files in the trial
    for file_number in range(1, len(files) + 1):
        file_name = trial_path + "/" + str(file_number) + ".txt"

        try:
            file_object = open(file_name, "r")
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
        # print(frequency_intensity_dict)
        outputs[file_number] = frequency_intensity_dict

    # Write output data to CSV
    bcsv.create_rawdata_csv(args['output'], outputs, trial_number)
    bcsv.create_table_csv(args['output'], outputs, trial_number, diffusion_values)
    trial_number += 1

print("Complete.")