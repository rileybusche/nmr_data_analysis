import sys
import os.path

print("Python Script Start")

args = sys.argv[1].split(',')

path = args[0].split('\\')
frequencies = args[1:]

path_separator = '/'

path = path_separator.join(path)

try:
    print(path, frequencies)
    print('Does file exist: ', os.path.exists('test'))
except:
    print('Python Script Failed with ', sys.exc_info()[0])