import calendar
import json

import pandas


def ingate_ratio(input_path, export_path, consider_loaded_empty):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    final_result = []

    cities = ["GARDEN_CITY", "CHARLESTON", "GREER", "MEMPHIS", "CHICAGO", "JACKSONVILLE", "NEW_ORLEANS", "KANSAS_CITY",
              "ROSSVILLE", "SHREVEPORT"]
    loaded_empty = ["E", "L"]
    length_list = [20, 40, 45, 53]
    hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    for i in range(7):
        for hour in range(len(hours)):
            count = [0] * 10 * 2 * 4 * 24  # count = [0] * cities * loaded * length-list * hours
            dic = {}
            weekday_count = 1
            j = 0
            date = 0
            for data in values:
                if data[2].weekday() == i:
                    if j > 0:
                        if date + 604800 <= data[2].timestamp():
                            weekday_count += 1
                            date = data[2].timestamp()
                    else:
                        date = data[2].timestamp()
                    j += 1
                    dic['DayOfWeek'] = str(calendar.day_name[data[2].weekday()])
                    dic['HourOfDay'] = str(hours[hour] - 1)
                    index = 0
                    for city in range(len(cities)):
                        for length in range(len(length_list)):
                            for le in range(len(loaded_empty)):
                                count[index] += get_count(data, length_list[length], loaded_empty[le], cities[city],
                                                          hours[hour]) \
                                    if consider_loaded_empty else get_count_without_loaded(data, length_list[length],
                                                                                           cities[city],
                                                                                           hours[hour])
                                index += 1
            for c in count:
                if c > 0:
                    c /= weekday_count

            index = 0
            for city in range(len(cities)):
                for length in range(len(length_list)):
                    for le in range(len(loaded_empty)):
                        if consider_loaded_empty:
                            if length_list[length] == 53:
                                if cities[city] == "CHICAGO" or cities[city] == "KANSAS_CITY" or cities[
                                    city] == "MEMPHIS" or cities[city] == "ROSSVILLE" or cities[
                                    city] == "SHREVEPORT":
                                    dic[str(length_list[length]) + loaded_empty[le] + cities[city]] = count[
                                        index]
                            else:
                                if not (cities[city] == "KANSAS_CITY" or cities[city] == "ROSSVILLE" or cities[
                                    city] == "SHREVEPORT"):
                                    dic[str(length_list[length]) + loaded_empty[le] + cities[city]] = count[
                                        index]
                        else:
                            if length_list[length] == 53:
                                if cities[city] == "CHICAGO" or cities[city] == "KANSAS_CITY" or cities[
                                    city] == "MEMPHIS" or cities[city] == "ROSSVILLE" or cities[
                                    city] == "SHREVEPORT":
                                    dic[str(length_list[length]) + cities[city]] = count[index]
                            else:
                                if not (cities[city] == "KANSAS_CITY" or cities[city] == "ROSSVILLE" or cities[
                                    city] == "SHREVEPORT"):
                                    dic[str(length_list[length]) + cities[city]] = count[index]
                        index += 1

            if len(dic) > 0:
                final_result.append(dic)

    with open(export_path, 'w') as outfile:  # export result Json to json file
        json.dump(final_result, outfile, indent=4)


def get_count(shipment, length, empty_loaded, city, hour):
    count = 0
    if city == 'GARDEN_CITY':
        if shipment[5] == length and shipment[4] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (
                shipment[9] == city or shipment[9] == 'SAVANNAH'):  # if city name is savannah add count to garden city
            count += 1
    elif city == 'CHARLESTON':
        if shipment[5] == length and shipment[4] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (shipment[9] == city or shipment[
            9] == 'NORTH_CHARLESTON'):  # if city name is north charleston add count to charleston
            count += 1
    elif city == 'NEW_ORLEANS':
        if shipment[5] == length and shipment[4] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (
                shipment[9] == city or shipment[9] == 'MCCALLA'):  # if city name is MCCALLA add count to NEW_ORLEANS
            count += 1
    elif city == 'CHICAGO':
        if shipment[5] == length and shipment[4] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (
                shipment[9] == city or shipment[9] == 'COLUMBUS'):  # if city name is COLUMBUS add count to CHICAGO
            count += 1
        elif shipment[5] == length and shipment[4] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (shipment[9] == city or shipment[
            9] == 'CINCINNATI'):  # if city name is CINCINNATI add count to CHICAGO
            count += 1
        elif shipment[5] == length and shipment[4] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (shipment[9] == city or shipment[
            9] == 'GEORGETOWN'):  # if city name is GEORGETOWN add count to CHICAGO
            count += 1
    else:
        if shipment[5] == length and shipment[4] == empty_loaded and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and shipment[
            9] == city:  # if length and empty loaded and city is equel => count++
            count += 1
    return count


def get_count_without_loaded(shipment, length, city, hour):
    count = 0
    if city == 'GARDEN_CITY':
        if shipment[5] == length and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (shipment[9] == city or shipment[
            9] == 'SAVANNAH'):  # if city name is savannah add count to garden city
            count += 1
    elif city == 'CHARLESTON':
        if shipment[5] == length and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (shipment[9] == city or shipment[
            9] == 'NORTH_CHARLESTON'):  # if city name is north charleston add count to charleston
            count += 1
    elif city == 'NEW_ORLEANS':
        if shipment[5] == length and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (
                shipment[9] == city or shipment[9] == 'MCCALLA'):  # if city name is MCCALLA add count to NEW_ORLEANS
            count += 1
    elif city == 'CHICAGO':
        if shipment[5] == length and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (
                shipment[9] == city or shipment[9] == 'COLUMBUS'):  # if city name is COLUMBUS add count to CHICAGO
            count += 1
        elif shipment[5] == length and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (shipment[9] == city or shipment[
            9] == 'CINCINNATI'):  # if city name is CINCINNATI add count to CHICAGO
            count += 1
        elif shipment[5] == length and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and (shipment[9] == city or shipment[
            9] == 'GEORGETOWN'):  # if city name is GEORGETOWN add count to CHICAGO
            count += 1
    else:
        if shipment[5] == length and hour - 2 >= convert_str_to_time(
                shipment[2]) <= hour and shipment[
            9] == city:  # if length and empty loaded and city is equel => count++
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
url = "C:/Users/Hassan/Desktop/pythonExport/IngateRatio/"
ingate_ratio(url + 'input.xlsx', url + "output.json", False)
print("Finished")
