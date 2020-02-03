import pandas


def main(input, exportFile):
    values = []
    for i in range(len(input)):
        values.append(read_txt_file(input[i]))

    result = []
    for i in range(4):
        a = []
        for j in range(1):
            b = 0
            for s in range(len(values)):
                b += float(values[s][i][j])
            b = b / len(values)
            a.append(b)
        result.append(a)

    header = ['Train_2_Outbound', 'Train_2_Inbound', 'Train_1_Outbound', 'Train_1_Inbound']
    r = []
    res = []
    res.append(result[0][0])
    res.append(result[1][0])
    res.append(result[2][0])
    res.append(result[3][0])
    r.append(res)
    pandas.DataFrame(r, [""] * len(r), header).to_excel(exportFile)  # export data in excel


def read_txt_file(file):
    result = []
    with open(file, 'r') as r_file:
        values = r_file.readlines()
        for data in values:
            result.append((data.replace('[', '').replace(']', '').split(':'))[1].replace('\n', '').split(','))
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/TrainHandlingTime/"
main([url + 'input1.txt', url + 'input2.txt', url + 'input3.txt', url + 'input4.txt', url + 'input5.txt'],
     url + "export.xlsx")
print("finished")
