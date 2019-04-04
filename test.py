import argparse
import glob

# parser = argparse.ArgumentParser(description='Options.')
# parser.add_argument('--freq', metavar='N', type=float, nargs='+',
#                     help='frequency(s)', required=True)
# parser.add_argument('--path')

# args = vars(parser.parse_args())

# folder = glob.glob(args['path'] + '/*')

# for trials in folder:
#         print(trials)

# frequencies = []

# for frequency in args['freq']:
#         frequencies.append(frequency)

# print(frequencies)

# print(type(frequencies[1]))

d1= {1: {-0.1202: 2578039.03125, 3.1225: 4778900.5} }

for item in d1:
        print(item)
        peak_dict = d1.get(item)
        value_list  = []
        for key in peak_dict:
                value = peak_dict.get(key)
                value_list.append(value)

print(value_list)