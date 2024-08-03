# Python Dummy Data Generator for testing purposes only
# Author: Mehmet Kahya 
# Date: 3-08-2024 DD-MM-YYYY
# Version: 1.0
# Description: Generates dummy data for testing purposes only
# Usage: python main.py

import random
import string
import json
import os
import sys
from datetime import datetime
from datetime import timedelta
from colorama import Fore, Back, Style
import argparse

# Function to generate random string
def random_string(string_length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

# Function to generate random number
def random_number():
    return random.randint(1, 100)

# Function to generate random date
def random_date():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=365)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

# Function to generate random boolean
def random_boolean():
    return random.choice([True, False])

# Function to generate random data
def generate_data():
    data = {}
    data['name'] = random_string()
    data['age'] = random_number()
    data['date'] = random_date()
    data['is_active'] = random_boolean()
    return data

# Function to write data to file
def write_data_to_file(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
        print(Fore.GREEN + 'Data has been written to file: ' + file_name)
        print(Style.RESET_ALL)
        
# Function to read data from file
def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(Fore.GREEN + 'Data has been read from file: ' + file_name)
        print(Style.RESET_ALL)
        print(data)
        
# Function to generate data and write to file
def generate_data_and_write_to_file(file_name, number):
    data_list = [generate_data() for _ in range(number)]
    write_data_to_file(data_list, file_name)
    
def main():
    parser = argparse.ArgumentParser(description='Python Dummy Data Generator')
    parser.add_argument('-f', '--file', help='File name to write data', required=True)
    parser.add_argument('-r', '--read', help='Read data from file', action='store_true')
    parser.add_argument('-n', '--number', help='Number of data to generate', type=int, default=1)
    args = parser.parse_args()
    
    if args.read:
        read_data_from_file(args.file)
    else:
        generate_data_and_write_to_file(args.file, args.number)
        
if __name__ == '__main__':
    main()