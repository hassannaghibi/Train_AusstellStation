import datetime
import json
import random


def train_json_creator_based_on_ratios(input_path, trains_export_path, consists_export_path):
    with open(input_path) as json_file:
        values = json.load(json_file)
        calculate_trains(values, trains_export_path)
        calculation_consists(values, consists_export_path)


def calculation_consists(values, export_path):
    final_dic = {}
    final_result = []
    for data in values:
        day_of_week = set_day(data['DayOfWeek'].split(', '))
        times = set_time(data['Time'].split(', '))
        for i in range(len(day_of_week)):
            railcars = []

            result = {}
            result['trainSymbol'] = data['Train Symbol']
            result['truckId'] = 'RH01'
            result['arrivalTime'] = datetime.datetime.fromtimestamp(times[i].timestamp()).strftime("%m/%d/%Y %H:%M:%S")
            result['direction'] = data['Inbound/OutBound']

            count_20 = int(float(data['20']) / 2)
            count_40 = int(float(data['40'])) - count_20
            count_45 = int(float(data['45']) / 2)

            rnd = random.randint(1, 4)
            if rnd == 1:
                for j in range(count_20):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
                for j1 in range(int(count_40 / 2)):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
                for j2 in range(int(count_45 / 2)):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
            if rnd == 2:
                for j1 in range(int(count_40 / 2)):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
                for j in range(count_20):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
                for j2 in range(int(count_45 / 2)):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
            if rnd == 3:
                for j2 in range(int(count_45 / 2)):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
                for j in range(count_20):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })
                for j1 in range(int(count_40 / 2)):
                    railcars.append({
                        "aarType": "s615",
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
                                    "eqTypeCd": "c",
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
                                    "eqTypeCd": "c",
                                    "isEmpty": False,
                                    "boundTypeCd": data['Inbound/OutBound'],
                                    "isWheeled": True,
                                    "priority": 11.3
                                }
                            }
                        ]
                    })

            result['railcars'] = railcars
            final_result.append(result)

    final_dic['consists'] = final_result
    with open(export_path, 'w') as outbound_outfile:  # export result Json to json file
        json.dump(final_dic, outbound_outfile, indent=4)


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
            result['arrivalTime'] = datetime.datetime.fromtimestamp(times[i].timestamp()).strftime("%m/%d/%Y %H:%M:%S")
            result['truckId'] = 'RH01'
            final_result.append(result)
    final_dic['trains'] = final_result
    with open(export_path, 'w') as outbound_outfile:  # export result Json to json file
        json.dump(final_dic, outbound_outfile, indent=4)


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


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TrainJsonCreatorBasedOnRatios/"
train_json_creator_based_on_ratios(url + "input.json", url + "trainSchedule.json", url + "trainConsists.json")
print("finished")
