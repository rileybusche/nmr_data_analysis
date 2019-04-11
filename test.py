import argparse
import glob
import math
import csv
import functions as fl

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

values_dict = {
        1: {-0.1202: 2578039.03125, 3.1225: 4778900.5}, 
        2: {-0.1202: 2614033.0, 3.1225: 4783657.0},
        3: {-0.1202: 2640449.875, 3.1225: 4736611.65625}, 
        4: {-0.1202: 2629434.25, 3.1225: 4705407.0}, 
        5: {-0.1202: 2603388.6875, 3.1225: 4524876.5}, 
        6: {-0.1202: 2566239.3125, 3.1225: 4337488.0625}, 
        7: {-0.1202: 2524569.5, 3.1225: 4186289.25}, 
        8: {-0.1202: 2487107.375, 3.1225: 3816702.71875}, 
        9: {-0.1202: 2431239.9375, 3.1225: 3378194.9375}, 
        10: {-0.1202: 2314544.0, 3.1225: 2792606.09375}, 
        11: {-0.1202: 2120858.5625, 3.1225: 2032667.375}, 
        12: {-0.1202: 1868294.90625, 3.1225: 1253399.796875}, 
        13: {-0.1202: 1559088.546875, 3.1225: 607728.0}, 
        14: {-0.1202: 1184465.2109375, 3.1225: 197125.9921875}, 
        15: {-0.1202: 780065.8984375, 3.1225: 38356.0703125}, 
        16: {-0.1202: 402372.0625, 3.1225: 1952.75390625}, 
        17: {-0.1202: 146137.966796875, 3.1225: 742.791015625}, 
        18: {-0.1202: 34114.24462890625, 3.1225: 2233.64794921875}
}
trial_number = 1

with open("t_test.csv", mode='w') as output_file:
        # Build Fieldnames from dictionary keys
        writer = csv.DictWriter(output_file, fieldnames=[-0.1202, 3.1225])
        writer.writeheader()
        writer.writerow({-0.1202: 2578039.03125, 3.1225: 4778900.5})
        writer.writerow({-0.1202: 2614033.0, 3.1225: 4783657.0})
        writer.writerow({-0.1202: 2640449.875, 3.1225: 4736611.65625})
print(values_dict[1])

#fl.create_csv("t_test", values_dict, 1)


# key_list = []
# value_list = []

# for number in d:
#         values = d[number]
        
#         for freq in values:
#                 key_list.append("ln(" + str(values[freq]) + ")")
#                 value_list.append(math.log(values[freq], math.e))

# key_list.reverse()
# value_list.reverse()

# for number in d:
#         values = d[number]
#         for index in range(len(values)):
#                 values[key_list.pop()] = value_list.pop()
#         # Add %G here
#         values["G"] = " "

# for x in d:
#         print(d[x])