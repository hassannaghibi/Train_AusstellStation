import os

import matplotlib.pyplot as plt
import numpy as np
import pandas


def bar_chart(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    fig = plt.figure()
    ax = plt.gca()
    width = 0.01  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(1):
        a = []
        for j in range(4):
            b = 0
            for s in range(len(values)):
                b += float(values[s][i][j])
            b = b / len(values)
            a.append(b)
        result.append(a)

    if len(result) > 0:
        move_from_truck = []
        move_to_truck = []
        move_to_train = []
        move_from_train = []

        for i in range(len(result)):
            move_from_truck.append(result[i][0])
            move_to_truck.append(result[i][1])
            move_to_train.append(result[i][2])
            move_from_train.append(result[i][3])

        max_y = ((int((max([max(move_from_truck), max(np.array(move_from_truck) + np.array(move_to_truck)),
                            max(np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train)), max(
                np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train) + np.array(
                    move_from_train)), max(
                np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train) + np.array(
                    move_from_train))])) / 10) * 10) + 101)

        ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
        p1 = plt.bar(1, move_from_truck, width, color='DarkOliveGreen')
        p2 = plt.bar(1, move_to_truck, width, bottom=move_from_truck, color='khaki')
        p3 = plt.bar(1, move_to_train, width, bottom=np.array(move_from_truck) + np.array(move_to_truck),
                     color='DarkRed')
        p4 = plt.bar(1, move_from_train, width,
                     bottom=np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train),
                     color='IndianRed')

        plt.ylabel('')
        plt.xlabel('', fontweight="bold")
        plt.title('RTGs Total Moves', fontweight="bold")
        plt.xticks(np.arange(1, 1, 1), fontsize=8)
        plt.yticks(np.arange(0, max_y, 100), fontsize=8)
        plt.legend((p1[0], p2[0], p3[0], p4[0]),
                   ('Total Move From Truck',
                    'Total Move To Truck',
                    'Total Move To Train',
                    'Total Move From Train'),
                   loc=2, bbox_to_anchor=(1, 1), )

        plt.figure(figsize=(0.1, 0.1))
        plt.show()

        if not os.path.exists(url):
            os.makedirs(url)

        fig.savefig(url + "VisualizationRTGsTotalMoves.png")  # save chart pic

        a = []
        for i in range(1):
            b = []
            b.insert(0, move_from_train[i])
            b.insert(1, move_to_truck[i])
            b.insert(2, move_to_train[i])
            b.insert(3, move_from_train[i])
            a.append(b)

        header = ["Total Move From Truck",
                  "Total Move To Truck",
                  "Total Move To Train",
                  "Total Move From Train", ]
        pandas.DataFrame(a, [""] * len(a), header).to_excel(exportFile)  # export data in excel


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/VisualizationRTGsTotalMoves/"
bar_chart([url + 'input1.txt'], url + "result/", url + "result/export.xlsx")
print("finished")
