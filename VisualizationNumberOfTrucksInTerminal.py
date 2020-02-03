import os

import matplotlib.pyplot as plt
import numpy as np


def first_line_chart(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 30
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(1, N, 1)  # the x locations for the groups
    width = 0.8  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(29):
        b = 0
        for s in range(len(values)):
            b += float(values[s][i][0])
        b = b / len(values)
        result.append(b)

    if len(result) > 0:
        max_y = int(max(result)) + 6

    ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
    p1 = plt.plot(ind, result, label='line 1', linewidth=2, color='Blue')

    plt.ylabel('')
    plt.xlabel('', fontweight="bold")
    plt.title('Number Of Trucks in Terminal', fontweight="bold")
    plt.xticks(np.arange(1, N, 1), fontsize=8)
    plt.yticks(np.arange(0, max_y, 5), fontsize=8)
    plt.legend((p1[0],), ('Line',), loc=2, bbox_to_anchor=(1, 1), )

    # plt.figure(figsize=(40, 40))
    plt.show()

    if not os.path.exists(url):
        os.makedirs(url)

    fig.savefig(url + "VisualizationNumberOfTrucksInTerminal.png")  # save chart pic


def second_line_chart(input, url):
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
        c = []
        for j in range(29):
            c.append(float(values[i][j][0]))
        result.append(c)

    if len(result) > 0:
        run1 = result[0]
        run2 = result[1]
        run3 = result[2]
        run4 = result[3]
        run5 = result[4]

    max_y = int(max(max(run1), max(run2), max(run3), max(run4), max(run5))) + 6

    ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
    p1 = plt.plot(ind, run1, label='line 1', linewidth=2, color='IndianRed')
    p2 = plt.plot(ind, run2, label='line 3', linewidth=2, color='LightCoral')
    p3 = plt.plot(ind, run3, label='line 5', linewidth=2, color='Salmon')
    p4 = plt.plot(ind, run4, label='line 7', linewidth=2, color='Crimson')
    p5 = plt.plot(ind, run5, label='line 9', linewidth=2, color='Red')

    plt.ylabel('')
    plt.xlabel('', fontweight="bold")
    plt.title('', fontweight="bold")
    plt.xticks(np.arange(1, N, 1), fontsize=8)
    plt.yticks(np.arange(0, max_y, 5), fontsize=8)
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]),
               ('run1', 'run2', 'run3', 'run4', 'run5'),
               loc=2, bbox_to_anchor=(1, 1), )

    # plt.figure(figsize=(40, 40))
    plt.show()

    if not os.path.exists(url):
        os.makedirs(url)

    fig.savefig(url + "VisualizationNumberOfTrucksInTerminalSecond.png")  # save chart pic


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/VisualizationNumberOfTrucksInTerminal/"
first_line_chart([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
                 url + "result/", url + "result/export.xlsx")
second_line_chart([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
                  url + "result/")
print("finished")
