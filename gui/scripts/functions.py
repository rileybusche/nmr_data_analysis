# Riley Busche 2019
# File containing functions used in main.py
import os

def calculateIndexs(left_bound:float, right_bound:float, size:int, frequencies:[float]) -> [int]:
    indices = []
    # Calculating y = m x + b equation for finding index of intestity from given frequency
    
    slope = (0 - size)/(left_bound - right_bound)       # Point Slope form to find m
    y_int = 0 - (slope * left_bound)                    # Using line equaiton to find y-int

    # index = slope * (given frequency) + y_int
    # This index (frequency) will be truncated to get a valid whole number for the index
    # Any rounding errors here are taken care of with the searching algorithm
    for frequency in frequencies:
        indices.append(int((slope * frequency) + y_int))
    
    return indices
    
# Reads in the values from Difframp into diffusion_values[]
def read_diffusion_ramp(path:str) -> [float]:
    # print(path)
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

    file_object.close()
    
    return diffusion_values


def build_peak_logging_dirs(experiment_path:str, samples:[str]):
    for sample in samples:
        trials = os.listdir(os.path.join(experiment_path, sample))
        for trials in trials:
            os.makedirs(os.path.join(experiment_path, 'logging', sample, trial))
            os.makedirs(os.path.join(experiment_path, 'graphing', sample, trial))
            