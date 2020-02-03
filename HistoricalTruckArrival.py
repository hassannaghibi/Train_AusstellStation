import datetime
import json

import pandas


def calculate_truck_arrival(input_excel_path, export_path, start_time):
    input_data = pandas.read_excel(input_excel_path)  # get data from excel
    input_data = input_data.get_values()  # get all values from input excel

    start_time = convert_str_to_time(start_time).timestamp()  # convert str to time
    result = []
    index = 1
    for data in input_data:  # for in all rows in excel data
        time = data[2].timestamp()
        result.append({  # add to result json
            'id': index,
            'ArrivalTime': int((time - start_time) / 60),  # calculate arrival time
            'EventType': data[3],
            'EqInitNr': data[0],
            'WayBill': data[1],
            'EqLength': data[5],
            'EqType': data[6],
            'IsEmpty': True if data[4] == "E" else False,
            'NET_WGT': data[15],
            'SHPR_CUST_NM': data[16],
            'CY_NotStackable': data[17],
            'HoursStayedInParking': data[18],
            'EqDest': data[13],
            'EqDestSt': data[14],
            'EqNsDest': data[9],
            'EqNsDestSt': data[10],
            'EqOrigin': data[11],
            'EqOriginSt': data[12],
            'EqNsOrigin': data[7],
            'EqNsOriginSt': data[8]
        })
        index += 1

    with open(export_path, 'w') as outfile:  # export result Json to json file
        json.dump(result, outfile, indent=2)


def convert_str_to_time(date):
    start_date = date.split()
    date = start_date[0].split("/")
    time = start_date[1].split(":")

    year = int(date[2])
    month = int(date[0])
    day = int(date[1])
    hour = int(time[0])
    minute = int(time[1])

    result = datetime.datetime(year, month, day, hour, minute, 0)
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/HistoricalTruckArrival/"
calculate_truck_arrival(url + "input.xlsx", url + "output.json",
                        "11/13/2018 0:05")  # shours before actual time due to time zone difference
print("finished")
