import random
import string
import json
import os
import sys
from datetime import datetime, timedelta
from colorama import Fore, Style
import argparse

print(Fore.RED + 'Python Dummy Data Generator')
print(Style.RESET_ALL)

def random_string(string_length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def random_number():
    return random.randint(1, 100)

def random_date():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=365)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

def random_boolean():
    return random.choice([True, False])

def generate_data():
    data = {}
    data['name'] = random_string()
    data['age'] = random_number()
    data['date'] = random_date()
    data['is_active'] = random_boolean()
    return data

def write_data_to_file(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
        print(Fore.GREEN + 'Data has been written to file: ' + file_name)
        print(Style.RESET_ALL)

def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(Fore.GREEN + 'Data has been read from file: ' + file_name)
        print(Style.RESET_ALL)
        print(data)

def generate_data_and_write_to_file(file_name, number):
    data_list = [generate_data() for _ in range(number)]
    write_data_to_file(data_list, file_name)

def calculate_data_size(data):
    return sys.getsizeof(data)

def calculate_file_size(file_name):
    return os.path.getsize(file_name)

def calculate_data_and_file_size(data, file_name):
    data_size = calculate_data_size(data)
    file_size = calculate_file_size(file_name)
    print(Fore.RESET + 'Data Size: ' + str(data_size) + ' bytes')
    print('File Size: ' + str(file_size) + ' bytes')
    print(Style.RESET_ALL)

def calculate_runtime(start_time, end_time):
    runtime = end_time - start_time
    print(Fore.BLUE + 'Start Time: ' + str(start_time))
    print('End Time: ' + str(end_time))
    print('Runtime: ' + str(runtime.total_seconds()) + ' seconds')
    print(Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(description='Python Dummy Data Generator')
    parser.add_argument(
        '-f', '--file', help='File name to write data', required=True)
    parser.add_argument(
        '-r', '--read', help='Read data from file', action='store_true')
    parser.add_argument(
        '-n', '--number', help='Number of data to generate', type=int, default=1)
    args = parser.parse_args()

    start_time = datetime.now()

    if args.read:
        read_data_from_file(args.file)
        calculate_data_and_file_size(read_data_from_file(args.file), args.file)
    else:
        generate_data_and_write_to_file(args.file, args.number)
        calculate_data_and_file_size(generate_data(), args.file)

    end_time = datetime.now()
    calculate_runtime(start_time, end_time)

if __name__ == '__main__':
    main()