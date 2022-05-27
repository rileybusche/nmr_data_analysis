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
import graphing

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
        # Builds folders in the logging dir for the input peak and actual peak raw data
        fl.build_peak_logging_dirs(experiment_path=experiment_path, samples=samples)
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
            # Path to output raw data
            logging_path = os.path.join(experiment_path, 'logging')
            graphing_path = os.path.join(experiment_path, 'graphing')

            ##################################
            peak_data = graphing.build_graph(
                file_path=run_number_file, 
                frequencies=frequencies, 
                graph_output_path=graphing_path, 
                logging_path=logging_path, 
                run_number=run_number
            )
            ##################################

            # Builds Dict {frequency : Intensity}
            frequency_intensity_dict = {'Run' : run_number}
            frequency_intensity_dict.update(peak_data)
            # Adding in ln(frequency)
            for frequency in list(frequency_intensity_dict.keys()):
                if frequency != 'Run':
                    frequency_intensity_dict[f'ln({frequency})'] = math.log(frequency_intensity_dict[frequency], math.e)
            # Run numbers start at 1-18
            frequency_intensity_dict['G'] = diffusion_values[run_number-1]

            json_logging_obj[f'Trial{trial_number}'][run_number] = frequency_intensity_dict
            # print(frequency_intensity_dict)

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