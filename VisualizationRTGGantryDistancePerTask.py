import os

import matplotlib.pyplot as plt
import numpy as np
import pandas


def main(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 9
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(1, N, 1)  # the x locations for the groups
    width = 1  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(8):
        a = []
        for j in range(1):
            b = 0
            for s in range(len(values)):
                b += float(values[s][i][j])
            b = b / len(values)
            a.append(b)
        result.append(a)

    if len(result) > 0:
        load_train_laden = []
        load_train_unladen = []
        unload_train_laden = []
        unload_train_unladen = []
        load_truck_laden = []
        load_truck_unladen = []
        unload_truck_laden = []
        unload_truck_unladen = []

        load_train_laden.append(result[0][0])
        load_train_unladen.append(result[1][0])
        unload_train_laden.append(result[2][0])
        unload_train_unladen.append(result[3][0])
        load_truck_laden.append(result[4][0])
        load_truck_unladen.append(result[5][0])
        unload_truck_laden.append(result[6][0])
        unload_truck_unladen.append(result[7][0])

    max_y = ((int((max(
        [max(load_train_laden), max(load_train_unladen), max(unload_train_laden), max(unload_train_unladen),
         max(load_truck_laden), max(load_truck_unladen), max(unload_truck_laden),
         max(unload_truck_unladen)])) / 10) * 10) + 11)

    ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)

    p1 = plt.bar(0, load_train_laden, width, color='FireBrick')
    p2 = plt.bar(1 + 0.1, load_train_unladen, width, color='Salmon')
    p3 = plt.bar(2 + 0.2, unload_train_laden, width, color='Blue')
    p4 = plt.bar(3 + 0.3, unload_train_unladen, width, color='DodgerBlue')
    p5 = plt.bar(4 + 0.4, load_truck_laden, width, color='Gold')
    p6 = plt.bar(5 + 0.5, load_truck_unladen, width, color='Yellow')
    p7 = plt.bar(6 + 0.6, unload_truck_laden, width, color='DarkGreen')
    p8 = plt.bar(7 + 0.7, unload_truck_unladen, width, color='#999999')

    plt.ylabel('')
    plt.xlabel('')
    plt.title('Average RTG Laden/Unladen Gantry \n Distance Per Task Type (m)', fontweight="bold")
    plt.xticks(np.arange(1, 1, 1), fontsize=8)
    plt.yticks(np.arange(0, max_y, 20), fontsize=8)
    plt.legend((p8[0], p7[0], p6[0], p5[0], p4[0], p3[0], p2[0], p1[0]),
               ('Average Load Train Laden Gantry Distance Per Task: 81.355',
                'Average Load Train Unladen Gantry Distance Per Task: 65.246',
                'Average Unload Train Laden Gantry Distance Per Task: 27.083',
                'Average Unload Train Unladen Gantry Distance Per Task: 44.843',
                'Average Load Truck Laden Gantry Distance Per Task: 0',
                'Average Load Truck Unladen Gantry Distance Per Task: 103.862',
                'Average Unload Truck Laden Gantry Distance Per Task: 0',
                'Average Unload Truck Unladen Gantry Distance Per Task: 83.527',),
               loc=1, bbox_to_anchor=(1, 1), )

    plt.show()

    if not os.path.exists(url):
        os.makedirs(url)

    fig.savefig(url + "VisualizationRTGGantryDistancePerTask.png")  # save chart pic

    a = []
    a.append([load_train_laden[0],
              load_train_unladen[0],
              unload_train_laden[0],
              unload_train_unladen[0],
              load_truck_unladen[0],
              load_truck_unladen[0],
              unload_truck_laden[0],
              unload_truck_unladen[0],
              ])
    header = ['Average Load Train Laden Gantry Distance Per Task: 81.355',
              'Average Load Train Unladen Gantry Distance Per Task: 65.246',
              'Average Unload Train Laden Gantry Distance Per Task: 27.083',
              'Average Unload Train Unladen Gantry Distance Per Task: 44.843',
              'Average Load Truck Laden Gantry Distance Per Task: 0',
              'Average Load Truck Unladen Gantry Distance Per Task: 103.862',
              'Average Unload Truck Laden Gantry Distance Per Task: 0',
              'Average Unload Truck Unladen Gantry Distance Per Task: 83.527']
    pandas.DataFrame(a, [""] * len(a), header).to_excel(exportFile)  # export data in excel


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/VisualizationRTGGantryDistancePerTask/"
main([url + 'input1.txt'], url + "result/", url + "result/export.xlsx")
print("finished")
