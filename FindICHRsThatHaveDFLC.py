import pandas


def initial_inventory_summary(input_path, export_path):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    final_result = []
    header = ["EQ_INIT_NR", "WAYBILL", "EVENT TIMESTAMP EST", "EVENT TYPE", "LOADED EMPTY", "EQ LENGTH", "EQ TYPE",
              "NS ORGIN", "NS ORIGIN ST", "NS DEST", "NS DEST ST", "ORGN", "ORGN ST", "DEST", "DEST ST", "NET_WGT",
              "SHPR_CUST_NM", "CY_NotStackable", "IS SHIPMENT IN PARKING", "HOURS STAYED IN PARKING", "Has DFLC",
              "DFLC LOADED EMPTY", "DFLC NET_WGT"]

    for data in values:
        result = []
        for i in range(20):
            result.insert(i, data[i + 1])
        result.insert(20, False)
        result.insert(21, "")
        result.insert(22, 0)
        final_result.append(result)

    index = 0
    for data in final_result:
        if data[3] == 'ICHR':
            sub_index = 0
            for i in range(index, len(final_result)):
                if final_result[index + sub_index][0] == data[0]:
                    if final_result[index + sub_index][3] == 'DFLC':
                        final_result[index][20] = True
                        final_result[index][21] = data[4]
                        final_result[index][22] = data[15]
                sub_index += 1
        index += 1

    pandas.DataFrame(final_result, [""] * len(final_result), header).to_excel(export_path)  # export data


print("Start")
url = "C:/Users/Hassan/Desktop/pythonExport/FindICHRsThatHaveDFLC/"
initial_inventory_summary(url + 'input.xlsx', url + "output.xlsx")
print("Finished")
