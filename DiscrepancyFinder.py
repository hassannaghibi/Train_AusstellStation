import pandas


def calculator(first_input_path, second_input_path, first_export_path, second_export_path):
    first_input_data = pandas.read_excel(first_input_path)  # get data from excel
    first_values = first_input_data.get_values()  # get all values from input excel

    second_input_data = pandas.read_excel(second_input_path)  # get data from excel
    second_values = second_input_data.get_values()  # get all values from input excel

    first_result = []
    for first_data in first_values:  # first file finding
        eqinitnr_status = False

        for second_data in second_values:
            second_eqinitnr = second_data[2].replace(" ", "")
            if first_data[1] == second_eqinitnr:
                eqinitnr_status = True

        if not eqinitnr_status:
            first_result.append(first_data)

    second_result = []
    for second_data in second_values:  # second file finding
        eqinitnr_status = False
        second_eqinitnr = second_data[2].replace(" ", "")
        for first_data in first_values:

            if second_eqinitnr == first_data[1]:
                eqinitnr_status = True

        if not eqinitnr_status:
            second_result.append(second_data)

    header = ["", "EQ_INIT_NR", "WAYBILL", "EVENT TIMESTAMP EST", "EVENT TYPE", "LOADED EMPTY", "EQ LENGTH", "EQ TYPE",
              "NS ORGIN", "NS ORIGIN ST", "NS DEST", "NS DEST ST", "ORGN", "ORGN ST", "DEST", "DEST ST", "NET_WGT",
              "SHPR_CUST_NM", "CY_NotStackable", "IS SHIPMENT IN PARKING", "HOURS STAYED IN PARKING"]
    pandas.DataFrame(first_result, [""] * len(first_result), header).to_excel(first_export_path)  # export data in excel
    pandas.DataFrame(second_result, [""] * len(second_result), [""] * 33).to_excel(
        second_export_path)  # export data in excel


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/DiscrepancyFinder/"
calculator(url + "first_input.xlsx", url + "second_input.xlsx", url + "first_output.xlsx", url + "second_output.xlsx")
print("finished")
