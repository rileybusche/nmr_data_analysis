# Riley Busche 2022
# This Helper file takes the JSON output from the data analysis and generates a CSV report from it
import csv
import json
import glob
import os.path

def write_report(logging_path:str, reporting_path:str, samples:list):
    files = glob.glob(os.path.join(logging_path, '*.json'))
    print('reporting files: ', files)

    for data_file, ph in zip(files, samples):
        # JSON file to read data from
        # print(data_file)
        with open(data_file, 'r') as json_file:
            
            data = json.load(json_file)

            # CSV to write data to
            print(os.path.join(reporting_path, ph, '.csv'))
            with open(os.path.join(reporting_path, f'{ph}.csv'), 'w') as csv_file:

                #  Loop trough 'Trials'
                for run in list(data.keys()):

                    output_file = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    output_file.writerow([''])
                    output_file.writerow([run])

                    samples = list(data[run].keys())

                    # Grab keys from first sample
                    csv_fields = list(data[run][samples[0]].keys())
                    output_file = csv.DictWriter(csv_file, fieldnames=csv_fields)
                    output_file.writeheader()

                    # Loop through 'Samples'
                    for sample in samples:
                        # print(data[run][sample].keys())
                        # pp.pprint(data[run][sample])
                        output_file.writerow(data[run][sample])
                    