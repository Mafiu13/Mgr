import json
import operator


def filter_for_users(records_by_user):
    # todd - 10
    filtered_few_checkins = filter_user_with_few_checkins(records_by_user, 2)
    print(len(filtered_few_checkins))

    # todd - 60
    filtered_bots = filter_bots_users(filtered_few_checkins, 1000)
    print(len(filtered_bots))
    return filtered_bots


def filter_user_with_few_checkins(records_by_user, min_treshold):
    filtered_records = records_by_user.copy()
    for key in records_by_user:
        if len(records_by_user[key]) < min_treshold:
            filtered_records.pop(key)
    return filtered_records


def filter_bots_users(records_by_user, min_time_treshold):
    filtered_records = records_by_user.copy()
    for key in records_by_user:
        counter = 0
        filtered_records[key].sort(key = operator.itemgetter('timestamp'))

        for filtered_record in filtered_records[key]:
            print(filtered_record)

        previous_timestamp = None
        for record in filtered_records[key]:
            current_timestamp = record['timestamp']
            if previous_timestamp is None:
                previous_timestamp = current_timestamp
            else:
                if current_timestamp - previous_timestamp < min_time_treshold:
                    counter += 1
                previous_timestamp = current_timestamp

        # todd - counter > 1
        if counter > 0:
            filtered_records.pop(key)
    return filtered_records
