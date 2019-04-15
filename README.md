Riley Busche 2019

# NMR Data Anylsis Program

The repository (and a more formated view of this README) for this code can be found [here](https://github.com/rileybusche/nmr_data_analysis/).

`main.py` and `functions.py` must be in the same folder for the program to function.

# Program Arguements
The program currently has 3 user arguements, all of which are required inorder for the program to run.
    --path 
        This the path to the folder containing the file structure to be analyized. The required file structure is detailed below.
        To prevent possible errors due to naming of folders, include the path in side quotation marks.
        
        Example path:
            --path "/Users/rileybusche/Research/ph_10"
    
    --freq
        This command is used to specify the frequencies to be analyzed. Separate each new frequency with a space.
        These values are found by peaking the peaks of interest in Topspin 3.2.

        Example freq:
            --freq -0.1202 3.1225 5.6074
    
    --output
        This command is used to name the output files from the program. This program produces CSV files containing a table of 
        the frequencies and associated intensities, the natural log of the intensities, and the %G values for each trial.
        When specifying a file name, DO NOT include the file extension in the name.

        Example output:
            --output ph10

# Full Command Example:
Navigate to the folder containing `main.py` in terminal (OSx/Unix) or PowerShell/CommandPrompt (Windows) and type:
    `python main.py --path "/Users/rileybusche/Research/ph_10" --freq -0.1202 3.1225 --output test`

# FILE STRUCTURE