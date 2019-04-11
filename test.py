import argparse
import glob
import math

# parser = argparse.ArgumentParser(description='Options.')
# # parser.add_argument('--freq', metavar='N', type=float, nargs='+',
# #                     help='frequency(s)', required=True)
# parser.add_argument('--path')

# args = vars(parser.parse_args())

# #--path "/Users/rileybusche/research_test/ph_10"
# path = args['path']

# number_of_trials = glob.glob(path + "/*")

# print(number_of_trials)

# for trial_path in number_of_trials:
#         path = trial_path
#         print(trial_path)

# print(len(number_of_trials))
# for trial_number in range(1,len(number_of_trials) + 1):
#         trial_path = glob.glob(path + "/" + "Trial_" + str(trial_number) + "/*[0-99].txt")
#         print(len(trial_path))
#         for file_number in range(1, len(trial_path) + 1):
#                 #file_path = path + "/" + "Trail_" + str(trial_number) + "/" + str(file_number) + ".txt"
                
#                 print(file_path)

#                 file_name = open(file_path, "r")
#                 print(file_name)


# frequencies = []

# for frequency in args['freq']:
#         frequencies.append(frequency)

# print(frequencies)

# print(type(frequencies[1]))

d = {1 : {-0.1202: 2578039.03125, 3.1225: 4778900.5}, 2 : {-0.1202: 6078039.03125, 3.1225: 47998900.5}}

key_list = []
value_list = []

for number in d:
        values = d[number]
        
        for freq in values:
                key_list.append("ln(" + str(values[freq]) + ")")
                value_list.append(math.log(values[freq], math.e))

key_list.reverse()
value_list.reverse()

for number in d:
        values = d[number]
        for index in range(len(values)):
                values[key_list.pop()] = value_list.pop()
        # Add %G here
        values["G"] = " "

for x in d:
        print(d[x])