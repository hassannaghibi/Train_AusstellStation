import os

import matplotlib.pyplot as plt
import numpy as np
import pandas


def main(input, url, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    N = 2
    fig = plt.figure()
    ax = plt.gca()
    ind = np.arange(1, N, 1)  # the x locations for the groups
    width = 0.8  # the width of the bars: can also be len(x) sequence
    result = []
    for i in range(2):
        a = []
        for j in range(1):
            b = 0
            for s in range(len(values)):
                b += float(values[s][i][j])
            b = b / len(values)
            a.append(b)
        result.append(a)

    if len(result) > 0:
        average_distance_per_box_including_shuffle = []
        average_distance_per_box_excluding_shuffle = []

        average_distance_per_box_including_shuffle.append(result[0][0])
        average_distance_per_box_excluding_shuffle.append(result[1][0])

    max_y = ((int((max([max(average_distance_per_box_including_shuffle),
                        max(average_distance_per_box_excluding_shuffle)])) / 10) * 10) + 11)

    ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
    p1 = plt.bar(ind, average_distance_per_box_including_shuffle, width, color='yellow')
    p2 = plt.bar(ind + width + 0.2, average_distance_per_box_excluding_shuffle, width, color='LimeGreen')

    plt.ylabel('')
    plt.xlabel('')
    plt.title('RTGs Average Gantry Distance PerBox', fontweight="bold")
    plt.xticks(np.arange(1, 1, 1), fontsize=8)
    plt.yticks(np.arange(0, max_y, 10), fontsize=8)
    plt.legend((p2[0], p1[0]),
               ('\nAverage distance \nper box Excluding \nShuffle\n',
                '\nAverage distance \nper box Including \nShuffle\n'),
               loc=0, bbox_to_anchor=(1, 1), )

    plt.show()

    if not os.path.exists(url):
        os.makedirs(url)

    fig.savefig(url + "RTGsAverageGantryDistancePerBox.png")  # save chart pic

    a = []
    a.append([average_distance_per_box_including_shuffle[0], average_distance_per_box_excluding_shuffle[0]])
    header = ["average distance per box including shuffle", "average distance per box excluding shuffle"]
    pandas.DataFrame(a, [""] * len(a), header).to_excel(exportFile)  # export data in excel


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split('='))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/RTGsAverageGantryDistancePerBox/"
main([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
     url + "result/", url + "result/export.xlsx")
print("finished")
