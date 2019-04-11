This is currently a "To-do/Notes" Readme. Will transition this to a formal Readme
in the future.

Loop through all files using glob now

write search algorithm to find highest values near peaks.
    -   maybe re construct a graph from intensity values? 

Use regex to differentiate between numbered files and Diffusion gradient file?

--path "/Users/rileybusche/Research/LVR_DIFFUSION_pH10.10_Trial_1/*.txt"

glob.glob('./[0-9].txt')
path = args['path'] + '/*[0-99].txt'

/Users/rileybusche/research_test/ph_10

OUTPUTS STRUCTURE:

{1: {-0.1202: 2578039.03125, 3.1225: 4778900.5} }

for inner_dict in outputs:
    inner_dict = 1, 2, 3, ...

freq-intensity dict:
{-0.1202: 2578039.03125, 3.1225: 4778900.5, 4.09: 23206.625}

python main.py --path "/Users/rileybusche/Research/LVR_DIFFUSION_pH10.10_Trial_1" --freq -0.1202 3.1225



/Users/rileybusche/Research/ph10