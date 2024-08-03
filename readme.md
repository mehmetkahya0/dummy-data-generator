# Python Dummy Data Generator

This Python script generates dummy data and writes it to a file. It can also read the data back from the file and display information about the size of the data and the file. It includes functionality to generate random strings, numbers, dates, and boolean values.

## Features

- Generate random strings, numbers, dates, and boolean values
- Write generated data to a JSON file
- Read data from a JSON file
- Calculate and display the size of the data and the file
- Calculate and display the runtime of the script

## Requirements

- Python 3.x
- colorama library

You can install the required library using pip:
```sh
pip install colorama
```

## Usage
Command-line Arguments
-f or --file: Specify the file name to write or read data (required)
-r or --read: Read data from the specified file (optional)
-n or --number: Specify the number of data entries to generate (default is 1)

## Examples
Generate Dummy Data and Write to a File

```sh
python main.py -f data.json -n 10
```
This command will generate 10 dummy data entries and write them to data.json.

## Read Data from a File
```sh
python main.py -f data.json -r
```
This command will read the data from data.json and display it along with the size of the data and the file.


## Functions
- random_string(string_length=10)
Generates a random string of lowercase letters with a default length of 10.

- random_number()
Generates a random integer between 1 and 100.

- random_date()
Generates a random date within one year from the current date.

- random_boolean()
Generates a random boolean value (True or False).

- generate_data()
Generates a dictionary with random values for name, age, date, and is_active.

- write_data_to_file(data, file_name)
Writes the provided data to the specified JSON file.

- read_data_from_file(file_name)
Reads and returns the data from the specified JSON file.

- generate_data_and_write_to_file(file_name, number)
Generates the specified number of data entries and writes them to the specified JSON file.

- calculate_data_size(data)
Calculates and returns the size of the provided data in bytes.

- calculate_file_size(file_name)
Calculates and returns the size of the specified file in bytes.

- calculate_data_and_file_size(data, file_name)
Calculates and displays the size of the provided data and the specified file.

- calculate_runtime(start_time, end_time)
Calculates and displays the runtime of the script.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
@mehmetkahya0
