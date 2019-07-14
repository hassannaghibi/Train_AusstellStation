import calendar
import json

import pandas


def train_classification_ratio(input_excel_path, inbound_export_path, outbound_export_path, status):
    input_data = pandas.read_excel(input_excel_path)  # get data from excel
    input_data = input_data.get_values()  # get all values from input excel

    inbound_result = []  # inbound result list
    outbound_result = []  # outbound result list
    trains = []  # train list

    index = 0
    for data in input_data:  # for in all excel data
        if index <= len(input_data):  # if any row to calculate
            train = []
            if index > 0:
                train = [input_data[index]]  # add first shipment to train
            sub_index = 0
            for i in range(index, len(input_data)):  # for from current index to last row of excel
                if input_data[index][2] == input_data[index + sub_index][2] and input_data[index][4] == \
                        input_data[index + sub_index][
                            4]:  # if current shipment dateTime == shipment dateTime and couple trn col is equal
                    train.append(input_data[index + sub_index])  # add shipment to train list
                else:
                    trains.append(train)  # if no any shipment add train to trains list and go to add other train
                    break

                if i + 1 == len(input_data):  # if last row
                    trains.append(train)  # add train list to trains
                sub_index += 1
            index = index + sub_index + 1
        else:
            break  # if list is finished exit from for

    index = 0
    for train in trains:  # for in train list
        dic = {}
        if not repetitious(train[0][4], inbound_result, outbound_result):  # if not repetitious
            count = [0] * 48
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
                        coefficient = sub_index + 1  # if status is true all train length to ratio

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

                    count[0] += get_count(sub_train, 20, 'E', 'AUSTELL')  # get count with 3 parameter
                    dic['20EAUSTELL'] = format((count[0] / coefficient) * sub_coefficient, '.2f')
                    count[1] += get_count(sub_train, 20, 'L', 'AUSTELL')
                    dic['20LAUSTELL'] = format((count[1] / coefficient) * sub_coefficient, '.2f')
                    count[2] += get_count(sub_train, 40, 'E', 'AUSTELL')
                    dic['40EAUSTELL'] = format((count[2] / coefficient) * sub_coefficient, '.2f')
                    count[3] += get_count(sub_train, 40, 'L', 'AUSTELL')
                    dic['40LAUSTELL'] = format((count[3] / coefficient) * sub_coefficient, '.2f')
                    count[4] += get_count(sub_train, 45, 'E', 'AUSTELL')
                    dic['45EAUSTELL'] = format((count[4] / coefficient) * sub_coefficient, '.2f')
                    count[5] += get_count(sub_train, 45, 'L', 'AUSTELL')
                    dic['45LAUSTELL'] = format((count[5] / coefficient) * sub_coefficient, '.2f')

                    count[6] += get_count(sub_train, 20, 'E', 'GARDEN_CITY')
                    dic['20EGARDEN_CITY'] = format((count[6] / coefficient) * sub_coefficient, '.2f')
                    count[7] += get_count(sub_train, 20, 'L', 'GARDEN_CITY')
                    dic['20LGARDEN_CITY'] = format((count[7] / coefficient) * sub_coefficient, '.2f')
                    count[8] += get_count(sub_train, 40, 'E', 'GARDEN_CITY')
                    dic['40EGARDEN_CITY'] = format((count[8] / coefficient) * sub_coefficient, '.2f')
                    count[9] += get_count(sub_train, 40, 'L', 'GARDEN_CITY')
                    dic['40LGARDEN_CITY'] = format((count[9] / coefficient) * sub_coefficient, '.2f')
                    count[10] += get_count(sub_train, 45, 'E', 'GARDEN_CITY')
                    dic['45EGARDEN_CITY'] = format((count[10] / coefficient) * sub_coefficient, '.2f')
                    count[11] += get_count(sub_train, 45, 'L', 'GARDEN_CITY')
                    dic['45LGARDEN_CITY'] = format((count[11] / coefficient) * sub_coefficient, '.2f')

                    count[12] += get_count(sub_train, 20, 'E', 'CHARLESTON')
                    dic['20ECHARLESTON'] = format((count[12] / coefficient) * sub_coefficient, '.2f')
                    count[13] += get_count(sub_train, 20, 'L', 'CHARLESTON')
                    dic['20LCHARLESTON'] = format((count[13] / coefficient) * sub_coefficient, '.2f')
                    count[14] += get_count(sub_train, 40, 'E', 'CHARLESTON')
                    dic['40ECHARLESTON'] = format((count[14] / coefficient) * sub_coefficient, '.2f')
                    count[15] += get_count(sub_train, 40, 'L', 'CHARLESTON')
                    dic['40LCHARLESTON'] = format((count[15] / coefficient) * sub_coefficient, '.2f')
                    count[16] += get_count(sub_train, 45, 'E', 'CHARLESTON')
                    dic['45ECHARLESTON'] = format((count[16] / coefficient) * sub_coefficient, '.2f')
                    count[17] += get_count(sub_train, 45, 'L', 'CHARLESTON')
                    dic['45LCHARLESTON'] = format((count[17] / coefficient) * sub_coefficient, '.2f')

                    count[18] += get_count(sub_train, 20, 'E', 'GREER')
                    dic['20EGREER'] = format((count[18] / coefficient) * sub_coefficient, '.2f')
                    count[19] += get_count(sub_train, 20, 'L', 'GREER')
                    dic['20LGREER'] = format((count[19] / coefficient) * sub_coefficient, '.2f')
                    count[20] += get_count(sub_train, 40, 'E', 'GREER')
                    dic['40EGREER'] = format((count[20] / coefficient) * sub_coefficient, '.2f')
                    count[21] += get_count(sub_train, 40, 'L', 'GREER')
                    dic['40LGREER'] = format((count[21] / coefficient) * sub_coefficient, '.2f')
                    count[22] += get_count(sub_train, 45, 'E', 'GREER')
                    dic['45EGREER'] = format((count[22] / coefficient) * sub_coefficient, '.2f')
                    count[23] += get_count(sub_train, 45, 'L', 'GREER')
                    dic['45LGREER'] = format((count[23] / coefficient) * sub_coefficient, '.2f')

                    count[24] += get_count(sub_train, 20, 'E', 'MEMPHIS')
                    dic['20EMEMPHIS'] = format((count[24] / coefficient) * sub_coefficient, '.2f')
                    count[25] += get_count(sub_train, 20, 'L', 'MEMPHIS')
                    dic['20LMEMPHIS'] = format((count[25] / coefficient) * sub_coefficient, '.2f')
                    count[26] += get_count(sub_train, 40, 'E', 'MEMPHIS')
                    dic['40EMEMPHIS'] = format((count[26] / coefficient) * sub_coefficient, '.2f')
                    count[27] += get_count(sub_train, 40, 'L', 'MEMPHIS')
                    dic['40LMEMPHIS'] = format((count[27] / coefficient) * sub_coefficient, '.2f')
                    count[28] += get_count(sub_train, 45, 'E', 'MEMPHIS')
                    dic['45EMEMPHIS'] = format((count[28] / coefficient) * sub_coefficient, '.2f')
                    count[29] += get_count(sub_train, 45, 'L', 'MEMPHIS')
                    dic['45LMEMPHIS'] = format((count[29] / coefficient) * sub_coefficient, '.2f')

                    count[30] += get_count(sub_train, 20, 'E', 'CHICAGO')
                    dic['20ECHICAGO'] = format((count[30] / coefficient) * sub_coefficient, '.2f')
                    count[31] += get_count(sub_train, 20, 'L', 'CHICAGO')
                    dic['20LCHICAGO'] = format((count[31] / coefficient) * sub_coefficient, '.2f')
                    count[32] += get_count(sub_train, 40, 'E', 'CHICAGO')
                    dic['40ECHICAGO'] = format((count[32] / coefficient) * sub_coefficient, '.2f')
                    count[33] += get_count(sub_train, 40, 'L', 'CHICAGO')
                    dic['40LCHICAGO'] = format((count[33] / coefficient) * sub_coefficient, '.2f')
                    count[34] += get_count(sub_train, 45, 'E', 'CHICAGO')
                    dic['45ECHICAGO'] = format((count[34] / coefficient) * sub_coefficient, '.2f')
                    count[35] += get_count(sub_train, 45, 'L', 'CHICAGO')
                    dic['45LCHICAGO'] = format((count[35] / coefficient) * sub_coefficient, '.2f')

                    count[36] += get_count(sub_train, 20, 'E', 'JACKSONVILLE')
                    dic['20EJACKSONVILLE'] = format((count[36] / coefficient) * sub_coefficient, '.2f')
                    count[37] += get_count(sub_train, 20, 'L', 'JACKSONVILLE')
                    dic['20LJACKSONVILLE'] = format((count[37] / coefficient) * sub_coefficient, '.2f')
                    count[38] += get_count(sub_train, 40, 'E', 'JACKSONVILLE')
                    dic['40EJACKSONVILLE'] = format((count[38] / coefficient) * sub_coefficient, '.2f')
                    count[39] += get_count(sub_train, 40, 'L', 'JACKSONVILLE')
                    dic['40LJACKSONVILLE'] = format((count[39] / coefficient) * sub_coefficient, '.2f')
                    count[40] += get_count(sub_train, 45, 'E', 'JACKSONVILLE')
                    dic['45EJACKSONVILLE'] = format((count[40] / coefficient) * sub_coefficient, '.2f')
                    count[41] += get_count(sub_train, 45, 'L', 'JACKSONVILLE')
                    dic['45LJACKSONVILLE'] = format((count[41] / coefficient) * sub_coefficient, '.2f')

                    count[42] += get_count(sub_train, 20, 'E', 'NEW_ORLEANS')
                    dic['20ENEW_ORLEANS'] = format((count[42] / coefficient) * sub_coefficient, '.2f')
                    count[43] += get_count(sub_train, 20, 'L', 'NEW_ORLEANS')
                    dic['20LNEW_ORLEANS'] = format((count[43] / coefficient) * sub_coefficient, '.2f')
                    count[44] += get_count(sub_train, 40, 'E', 'NEW_ORLEANS')
                    dic['40ENEW_ORLEANS'] = format((count[44] / coefficient) * sub_coefficient, '.2f')
                    count[45] += get_count(sub_train, 40, 'L', 'NEW_ORLEANS')
                    dic['40LNEW_ORLEANS'] = format((count[45] / coefficient) * sub_coefficient, '.2f')
                    count[46] += get_count(sub_train, 45, 'E', 'NEW_ORLEANS')
                    dic['45ENEW_ORLEANS'] = format((count[46] / coefficient) * sub_coefficient, '.2f')
                    count[47] += get_count(sub_train, 45, 'L', 'NEW_ORLEANS')
                    dic['45LNEW_ORLEANS'] = format((count[47] / coefficient) * sub_coefficient, '.2f')
                    sub_index += 1

        if len(dic) > 0:  # if dic length >0
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
