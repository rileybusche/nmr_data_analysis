# import sys
# import os.path
# import json
# import glob

# print("Python Script Start")

# # print(sys.argv[0])
# # path = sys.argv[0].split('\\')

# # path_separator = '/'

# # # path = path_separator.join(path)
# # path = sys.argv[1].strip()
# path = '/Users/rileybusche/Development/nmr_data_analysis/gui/public/data.json'

# try:
#     if os.path.exists(path):
#         data_file = open(path)
#         data = json.load(data_file)
#         print('/'.join(data['SamplesFilePath'].split('/')[:-1]))
#         print(list(data['Samples'].keys()))
#         data_file.close()
# except:
#     print('Python Script Failed with ', sys.exc_info()[0])
# path = '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/'
# trials = glob.glob(path + "*/")

# for trial in trials:
#     print(trial)

# freq_string = '  1.231   -123.123'
# freq_string_list = freq_string.split()

# frequencies = [float(freq) for freq in freq_string_list]

# print(frequencies)

list_1 = [
    '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/Trial1/',
    '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/Trial3/',
    '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/Trial2/'
]

print(sorted(list_1))