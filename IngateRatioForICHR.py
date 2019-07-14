import calendar
import json

import pandas


def ingate_ratio_for_ichr(input_path, export_path, ratio_export_path):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    first_result = []
    second_result = []

    weekday_count = [0] * 7
    cities = ["GARDEN_CITY", "CHARLESTON", "GREER", "MEMPHIS", "CHICAGO", "JACKSONVILLE", "NEW_ORLEANS"]
    loaded = ["E", "L"]
    length_list = [20, 40, 45]

    for i in range(7):
        count = [0] * 42
        dic = {}
        for data in values:
            if data[3].weekday() == i:
                dic['DayOfWeek'] = str(calendar.day_name[data[3].weekday()])
                index = 0
                for i1 in range(len(cities)):
                    for i2 in range(len(length_list)):
                        for i3 in range(len(loaded)):
                            count[index] += get_count(data, length_list[i2], loaded[i3], cities[i1])
                            dic[str(length_list[i2]) + loaded[i3] + cities[i1]] = count[index]
                            index += 1
        weekday_count[i] = sum(count)

        if len(dic) > 0:
            first_result.append(dic)

    with open(export_path, 'w') as outfile:  # export result Json to json file
        json.dump(first_result, outfile, indent=4)

    i = 0
    for data in first_result:
        for i1 in range(len(cities)):
            for i2 in range(len(length_list)):
                for i3 in range(len(loaded)):
                    if data[str(length_list[i2]) + loaded[i3] + cities[i1]] > 0:
                        data[str(length_list[i2]) + loaded[i3] + cities[i1]] = format(
                            data[str(length_list[i2]) + loaded[i3] + cities[i1]] / weekday_count[i], '.3f')
        second_result.append(data)
        i += 1

    with open(ratio_export_path, 'w') as outfile:  # export result Json to json file
        json.dump(second_result, outfile, indent=4)


def get_count(shipment, length, empty_loaded, city):
    count = 0
    if city == 'GARDEN_CITY':
        if shipment[6] == length and shipment[5] == empty_loaded and (shipment[10] == city or shipment[
            10] == 'SAVANNAH'):  # if city name is savannah add count to garden city
            count += 1
    elif city == 'CHARLESTON':
        if shipment[6] == length and shipment[5] == empty_loaded and (shipment[10] == city or shipment[
            10] == 'NORTH_CHARLESTON'):  # if city name is north charleston add count to charleston
            count += 1
    elif city == 'NEW_ORLEANS':
        if shipment[6] == length and shipment[5] == empty_loaded and (
                shipment[10] == city or shipment[10] == 'MCCALLA'):  # if city name is MCCALLA add count to NEW_ORLEANS
            count += 1
    elif city == 'CHICAGO':
        if shipment[6] == length and shipment[5] == empty_loaded and (
                shipment[10] == city or shipment[10] == 'COLUMBUS'):  # if city name is COLUMBUS add count to CHICAGO
            count += 1
        elif shipment[6] == length and shipment[5] == empty_loaded and (shipment[10] == city or shipment[
            10] == 'CINCINNATI'):  # if city name is CINCINNATI add count to CHICAGO
            count += 1
        elif shipment[6] == length and shipment[5] == empty_loaded and (shipment[10] == city or shipment[
            10] == 'GEORGETOWN'):  # if city name is GEORGETOWN add count to CHICAGO
            count += 1
    else:
        if shipment[6] == length and shipment[5] == empty_loaded and shipment[
            10] == city:  # if length and empty loaded and city is equel => count++
            count += 1
    return count


print("Start")
url = "C:/Users/Hassan/Desktop/pythonExport/IngateRatioForICHR/"
ingate_ratio_for_ichr(url + 'input.xlsx', url + "output.json", url + "ratioOutput.json")
print("Finished")
