import datetime
import json

import pandas


def train_weekly_summary(input_excel_path, inbound_export_path, outbound_export_path, status):
    input_data = pandas.read_excel(input_excel_path)  # get data from excel
    input_data = input_data.get_values()  # get all values from input excel

    inbound_result = calculate(get_result_type(input_data, True))
    outbound_result = calculate(get_result_type(input_data, False))

    with open(inbound_export_path, 'w') as inbound_outfile:  # export result Json to json file
        json.dump(inbound_result, inbound_outfile, indent=4)
    with open(outbound_export_path, 'w') as outbound_outfile:  # export result Json to json file
        json.dump(outbound_result, outbound_outfile, indent=4)


def calculate(input_data):
    result = []
    if len(input_data) > 0:
        start_week = input_data[0][2].timestamp()
        end_week = input_data[0][2].timestamp() + (24 * 60 * 60 * 7)

        count = [0] * 48
        dic = {}

        index = 0
        for data in input_data:
            if start_week <= data[2].timestamp():
                if data[2].timestamp() <= end_week:

                    dic['StartDay'] = datetime.datetime.fromtimestamp(start_week).strftime("%m/%d/%Y %H:%M:%S")
                    dic['EndDay'] = datetime.datetime.fromtimestamp(end_week).strftime("%m/%d/%Y %H:%M:%S")
                    dic['NumberOfAllShipments'] = index + 1

                    count[0] += get_count(data, 20, 'E', 'AUSTELL')
                    dic['20EAUSTELL'] = format(count[0], '.2f')
                    count[1] += get_count(data, 20, 'L', 'AUSTELL')
                    dic['20LAUSTELL'] = format(count[1], '.2f')
                    count[2] += get_count(data, 40, 'E', 'AUSTELL')
                    dic['40EAUSTELL'] = format(count[2], '.2f')
                    count[3] += get_count(data, 40, 'L', 'AUSTELL')
                    dic['40LAUSTELL'] = format(count[3], '.2f')
                    count[4] += get_count(data, 45, 'E', 'AUSTELL')
                    dic['45EAUSTELL'] = format(count[4], '.2f')
                    count[5] += get_count(data, 45, 'L', 'AUSTELL')
                    dic['45LAUSTELL'] = format(count[5], '.2f')

                    count[6] += get_count(data, 20, 'E', 'GARDEN_CITY')
                    dic['20EGARDEN_CITY'] = format(count[6], '.2f')
                    count[7] += get_count(data, 20, 'L', 'GARDEN_CITY')
                    dic['20LGARDEN_CITY'] = format(count[7], '.2f')
                    count[8] += get_count(data, 40, 'E', 'GARDEN_CITY')
                    dic['40EGARDEN_CITY'] = format(count[8], '.2f')
                    count[9] += get_count(data, 40, 'L', 'GARDEN_CITY')
                    dic['40LGARDEN_CITY'] = format(count[9], '.2f')
                    count[10] += get_count(data, 45, 'E', 'GARDEN_CITY')
                    dic['45EGARDEN_CITY'] = format(count[10], '.2f')
                    count[11] += get_count(data, 45, 'L', 'GARDEN_CITY')
                    dic['45LGARDEN_CITY'] = format(count[11], '.2f')

                    count[12] += get_count(data, 20, 'E', 'CHARLESTON')
                    dic['20ECHARLESTON'] = format(count[12], '.2f')
                    count[13] += get_count(data, 20, 'L', 'CHARLESTON')
                    dic['20LCHARLESTON'] = format(count[13], '.2f')
                    count[14] += get_count(data, 40, 'E', 'CHARLESTON')
                    dic['40ECHARLESTON'] = format(count[14], '.2f')
                    count[15] += get_count(data, 40, 'L', 'CHARLESTON')
                    dic['40LCHARLESTON'] = format(count[15], '.2f')
                    count[16] += get_count(data, 45, 'E', 'CHARLESTON')
                    dic['45ECHARLESTON'] = format(count[16], '.2f')
                    count[17] += get_count(data, 45, 'L', 'CHARLESTON')
                    dic['45LCHARLESTON'] = format(count[17], '.2f')

                    count[18] += get_count(data, 20, 'E', 'GREER')
                    dic['20EGREER'] = format(count[18], '.2f')
                    count[19] += get_count(data, 20, 'L', 'GREER')
                    dic['20LGREER'] = format(count[19], '.2f')
                    count[20] += get_count(data, 40, 'E', 'GREER')
                    dic['40EGREER'] = format(count[20], '.2f')
                    count[21] += get_count(data, 40, 'L', 'GREER')
                    dic['40LGREER'] = format(count[21], '.2f')
                    count[22] += get_count(data, 45, 'E', 'GREER')
                    dic['45EGREER'] = format(count[22], '.2f')
                    count[23] += get_count(data, 45, 'L', 'GREER')
                    dic['45LGREER'] = format(count[23], '.2f')

                    count[24] += get_count(data, 20, 'E', 'MEMPHIS')
                    dic['20EMEMPHIS'] = format(count[24], '.2f')
                    count[25] += get_count(data, 20, 'L', 'MEMPHIS')
                    dic['20LMEMPHIS'] = format(count[25], '.2f')
                    count[26] += get_count(data, 40, 'E', 'MEMPHIS')
                    dic['40EMEMPHIS'] = format(count[26], '.2f')
                    count[27] += get_count(data, 40, 'L', 'MEMPHIS')
                    dic['40LMEMPHIS'] = format(count[27], '.2f')
                    count[28] += get_count(data, 45, 'E', 'MEMPHIS')
                    dic['45EMEMPHIS'] = format(count[28], '.2f')
                    count[29] += get_count(data, 45, 'L', 'MEMPHIS')
                    dic['45LMEMPHIS'] = format(count[29], '.2f')

                    count[30] += get_count(data, 20, 'E', 'CHICAGO')
                    dic['20ECHICAGO'] = format(count[30], '.2f')
                    count[31] += get_count(data, 20, 'L', 'CHICAGO')
                    dic['20LCHICAGO'] = format(count[31], '.2f')
                    count[32] += get_count(data, 40, 'E', 'CHICAGO')
                    dic['40ECHICAGO'] = format(count[32], '.2f')
                    count[33] += get_count(data, 40, 'L', 'CHICAGO')
                    dic['40LCHICAGO'] = format(count[33], '.2f')
                    count[34] += get_count(data, 45, 'E', 'CHICAGO')
                    dic['45ECHICAGO'] = format(count[34], '.2f')
                    count[35] += get_count(data, 45, 'L', 'CHICAGO')
                    dic['45LCHICAGO'] = format(count[35], '.2f')

                    count[36] += get_count(data, 20, 'E', 'JACKSONVILLE')
                    dic['20EJACKSONVILLE'] = format(count[36], '.2f')
                    count[37] += get_count(data, 20, 'L', 'JACKSONVILLE')
                    dic['20LJACKSONVILLE'] = format(count[37], '.2f')
                    count[38] += get_count(data, 40, 'E', 'JACKSONVILLE')
                    dic['40EJACKSONVILLE'] = format(count[38], '.2f')
                    count[39] += get_count(data, 40, 'L', 'JACKSONVILLE')
                    dic['40LJACKSONVILLE'] = format(count[39], '.2f')
                    count[40] += get_count(data, 45, 'E', 'JACKSONVILLE')
                    dic['45EJACKSONVILLE'] = format(count[40], '.2f')
                    count[41] += get_count(data, 45, 'L', 'JACKSONVILLE')
                    dic['45LJACKSONVILLE'] = format(count[41], '.2f')

                    count[42] += get_count(data, 20, 'E', 'NEW_ORLEANS')
                    dic['20ENEW_ORLEANS'] = format(count[42], '.2f')
                    count[43] += get_count(data, 20, 'L', 'NEW_ORLEANS')
                    dic['20LNEW_ORLEANS'] = format(count[43], '.2f')
                    count[44] += get_count(data, 40, 'E', 'NEW_ORLEANS')
                    dic['40ENEW_ORLEANS'] = format(count[44], '.2f')
                    count[45] += get_count(data, 40, 'L', 'NEW_ORLEANS')
                    dic['40LNEW_ORLEANS'] = format(count[45], '.2f')
                    count[46] += get_count(data, 45, 'E', 'NEW_ORLEANS')
                    dic['45ENEW_ORLEANS'] = format(count[46], '.2f')
                    count[47] += get_count(data, 45, 'L', 'NEW_ORLEANS')
                    dic['45LNEW_ORLEANS'] = format(count[47], '.2f')
                    index += 1
                else:
                    if len(dic) > 0:
                        result.append(dic)
                    start_week = data[2].timestamp()
                    end_week = data[2].timestamp() + (24 * 60 * 60 * 7)
                    index = 0
                    dic = {}
                    count = [0] * 48

        if len(dic) > 0:
            result.append(dic)
    return result


def get_result_type(input_data, inbound):
    result = []
    for data in input_data:
        if not inbound:
            if data[3] == "DFLC":
                result.append(data)
        else:
            if data[3] not in "DFLC":
                result.append(data)
    return result


def get_count(shipment, length, empty_loaded, city):
    if city == 'GARDEN_CITY':
        if shipment[6] == length and shipment[5] == empty_loaded and (
                shipment[10] == city or shipment[10] == 'SAVANNAH'):
            return 1
    elif city == 'CHARLESTON':
        if shipment[6] == length and shipment[5] == empty_loaded and (
                shipment[10] == city or shipment[10] == 'NORTH_CHARLESTON'):
            return 1
    elif city == 'AUSTELL':
        if shipment[6] == length and shipment[5] == empty_loaded and (
                shipment[10] == city or shipment[10] == 'ATLANTA'):
            return 1
    else:
        if shipment[6] == length and shipment[5] == empty_loaded and shipment[10] == city:
            return 1
    return 0


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TrainWeeklySummary/"
train_weekly_summary(url + "input.xlsx", url + "inbound_output.json", url + "outbound_output.json", False)
print("finished")
