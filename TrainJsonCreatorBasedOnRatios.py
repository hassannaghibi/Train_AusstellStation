import datetime
import json


def train_json_creator_based_on_ratios(input_path, trains_export_path, consists_export_path):
    with open(input_path) as json_file:
        values = json.load(json_file)
        calculate_trains(values, trains_export_path)
        calculation_consists(values, consists_export_path, 89)


def calculation_consists(values, export_path, threshold):
    final_dic = {}
    final_result = []
    values = sort_by_date(values)
    for data in values:
        day_of_week = set_day(data['DayOfWeek'].split(', '))
        # times = set_time(data['Time'].split(', '))
        times = data['Time']
        for i in range(len(day_of_week)):
            railcars = []

            result = {}
            result['trainSymbol'] = data['Train Symbol']
            result['trackId'] = 'RH01'
            result['arrivalTime'] = datetime.datetime.fromtimestamp(convert_str_to_time(times[i]).timestamp()).strftime(
                "%Y-%m-%d %H:%M:%S")
            result['direction'] = data['Inbound/OutBound']
            status = data['Inbound/OutBound']
            count_20 = int(float(data['20']) / 2)
            count_40 = int((int(float(data['40'])) - count_20) / 2)
            count_45 = int(float(data['45']) / 2)

            cars = count_40 + count_20 + count_45
            th_index = int(cars / (abs(cars - threshold))) if cars > threshold else 1 if (abs(
                cars - threshold) / cars) < 1 else abs(cars - threshold) / cars
            th = False
            if cars % th_index != 0:
                th = True

            th_status = False
            if cars < th_index:
                th_status = True

            index = 0
            while True:
                if status == 'O':
                    if index >= threshold:
                        break
                    else:
                        railcars.append({
                            "aarType": "S615",
                            "carInit": "AAAA",
                            "carNum": 123456,
                            "shipments": [
                                {
                                    "wellCd": "A",
                                    "loadingLevelCd": "1",
                                    "shipment": {
                                        "eqInit": "AAAA",
                                        "eqNum": 123456,
                                        "length": "40",
                                        "eqTypeCd": "C",
                                        "isEmpty": False,
                                        "boundTypeCd": data['Inbound/OutBound'],
                                        "isWheeled": True,
                                        "priority": 11.3
                                    }
                                },
                                {
                                    "wellCd": "A",
                                    "loadingLevelCd": "2",
                                    "shipment": {
                                        "eqInit": "AAAA",
                                        "eqNum": 123456,
                                        "length": "40",
                                        "eqTypeCd": "C",
                                        "isEmpty": False,
                                        "boundTypeCd": data['Inbound/OutBound'],
                                        "isWheeled": True,
                                        "priority": 11.3
                                    }
                                }
                            ]
                        })
                        index += 1
                else:
                    if index >= threshold:
                        break
                    if not th_status:
                        if index > 0 and (index % 16 == 0 or (count_20 <= 0 and count_40 <= 0)):
                            if count_45 > 0:
                                # 45 45
                                count_45 -= 1
                                railcars.append({
                                    "aarType": "S615",
                                    "carInit": "AAAA",
                                    "carNum": 123456,
                                    "shipments": [
                                        {
                                            "wellCd": "A",
                                            "loadingLevelCd": "1",
                                            "shipment": {
                                                "eqInit": "AAAA",
                                                "eqNum": 123456,
                                                "length": "45",
                                                "eqTypeCd": "C",
                                                "isEmpty": False,
                                                "boundTypeCd": data['Inbound/OutBound'],
                                                "isWheeled": True,
                                                "priority": 11.3
                                            }
                                        },
                                        {
                                            "wellCd": "A",
                                            "loadingLevelCd": "2",
                                            "shipment": {
                                                "eqInit": "AAAA",
                                                "eqNum": 123456,
                                                "length": "45",
                                                "eqTypeCd": "C",
                                                "isEmpty": False,
                                                "boundTypeCd": data['Inbound/OutBound'],
                                                "isWheeled": True,
                                                "priority": 11.3
                                            }
                                        }
                                    ]
                                })
                                index += 1
                        else:
                            if count_40 > 0:
                                for jj in range(3):
                                    # 40 40
                                    count_40 -= 1
                                    railcars.append({
                                        "aarType": "S615",
                                        "carInit": "AAAA",
                                        "carNum": 123456,
                                        "shipments": [
                                            {
                                                "wellCd": "A",
                                                "loadingLevelCd": "1",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "40",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            },
                                            {
                                                "wellCd": "A",
                                                "loadingLevelCd": "2",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "40",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            }
                                        ]
                                    })
                                    index += 1
                            if count_20 > 0:
                                # 20 20 40
                                count_20 -= 1
                                railcars.append({
                                    "aarType": "S615",
                                    "carInit": "AAAA",
                                    "carNum": 123456,
                                    "shipments": [
                                        {
                                            "wellCd": "A1",
                                            "loadingLevelCd": "1",
                                            "shipment": {
                                                "eqInit": "AAAA",
                                                "eqNum": 123456,
                                                "length": "20",
                                                "eqTypeCd": "C",
                                                "isEmpty": False,
                                                "boundTypeCd": data['Inbound/OutBound'],
                                                "isWheeled": True,
                                                "priority": 11.3
                                            }
                                        },
                                        {
                                            "wellCd": "A2",
                                            "loadingLevelCd": "1",
                                            "shipment": {
                                                "eqInit": "AAAA",
                                                "eqNum": 123456,
                                                "length": "20",
                                                "eqTypeCd": "C",
                                                "isEmpty": False,
                                                "boundTypeCd": data['Inbound/OutBound'],
                                                "isWheeled": True,
                                                "priority": 11.3
                                            }
                                        },
                                        {
                                            "wellCd": "A",
                                            "loadingLevelCd": "2",
                                            "shipment": {
                                                "eqInit": "AAAA",
                                                "eqNum": 123456,
                                                "length": "40",
                                                "eqTypeCd": "C",
                                                "isEmpty": False,
                                                "boundTypeCd": data['Inbound/OutBound'],
                                                "isWheeled": True,
                                                "priority": 11.3
                                            }
                                        }
                                    ]
                                })
                                index += 1

                        if count_45 <= 0 and count_20 <= 0 and count_40 <= 0:
                            if index >= threshold:
                                break
                            elif index < threshold:
                                railcars.append({
                                    "aarType": "S615",
                                    "carInit": "EMPTYCAR",
                                    "carNum": 123456,
                                    "shipments": [
                                        {
                                            "wellCd": "A",
                                            "loadingLevelCd": "1",
                                            "shipment": {
                                                "eqInit": "AAAA",
                                                "eqNum": 123456,
                                                "length": "40",
                                                "eqTypeCd": "C",
                                                "isEmpty": False,
                                                "boundTypeCd": data['Inbound/OutBound'],
                                                "isWheeled": True,
                                                "priority": 11.3
                                            }
                                        },
                                        {
                                            "wellCd": "A",
                                            "loadingLevelCd": "2",
                                            "shipment": {
                                                "eqInit": "AAAA",
                                                "eqNum": 123456,
                                                "length": "40",
                                                "eqTypeCd": "C",
                                                "isEmpty": False,
                                                "boundTypeCd": data['Inbound/OutBound'],
                                                "isWheeled": True,
                                                "priority": 11.3
                                            }
                                        }
                                    ]
                                })
                                index += 1
                                continue
                        if index > 0 and index % th_index == 0:
                            railcars.append({
                                "aarType": "S615",
                                "carInit": "EMPTYCAR",
                                "carNum": 123456,
                                "shipments": [
                                    {
                                        "wellCd": "A",
                                        "loadingLevelCd": "1",
                                        "shipment": {
                                            "eqInit": "AAAA",
                                            "eqNum": 123456,
                                            "length": "40",
                                            "eqTypeCd": "C",
                                            "isEmpty": False,
                                            "boundTypeCd": data['Inbound/OutBound'],
                                            "isWheeled": True,
                                            "priority": 11.3
                                        }
                                    },
                                    {
                                        "wellCd": "A",
                                        "loadingLevelCd": "2",
                                        "shipment": {
                                            "eqInit": "AAAA",
                                            "eqNum": 123456,
                                            "length": "40",
                                            "eqTypeCd": "C",
                                            "isEmpty": False,
                                            "boundTypeCd": data['Inbound/OutBound'],
                                            "isWheeled": True,
                                            "priority": 11.3
                                        }
                                    }
                                ]
                            })
                            index += 1
                            continue
                        if th and index == threshold:
                            th = False
                            railcars.append({
                                "aarType": "S615",
                                "carInit": "EMPTYCAR",
                                "carNum": 123456,
                                "shipments": [
                                    {
                                        "wellCd": "A",
                                        "loadingLevelCd": "1",
                                        "shipment": {
                                            "eqInit": "AAAA",
                                            "eqNum": 123456,
                                            "length": "40",
                                            "eqTypeCd": "C",
                                            "isEmpty": False,
                                            "boundTypeCd": data['Inbound/OutBound'],
                                            "isWheeled": True,
                                            "priority": 11.3
                                        }
                                    },
                                    {
                                        "wellCd": "A",
                                        "loadingLevelCd": "2",
                                        "shipment": {
                                            "eqInit": "AAAA",
                                            "eqNum": 123456,
                                            "length": "40",
                                            "eqTypeCd": "C",
                                            "isEmpty": False,
                                            "boundTypeCd": data['Inbound/OutBound'],
                                            "isWheeled": True,
                                            "priority": 11.3
                                        }
                                    }
                                ]
                            })
                            index += 1
                            continue
                    else:
                        if index > 0 and index % th_index == 0:
                            if index % 16 == 0 or (count_20 <= 0 and count_40 <= 0):
                                if count_45 > 0:
                                    # 45 45
                                    count_45 -= 1
                                    railcars.append({
                                        "aarType": "S615",
                                        "carInit": "AAAA",
                                        "carNum": 123456,
                                        "shipments": [
                                            {
                                                "wellCd": "A",
                                                "loadingLevelCd": "1",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "45",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            },
                                            {
                                                "wellCd": "A",
                                                "loadingLevelCd": "2",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "45",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            }
                                        ]
                                    })
                                    index += 1
                                else:
                                    railcars.append({
                                        "aarType": "S615",
                                        "carInit": "EMPTYCAR",
                                        "carNum": 123456,
                                        "shipments": [
                                            {
                                                "wellCd": "A",
                                                "loadingLevelCd": "1",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "40",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            },
                                            {
                                                "wellCd": "A",
                                                "loadingLevelCd": "2",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "40",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            }
                                        ]
                                    })
                                    index += 1
                                    continue
                            else:
                                if count_40 > 0:
                                    for jj in range(3):
                                        # 40 40
                                        count_40 -= 1
                                        railcars.append({
                                            "aarType": "S615",
                                            "carInit": "AAAA",
                                            "carNum": 123456,
                                            "shipments": [
                                                {
                                                    "wellCd": "A",
                                                    "loadingLevelCd": "1",
                                                    "shipment": {
                                                        "eqInit": "AAAA",
                                                        "eqNum": 123456,
                                                        "length": "40",
                                                        "eqTypeCd": "C",
                                                        "isEmpty": False,
                                                        "boundTypeCd": data['Inbound/OutBound'],
                                                        "isWheeled": True,
                                                        "priority": 11.3
                                                    }
                                                },
                                                {
                                                    "wellCd": "A",
                                                    "loadingLevelCd": "2",
                                                    "shipment": {
                                                        "eqInit": "AAAA",
                                                        "eqNum": 123456,
                                                        "length": "40",
                                                        "eqTypeCd": "C",
                                                        "isEmpty": False,
                                                        "boundTypeCd": data['Inbound/OutBound'],
                                                        "isWheeled": True,
                                                        "priority": 11.3
                                                    }
                                                }
                                            ]
                                        })
                                        index += 1
                                if count_20 > 0:
                                    # 20 20 40
                                    count_20 -= 1
                                    railcars.append({
                                        "aarType": "S615",
                                        "carInit": "AAAA",
                                        "carNum": 123456,
                                        "shipments": [
                                            {
                                                "wellCd": "A1",
                                                "loadingLevelCd": "1",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "20",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            },
                                            {
                                                "wellCd": "A2",
                                                "loadingLevelCd": "1",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "20",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            },
                                            {
                                                "wellCd": "A",
                                                "loadingLevelCd": "2",
                                                "shipment": {
                                                    "eqInit": "AAAA",
                                                    "eqNum": 123456,
                                                    "length": "40",
                                                    "eqTypeCd": "C",
                                                    "isEmpty": False,
                                                    "boundTypeCd": data['Inbound/OutBound'],
                                                    "isWheeled": True,
                                                    "priority": 11.3
                                                }
                                            }
                                        ]
                                    })
                                    index += 1
                        else:
                            railcars.append({
                                "aarType": "S615",
                                "carInit": "EMPTYCAR",
                                "carNum": 123456,
                                "shipments": [
                                    {
                                        "wellCd": "A",
                                        "loadingLevelCd": "1",
                                        "shipment": {
                                            "eqInit": "AAAA",
                                            "eqNum": 123456,
                                            "length": "40",
                                            "eqTypeCd": "C",
                                            "isEmpty": False,
                                            "boundTypeCd": data['Inbound/OutBound'],
                                            "isWheeled": True,
                                            "priority": 11.3
                                        }
                                    },
                                    {
                                        "wellCd": "A",
                                        "loadingLevelCd": "2",
                                        "shipment": {
                                            "eqInit": "AAAA",
                                            "eqNum": 123456,
                                            "length": "40",
                                            "eqTypeCd": "C",
                                            "isEmpty": False,
                                            "boundTypeCd": data['Inbound/OutBound'],
                                            "isWheeled": True,
                                            "priority": 11.3
                                        }
                                    }
                                ]
                            })
                            index += 1
                        if count_45 <= 0 and count_20 <= 0 and count_40 <= 0 and index == threshold:
                            break

            result['railcars'] = railcars
            final_result.append(result)

    final_dic['consists'] = final_result
    with open(export_path, 'w') as outbound_outfile:  # export result Json to json file
        json.dump(final_dic, outbound_outfile, indent=2)


