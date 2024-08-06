import csv
import os

FILE_PATH = 'WEEK17/FINANCEs_MANAGER.csv'

def export_data(data_list):
    try:
        with open(FILE_PATH, 'w', newline='') as file_w:
            writer = csv.writer(file_w)
            writer.writerow(['TYPE', 'TITLE', 'AMOUNT', 'CATEGORY'])
            writer.writerows(data_list)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def import_data():
    data_list = []
    if not os.path.exists(FILE_PATH):
        print(f"The file {FILE_PATH} does not exist.")
        return data_list

    try:
        with open(FILE_PATH, 'r', newline='') as file_r:
            reader = csv.reader(file_r)
            headers = next(reader, None)  # Skip header row
            if headers:
                data_list = [row for row in reader]
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

    return data_list

def return_categories(data_list, category_list = []):
    for row in data_list:
        category = row[1]
        if not category in category_list:
            category_list.append(category)
    return category_list