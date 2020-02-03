import calendar
import json

import pandas


def ingate_ratio_for_ichr(input_path, export_path, is_loaded):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    first_result = []

    weekday_count = [0] * 7
    cities = ["GARDEN_CITY", "CHARLESTON", "GREER", "MEMPHIS", "CHICAGO", "JACKSONVILLE", "NEW_ORLEANS"]
    loaded = ["E", "L"]
    length_list = [20, 40, 45]
    hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

    for i in range(7):

        for i4 in range(len(hours)):
            count = [0] * 42 * 12
            dic = {}
            for data in values:
                if data[3].weekday() == i:
                    dic['DayOfWeek'] = str(calendar.day_name[data[3].weekday()])
                    dic['Time bucket'] = str(hours[i4] - 2) + " - " + str(hours[i4])
                    index = 0
                    for i1 in range(len(cities)):
                        for i2 in range(len(length_list)):
                            for i3 in range(len(loaded)):
                                count[index] += get_count(data, length_list[i2], loaded[i3], cities[i1], hours[i4]) \
                                    if is_loaded else get_count_without_loaded(data, length_list[i2], cities[i1],
                                                                               hours[i4])
                                if is_loaded:
                                    dic[str(length_list[i2]) + loaded[i3] + cities[i1]] = count[
                                        index]
                                else:
                                    dic[str(length_list[i2]) + cities[i1]] = count[
                                        index]

                                index += 1
            weekday_count[i] = sum(count)

            if len(dic) > 0:
                first_result.append(dic)

    with open(export_path, 'w') as outfile:  # export result Json to json file
        json.dump(first_result, outfile, indent=4)


def get_count(shipment, length, empty_loaded, city, hour):
    count = 0
    if city == 'GARDEN_CITY':
        if shipment[6] == length and shipment[5] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'SAVANNAH'):  # if city name is savannah add count to garden city
            count += 1
    elif city == 'CHARLESTON':
        if shipment[6] == length and shipment[5] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'NORTH_CHARLESTON'):  # if city name is north charleston add count to charleston
            count += 1
    elif city == 'NEW_ORLEANS':
        if shipment[6] == length and shipment[5] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (
                shipment[10] == city or shipment[10] == 'MCCALLA'):  # if city name is MCCALLA add count to NEW_ORLEANS
            count += 1
    elif city == 'CHICAGO':
        if shipment[6] == length and shipment[5] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (
                shipment[10] == city or shipment[10] == 'COLUMBUS'):  # if city name is COLUMBUS add count to CHICAGO
            count += 1
        elif shipment[6] == length and shipment[5] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'CINCINNATI'):  # if city name is CINCINNATI add count to CHICAGO
            count += 1
        elif shipment[6] == length and shipment[5] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'GEORGETOWN'):  # if city name is GEORGETOWN add count to CHICAGO
            count += 1
    else:
        if shipment[6] == length and shipment[5] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and shipment[
            10] == city:  # if length and empty loaded and city is equel => count++
            count += 1
    return count


def get_count_without_loaded(shipment, length, city, hour):
    count = 0
    if city == 'GARDEN_CITY':
        if shipment[6] == length and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'SAVANNAH'):  # if city name is savannah add count to garden city
            count += 1
    elif city == 'CHARLESTON':
        if shipment[6] == length and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'NORTH_CHARLESTON'):  # if city name is north charleston add count to charleston
            count += 1
    elif city == 'NEW_ORLEANS':
        if shipment[6] == length and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (
                shipment[10] == city or shipment[10] == 'MCCALLA'):  # if city name is MCCALLA add count to NEW_ORLEANS
            count += 1
    elif city == 'CHICAGO':
        if shipment[6] == length and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (
                shipment[10] == city or shipment[10] == 'COLUMBUS'):  # if city name is COLUMBUS add count to CHICAGO
            count += 1
        elif shipment[6] == length and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'CINCINNATI'):  # if city name is CINCINNATI add count to CHICAGO
            count += 1
        elif shipment[6] == length and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and (shipment[10] == city or shipment[
            10] == 'GEORGETOWN'):  # if city name is GEORGETOWN add count to CHICAGO
            count += 1
    else:
        if shipment[6] == length and hour - 2 >= convert_str_to_time(
                shipment[3]) <= hour and shipment[
            10] == city:  # if length and empty loaded and city is equel => count++
            count += 1
    return count


def convert_str_to_time(date):
    start_date = str(date).split()
    date = start_date[0].split("-")
    time = start_date[1].split(":")

    year = int(date[2])
    month = int(date[0])
    day = int(date[1])
    hour = int(time[0])
    minute = int(time[1])

    return hour


print("Start")
url = "C:/Users/Hassan/Desktop/pythonExport/IngateRatioForICHR/"
ingate_ratio_for_ichr(url + 'input.xlsx', url + "output.json", False)
print("Finished")
