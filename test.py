import argparse
import glob
import math
import csv
import functions as fl

path = "/Users/rileybusche/Research/ph_10"

diffusion_values = fl.read_diffusion_ramp(path)

g_list = []

for value in diffusion_values:

        pos = value.find("e")
        number = float(value[0:pos])
        power = int(value[pos+1:len(value)])

        g_list.append(number * pow(10, power))

for x in g_list:
        print(x)














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

# values_dict = {
#         1: {'ln(-0.1202)': 14.762539602494666, 'ln(3.1225)': 15.379721057088267, 'G': ' x ', -0.1202: 2578039.03125, 3.1225: 4778900.5}, 
#         2: {'ln(-0.1202)': 14.776404797417147, 'ln(3.1225)': 15.380715874717813, 'G': ' x ', -0.1202: 2614033.0, 3.1225: 4783657.0}, 
#         3: {'ln(-0.1202)': 14.786459867801812, 'ln(3.1225)': 15.37083259759741, 'G': ' x ', -0.1202: 2640449.875, 3.1225: 4736611.65625}, 
#         4: {'ln(-0.1202)': 14.782279266945157, 'ln(3.1225)': 15.364222830979834, 'G': ' x ', -0.1202: 2629434.25, 3.1225: 4705407.0}, 
#         5: {'ln(-0.1202)': 14.772324495725806, 'ln(3.1225)': 15.325100841926028, 'G': ' x ', -0.1202: 2603388.6875, 3.1225: 4524876.5}, 
#         6: {'ln(-0.1202)': 14.757952082669492, 'ln(3.1225)': 15.282805951072081, 'G': ' x ', -0.1202: 2566239.3125, 3.1225: 4337488.0625}, 
#         7: {'ln(-0.1202)': 14.741581111106159, 'ln(3.1225)': 15.247325278979712, 'G': ' x ', -0.1202: 2524569.5, 3.1225: 4186289.25}, 
#         8: {'ln(-0.1202)': 14.726630896360987, 'ln(3.1225)': 15.1548974452125, 'G': ' x ', -0.1202: 2487107.375, 3.1225: 3816702.71875}, 
#         9: {'ln(-0.1202)': 14.703911947522847, 'ln(3.1225)': 15.032852082648134, 'G': ' x ', -0.1202: 2431239.9375, 3.1225: 3378194.9375}, 
#         10: {'ln(-0.1202)': 14.654723249858202, 'ln(3.1225)': 14.842485801594131, 'G': ' x ', -0.1202: 2314544.0, 3.1225: 2792606.09375}, 
#         11: {'ln(-0.1202)': 14.567331546976314, 'ln(3.1225)': 14.524859466337077, 'G': ' x ', -0.1202: 2120858.5625, 3.1225: 2032667.375}, 
#         12: {'ln(-0.1202)': 14.440536758035178, 'ln(3.1225)': 14.0413702547135, 'G': ' x ', -0.1202: 1868294.90625, 3.1225: 1253399.796875}, 
#         13: {'ln(-0.1202)': 14.259611943652798, 'ln(3.1225)': 13.317482692428143, 'G': ' x ', -0.1202: 1559088.546875, 3.1225: 607728.0}, 
#         14: {'ln(-0.1202)': 13.984801931898502, 'ln(3.1225)': 12.191598357543732, 'G': ' x ', -0.1202: 1184465.2109375, 3.1225: 197125.9921875}, 
#         15: {'ln(-0.1202)': 13.567133680273384, 'ln(3.1225)': 10.554668081427069, 'G': ' x ', -0.1202: 780065.8984375, 3.1225: 38356.0703125}, 
#         16: {'ln(-0.1202)': 12.90513246817061, 'ln(3.1225)': 7.576995914872479, 'G': ' x ', -0.1202: 402372.0625, 3.1225: 1952.75390625}, 
#         17: {'ln(-0.1202)': 11.892306432540577, 'ln(3.1225)': 6.610414734124034, 'G': ' x ', -0.1202: 146137.966796875, 3.1225: 742.791015625}, 
#         18: {'ln(-0.1202)': 10.437470307099252, 'ln(3.1225)': 7.711391379573824, 'G': ' x ', -0.1202: 34114.24462890625, 3.1225: 2233.64794921875}
# }

# trial_number = 1

# list_of_dicts = []



# try:
#         print(values_dict.pop(1))
# except:
#         print("ERROR : No data exists in dictionary")

# for number in values_dict:
#         list_of_dicts.append(values_dict[number])

# with open("t_test.csv", mode='w') as output_file:
#         # Build Fieldnames from dictionary keys
#         writer = csv.DictWriter(output_file, fieldnames=[-0.1202, 3.1225, 'ln(3.1225)', 'ln(-0.1202)', 'G'])
#         writer.writeheader()
#         for x in list_of_dicts:
#                 writer.writerow(x)


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