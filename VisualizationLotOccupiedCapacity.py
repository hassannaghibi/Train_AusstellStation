import random

import matplotlib.pyplot as plt
import numpy as np


def main(input_path, pic_path):
    data = read_txt_file(input_path, 1)

    lot_ids_type = []
    [lot_ids_type.append(x) for x in get_specific_col(data, 2) if x not in lot_ids_type]

    hour_type = []
    [hour_type.append(x) for x in get_specific_col(data, 1) if x not in hour_type]

    fig = plt.figure()
    ax = plt.gca()

    ax.yaxis.grid(color='white', linestyle='-', linewidth=0.1)
    # max_time = int((max(get_specific_col(data, 5)) / 10) * 10 + 11)

    p = []
    rnd = lambda: random.randint(0, 255)
    for i in lot_ids_type:
        color = '#{:02x}{:02x}{:02x}'.format(rnd(), rnd(), rnd())
        ind_type = []
        [ind_type.append(x) for x in get_lot_data(data, i, 1) if x not in ind_type]
        p.append(ax.plot(ind_type, get_lot_data(data, i, 5), linewidth=1, color=color, label='plot ' + str(i)))

    ax.set_ylabel("", fontweight="bold")
    plt.xlabel("Time (hour)", fontweight="bold")
    plt.title("VisualizationLotOccupiedCapacity", fontweight="bold")
    plt.xticks(hour_type, fontsize=8)
    ax.set_yticklabels(['{:d}%'.format(elm) for elm in np.arange(0, 110, 10)])
    plt.yticks(np.arange(0, 110, 10), fontsize=8)
    plt.legend(loc=2, bbox_to_anchor=(1, 1), )

    plt.show()
    fig.savefig(pic_path + "VisualizationLotOccupiedCapacity" + ".png")  # save chart pic


def get_lot_data(data, i, index):
    result = []
    for d in data:
        if d[2] == i:
            result.append(d[index])
    return result


def get_specific_col(list, index):
    result = []
    for data in list:
        result.append(data[index])
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
                r[5] = float(r[5].replace('\n', ''))
                r[1] = float(r[1])
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/VisualizationLotOccupiedCapacity/"
main(url + 'input.txt', url)
print("finished")
