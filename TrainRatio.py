import calendar
import json

import pandas


def trainRation_domestic_and_international(input_excel_path, export_path):
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
                if i + 1 == len(input_data):  # if the last index of array just add train to train list
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
            'NumberOf20Austell': get_count(train, 20, 'AUSTELL'),
            'NumberOf40Austell': get_count(train, 40, 'AUSTELL'),
            'NumberOf45Austell': get_count(train, 45, 'AUSTELL'),
            'NumberOf20GardenCity': get_count(train, 20, 'GARDEN_CITY'),
            'NumberOf40GardenCity': get_count(train, 40, 'GARDEN_CITY'),
            'NumberOf45GardenCity': get_count(train, 45, 'GARDEN_CITY'),
            'NumberOf20Charleston': get_count(train, 20, 'CHARLESTON'),
            'NumberOf40Charleston': get_count(train, 40, 'CHARLESTON'),
            'NumberOf45Charleston': get_count(train, 45, 'CHARLESTON'),
            'NumberOf20Greer': get_count(train, 20, 'GREER'),
            'NumberOf40Greer': get_count(train, 40, 'GREER'),
            'NumberOf45Greer': get_count(train, 45, 'GREER'),
            'NumberOf20Memphis': get_count(train, 20, 'MEMPHIS'),
            'NumberOf40Memphis': get_count(train, 40, 'MEMPHIS'),
            'NumberOf45Memphis': get_count(train, 45, 'MEMPHIS'),
            'NumberOf53Memphis': get_count(train, 53, 'MEMPHIS'),
            'NumberOf20Chicago': get_count(train, 20, 'CHICAGO'),
            'NumberOf40Chicago': get_count(train, 40, 'CHICAGO'),
            'NumberOf45Chicago': get_count(train, 45, 'CHICAGO'),
            'NumberOf53Chicago': get_count(train, 53, 'CHICAGO'),
            'NumberOf20Jacksonville': get_count(train, 20, 'JACKSONVILLE'),
            'NumberOf40Jacksonville': get_count(train, 40, 'JACKSONVILLE'),
            'NumberOf45Jacksonville': get_count(train, 45, 'JACKSONVILLE'),
            'NumberOf20NewOrleans': get_count(train, 20, 'NEW_ORLEANS'),
            'NumberOf40NewOrleans': get_count(train, 40, 'NEW_ORLEANS'),
            'NumberOf45NewOrleans': get_count(train, 45, 'NEW_ORLEANS'),
            'NumberOf53KansasCity': get_count(train, 53, 'KANSAS_CITY'),
            'NumberOf53Rossville': get_count(train, 53, 'ROSSVILLE'),
            'NumberOf53Shreveport': get_count(train, 53, 'SHREVEPORT')
        })
        index += 1

    with open(export_path, 'w') as outfile:  # export result Json to json file
        json.dump(result, outfile, indent=4)


def get_count(shipments, length, city):
    count = 0
    for shipment in shipments:
        if city == 'GARDEN_CITY':
            if shipment[6] == length and (shipment[10] == city or shipment[10] == 'SAVANNAH'):
                count += 1
        elif city == 'CHARLESTON':
            if shipment[6] == length and (shipment[10] == city or shipment[10] == 'NORTH_CHARLESTON'):
                count += 1
        elif city == 'AUSTELL':
            if shipment[6] == length and (shipment[10] == city or shipment[10] == 'ATLANTA'):
                count += 1
        else:
            if shipment[6] == length and shipment[10] == city:
                count += 1
    return count


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TrainRationDomesticAndInternational/"
trainRation_domestic_and_international(url + "input.xlsx", url + "output.json")
print("finished")
