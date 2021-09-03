# Insurance-CSV-Processor
Welcome to my solution for the At-Home Data Engineering assignment! I hope the results are satisfactory and I look forward to hearing from you soon. 
I also wanted to thank you for the opportunity to join the team. Please let me know if you have any questions or concerns about the code.
## How to run
Simply update input directory on line 11 to the directory where the csv files are located (if not a valid directory an error will be printed and the script will terminate).

`
input_dir = r'./inputs'
`

Then, edit the output directory on line 55 to your desired output directory (if not a valid directory it will default to the location of the script).

`
output_dir = 'outputs'
`


## Explanation of Solution
### Thought Process
I decided to use dicts for processing all data, the reason behind this the importance of key value pairs 
and the consideration that input csvs may have differently ordered headers (and may even have extra columns not 
required for output).

I initially started by creating a list that would eventually contain every line from the csvs read that had correct data.

`
output_data = []
`

I then looped through all csvs in the input folder.

`
for filename in os.listdir(input_dir):
`

For each file I converted the data within them to dictionaries (using csv.DictReader) and processed each row.

`
reader = csv.DictReader(open(input_dir + '/' + filename, 'r'))
`

I also made sure to keep track of row number for error reporting purposes.

`
row_number = 1
`

### Error reporting / handling
For all rows I kept track if an error shows up during parsing with a Boolean 'error'.  
I also made sure to continuously keep track of row number, incrementing it at every row

`
row_number += 1
`

First, I checked if the row contained a NULL (blank data) in any column that is non-nullable.

For each offense, I printed the offending row number and column name (and set error to True).

When parsing ends, if error is set to True, the code will stop parsing and continue to the next record.

```
non_null = ['Provider Name', 'CampaignID', 'Cost Per Ad Click', 'Redirect Link', 'Address', 'Zipcode']
            # Set initial state of error to false
            error = False
            for key in non_null:
                if row[key] == '':
                    # For any error found print the offending row number and column name and then continue to the next row
                    print(f"Error: {filename} Row {row_number} does not contain {key}")
                    # If an error is found, set error to true
                    error = True
            # If there was an error found continue to the next row
            if error:
                continue
```

#### Cost Per Ad Click (special check)
A special check is made for Cost Per Ad Click, which needs to be of type float.
So the first thing in processing is to attempt to remove all non-float related characters from Cost Per Ad Click.
This will allow data such as "15.0" to be converted to 15.0 for exporting.

`
row['Cost Per Ad Click'] = re.sub("[^0-9^.]", "", row['Cost Per Ad Click'])
`

Next, the code will try to convert the Cost Per Ad Click to a float. If this fails, we know that even after removing 
extra characters such as quotes, the Cost Per Ad Click is still not a valid float. 
In case a failure an error is printed and the error variable is set to true.

```
            try:
                row['Cost Per Ad Click'] = float(row['Cost Per Ad Click'])
            except ValueError:
                print(f"Error: {filename} Row {row_number} contains a non-float Cost Per Ad Click")
                error = True
```

### Valid data processing
If the row had no offenses (correct data types and no blanks in non-nullable columns) 
I added that row's data to a new dictionary containing only the required columns (as keys).
I then appended that new dictionary to the list I had created initially to store the output data.

```
output_row = {'Provider Name': row['Provider Name'],
                          'CampaignID': row['CampaignID'],
                          'Cost Per Ad Click': row['Cost Per Ad Click'],
                          'Redirect Link': row['Redirect Link'],
                          'Phone Number': row['Phone Number'],
                          'Address': row['Address'],
                          'Zipcode': row['Zipcode']}
output_data.append(output_row)
```


Once all csvs were processed I exported the data to an output csv, this time using csv.DictWriter.

```
    with open(output_file, 'w') as output:
        writer = csv.DictWriter(output, delimiter=',', lineterminator='\n', fieldnames=output_columns)
        writer.writeheader()
        for data in output_data:
            writer.writerow(data)
```

The function closes by returning the output data list

`
return output_data
`

## Expansion Ideas
These are some ideas I've thought of for expanding this project and potentially improving it:
* Processing errors to a separate csv instead of to the console
    * including data such as offending file name, offending columns, row numbers
    * possibly can be used to gather statistics on different providers and improve process permanently
* Allow input directory and output csv + directory to be arguments (kept them as variables for simplicity purposes and testing)
* Scan folder for only specified file types (csv, excel sheets, comma separate texts files, etc.) and ignore all other files


## Testing
A small unit test is included (unittest.py).

The unit test will run the script and compare the results to an already established correct output file (test_output/output.csv).