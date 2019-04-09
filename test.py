import argparse
import glob

parser = argparse.ArgumentParser(description='Options.')
# parser.add_argument('--freq', metavar='N', type=float, nargs='+',
#                     help='frequency(s)', required=True)
parser.add_argument('--path')

args = vars(parser.parse_args())

#--path "/Users/rileybusche/research_test/ph_10"
path = args['path']

number_of_trials = glob.glob(path + "/*")

print(len(number_of_trials))
for trial_number in range(1,len(number_of_trials) + 1):
        trial_path = glob.glob(path + "/" + "Trial_" + str(trial_number) + "/*[0-99].txt")
        print(len(trial_path))
        for file_number in range(1, len(trial_path) + 1):
                #file_path = path + "/" + "Trail_" + str(trial_number) + "/" + str(file_number) + ".txt"
                
                print(file_path)

                file_name = open(file_path, "r")
                print(file_name)


# frequencies = []

# for frequency in args['freq']:
#         frequencies.append(frequency)

# print(frequencies)

# print(type(frequencies[1]))
