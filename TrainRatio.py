import calendar
import json

import pandas


def train_ratio(input_excel_path, export_path):
    input_data = pandas.read_excel(input_excel_path)  # get data from excel
    input_data = input_data.get_values()  # get all values from input excel

    result = []
    trains = []

    index = 0
    for data in input_data:
        if index <= len(input_data):
            train = []
            if index > 0:
                train = [input_data[index]]
            sub_index = 0
            for i in range(index, len(input_data)):
                if input_data[index][2] == input_data[index + sub_index][2] and input_data[index][4] == \
                        input_data[index + sub_index][4]:
                    train.append(input_data[index + sub_index])
                else:
                    trains.append(train)
                    break
                j = len(input_data)
                if i + 1 == len(input_data):
                    trains.append(train)
                sub_index += 1
            index = index + sub_index + 1
        else:
            break

    index = 0
    for train in trains:
        result.append({  # add to result json
            'DayOfWeek': calendar.day_name[train[0][2].weekday()],
            'Date': train[0][2].strftime("%m/%d/%Y %H:%M:%S"),
            'Inbound/OutBound': 'O' if train[0][3] == 'DFLC' else 'I',
            'Train Symbol': train[0][4],
            'NumberOfAllShipments': len(train),
            'NumberOf20EAustell': get_count(train, 20, 'E', 'AUSTELL'),
            'NumberOf20LAustell': get_count(train, 20, 'L', 'AUSTELL'),
            'NumberOf40EAustell': get_count(train, 40, 'E', 'AUSTELL'),
            'NumberOf40LAustell': get_count(train, 40, 'L', 'AUSTELL'),
            'NumberOf45EAustell': get_count(train, 45, 'E', 'AUSTELL'),
            'NumberOf45LAustell': get_count(train, 45, 'L', 'AUSTELL'),
            'NumberOf20EGardenCity': get_count(train, 20, 'E', 'GARDEN_CITY'),
            'NumberOf20LGardenCity': get_count(train, 20, 'L', 'GARDEN_CITY'),
            'NumberOf40EGardenCity': get_count(train, 40, 'E', 'GARDEN_CITY'),
            'NumberOf40LGardenCity': get_count(train, 40, 'L', 'GARDEN_CITY'),
            'NumberOf45EGardenCity': get_count(train, 45, 'E', 'GARDEN_CITY'),
            'NumberOf45LGardenCity': get_count(train, 45, 'L', 'GARDEN_CITY'),
            'NumberOf20ECharleston': get_count(train, 20, 'E', 'CHARLESTON'),
            'NumberOf20LCharleston': get_count(train, 20, 'L', 'CHARLESTON'),
            'NumberOf40ECharleston': get_count(train, 40, 'E', 'CHARLESTON'),
            'NumberOf40LCharleston': get_count(train, 40, 'L', 'CHARLESTON'),
            'NumberOf45ECharleston': get_count(train, 45, 'E', 'CHARLESTON'),
            'NumberOf45LCharleston': get_count(train, 45, 'L', 'CHARLESTON'),
            'NumberOf20EGreer': get_count(train, 20, 'E', 'GREER'),
            'NumberOf20LGreer': get_count(train, 20, 'L', 'GREER'),
            'NumberOf40EGreer': get_count(train, 40, 'E', 'GREER'),
            'NumberOf40LGreer': get_count(train, 40, 'L', 'GREER'),
            'NumberOf45EGreer': get_count(train, 45, 'E', 'GREER'),
            'NumberOf45LGreer': get_count(train, 45, 'L', 'GREER'),
            'NumberOf20EMemphis': get_count(train, 20, 'E', 'MEMPHIS'),
            'NumberOf20LMemphis': get_count(train, 20, 'L', 'MEMPHIS'),
            'NumberOf40EMemphis': get_count(train, 40, 'E', 'MEMPHIS'),
            'NumberOf40LMemphis': get_count(train, 40, 'L', 'MEMPHIS'),
            'NumberOf45EMemphis': get_count(train, 45, 'E', 'MEMPHIS'),
            'NumberOf45LMemphis': get_count(train, 45, 'L', 'MEMPHIS'),
            'NumberOf20EChicago': get_count(train, 20, 'E', 'CHICAGO'),
            'NumberOf20LChicago': get_count(train, 20, 'L', 'CHICAGO'),
            'NumberOf40EChicago': get_count(train, 40, 'E', 'CHICAGO'),
            'NumberOf40LChicago': get_count(train, 40, 'L', 'CHICAGO'),
            'NumberOf45EChicago': get_count(train, 45, 'E', 'CHICAGO'),
            'NumberOf45LChicago': get_count(train, 45, 'L', 'CHICAGO'),
            'NumberOf20EJacksonville': get_count(train, 20, 'E', 'JACKSONVILLE'),
            'NumberOf20LJacksonville': get_count(train, 20, 'L', 'JACKSONVILLE'),
            'NumberOf40EJacksonville': get_count(train, 40, 'E', 'JACKSONVILLE'),
            'NumberOf40LJacksonville': get_count(train, 40, 'L', 'JACKSONVILLE'),
            'NumberOf45EJacksonville': get_count(train, 45, 'E', 'JACKSONVILLE'),
            'NumberOf45LJacksonville': get_count(train, 45, 'L', 'JACKSONVILLE'),
            'NumberOf20ENewOrleans': get_count(train, 20, 'E', 'NEW_ORLEANS'),
            'NumberOf20LNewOrleans': get_count(train, 20, 'L', 'NEW_ORLEANS'),
            'NumberOf40ENewOrleans': get_count(train, 40, 'E', 'NEW_ORLEANS'),
            'NumberOf40LNewOrleans': get_count(train, 40, 'L', 'NEW_ORLEANS'),
            'NumberOf45ENewOrleans': get_count(train, 45, 'E', 'NEW_ORLEANS'),
            'NumberOf45LNewOrleans': get_count(train, 45, 'L', 'NEW_ORLEANS'),
        })
        index += 1

    with open(export_path, 'w') as outfile:  # export result Json to json file
        json.dump(result, outfile, indent=4)


def get_count(shipments, length, empty_loaded, city):
    count = 0
    for shipment in shipments:
        if city == 'GARDEN_CITY':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[10] == 'SAVANNAH'):
                count += 1
        elif city == 'CHARLESTON':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[10] == 'NORTH_CHARLESTON'):
                count += 1
        elif city == 'AUSTELL':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[10] == 'ATLANTA'):
                count += 1
        else:
            if shipment[6] == length and shipment[5] == empty_loaded and shipment[10] == city:
                count += 1
    return count


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TrainRatio/"
train_ratio(url + "input.xlsx", url + "output.json")
print("finished")
