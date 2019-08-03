import json
from DataLoader import get_data_from

def read_csv_data(csv_data):
    # checkins_swarmapp_foursquare_world_1-8_sorted_uq.csv
    file = open(csv_data, encoding="utf8")
    records = []
    counter = 0
    for i, f in enumerate(file):
        if counter == 1000: break
        counter += 1
        try:
            json_data = json.loads(f)
            formatted_data = get_formatted_data(json_data)
        except:
           continue
        records.append(formatted_data)
    print(f'Początkowa liczba rekordów{counter}')
    print(f'Odfiltorowana liczba rekordów{len(records)}')
    return list(records)


def get_formatted_data(json_data):
    status = get_data_from(json_data, "status")

    checkin = get_data_from(json_data, "checkin")
    user = get_data_from(checkin, "user")
    venue = get_data_from(checkin, "venue")
    categories = get_data_from(venue, "categories")
    if len(categories) > 1:
        print(f'LICZBA KATEGORI WIEKSZA NIZ 1 {categories}')
    location = get_data_from(venue, "location")

    id = get_data_from(checkin, "id")
    user_id = get_data_from(user, "id")
    created_at = get_data_from(status, "createdAt")
    timestamp = get_data_from(checkin, "createdAt")
    venue_id = get_data_from(venue, "id")
    category_id = get_data_from(categories[0], "id")
    category_name = get_data_from(categories[0], "name")
    latitude = get_data_from(location, "lat")
    longitude = get_data_from(location, "lng")
    gender =  get_data_from(user, "gender")
    language = get_data_from(status, "lang")

    formatted = {
        "id": id,
        "user_id": user_id,
        "timestamp": timestamp,
        "venue_id": venue_id,
        "category_id": category_id,
        "category_name": category_name,
        "latitude": latitude,
        "longitude": longitude,
        "gender": gender,
        "language": language
    }
    return formatted