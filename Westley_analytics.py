'''
Project 3 emphasizes skills in using Git for version control, creating
and managing Python virtual environments, and handling different types
of data. The project involves fetching data from the web, processing 
it using appropriate Python collections, and writing the processed data
to files.

'''

# Standard library imports
import csv
import os
import re
import json

# External library imports (requires virtual environment)
import requests  
from collections import Counter
import pandas as pd
import xlrd

def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
    """
    Fetches text data from the specified URL and writes it to a new file.

    Parameters:
    - txt_folder_name (str): The name of the folder where the text file will be saved.
    - txt_filename (str): The name of the text file to be created.
    - txt_url (str): The URL of the online source.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(txt_folder_name):
            os.makedirs(txt_folder_name)

        # Fetch text data from the URL
        response = requests.get(txt_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Extract text from HTML using regex
        text_data = re.sub('<[^<]+?>', '', response.text)
        
        # Write text data to the output file
        output_file_path = os.path.join(txt_folder_name, txt_filename)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text_data)
        
        print(f"Text data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing text data: {e}")

def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):
    """
    Fetches CSV data from the specified URL and writes it to a new file.

    Parameters:
    - csv_folder_name (str): The name of the folder where the CSV file will be saved.
    - csv_filename (str): The name of the CSV file to be created.
    - csv_url (str): The URL of the online CSV file.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(csv_folder_name):
            os.makedirs(csv_folder_name)

        # Fetch CSV data from the URL
        response = requests.get(csv_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Write CSV data to the output file
        output_file_path = os.path.join(csv_folder_name, csv_filename)
        with open(output_file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"CSV data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing CSV data: {e}")

def fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url):
    """
    Fetches Excel data from the specified URL and writes it to a new file.

    Parameters:
    - excel_folder_name (str): The name of the folder where the Excel file will be saved.
    - excel_filename (str): The name of the Excel file to be created.
    - excel_url (str): The URL of the online Excel file.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(excel_folder_name):
            os.makedirs(excel_folder_name)

        # Fetch Excel data from the URL
        response = requests.get(excel_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Write Excel data to the output file
        output_file_path = os.path.join(excel_folder_name, excel_filename)
        with open(output_file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Excel data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing Excel data: {e}")

def fetch_and_write_json_data(json_folder_name, json_filename, json_url):
    """
    Fetches JSON data from the specified URL and writes it to a new file.

    Parameters:
    - json_folder_name (str): The name of the folder where the JSON file will be saved.
    - json_filename (str): The name of the JSON file to be created.
    - json_url (str): The URL of the online JSON data.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(json_folder_name):
            os.makedirs(json_folder_name)

        # Fetch JSON data from the URL
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON data
        json_data = response.json()
        
        # Write JSON data to the output file
        output_file_path = os.path.join(json_folder_name, json_filename)
        with open(output_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        print(f"JSON data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing JSON data: {e}")

def process_txt_file(txt_folder_name, input_filename, output_filename):
    """
    Process the contents of a text file and write the results to another text file.

    Parameters:
    - txt_folder_name (str): The name of the folder containing the input and output files.
    - input_filename (str): The name of the input text file to be processed.
    - output_filename (str): The name of the output text file to write the results to.
    """
    try:
        # Construct the file paths
        input_file_path = os.path.join(txt_folder_name, input_filename)
        output_file_path = os.path.join(txt_folder_name, output_filename)
        
        # Read input text file
        with open(input_file_path, 'r') as input_file:
            data = input_file.read()
        
        # Use Counter to count occurrences of each character
        character_counts = Counter(data)
        
        # Convert the Counter object to a string for writing to file
        processed_data = '\n'.join([f"{char}: {count}" for char, count in character_counts.items()])
        
        # Write processed data to output text file
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_data)
        
        print(f"Processed data written to '{output_file_path}'")
    except Exception as e:
        print(f"Error processing text file: {e}")

