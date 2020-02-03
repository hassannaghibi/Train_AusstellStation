import os

import matplotlib.pyplot as plt
import numpy as np
import pandas
from matplotlib import ticker


def main(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 29
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(5, N, 1)  # the x locations for the groups
    width = 0.91  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(24):
        a = []
        for j in range(3):
            b = 0
            for s in range(len(values)):
                b += float(values[s][i][j])
            b = b / len(values)
            a.append(b)
        result.append(a)

    if len(result) > 0:
        executing_shuffle_move = []
        executing_productive_move = []
        idle = []

        for i in range(len(result)):
            executing_shuffle_move.append(result[i][0])
            executing_productive_move.append(result[i][1])
            idle.append(result[i][2])

        # max_y = ((int((max([max(executing_shuffle_move), max(np.array(executing_shuffle_move) + np.array(executing_productive_move)),
        #                     max(np.array(executing_shuffle_move) + np.array(executing_productive_move) + np.array(idle))])) / 10) * 10) + 6)

        ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
        p1 = plt.bar(ind, executing_shuffle_move, width, color='DodgerBlue')
        p2 = plt.bar(ind, executing_productive_move, width, bottom=executing_shuffle_move, color='LimeGreen')
        p3 = plt.bar(ind, idle, width, bottom=np.array(executing_shuffle_move) + np.array(executing_productive_move),
                     color='Gainsboro')

        plt.ylabel('')
        plt.xlabel('')
        plt.title('RTGs Status Per Hour', fontweight="bold")
        plt.xticks(np.arange(5, N, 1), fontsize=8)
        plt.yticks(np.arange(0, 101, 10), fontsize=8)
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100))

        plt.legend((p3[0], p2[0], p1[0]),
                   ('\nIdle\n', '\nExecuting \nProductive Move\n', '\nExecuting \nShuffle Mov\n'),
                   loc=0, bbox_to_anchor=(1, 1))

        plt.show()

        if not os.path.exists(url):
            os.makedirs(url)

        fig.savefig(url + "RTGsStatusPerHour.png")  # save chart pic

        a = []
        for i in range(24):
            b = []
            b.insert(0, executing_shuffle_move[i])
            b.insert(1, executing_productive_move[i])
            b.insert(2, idle[i])
            a.append(b)

        header = ["Executing Shuffle Move", "Executing Productive Move", "Idle"]
        pandas.DataFrame(a, [""] * len(a), header).to_excel(exportFile)  # export data in excel


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/RTGsStatusPerHour/"
main([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
     url + "result/", url + "result/export.xlsx")
print("finished")
