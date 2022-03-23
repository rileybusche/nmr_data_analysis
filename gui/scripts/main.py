# Riley Busche 2019
# Program to sort through NMR text files and pull out the Intensities associated with given Frequencys
import functions as fl
import build_csv as bcsv
import glob
import os.path
import json
import sys

outputs = {}

data_path = sys.argv[1].strip()
samples = []
data = {}
experiment_path = ''
try:
    if os.path.exists(data_path):
        data_file = open(data_path)
        data = json.load(data_file)
        # Gets the path to experiment files from data.json file
        experiment_path = '/'.join(data['SamplesFilePath'].split('/')[:-1]) + '/'
        samples = list(data['Samples'].keys())
        print(samples)
        data_file.close()
except:
    print(f'Failed to get Data Files from: {data_path}', sys.exc_info()[0])

print(experiment_path)

diffusion_values = fl.read_diffusion_ramp(experiment_path + 'Difframp')

# Loop through PH array
for ph in samples:

    # Path from user arugument
    try:
        # /Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/*/ <-
        trials = glob.glob(experiment_path + ph + "/*/")
        trails = sorted(trials)
        print(trails)
    except:
        print("ERROR : Could not access files. Check path to folder and try again.")

    trial_number = 1

    file_name_output = ph
    
    frequencies_string = data['Samples'][ph].split()
    frequencies = [float(freq) for freq in frequencies_string]

    # Runs for the number of Trials 
    for trail in trails:
        print(trail)

        # Getting number of files to be read in the folder
        files = glob.glob(trail + "*[0-99].txt")
        files = sorted(files)
        # print(trial_path)

        # looping through all files in the trial
        for file_number in files:

            try:
                file_object = open(file_number, "r")
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
        bcsv.create_rawdata_csv(file_name_output, outputs, trial_number)
        bcsv.create_table_csv(file_name_output, outputs, trial_number, diffusion_values)
        trial_number += 1


print("Complete.")