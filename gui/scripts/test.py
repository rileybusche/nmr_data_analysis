import os


# print(os.listdir('/Users/rileybusche/Development/nmr_data_analysis/SULVdiamine/ph8.50'))

path = '/Users/rileybusche/Development/nmr_data_analysis/SULVdiamine/ph8.50/Trial1/18.txt'
logging_path = '/Users/rileybusche/Development/nmr_data_analysis/SULVdiamine/graphing/'
trial_number = 1

print(path.split(os.sep)[-3:-1])

print(os.path.join(logging_path, os.sep.join(path.split(os.sep)[-3:-1]), f'{trial_number}.json'))