import calendar
import json

import pandas


def train_classification_ratio(input_excel_path, inbound_export_path, outbound_export_path, status):
    input_data = pandas.read_excel(input_excel_path)  # get data from excel
    input_data = input_data.get_values()  # get all values from input excel

    inbound_result = []  # inbound result list
    outbound_result = []  # outbound result list
    trains = []  # train list0
    cities = ["GARDEN_CITY", "CHARLESTON", "GREER", "MEMPHIS", "CHICAGO", "JACKSONVILLE", "NEW_ORLEANS", "KANSAS_CITY",
              "ROSSVILLE", "SHREVEPORT"]
    loaded_empty = ["E", "L"]
    length_list = [20, 40, 45, 53]

    index = 0
    for data in input_data:
        if index <= len(input_data):  # if any row to calculate
            train = []
            if index > 0:
                train = [input_data[index]]  # add first shipment to train
            sub_index = 0
            for i in range(index, len(input_data)):  # for from current index to last row of excel
                if input_data[index][2] == input_data[index + sub_index][2] and input_data[index][4] == \
                        input_data[index + sub_index][
                            4]:
                    train.append(input_data[index + sub_index])
                else:
                    trains.append(train)
                    break

                if i + 1 == len(input_data):  # if last row
                    trains.append(train)  # add train list to trains
                sub_index += 1
            index = index + sub_index + 1
        else:
            break

    index = 0
    for train in trains:
        dic = {}
        if not repetitious(train[0][4], inbound_result, outbound_result):  # if not repetitious
            count = [0] * 10 * 2 * 4  # count = [0] * cities * loaded * length-list
            all_shipment = 0
            day_of_week = ""
            date = ""
            shipment = ""
            sub_index = 0
            for sub_train in trains:
                if sub_train[0][3] == train[0][3] and sub_train[0][4] == train[0][4]:  # if event type and trn is equal
                    coefficient = 1  # ratio for NumberOfAllShipments. if status is true changed
                    sub_coefficient = 1  # ratio for all counts. if status is true changed

                    if status:
                        coefficient = sub_index + 1

                    day_of_week += str(sub_index + 1) + " = " + str(calendar.day_name[sub_train[0][2].weekday()]) + "  "
                    dic['DayOfWeek'] = day_of_week
                    date += str(sub_index + 1) + " = " + str(sub_train[0][2].strftime("%m/%d/%Y %H:%M:%S")) + "  "
                    dic['Date'] = date
                    dic['Inbound/OutBound'] = 'O' if sub_train[0][3] == 'DFLC' else 'I'
                    dic['Train Symbol'] = sub_train[0][4]  # add trn in this item
                    shipment += str(sub_index + 1) + " = " + str(len(sub_train)) + "  "
                    dic['NumberOfAllShipmentsForEachTrain'] = shipment
                    all_shipment += len(sub_train)
                    dic['NumberOfAllShipments'] = format(all_shipment / coefficient, '.2f')

                    if status:
                        sub_coefficient = 100 / (
                                all_shipment / coefficient)  # if status is true all train length to ratio

                    i = 0
                    for city in range(len(cities)):
                        for length in range(len(length_list)):
                            for le in range(len(loaded_empty)):
                                count[i] += get_count(sub_train, length_list[length], loaded_empty[le],
                                                      cities[city])
                                if length_list[length] == 53:
                                    if cities[city] == "CHICAGO" or cities[city] == "KANSAS_CITY" or cities[
                                        city] == "MEMPHIS" or cities[city] == "ROSSVILLE" or cities[
                                        city] == "SHREVEPORT":
                                        dic[str(length_list[length]) + str(loaded_empty[le]) + cities[city]] = format(
                                            (count[i] / coefficient) * sub_coefficient, '.2f')
                                else:
                                    if not (cities[city] == "KANSAS_CITY" or cities[city] == "ROSSVILLE" or cities[
                                        city] == "SHREVEPORT"):
                                        dic[str(length_list[length]) + str(loaded_empty[le]) + cities[city]] = format(
                                            (count[i] / coefficient) * sub_coefficient, '.2f')
                                i += 1
                    sub_index += 1

        if len(dic) > 0:
            if train[0][3] == 'DFLC':  # if outbound or inbound added
                outbound_result.append(dic)
            else:
                inbound_result.append(dic)

        index += 1

    with open(inbound_export_path, 'w') as inbound_outfile:  # export result Json to json file
        json.dump(inbound_result, inbound_outfile, indent=4)
    with open(outbound_export_path, 'w') as outbound_outfile:  # export result Json to json file
        json.dump(outbound_result, outbound_outfile, indent=4)


def repetitious(trn_symbol, inbounds,
                outbounds):  # if don't repetitive trn symbol in inbound and outbound list return false else return true
    for inbound in inbounds:
        if inbound['Train Symbol'] == trn_symbol:
            return True

    for outbound in outbounds:
        if outbound['Train Symbol'] == trn_symbol:
            return True
    return False


def get_count(shipments, length, empty_loaded, city):
    count = 0
    for shipment in shipments:
        if city == 'GARDEN_CITY':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[
                10] == 'SAVANNAH'):  # if city name is savannah add count to garden city
                count += 1
        elif city == 'CHARLESTON':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[
                10] == 'NORTH_CHARLESTON'):  # if city name is north charleston add count to charleston
                count += 1
        elif city == 'AUSTELL':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[10] == 'ATLANTA'):  # if city name is atlanta add count to austell
                count += 1
        elif city == 'NEW_ORLEANS':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[
                10] == 'MCCALLA'):  # if city name is MCCALLA add count to NEW_ORLEANS
                count += 1
        elif city == 'CHICAGO':
            if shipment[6] == length and shipment[5] == empty_loaded and (
                    shipment[10] == city or shipment[
                10] == 'COLUMBUS'):  # if city name is COLUMBUS add count to CHICAGO
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


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TrainClassificationRatio/"
train_classification_ratio(url + "input.xlsx", url + "inbound_output.json", url + "outbound_output.json", False)
print("finished")
