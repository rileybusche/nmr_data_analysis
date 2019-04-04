import argparse
import glob

parser = argparse.ArgumentParser(description='Options.')
parser.add_argument('--freq', metavar='N', type=float, nargs='+',
                    help='frequency(s)', required=True)
parser.add_argument('--path')

args = vars(parser.parse_args())

folder = glob.glob(args['path'] + '/*')

for trials in folder:
        print(trials)

frequencies = []

for frequency in args['freq']:
        frequencies.append(frequency)

print(frequencies)
