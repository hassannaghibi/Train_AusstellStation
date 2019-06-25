from itertools import groupby

import pandas


def calculator(input_path, export_path):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    result = []
    eqinits = []
    for value in values:
        eqinits.append(value[0][0:4])

    [result.append((i, len(list(c)))) for i, c in groupby(sorted(eqinits))]
    result.sort(key=sort_second, reverse=True)
    header = ["EQ_INIT_NR", "Count"]
    pandas.DataFrame(result, [""] * len(result), header).to_excel(export_path)  # export data in excel


def sort_second(val):
    return val[1]


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/FindEqinitCount/"
calculator(url + "input.xlsx", url + "output.xlsx")
print("finished")
