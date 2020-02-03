import statistics

import matplotlib.pyplot as plt
import numpy as np
import pandas


def main(input_path, export_path, pic_path):
    list = read_txt_file(input_path, 1)
    drop_off = []
    pick_up = []
    both = []

    for data in list:
        if data[3] == 'true' and data[4] == 'true':
            both.append(data)
        elif data[3] == 'true' and data[4] == 'false':
            drop_off.append(data)
        elif data[3] == 'false' and data[4] == 'true':
            pick_up.append(data)

    drop_off_hour_type = []
    [drop_off_hour_type.append(x) for x in get_hours(drop_off) if x not in drop_off_hour_type]

    pick_up_hour_type = []
    [pick_up_hour_type.append(x) for x in get_hours(pick_up) if x not in pick_up_hour_type]

    both_hour_type = []
    [both_hour_type.append(x) for x in get_hours(both) if x not in both_hour_type]

    drop_off_result = [
        ["Number Of Lots Searched", min(drop_off)[0], _max(drop_off)[0], avg(drop_off)[0], stdev(drop_off)[0]],
        ["Truck Dwell (minutes)", min(drop_off)[1], _max(drop_off)[1], avg(drop_off)[1], stdev(drop_off)[1]],
        ["Search Time (minutes)", min(drop_off)[2], _max(drop_off)[2], avg(drop_off)[2], stdev(drop_off)[2]]
    ]
    pick_up_result = [
        ["Number Of Lots Searched", min(pick_up)[0], _max(pick_up)[0], avg(pick_up)[0], stdev(pick_up)[0]],
        ["Truck Dwell (minutes)", min(pick_up)[1], _max(pick_up)[1], avg(pick_up)[1], stdev(pick_up)[1]],
        ["Search Time (minutes)", min(pick_up)[2], _max(pick_up)[2], avg(pick_up)[2], stdev(pick_up)[2]]
    ]
    both_result = [
        ["Number Of Lots Searched", min(both)[0], _max(both)[0], avg(both)[0], stdev(both)[0]],
        ["Truck Dwell (minutes)", min(both)[1], _max(both)[1], avg(both)[1], stdev(both)[1]],
        ["Search Time (minutes)", min(both)[2], _max(both)[2], avg(both)[2], stdev(both)[2]]
    ]

    header = ["title", "Min", "Max", "AVG", "Standard Deviation"]
    pandas.DataFrame().to_excel(export_path)
    writer = pandas.ExcelWriter(export_path, writer_options={'use_xlsxwriter': True})
    pandas.DataFrame(drop_off_result, None, header).to_excel(writer, sheet_name='Drop-Off')
    chart("Drop-Off Visualization Data", drop_off_hour_type, drop_off, pic_path)
    pandas.DataFrame(pick_up_result, None, header).to_excel(writer, sheet_name='Pick-up')
    chart("Pick-up Visualization Data", pick_up_hour_type, pick_up, pic_path)
    pandas.DataFrame(both_result, None, header).to_excel(writer, sheet_name='Both')
    chart("Both Visualization Data", both_hour_type, both, pic_path)
    writer.save()
    writer.close()


def get_avg_hour(list_type, list, index):
    result = []
    for hour in list_type:
        result_type = []
        for data in list:
            if data[2] == hour:
                result_type.append(data)
        if len(result_type) > 0:
            result.append(avg(result_type)[index])
    return result


def get_hours(list):
    result = []
    for data in list:
        result.append(data[2])
    return result


