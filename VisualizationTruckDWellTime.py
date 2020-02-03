import os

import matplotlib.pyplot as plt
import numpy as np
import pandas


def main(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 25
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(1, N, 1)  # the x locations for the groups
    width = 0.8  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(24):
        a = []
        for j in range(2):
            b = 0
            for s in range(len(values)):
                b += float(values[s][i][j])
            b = b / len(values)
            a.append(b)
        result.append(a)

    if len(result) > 0:
        average_truck_total_dwell_time = []
        average_truck_dwell_time_at_stacking_area = []

        for i in range(len(result)):
            average_truck_total_dwell_time.append(result[i][0])
            average_truck_dwell_time_at_stacking_area.append(result[i][1])

        ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
        p1 = plt.plot(ind, average_truck_total_dwell_time, 'go-', label='line 1', linewidth=2, color='YELLOWGREEN')
        p2 = plt.plot(ind, average_truck_dwell_time_at_stacking_area, 'go-', label='line 2', linewidth=2, color='GOLD')

        plt.ylabel('')
        plt.xlabel('', fontweight="bold")
        plt.title('Truck Dwell Time', fontweight="bold")
        plt.xticks(np.arange(1, 25, 1), fontsize=8)
        plt.yticks(np.arange(0, 1.1, 0.1), fontsize=8)
        plt.legend((p2[0], p1[0]),
                   ('\nAverage Truck\n Total Dwell Time\n', '\nAverage Truck \nDwell Time At \nStacking Area\n'),
                   loc=2, bbox_to_anchor=(1, 1), )

        plt.show()

        if not os.path.exists(url):
            os.makedirs(url)

        fig.savefig(url + "TruckDWellTimeVisualization.png")  # save chart pic

        a = []
        for i in range(24):
            b = []
            b.insert(0, average_truck_total_dwell_time[i])
            b.insert(1, average_truck_dwell_time_at_stacking_area[i])
            a.append(b)

        header = ["Average Truck Total Dwell Time", "Average Truck Dwell Time At Stacking Area", ]
        pandas.DataFrame(a, [""] * len(a), header).to_excel(exportFile)  # export data in excel


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TruckDWellTimeVisualization/"
main([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
     url + "result/", url + "result/export.xlsx")
print("finished")
