import os
import csv
import re
import sys


def csv_processor():
    # Resultant list of dicts that will contain valid rows
    output_data = []
    # This is the directory containing all csv files to be processed, feel free to change it!
    input_dir = r'./inputs'
    if not os.path.isdir(input_dir):
        print('Specified input directory does not exist!')
        sys.exit()
    # Loop through all files in our inputs directory
    for filename in os.listdir(input_dir):
        # Open the file at: input directory / filename
        reader = csv.DictReader(open(input_dir + '/' + filename, 'r'))
        # Count row numbers for error reporting
        row_number = 1
        for row in reader:
            # Increment the row number
            row_number += 1
            # Check for non-nullable values being blank (Provider Name, CampaignID, Cost Per Ad Click, Redirect Link, Address, Zipcode)
            non_null = ['Provider Name', 'CampaignID', 'Cost Per Ad Click', 'Redirect Link', 'Address', 'Zipcode']
            # Set initial state of error to false
            error = False
            for key in non_null:
                if row[key] == '':
                    # For any error found print the offending row number and column name and set error to True
                    print(f"Error: {filename} Row {row_number} does not contain {key}")
                    # If an error is found, set error to true
                    error = True
            # Remove all non-float related characters from Cost Per Ad Click
            row['Cost Per Ad Click'] = re.sub("[^0-9^.]", "", row['Cost Per Ad Click'])
            # Try to convert Cost Per Ad Click to a float, if the value is not a valid float, report the error and set error to True
            try:
                row['Cost Per Ad Click'] = float(row['Cost Per Ad Click'])
            except ValueError:
                print(f"Error: {filename} Row {row_number} contains a non-float Cost Per Ad Click")
                error = True
            # If there was an error found continue to the next row
            if error:
                continue
            # If the row is cleared, create a dict from the required output data and append that dict to the output list
            output_row = {'Provider Name': row['Provider Name'],
                          'CampaignID': row['CampaignID'],
                          'Cost Per Ad Click': row['Cost Per Ad Click'],
                          'Redirect Link': row['Redirect Link'],
                          'Phone Number': row['Phone Number'],
                          'Address': row['Address'],
                          'Zipcode': row['Zipcode']}
            output_data.append(output_row)
    # This is the directory / filename for the output csv, feel free to change it!
    output_dir = 'outputs'
    if not os.path.isdir(output_dir):
        print('Specified output directory does not exist! Outputting to script directory.')
        output_dir = '.'
    output_file = f"{output_dir}/output.csv"
    # Columns for output csv
    output_columns = ['Provider Name', 'CampaignID', 'Cost Per Ad Click', 'Redirect Link', 'Phone Number', 'Address', 'Zipcode']
    # Write everything from output list to the output csv
    with open(output_file, 'w') as output:
        writer = csv.DictWriter(output, delimiter=',', lineterminator='\n', fieldnames=output_columns)
        writer.writeheader()
        for data in output_data:
            writer.writerow(data)
    return output_data


if __name__ == '__main__':
    csv_processor()
