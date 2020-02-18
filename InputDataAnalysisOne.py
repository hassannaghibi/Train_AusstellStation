import numpy as np
import pandas


def main(value, input, export):
    values = read_txt_file(input)  # read value from txt file

    export_header = ["First Time (minute)", "Second Time (minute)", "Arrival Time (minute)"]
    units = np.unique(np.array(values)[:, 2])  # get third columns of array in list and then get unique number of list
    writer = pandas.ExcelWriter(export)  # set excel

    for unit in units:
        result = []
        for i in range(len(values)):
            if i < len(values) - 1:
                if values[i][0] == value:
                    if values[i][2] == unit:
                        first_time = float(values[i][1])
                        second_time = float(values[i + 1][1])
                        result.append([
                            round(first_time / 60, 2),  # round float num to 0.00
                            round(second_time / 60, 2),  # round float num to 0.00
                            round((
                                      first_time - second_time if first_time > second_time else second_time - first_time) / 60,
                                  2)])  # set arrival time
        pandas.DataFrame(result, None, export_header).to_excel(writer,
                                                               "unit " + unit)  # write each unit of arrival times list into specific sheet
        writer.save()


def read_txt_file(file):
    result = []
    i = 0
    values = open(file, 'r').readlines()
    for data in values:
        if i == 0:
            i += 1
        else:
            result.append(data.replace('\n', '').split('\t'))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/InputDataAnalysisOne/"
main("5445", url + 'input.txt', url + "export.xlsx")  # condition value , input data path , output data path
print("finished")
