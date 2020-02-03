import os

import matplotlib.pyplot as plt
import numpy as np
import pandas


def main(input, step_over, to_index, from_index, group_count, export_chart_path, export_file_path):
    input = read_txt_file(input, step_over)
    header = ["Model Run ID", "HostlerID", "Minutes Spent Loaded", "Minutes Spent Empty",
              "Total Miles (Loaded + Empty)", "Idle Times", "Loaded Moves Count"]

    for a in range(to_index, from_index):
        loaded_array = []
        for data in input:
            loaded_array.append(float(data[a]))
        avg_loaded = 0.0
        avg_loaded_list = []
        avg_loaded_list_count = []
        for i in range(int(len(loaded_array) / group_count)):
            for j in range(i * group_count, group_count * (i + 1)):
                avg_loaded += loaded_array[j]
            avg_loaded_list.append(avg_loaded / group_count)
            avg_loaded = 0.0
            avg_loaded_list_count.append(i)
        show_diagram(export_chart_path, avg_loaded_list_count, avg_loaded_list, "(Average)" + header[a])

    pandas.DataFrame(input, [""] * len(input), header).to_excel(export_file_path)  # export data in excel


def show_diagram(export_chart_path, avg_loaded_list_count, avg_loaded_list, title):
    fig = plt.figure()
    ax = plt.gca()
    width = 0.91  # the width of the bars: can also be len(x) sequence

    ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.1)
    p1 = plt.bar(avg_loaded_list_count, avg_loaded_list, width, color='Blue')

    plt.ylabel("Minutes")
    plt.xlabel("Count (Hours)", fontweight="bold")
    plt.title(title, fontweight="bold")
    plt.xticks(np.arange(0, len(avg_loaded_list_count), 1), fontsize=8)
    plt.yticks(np.arange(0, (((max(avg_loaded_list) / 10) * 10) + 10), 5), fontsize=8)
    plt.legend((p1[0],), ('Desc',), loc=2, bbox_to_anchor=(1, 1), )

    plt.show()
    if not os.path.exists(export_chart_path):
        os.makedirs(export_chart_path)
    fig.savefig(export_chart_path + title + ".png")  # save chart pic


def read_txt_file(file, step_over):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        i = 0
        for data in values:
            if i > step_over:
                result.append(data.split('\t'))
            i += 1
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/VisualizationHostlerHourlyData/"
main(url + 'input.txt', 1, 2, 7, 15, url + "result/",
     url + "result/export.xlsx")  # input file , step over , from col , to col , export path for image , export path for excel file

print("finished")
