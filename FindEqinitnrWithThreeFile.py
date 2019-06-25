import pandas


def calculator(input_path, first_path, second_path, export_path):
    input_data = pandas.read_excel(input_path)  # get data from excel
    input_values = input_data.get_values()  # get all values from input excel

    first_path_data = pandas.read_excel(first_path)  # get data from excel
    first_values = first_path_data.get_values()  # get all values from input excel

    second_data = pandas.read_excel(second_path)  # get data from excel
    second_values = second_data.get_values()  # get all values from input excel

    result = []
    for input_data in input_values:  # input file finding
        eqinitnr_status = False
        for first_data in first_values:  # search in first excel
            if input_data[0] == first_data[0]:
                eqinitnr_status = True

        for second_data in second_values:  # search in second excel
            if input_data[0] == second_data[0]:
                eqinitnr_status = True

        if not eqinitnr_status:  # if not in both file add to result list
            result.append(input_data[0])

    header = ["EQ_INIT_NR"]
    pandas.DataFrame(result, [""] * len(result), header).to_excel(export_path)  # export data in excel


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/FindEqinitnrWithThreeFile/"
calculator(url + "input.xlsx", url + "first.xlsx", url + "second.xlsx", url + "output.xlsx")
print("finished")
