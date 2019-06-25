import pandas


def calculator(first_input_path, second_input_path, export_path, consider_waybill,
               consider_timestamp):
    first_input_data = pandas.read_excel(first_input_path)  # get data from excel
    first_values = first_input_data.get_values()  # get all values from input excel

    second_input_data = pandas.read_excel(second_input_path)  # get data from excel
    second_values = second_input_data.get_values()  # get all values from input excel

    result = []
    for first_data in first_values:  # first file finding
        eqinitnr_status = False

        if consider_waybill:
            waybill_status = False

        if consider_timestamp:
            timestamp_status = False

        for second_data in second_values:
            if first_data[0] == second_data[0]:
                eqinitnr_status = True

            if consider_waybill:
                if first_data[1] == second_data[1]:
                    waybill_status = True

            if consider_timestamp:
                if first_data[2] == second_data[2]:
                    timestamp_status = True

        if consider_timestamp and consider_waybill:
            if not eqinitnr_status and not waybill_status and not timestamp_status:
                result.append(first_data[0])
        elif consider_waybill and not consider_timestamp:
            if not eqinitnr_status and not waybill_status:
                result.append(first_data[0])
        elif not consider_waybill and consider_timestamp:
            if not eqinitnr_status and not timestamp_status:
                result.append(first_data[0])
        else:
            if not eqinitnr_status:
                result.append(first_data[0])

    for second_data in second_values:  # second file finding
        eqinitnr_status = False

        if consider_waybill:
            waybill_status = False

        if consider_timestamp:
            timestamp_status = False

        for first_data in first_values:

            if second_data[0] == first_data[0]:
                eqinitnr_status = True

            if consider_waybill:
                if second_data[1] == first_data[1]:
                    waybill_status = True

            if consider_timestamp:
                if second_data[2] == first_data[2]:
                    timestamp_status = True

        if consider_timestamp and consider_waybill:
            if not eqinitnr_status and not waybill_status and not timestamp_status:
                result.append(second_data[0])
        elif consider_waybill and not consider_timestamp:
            if not eqinitnr_status and not waybill_status:
                result.append(second_data[0])
        elif not consider_waybill and consider_timestamp:
            if not eqinitnr_status and not timestamp_status:
                result.append(second_data[0])
        else:
            if not eqinitnr_status:
                result.append(second_data[0])

    header = ["EQ_INIT_NR"]
    pandas.DataFrame(result, [""] * len(result), header).to_excel(export_path)  # export data in excel


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/FindEqinitnr/"
calculator(url + "first_input.xlsx", url + "second_input.xlsx", url + "output.xlsx", True,
           True)  # consider_waybill , consider_timestamp
print("finished")
