import sys
import json

def read_csv_data(csv_data):
    # checkins_swarmapp_foursquare_world_1-8_sorted_uq.csv
    file = open(csv_data, encoding="utf8")
    records = {}
    for i, f in enumerate(file):
        r = json.loads(f)

        #validowac ladniej (biblioteka marshmallow, pydantic - macko preferuje)
        checkin_id = r.get("checkin", {}).get("id")
        if not checkin_id: continue

        formatted = {
            "checkin_id": checkin_id,
            "checkin_date": r["checkin"]["createdAt"],
            "user": r["user"],
            "language": r["lang"],
            "venue": r["venue"],
            "categories": r["categories"],
        }
        records[checkin_id] = formatted
        print(i)
    return list(records.values())
    #print(records[0]["status"]["createdAt"])