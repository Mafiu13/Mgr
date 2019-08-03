from RawDataLoader import read_csv_data
from DataLoader import read_json, restructure_data_by_key, restructure_data_to_default
from DataExporter import  write_csv_data
from DataFilters import filter_for_users

# Load raw data from csv file
#records = read_csv_data("checkins_swarmapp_foursquare_world_1-8_sorted_uq.csv")

# Write formatted json data to txt file
file_name = "formatted_data.txt"
#write_csv_data(records, file_name)

json_data = read_json(file_name)
print(len(json_data))

records_by_user = restructure_data_by_key(json_data, "user_id")
print(len(records_by_user))

#filter user < tresholds
records_by_user = filter_for_users(records_by_user)
print(len(records_by_user))

default_records = restructure_data_to_default(records_by_user)
print(len(default_records))
