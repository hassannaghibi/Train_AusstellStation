import os

import matplotlib.pyplot as plt
import numpy as np
import pandas


def first_chart(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 31
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(1, N, 1)  # the x locations for the groups
    width = 0.8  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(30):
        a = []
        for j in range(4):
            b = 0
            for s in range(len(values)):
                b += float(values[s][i][j])
            b = b / len(values)
            a.append(b)
        result.append(a)

    if len(result) > 0:
        average_truck_total_dwell_timea = []
        average_truck_total_dwell_timeb = []
        average_truck_total_dwell_time = []
        average_truck_dwell_time_at_stacking_area = []

        for i in range(len(result)):
            average_truck_total_dwell_time.append(result[i][0])
            average_truck_dwell_time_at_stacking_area.append((result[i][1]))
            average_truck_total_dwell_timea.append(result[i][3])
            average_truck_total_dwell_timeb.append(result[i][2])

        ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
        max_time = max(max(average_truck_total_dwell_time), max(average_truck_dwell_time_at_stacking_area)) + 6

        p3 = plt.bar(ind, average_truck_total_dwell_timea, width, color='SkyBlue')
        p4 = plt.bar(ind, average_truck_total_dwell_timeb, width, bottom=average_truck_total_dwell_timea, color='khaki')

        ax2 = ax.twinx()
        ax2.yaxis.grid(color='white', linestyle='-', linewidth=0.1)

        p1 = ax2.plot(ind, average_truck_total_dwell_time, 'go-', linewidth=2, color='YELLOWGREEN')
        p2 = ax2.plot(ind, average_truck_dwell_time_at_stacking_area, 'go-', linewidth=2, color='GOLD')

        ax.set_ylabel('Number Of Boxes', fontweight="bold")
        ax2.set_ylabel('Time(Minutes)', fontweight="bold")
        ax.yaxis.set_ticks(np.arange(0, 45, 10))

        plt.xlabel('')
        plt.title('Truck Average Dwell Time', fontweight="bold")
        plt.xticks(ind, fontsize=8)
        plt.yticks(np.arange(0, max_time, 1), fontsize=8)
        plt.legend((p4[0], p3[0], p2[0], p1[0]),
                   ('Hourly Total Delivered Boxes', 'Hourly Total Picked Up Boxes',
                    'Average Trucks Dwell Time At Terminal', 'Average Trucks Dwell Time At Stack side'),
                   loc=1, bbox_to_anchor=(1, 1), )

        plt.show()

        if not os.path.exists(url):
            os.makedirs(url)

        fig.savefig(url + "VisualizationTruckAverageTime.png")  # save chart pic

        a = []
        for i in range(5):
            b = []
            b.insert(0, average_truck_total_dwell_timea[i])
            b.insert(1, average_truck_total_dwell_timeb[i])
            b.insert(2, average_truck_total_dwell_time[i])
            b.insert(3, average_truck_dwell_time_at_stacking_area[i])
            a.append(b)

        header = ['Hourly Total Delivered Boxes', 'Hourly Total Picked Up Boxes',
                  'Average Trucks Dwell Time At Terminal', 'Average Trucks Dwell Time At Stack side']
        pandas.DataFrame(a, [""] * len(a), header).to_excel(exportFile)  # export data in excel


def line_chart(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 31
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(1, N, 1)  # the x locations for the groups
    width = 0.8  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(5):
        a = []
        b = []
        c = []
        for j in range(30):
            a.append(float(values[i][j][2]))
            b.append(float(values[i][j][3]))
        c.append(a)
        c.append(b)
        result.append(c)

    if len(result) > 0:
        run1 = result[0]
        run2 = result[1]
        run3 = result[2]
        run4 = result[3]
        run5 = result[4]

    max_y = int(max(max(run1[0]), max(run1[1]), max(run2[0]), max(run2[1]), max(run3[0]), max(run3[1]), max(run4[0]),
                    max(run4[1]), max(run5[0]), max(run5[1]))) + 6

    ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
    p1 = plt.plot(ind, run1[0], label='line 1', linewidth=2, color='IndianRed')
    p2 = plt.plot(ind, run1[1], label='line 2', linewidth=2, color='Aqua')

    p3 = plt.plot(ind, run2[0], label='line 3', linewidth=2, color='LightCoral')
    p4 = plt.plot(ind, run2[1], label='line 4', linewidth=2, color='PaleTurquoise')

    p5 = plt.plot(ind, run3[0], label='line 5', linewidth=2, color='Salmon')
    p6 = plt.plot(ind, run3[1], label='line 6', linewidth=2, color='Turquoise')

    p7 = plt.plot(ind, run4[0], label='line 7', linewidth=2, color='Crimson')
    p8 = plt.plot(ind, run4[1], label='line 8', linewidth=2, color='SteelBlue')

    p9 = plt.plot(ind, run5[0], label='line 9', linewidth=2, color='Red')
    p10 = plt.plot(ind, run5[1], label='line 10', linewidth=2, color='DodgerBlue')

    plt.ylabel('')
    plt.xlabel('', fontweight="bold")
    plt.title('', fontweight="bold")
    plt.xticks(np.arange(1, 31, 1), fontsize=8)
    plt.yticks(np.arange(0, max_y, 1), fontsize=8)
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0]),
               ('run1A', 'run1B', 'run2A', 'run2B', 'run3A', 'run3B', 'run4A', 'run4B', 'run5A', 'run5B'),
               loc=0, bbox_to_anchor=(1, 1), )

    # plt.figure(figsize=(40, 40))
    plt.show()

    if not os.path.exists(url):
        os.makedirs(url)

    fig.savefig(url + "VisualizationLineChartTruckAverageTime.png")  # save chart pic


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TruckAverageTimeVisualization/"
first_chart([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
            url + "result/", url + "result/export.xlsx")
line_chart([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
           url + "result/", url + "result/export.xlsx")
print("finished")