def calculate_trains(values, export_path):
    final_dic = {}
    final_result = []
    for data in values:
        day_of_week = set_day(data['DayOfWeek'].split(', '))
        times = set_time(data['Time'].split(', '))
        for i in range(len(day_of_week)):
            result = {}
            result['trainSymbol'] = data['Train Symbol']
            result['direction'] = data['Inbound/OutBound']
            result['arrivalTime'] = datetime.datetime.fromtimestamp(times[i].timestamp()).strftime("%Y-%m-%d %H:%M:%S")
            result['truakId'] = 'RH01'
            final_result.append(result)
    final_dic['trains'] = final_result
    with open(export_path, 'w') as outbound_outfile:  # export result Json to json file
        json.dump(final_dic, outbound_outfile, indent=2)


def set_day(values):
    result = []
    for data in values:
        array = data.split('= ')
        result.append(array[1])
    return result


def set_time(values):
    result = []
    for data in values:
        array = data.split('= ')
        result.append(convert_str_to_time(array[1]))
    return result


def convert_str_to_time(date):  # convert str date to real date type
    start_date = date.split()
    date = start_date[0].split("/")  # split date with /
    time = start_date[1].split(":")  # split time with :

    year = int(date[2])
    month = int(date[0])
    day = int(date[1])
    hour = int(time[0])
    minute = int(time[1])
    second = int(time[2])

    result = datetime.datetime(year, month, day, hour, minute, second)  # convert str to time
    return result


def sort_by_date(values):
    result = []
    min_time = 0
    for data in values:
        times = set_time(data['Time'].split(', '))
        current_time = []
        c_time = 0
        for i in range(len(times)):
            time = datetime.datetime.fromtimestamp(times[i].timestamp()).strftime("%m/%d/%Y %H:%M:%S")
            if len(current_time) == 0 and c_time == 0:
                current_time.append(time)
            elif times[i].timestamp() < c_time:
                c_time = times[i].timestamp()
                current_time.insert(1, current_time[0])
                current_time.insert(0, time)
            else:
                current_time.append(time)
        data["Time"] = current_time

        if min_time == 0:
            min_time = convert_str_to_time(data["Time"][0]).timestamp()
            result.append(data)
        elif convert_str_to_time(data["Time"][0]).timestamp() < min_time:
            min_time = convert_str_to_time(data["Time"][0]).timestamp()
            result.insert(1, result[0])
            result.insert(0, data)
        else:
            result.append(data)
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TrainJsonCreatorBasedOnRatios/"
train_json_creator_based_on_ratios(url + "input.json", url + "trainSchedule.json", url + "trainConsists.json")
print("finished")
