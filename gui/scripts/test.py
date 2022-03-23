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

# list_1 = [
#     '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/Trial1/',
#     '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/Trial3/',
#     '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/Trial2/'
# ]
import pprint

pp = pprint.PrettyPrinter(indent=4)
dct = {'/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/1.txt': {0.7784: 4542556.84375, 1.1742: 9686084.3125, 3.1393: 1964979.84375, 'ln(0.7784)': 15.32900059293311, 'ln(1.1742)': 16.08620080648104, 'ln(3.1393)': 14.490992545599301, 'G': 0.02}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/10.txt': {0.7784: 3916824.078125, 1.1742: 8252071.359375, 3.1393: 1328324.859375, 'ln(0.7784)': 15.180791699238304, 'ln(1.1742)': 15.925974800660732, 'ln(3.1393)': 14.099429202126526, 'G': 0.02475256}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/11.txt': {0.7784: 3552465.90625, 1.1742: 7578714.34375, 3.1393: 1065715.296875, 'ln(0.7784)': 15.083152541792632, 'ln(1.1742)': 15.840854131590392, 'ln(3.1393)': 13.879156771934502, 'G': 0.030634450000000004}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/12.txt': {0.7784: 3084755.640625, 1.1742: 6624579.171875, 3.1393: 749863.65625, 'ln(0.7784)': 14.941983003310854, 'ln(1.1742)': 15.706297406592586, 'ln(3.1393)': 13.52764667731972, 'G': 0.03791406}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/13.txt': {0.7784: 2499955.671875, 1.1742: 5399487.8125, 3.1393: 438177.3125, 'ln(0.7784)': 14.731783558431228, 'ln(1.1742)': 15.501814657498963, 'ln(3.1393)': 12.990378930499197, 'G': 0.046923490000000005}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/14.txt': {0.7784: 1835304.796875, 1.1742: 3982622.7109375, 3.1393: 198498.671875, 'ln(0.7784)': 14.422721127516661, 'ln(1.1742)': 15.197451132830878, 'ln(3.1393)': 12.198537688280954, 'G': 0.05807382}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/15.txt': {0.7784: 1361636.1484375, 1.1742: 2547102.703125, 3.1393: 56554.3046875, 'ln(0.7784)': 14.124197584948767, 'ln(1.1742)': 14.750467076322959, 'ln(3.1393)': 10.942956600442022, 'G': 0.07187378}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/16.txt': {0.7784: 726815.15234375, 1.1742: 1324306.8203125, 3.1393: 12155.47265625, 'ln(0.7784)': 13.496427463310708, 'ln(1.1742)': 14.096399726028276, 'ln(3.1393)': 9.405534771740799, 'G': 0.088953}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/17.txt': {0.7784: 296243.609375, 1.1742: 503067.931640625, 3.1393: 2528.259765625, 'ln(0.7784)': 12.598937399468847, 'ln(1.1742)': 13.128480492926515, 'ln(3.1393)': 7.835286505377411, 'G': 0.11009070000000001}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/18.txt': {0.7784: 45767.50634765625, 1.1742: 84246.79760742188, 3.1393: 1756.797607421875, 'ln(0.7784)': 10.731329649918692, 'ln(1.1742)': 11.341505836897788, 'ln(3.1393)': 7.471247889418721, 'G': 0.13625130000000002}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/2.txt': {0.7784: 4589972.78125, 1.1742: 9649983.71875, 3.1393: 1991689.03125, 'ln(0.7784)': 15.339384652008253, 'ln(1.1742)': 16.08246678613758, 'ln(3.1393)': 14.50449359613019, 'G': 0.1686284}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/3.txt': {0.7784: 4555257.65625, 1.1742: 9623468.59375, 3.1393: 1977774.125, 'ln(0.7784)': 15.33179265266369, 'ln(1.1742)': 16.07971531833638, 'ln(3.1393)': 14.497482591014275, 'G': 0.2086992}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/4.txt': {0.7784: 4573005.6875, 1.1742: 9614305.0, 3.1393: 1973260.53125, 'ln(0.7784)': 15.335681246352518, 'ln(1.1742)': 16.07876265150117, 'ln(3.1393)': 14.495197824563881, 'G': 0.258292}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/5.txt': {0.7784: 4524023.3125, 1.1742: 9526441.8125, 3.1393: 1932240.0625, 'ln(0.7784)': 15.324912269277373, 'ln(1.1742)': 16.069581838912622, 'ln(3.1393)': 14.47419054198785, 'G': 0.3196693}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/6.txt': {0.7784: 4459620.8125, 1.1742: 9482356.75, 3.1393: 1857825.0625, 'ln(0.7784)': 15.31057430076304, 'ln(1.1742)': 16.064943445655445, 'ln(3.1393)': 14.434917040263338, 'G': 0.39563170000000003}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/7.txt': {0.7784: 4411613.34375, 1.1742: 9308471.4375, 3.1393: 1794062.09375, 'ln(0.7784)': 15.299751018105809, 'ln(1.1742)': 16.046435450757304, 'ln(3.1393)': 14.39999293290268, 'G': 0.48964480000000005}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/8.txt': {0.7784: 4292310.96875, 1.1742: 9052284.28125, 3.1393: 1671030.25, 'ln(0.7784)': 15.272335833218564, 'ln(1.1742)': 16.018527690594837, 'ln(3.1393)': 14.32895091034605, 'G': 0.605998}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial1/9.txt': {0.7784: 4154504.59375, 1.1742: 8724060.625, 3.1393: 1536317.875, 'ln(0.7784)': 15.23970374781529, 'ln(1.1742)': 15.981595355500051, 'ln(3.1393)': 14.244899121148375, 'G': 0.75}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/1.txt': {0.7784: 4558266.625, 1.1742: 9656789.875, 3.1393: 1973659.59375}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/10.txt': {0.7784: 3882736.71875, 1.1742: 8272299.6875, 3.1393: 1313545.890625}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/11.txt': {0.7784: 3538848.46875, 1.1742: 7552275.65625, 3.1393: 1035864.96875}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/12.txt': {0.7784: 3081821.546875, 1.1742: 6584947.203125, 3.1393: 737456.234375}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/13.txt': {0.7784: 2511534.25, 1.1742: 5379492.671875, 3.1393: 437359.0625}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/14.txt': {0.7784: 1824791.703125, 1.1742: 3987060.921875, 3.1393: 194294.1171875}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/15.txt': {0.7784: 1361145.578125, 1.1742: 2556791.5078125, 3.1393: 59041.1484375}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/16.txt': {0.7784: 733221.96875, 1.1742: 1323266.52734375, 3.1393: 10029.59375}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/17.txt': {0.7784: 296632.2216796875, 1.1742: 507538.568359375, 3.1393: 1493.103515625}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/18.txt': {0.7784: 75688.65649414062, 1.1742: 88462.67236328125, 3.1393: 3898.9228515625}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/2.txt': {0.7784: 4604108.25, 1.1742: 9649060.96875, 3.1393: 2004641.8125}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/3.txt': {0.7784: 4563557.0625, 1.1742: 9645985.09375, 3.1393: 1974008.59375}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/4.txt': {0.7784: 4562721.1875, 1.1742: 9638256.0, 3.1393: 1953850.375}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/5.txt': {0.7784: 4496864.0625, 1.1742: 9505230.09375, 3.1393: 1902740.53125}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/6.txt': {0.7784: 4458249.125, 1.1742: 9438725.8125, 3.1393: 1824711.34375}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/7.txt': {0.7784: 4414980.21875, 1.1742: 9275231.75, 3.1393: 1787168.21875}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/8.txt': {0.7784: 4306541.875, 1.1742: 9054587.46875, 3.1393: 1672337.78125}, '/Users/rileybusche/Downloads/LV_Arginine_Riley/ph7.59/Trial2/9.txt': {0.7784: 4150188.21875, 1.1742: 8746571.71875, 3.1393: 1529260.9375}}

pp.pprint(dct)
# # Get first value of dictionary
# first_value = next(iter(dct.items()))[1]
# print(first_value)
# print(list(first_value.keys()))