def process_csv_file(csv_folder_name, input_filename, output_filename):
    """
    Process the contents of a CSV file and write the results to a text file.

    Parameters:
    - csv_folder_name (str): The name of the folder containing the input and output files.
    - input_filename (str): The name of the input CSV file to be processed.
    - output_filename (str): The name of the output text file to write the results to.
    """
    try:
        # Construct the file paths
        input_file_path = os.path.join(csv_folder_name, input_filename)
        output_file_path = os.path.join(csv_folder_name, output_filename)
        
        # Read input CSV file
        with open(input_file_path, 'r', newline='') as input_file:
            reader = csv.reader(input_file)
            # Skip the header row if present
            next(reader)
            
            # Flatten the CSV rows into a single list of values
            data = [value for row in reader for value in row]
        
        # Use Counter to count occurrences of each value
        value_counts = Counter(data)
        
        # Convert the Counter object to a string for writing to file
        processed_data = '\n'.join([f"{value}: {count}" for value, count in value_counts.items()])
        
        # Write processed data to output text file
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_data)
        
        print(f"Processed data written to '{output_file_path}'")
    except Exception as e:
        print(f"Error processing CSV file: {e}")

def process_excel_file(excel_folder_name, input_filename, output_filename):
    """
    Process the contents of an Excel file and write the results to a text file.

    Parameters:
    - excel_folder_name (str): The name of the folder containing the input and output files.
    - input_filename (str): The name of the input Excel file to be processed.
    - output_filename (str): The name of the output text file to write the results to.
    """
    try:
        # Construct the file paths
        input_file_path = os.path.join(excel_folder_name, input_filename)
        output_file_path = os.path.join(excel_folder_name, output_filename)
        
        # Read input Excel file
        workbook = xlrd.open_workbook(input_file_path)
        sheet = workbook.sheet_by_index(0)  # Assuming data is in the first sheet
        
        # Flatten the Excel rows into a single list of values
        data = [value for row in range(sheet.nrows) for value in sheet.row_values(row)]
        
        # Use Counter to count occurrences of each value
        value_counts = Counter(data)
        
        # Convert the Counter object to a string for writing to file
        processed_data = '\n'.join([f"{value}: {count}" for value, count in value_counts.items()])
        
        # Write processed data to output text file
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_data)
        
        print(f"Processed data written to '{output_file_path}'")
    except Exception as e:
        print(f"Error processing Excel file: {e}")

def process_json_file(json_folder_name, input_filename, output_filename):
    """
    Process the contents of a JSON file and write the results to a text file.

    Parameters:
    - json_folder_name (str): The name of the folder containing the input and output files.
    - input_filename (str): The name of the input JSON file to be processed.
    - output_filename (str): The name of the output text file to write the results to.
    """
    try:
        # Construct the file paths
        input_file_path = os.path.join(json_folder_name, input_filename)
        output_file_path = os.path.join(json_folder_name, output_filename)
        
        # Read input JSON file
        with open(input_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Flatten the JSON data into a single list of values
        flattened_data = flatten_json(data)
        
        # Use Counter to count occurrences of each value
        value_counts = Counter(flattened_data)
        
        # Convert the Counter object to a string for writing to file
        processed_data = '\n'.join([f"{value}: {count}" for value, count in value_counts.items()])
        
        # Write processed data to output text file
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_data)
        
        print(f"Processed data written to '{output_file_path}'")
    except Exception as e:
        print(f"Error processing JSON file: {e}")

def flatten_json(data, parent_key='', sep='.'):
    '''Helper function to flatten nested JSON'''
    items = []
    for k, v in data.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def main():
    ''' Main function to demonstrate module capabilities. '''
    #my name input
    name = "Westley Vance"
    print(f"Name: {name}")
    #url's for web data
    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    json_url = 'http://api.open-notify.org/astros.json'
    #names for output folders
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 
    #names for output files
    txt_filename = 'romeoJuliet.txt'
    csv_filename = 'countryLadderScore.csv'
    excel_filename = 'cattle.xls' 
    json_filename = 'astronauts.json' 
    #call functios to take web file and convert it to a usable file format
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)
    #call functons for text processing in different file formats
    process_txt_file(txt_folder_name, 'romeoJuliet.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'countryLadderScore.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'cattle.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'astronauts.json', 'results_json.txt')
    
if __name__ == '__main__':
    main()