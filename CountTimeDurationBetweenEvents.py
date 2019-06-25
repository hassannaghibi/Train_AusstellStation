import pandas


def count_time_duration_between_events(input_excel_path, export_path):
    input_data = pandas.read_excel(input_excel_path, index_col=0)  # get data from excel
    input_data = input_data.get_values()  # get all values from input excel

    header = ["Time Duration", "Inbound to Outgate", "Inbound to PLRM", "PLRM to RMFC", "RMFC to ICHD",
              "Ingate to Outgate", "Ingate to Outbound", "Ingate to LDFC", "LDFC to PURM", "PURM to DFLC",
              "AVG-Count Inbound to Outgate", "AVG-Count Inbound to PLRM", "AVG-Count PLRM to RMFC",
              "AVG-Count RMFC to ICHD",
              "AVG-Count Ingate to Outgate", "AVG-Count Ingate to Outbound", "AVG-Count Ingate to LDFC",
              "AVG-Count LDFC to PURM",
              "AVG-Count PURM to DFLC"]
    result = []  # save result in this list to show in excel
    result_value = []  # save all value in all rows to
    sum_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # save sum count in each col in all rows
    value = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # save sum value in each col in all rows
    pre_index = 17
    for i in range(300):
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # save all in loop
        average = ["", "", "", "", "", "", "", "", ""]  # save avg in loop
        input = []
        input.insert(0, str(i) + "-" + str((i + 1)))  # insert first column for example 1 - 2
        for data in input_data:
            for j in range(9):  # loop from 1 to 9 for just calculate columns Dwell time
                if data[3] == "ARIL" or data[3] == "ARRI" or data[3] == "DFLC" or data[
                    3] == "ICHR":  # if current row event type == ARIL or ARRI or DFLC or ICHR (because all Shipment Dwell Times are located in each theirs row)
                    if data[pre_index + j] != "-":  # if each column Dwell time not equal with "-"
                        if data[3] == "ICHR":  # if current eventtype == ICHR
                            if data[
                                pre_index + 4] != "-":  # when current eventtype == ICHR and Ingate to OutBound Column is equal "-" thats mean this state is Ingate to Outgate
                                if i < float(data[pre_index + j]) <= i + 1:
                                    count[j] += 1
                                    value[j] += float(data[pre_index + j])
                        elif data[3] == "DFLC":
                            if data[pre_index + 5] != "-" and data[pre_index + 6] != "-" and data[
                                pre_index + 7] != "-" and data[pre_index + 8] != "-":
                                if i < float(data[pre_index + j]) <= i + 1:
                                    count[j] += 1
                                    value[j] += float(data[pre_index + j])
                        else:
                            if i < float(data[pre_index + j]) <= i + 1:
                                count[j] += 1
                                value[j] += float(data[pre_index + j])

        index = 1
        for c in count:  # add array count to array input
            input.insert(index, c)
            sum_count[index - 1] = sum_count[
                                       index - 1] + c  # add each array count to array sum_count for calculate average in the last
            index += 1

        index = 10
        for avg in average:
            input.insert(index, avg)  # add average column in result array
            index += 1
        result.append(input)
        result_value.append(value)  # add input array to result array

    for i in range(300):
        for index in range(9):
            result[0][index + 10] = format(
                (result_value[i][index] / sum_count[index] if sum_count[index] > 0 else 0), '.2f') + " - " + str(
                sum_count[index])  # calculate average between result values and array sum count

    pandas.DataFrame(result, [""] * len(result), header).to_excel(export_path)  # export data in excel


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/ShipmentDWellCalculator/"
count_time_duration_between_events(url + "output.xlsx", url + "counts.xlsx")
print("finished")
