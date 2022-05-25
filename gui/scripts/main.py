# Riley Busche 2019
# Program to sort through NMR text files and pull out the Intensities associated with given Frequencys
import functions as fl
import code_logging
import generate_report as report
import glob
import os.path
import json
import sys
import math

print("Python script Starting")

outputs = {}

data_path = os.path.join(sys.argv[1].strip())
# print('data_path: ', data_path)
samples = []
data = {}
experiment_path = ''
logging_path = ''

try:
    if os.path.exists(data_path):
        # print('File Exists!')
        data_file = open(data_path)
        data = json.load(data_file)
        # Gets the path to experiment files from data.json file
        # /Users/rileybusche/Downloads/LV_Arginine_Riley
        experiment_path = os.path.join('/'.join(data['SamplesFilePath'].split('/')[:-1]),)
        # print('experiment_path: ', experiment_path)
        samples = list(data['Samples'].keys())
        # print('samples: ', samples)
        data_file.close()
except Exception as e:
    print(f'Failed to get Data Files from: {data_path}', sys.exc_info()[0], e)

difframp_file_path = os.path.join(experiment_path, 'Difframp')
# print('difframp_file_path', difframp_file_path)
diffusion_values = fl.read_diffusion_ramp(difframp_file_path)

# Loop through PH array
for ph in samples:

    # Path from user arugument
    try:
        # /Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/*/ <-
        trials = glob.glob(os.path.join(experiment_path, ph, '*'))
        trails = sorted(trials)
        # print('trials: ',trails)
    except Exception as e:
        print(f"ERROR : Could not access files. Check path to folder and try again: {ph_path}", sys.exc_info()[0], e)

    trial_number = 1

    file_name_output = ph
    
    frequencies_string = data['Samples'][ph].split()
    frequencies = [float(freq) for freq in frequencies_string]

    json_logging_obj = {}

    # Runs for the number of Trials 
    for trail in trails:
        # print(trail)

        json_logging_obj[f'Trial{trial_number}'] = {}
        # Getting number of files to be read in the folder
        files = glob.glob(os.path.join(trail, '*[0-99].txt'))
        files = sorted(files)
        # print('files: ', files)

        # looping through all files in the trial
        run_number = 1
        for run_number_file in files:
            try:
                file_object = open(run_number_file, "r")
            except Exception as e:
                print("Error : Could not access files. Check if folder and naming structure is correct and try agian.", sys.exc_info()[0], e)

            # Parsing for LEFT and RIGHT and SIZE of spectrum
            # Redo this with Regex...
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
            frequency_intensity_dict = {'Run' : run_number}
            frequency_intensity_dict.update(fl.findIntensities(intensity_list, indices, frequencies))
            # Adding in ln(frequency)
            for frequency in list(frequency_intensity_dict.keys()):
                if frequency != 'Run':
                    frequency_intensity_dict[f'ln({frequency})'] = math.log(frequency_intensity_dict[frequency], math.e)
            # Run numbers start at 1-18
            frequency_intensity_dict['G'] = diffusion_values[run_number-1]

            json_logging_obj[f'Trial{trial_number}'][run_number] = frequency_intensity_dict
            # print(frequency_intensity_dict)

            logging_path = os.path.join(experiment_path, 'logging')
            # If logging dir does not exist, create it
            if not os.path.exists(logging_path):
                os.makedirs(logging_path) 
            logging.write_to_file(file_path=os.path.join(logging_path, f'{ph}.json'), data_object=json_logging_obj)
            # outputs[file_number] = frequency_intensity_dict
            run_number += 1

        trial_number += 1

reporting_path = os.path.join(experiment_path, 'reporting')
if not os.path.exists(reporting_path):
    os.makedirs(reporting_path)
report.write_report(logging_path=logging_path, reporting_path=reporting_path, samples=samples)
print("Complete.")