import sys
import json


def write_csv_data(records, file_name):
    with open(file_name, 'w', newline = '') as fp:
        json.dump(records, fp)