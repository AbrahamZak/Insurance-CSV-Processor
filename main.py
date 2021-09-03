import os

if __name__ == '__main__':
    # This is the directory containing all csv files to be processed, feel free to change it!
    input_dir = r'./inputs'
    # Loop through all files in our inputs directory
    for filename in os.listdir(input_dir):
        print(filename)
        # Open the file at: input directory / filename
        with open(input_dir + '/' + filename, 'r') as f:
            # Skip the header
            next(f)
            # Read all lines
            lines = f.readlines()
        # Now we can process each line from the file
        for line in lines:
            # Strip the right newline character and then split the line by comma
            line = line.rstrip()
            data = line.split(',')
            print(data)

