import os
import csv

if __name__ == '__main__':
    # This is the directory containing all csv files to be processed, feel free to change it!
    input_dir = r'./inputs'
    # Loop through all files in our inputs directory
    for filename in os.listdir(input_dir):
        print(filename)
        # Open the file at: input directory / filename
        reader = csv.DictReader(open(input_dir + '/' + filename, 'r'))
        with open(input_dir + '/' + filename, 'r') as f:
            for row in reader:
                print(row)
