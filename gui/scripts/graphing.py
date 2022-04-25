import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4,5,6,7,8,9]
# y = x

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

y_values = []
with open('/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/ph7.59/Trial1/1.txt') as data_file:
    for line in data_file:
        if 'LEFT' in line:
            print(line)
        if '#' not in line:
            y_values.append(float(line.strip()))

print(len(y_values))

fig, ax = plt.subplots()
ax.plot(list(range(len(y_values))), y_values)
plt.show()