def chart(title, list_type, data, url):
    fig = plt.figure()
    ax = plt.gca()

    number_of_lots_searched_avg = get_avg_hour(list_type, data, 0)
    truck_dwell_avg = get_avg_hour(list_type, data, 1)
    search_time_avg = get_avg_hour(list_type, data, 2)

    ax.yaxis.grid(color='white', linestyle='-', linewidth=0.1)
    max_time = int((max(max(number_of_lots_searched_avg), max(truck_dwell_avg), max(search_time_avg)) / 10) * 10 + 11)

    p1 = ax.plot(list_type, number_of_lots_searched_avg, 'go-', linewidth=2, color='blue')
    p2 = ax.plot(list_type, truck_dwell_avg, 'go-', linewidth=2, color='red')
    p3 = ax.plot(list_type, search_time_avg, 'go-', linewidth=2, color='green')

    ax.set_ylabel("", fontweight="bold")

    plt.xlabel("Time", fontweight="bold")
    plt.title(title, fontweight="bold")
    plt.xticks(list_type, fontsize=8)
    plt.yticks(np.arange(0, max_time, 2), fontsize=8)
    plt.legend((p3[0], p2[0], p1[0]), ("Number Of Lots Searched", "Truck Dwell (minutes)", "Search Time (minutes)"),
               loc=3, bbox_to_anchor=(1, 1), )

    plt.show()
    fig.savefig(url + title + ".png")  # save chart pic


def avg(list):
    result = []
    number_of_lots_searched_avg = 0
    truck_dwell_avg = 0
    search_time_avg = 0
    for data in list:
        number_of_lots_searched_avg += data[7]
        truck_dwell_avg += data[8]
        search_time_avg += data[9]

    if number_of_lots_searched_avg > 0:
        result.append(number_of_lots_searched_avg / len(list))
    else:
        result.append(0)
    if truck_dwell_avg > 0:
        result.append(truck_dwell_avg / len(list))
    else:
        result.append(0)
    if search_time_avg > 0:
        result.append(search_time_avg / len(list))
    else:
        result.append(0)
    return result


def min(list):
    result = []
    number_of_lots_searched_min = 0
    truck_dwell_min = 0
    search_time_min = 0
    i = 0
    for data in list:
        i += 1
        if i > 1:
            if data[7] < number_of_lots_searched_min:
                number_of_lots_searched_min = data[7]
            if data[8] < truck_dwell_min:
                truck_dwell_min = data[8]
            if data[9] < search_time_min:
                search_time_min = data[9]
        else:
            number_of_lots_searched_min = data[7]
            truck_dwell_min = data[8]
            search_time_min = data[9]
    result.append(number_of_lots_searched_min)
    result.append(truck_dwell_min)
    result.append(search_time_min)
    return result


def _max(list):
    result = []
    number_of_lots_searched_max = 0
    truck_dwell_max = 0
    search_time_max = 0
    for data in list:
        if data[7] > number_of_lots_searched_max:
            number_of_lots_searched_max = data[7]
        if data[8] > truck_dwell_max:
            truck_dwell_max = data[8]
        if data[9] > search_time_max:
            search_time_max = data[9]
    result.append(number_of_lots_searched_max)
    result.append(truck_dwell_max)
    result.append(search_time_max)
    return result


def stdev(list):
    result = []
    number_of_lots_searched_stdev = []
    truck_dwell_stdev = []
    search_time_stdev = []
    for data in list:
        number_of_lots_searched_stdev.append(data[7])
        truck_dwell_stdev.append(data[8])
        search_time_stdev.append(data[9])

    if len(number_of_lots_searched_stdev) > 1:
        result.append(statistics.stdev(number_of_lots_searched_stdev))
    else:
        result.append(0)
    if len(truck_dwell_stdev) > 1:
        result.append(statistics.stdev(truck_dwell_stdev))
    else:
        result.append(0)
    if len(search_time_stdev) > 1:
        result.append(statistics.stdev(search_time_stdev))
    else:
        result.append(0)
    return result


def read_txt_file(file, step_over):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        i = 0
        for data in values:
            if i > step_over:
                result.append(data.split('\t'))
            i += 1

        for r in result:
            if len(r) > 0:
                r[9] = float(r[9].replace('\n', ''))
                r[2] = float(r[2])
                r[7] = float(r[7])
                r[8] = float(r[8])
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/SummarizingTruckData/"
main(url + 'input.txt', url + "export.xlsx", url)
print("finished")
