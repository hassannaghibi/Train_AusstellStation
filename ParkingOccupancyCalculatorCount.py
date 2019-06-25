import datetime

import pandas


def inside_parking_count(input_path, export_path, to_time, number_of_days, from_time, container_distance,
                         consider_cy_not_stackable):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    from_time = (24 * 60 * 60) * from_time
    final_result = []
    current_time = convert_str_to_time(to_time, False, False)
    index = 0
    for index in range(number_of_days):
        current_time = convert_str_to_time(current_time.strftime("%m/%d/%Y %H:%M:%S"), True,
                                           True if index == 0 else False)  # convert datetime to timestamp
        count_20 = 0
        count_40 = 0
        count_45 = 0
        eqinitnr = []
        for data in values:
            sub_time = data[2]
            if consider_cy_not_stackable:
                if not data[17]:
                    if current_time.timestamp() - from_time <= sub_time.timestamp() <= current_time.timestamp():  # if this shipment time
                        if data[3] == "RMFC" or data[3] == "ICHR":  # if the event type is arrive
                            if data[0] not in eqinitnr:  # if current eqinitnr not in eqinitnr list, counted
                                type = get_type_by_max_date(data[0], current_time.timestamp(),
                                                            values)  # get last type by time
                                if type == "RMFC" or type == "ICHR":  # if the event type is arrive
                                    eqinitnr.append(data[0])  # add current eqinitnr to list
                                    if data[5] == 20:
                                        count_20 += 1  # add count length 20
                                    elif data[5] == 40:
                                        count_40 += 1  # add count length 40
                                    elif data[5] == 45:
                                        count_45 += 1  # add count length 45
            else:
                if current_time.timestamp() - from_time <= sub_time.timestamp() <= current_time.timestamp():  # if this shipment time
                    if data[3] == "RMFC" or data[3] == "ICHR":  # if the event type is arrive
                        if data[0] not in eqinitnr:  # if current eqinitnr not in eqinitnr list, counted
                            type = get_type_by_max_date(data[0], current_time.timestamp(),
                                                        values)  # get last type by time
                            if type == "RMFC" or type == "ICHR":  # if the event type is arrive
                                eqinitnr.append(data[0])  # add current eqinitnr to list
                                if data[5] == 20:
                                    count_20 += 1  # add count length 20
                                elif data[5] == 40:
                                    count_40 += 1  # add count length 40
                                elif data[5] == 45:
                                    count_45 += 1  # add count length 45

        normalize = ((20 + container_distance) * count_20) + ((40 + container_distance) * count_40) + (
                (45 + container_distance) * count_45)  # normalizing

        result = []
        result.insert(0, current_time.strftime(
            "%m/%d/%Y %H:%M:%S"))  # add current time with this format mm/dd/yyyy hh:mm:ss
        result.insert(1, count_20)
        result.insert(2, count_40)
        result.insert(3, count_45)
        result.insert(4, normalize)
        print(str(index) + "/" + str(len(values)) + "=>" + str(result))
        final_result.append(result)  # appending to result array to showing in excel file

    header = ["Date", "20", "40", "45", "Normalized Occupied capacity"]
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
    result = ""
    time = 0
    for data in values:
        to_date = data[2].timestamp()
        if data[0] == iq_init_nr:
            if date >= to_date > time:  # find the last date in shipment
                time = to_date
                result = data[3]
    return result


print("Start inside_parking_count")
url = "C:/Users/Hassan/Desktop/pythonExport/ParkingOccupancyCalculator/"
inside_parking_count(url + 'input.xlsx', url + "ParkingOccupiedCapacity.xlsx", "5/5/2018 17:30:00", 30, 3,
                     2,
                     False)  # startdate, daycount, time_window, container distance, the code work with greenwich time zone to the hour is shifted 5 hours back due to time zone issue, it is actually 13:00 instead of 8:00
print("Finished")
