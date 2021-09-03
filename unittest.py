import csv
from main import csv_processor


if __name__ == "__main__":
    # Load in the data from the established correct output file
    correct_data = []
    reader = csv.DictReader(open('test_output/output.csv', 'r'))
    for row in reader:
        # Convert correct Cost Per Ad Click to floats for comparison purposes with return data from function
        row['Cost Per Ad Click'] = float(row['Cost Per Ad Click'])
        correct_data.append(row)
    # Assert the data from the correct csv and the data returned from the csv_processor function are equal
    assert(correct_data == csv_processor())
    print("Test has passed")
