import os

import matplotlib.pyplot as plt
import numpy as np
import pandas


def bar_chart(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 34
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(5, N, 1)  # the x locations for the groups
    width = 0.91  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(29):
        a = []
        for j in range(5):
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
        shuffles = []

        for i in range(len(result)):
            move_from_truck.append(result[i][0])
            move_to_truck.append(result[i][1])
            move_to_train.append(result[i][2])
            move_from_train.append(result[i][3])
            shuffles.append(result[i][4])

        max_y = ((int((max([max(move_from_truck), max(np.array(move_from_truck) + np.array(move_to_truck)),
                            max(np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train)), max(
                np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train) + np.array(
                    move_from_train)), max(
                np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train) + np.array(
                    move_from_train) + np.array(shuffles))])) / 10) * 10) + 11)

        ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
        p1 = plt.bar(ind, move_from_truck, width, color='DarkOliveGreen')
        p2 = plt.bar(ind, move_to_truck, width, bottom=move_from_truck, color='khaki')
        p3 = plt.bar(ind, move_to_train, width, bottom=np.array(move_from_truck) + np.array(move_to_truck),
                     color='DarkRed')
        p4 = plt.bar(ind, move_from_train, width,
                     bottom=np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train),
                     color='IndianRed')
        p5 = plt.bar(ind, shuffles, width,
                     bottom=np.array(move_from_truck) + np.array(move_to_truck) + np.array(move_to_train) + np.array(
                         move_from_train), color='Tan')

        plt.ylabel('')
        plt.xlabel('NO VBS - Freerider specs', fontweight="bold")
        plt.title('Freerider moves per hour - NO Austell - 2 train', fontweight="bold")
        plt.xticks(np.arange(5, N, 1), fontsize=8)
        plt.yticks(np.arange(0, max_y, 2), fontsize=8)
        plt.legend((p5[0], p4[0], p3[0], p2[0], p1[0]),
                   ('\nNummber Shuffles\n', '\nMove from Train\n', '\nMove to train\n',
                    '\nMove to Truck\n', '\nMove from Truck\n'),
                   loc=0, bbox_to_anchor=(1, 1), )

        ss = [p1, p2, p3, p4, p5]
        autolabel(ss, ax)
        # plt.figure(figsize=(40, 40))
        plt.show()

        if not os.path.exists(url):
            os.makedirs(url)

        fig.savefig(url + "BarChatRTGsMovesPerHour.png")  # save chart pic

        a = []
        for i in range(24):
            b = []
            b.insert(0, move_from_train[i])
            b.insert(1, move_to_truck[i])
            b.insert(2, move_to_train[i])
            b.insert(3, move_from_train[i])
            b.insert(4, shuffles[i])
            a.append(b)

        header = ["Move from Truck", "Move to Truck", "Move to train", "Move from Train", "Nummber Shuffles"]
        pandas.DataFrame(a, [""] * len(a), header).to_excel(exportFile)  # export data in excel


def line_chart(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 30
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(1, N, 1)  # the x locations for the groups
    width = 0.8  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(5):
        a = []
        for j in range(29):
            avg = 0
            for d in range(5):
                avg += float(values[i][j][d])
            a.append(avg)
        result.append(a)

    if len(result) > 0:
        move_from_truck = result[0]
        move_to_truck = result[1]
        move_to_train = result[2]
        move_from_train = result[3]
        shuffles = result[4]

    max_y = int(
        max(max(move_to_truck), max(move_to_train), max(move_from_truck), max(move_from_train), max(shuffles))) + 6

    ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
    p1 = plt.plot(ind, move_from_truck, label='line 1', linewidth=2, color='Gainsboro')
    p2 = plt.plot(ind, move_to_truck, label='line 2', linewidth=2, color='Silver')
    p3 = plt.plot(ind, move_to_train, label='line 3', linewidth=2, color='Gray')
    p4 = plt.plot(ind, move_from_train, label='line 4', linewidth=2, color='DimGray')
    p5 = plt.plot(ind, shuffles, label='line 5', linewidth=2, color='LightSlateGray')

    plt.ylabel('')
    plt.xlabel('NO VBS - Freerider specs', fontweight="bold")
    plt.title('Freerider moves per hour - NO Austell - 2 train', fontweight="bold")
    plt.xticks(np.arange(1, 30, 1), fontsize=8)
    plt.yticks(np.arange(0, max_y, 1), fontsize=8)
    plt.legend((p5[0], p4[0], p3[0], p2[0], p1[0]),
               ('\n run1 \n', '\n run2 \n', '\n run3 \n',
                '\nrun4\n', '\nrun5\n'),
               loc=0, bbox_to_anchor=(1, 1), )

    # plt.figure(figsize=(40, 40))
    plt.show()

    if not os.path.exists(url):
        os.makedirs(url)

    fig.savefig(url + "LineChartRTGsMovesPerHour.png")  # save chart pic


def autolabel(rects, ax):
    for i in range(len(rects)):
        for j in range(len(rects[i])):
            height = 0
            for k in range(len(rects)):
                height += (rects[k][j].get_height())
            height = int(height * 100) / 100.0
            ax.annotate('{}'.format(height),
                        xy=(rects[4][j].get_x() + rects[4][j].get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points", rotation="90",
                        ha='center', va='bottom')


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/RTGsMovesPerHour/"
bar_chart([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
          url + "result/", url + "result/export.xlsx")
line_chart([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
           url + "result/", url + "result/export.xlsx")
print("finished")
