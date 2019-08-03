import sys
import json


def read_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data


def restructure_data_to_default(dicionary):
    records = []
    for key in dicionary:
        records.extend(dicionary[key])
    return records


def restructure_data_by_key(records, key):
    user_data = {}
    for record in records:
        key_data = record[key]
        if not key_data in user_data:
            user_data[key_data] = []
        user_data[key_data].append(record)
    return user_data


def get_data_from(json_data, key):
    data = json_data.get(key, {})
    if not data:
        raise Exception("no data")
    return data