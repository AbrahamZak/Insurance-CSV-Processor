import os
import csv

if __name__ == '__main__':
    # Resultant list of dicts that will contain valid rows
    output_data = []
    # This is the directory containing all csv files to be processed, feel free to change it!
    input_dir = r'./inputs'
    # Loop through all files in our inputs directory
    for filename in os.listdir(input_dir):
        print(filename)
        # Open the file at: input directory / filename
        reader = csv.DictReader(open(input_dir + '/' + filename, 'r'))
        with open(input_dir + '/' + filename, 'r') as f:
            # Count row numbers for error reporting
            row_number = 1
            for row in reader:
                # Increment the row number
                row_number += 1
                # Check for non-nullable values being blank (Provider Name, CampaignID, Cost Per Ad Click, Redirect Link, Address, Zipcode)
                non_null = ['Provider Name', 'CampaignID', 'Cost Per Ad Click', 'Redirect Link', 'Address', 'Zipcode']
                for key in non_null:
                    if row[key] == '':
                        # For any error found print the offending row / column and then continue to the next row
                        print(f"Error: {filename} Row {row_number} does not contain {key}")
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
    output_file = "outputs/output.csv"
    # Columns for output csv
    output_columns = ['Provider Name', 'CampaignID', 'Cost Per Ad Click', 'Redirect Link', 'Phone Number', 'Address', 'Zipcode']
    # Write everything from output list to the output csv
    with open(output_file, 'w') as output:
        writer = csv.DictWriter(output, delimiter=',', lineterminator='\n', fieldnames=output_columns)
        writer.writeheader()
        for data in output_data:
            writer.writerow(data)
