import datetime

import pandas


def shipment_in_parking(input_path, export_path, start_date, day_window, consider_cy_not_stackable):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    day_window = (24 * 60 * 60) * day_window
    final_result = []
    current_time = convert_str_to_time(start_date, False, False)
    eqinitnr = []

    for data in values:
        hour_stayed = 0
        in_parking = False
        sub_time = data[2]
        if consider_cy_not_stackable:
            if not data[17]:
                if current_time.timestamp() - day_window <= sub_time.timestamp() <= current_time.timestamp():  # if this shipment time
                    if data[3] == "RMFC" or data[3] == "ICHR":  # if the event type is arrive
                        if data[0] not in eqinitnr:  # if current eqinitnr not in eqinitnr list, counted
                            max_data = get_type_by_max_date(data[0], current_time.timestamp(),
                                                            values)  # get last type by time
                            type = max_data[1]
                            max_date = max_data[0]
                            if (
                                    type == "RMFC" or type == "ICHR") and sub_time == max_date:  # if the event type is arrive
                                eqinitnr.append(data[0])  # add current eqinitnr to list
                                in_parking = True
                                hour_stayed = format(((current_time.timestamp() - sub_time.timestamp()) / 3600), '.2f')
        else:
            if current_time.timestamp() - day_window <= sub_time.timestamp() <= current_time.timestamp():  # if this shipment time
                if data[3] == "RMFC" or data[3] == "ICHR":  # if the event type is arrive
                    if data[0] not in eqinitnr:  # if current eqinitnr not in eqinitnr list, counted
                        max_data = get_type_by_max_date(data[0], current_time.timestamp(),
                                                        values)  # get last type by time
                        type = max_data[1]
                        max_date = max_data[0]
                        if (type == "RMFC" or type == "ICHR") and sub_time == max_date:  # if the event type is arrive
                            eqinitnr.append(data[0])  # add current eqinitnr to list
                            in_parking = True
                            hour_stayed = format(((current_time.timestamp() - sub_time.timestamp()) / 3600), '.2f')

        result = []
        result.insert(0, data[0])
        result.insert(1, data[1])
        result.insert(2, sub_time)
        result.insert(3, data[3])
        result.insert(4, data[4])
        result.insert(5, data[5])
        result.insert(6, data[6])
        result.insert(7, data[7])
        result.insert(8, data[8])
        result.insert(9, data[9])
        result.insert(10, data[10])
        result.insert(11, data[11])
        result.insert(12, data[12])
        result.insert(13, data[13])
        result.insert(14, data[14])
        result.insert(15, data[15])
        result.insert(16, data[16])
        result.insert(17, data[17])
        result.insert(18, in_parking)
        result.insert(19, hour_stayed)
        final_result.append(result)  # appending to result array to showing in excel file

    header = ["EQ_INIT_NR", "WAYBILL", "EVENT TIMESTAMP EST", "EVENT TYPE", "LOADED EMPTY", "EQ LENGTH", "EQ TYPE",
              "NS ORGIN",
              "NS ORIGIN ST", "NS DEST", "NS DEST ST", "ORGN", "ORGN ST", "DEST", "DEST ST", "NET_WGT", "SHPR_CUST_NM",
              "CY_NotStackable",
              "IS SHIPMENT IN PARKING", "HOURS STAYED IN PARKING"]
    pandas.DataFrame(final_result, [""] * len(final_result), header).to_excel(export_path)  # export data


def convert_str_to_time(date, increment, is_first):
    start_date = date.split()
    date = start_date[0].split("/")
    time = start_date[1].split(":")

    year = int(date[2])
    month = int(date[0])
    day = int(date[1])

    hour = int(time[0])
    minute = int(time[1])

    result = datetime.datetime(year, month, day, hour, minute, 0)  # change str to real date
    if increment and is_first == False:
        result += datetime.timedelta(days=1)  # add one day if increment is true
    return result


def get_type_by_max_date(iq_init_nr, date, values):
    result = ["", ""]
    time = 0
    for data in values:
        to_date = data[2].timestamp()
        if data[0] == iq_init_nr:
            if date >= to_date > time:  # find the last date in shipment
                time = to_date
                result[0] = data[2]  # date
                result[1] = data[3]  # type
    return result


print("Start shipment_in_parking")
url = "C:/Users/Hassan/Desktop/pythonExport/ParkingOccupancyCalculator/"
shipment_in_parking(url + 'input.xlsx', url + "ShipmentInParking.xlsx", "5/30/2018 17:30:00",
                    15, False)  # startday, time_window
print("Finished")
