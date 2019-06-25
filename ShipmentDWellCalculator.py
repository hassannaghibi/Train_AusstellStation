import datetime

import pandas


def shipment_dwell_calculator(input_path, export_path):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    result = []
    header = ["EQ_INIT_NR", "WAYBILL", "EVENT TIMESTAMP LOCAL",
              "EVENT TYPE", "TRN", "LOADED EMPTY", "EQ LENGTH", "EQ TYPE", "NS ORGIN", "NS ORIGIN ST",
              "NS DEST",
              "NS DEST ST", "ORGN", "ORGN ST", "DEST", "DEST ST", "WEIGHTS", "CY_NotStackable", "Inbound to Outgate",
              "Inbound to PLRM",
              "PLRM to RMFC", "RMFC to ICHD", "Ingate to Outgate", "Ingate to Outbound", "Ingate to LDFC",
              "LDFC to PURM", "PURM to DFLC", "Not Found", "Notice"]
    for value in values:
        data = [value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9],
                value[10], value[11], value[12], value[13], value[14], value[15], value[16], value[17],
                "-", "-", "-", "-", "-", "-", "-", "-", "-", True, False]
        result.append(data)

    index = 0
    for data in result:
        if data[3] == "ARIL" or data[3] == "ARRI" or data[3] == "ICHR":  # check event type
            time = data[2]
            plrm_time = ""
            rmfc_time = ""
            ldfc_time = ""
            purm_time = ""
            rmfc_ichd_time = 0
            ldfc_purm_time = 0
            plrm_rmfc_time = 0
            purm_dflc_time = 0
            arival_plrm_time = 0
            ichr_ldfc_time = 0
            sub_index = 0
            for i in range(index, len(result)):
                sub_time = result[index + sub_index][2]  # get current shipment event timestamp
                result_time = ((
                                       sub_time.timestamp() - time.timestamp()) / 60) / 60  # calculate between time in current shipment event timestamp and arrival event timestamp
                if result_time > 0:
                    result_time = float(format(((sub_time.timestamp() - time.timestamp()) / 60) / 60,
                                               '.2f'))  # just show two decimal places
                    if result[index + sub_index][0] == data[0]:  # if arrival eqinitnr == current shipment eqinitnr
                        if data[3] == "ARIL" or data[3] == "ARRI":  # if arrival eventtype == ARIL or ARRI
                            if result[index + sub_index][3] == "DFLC":  # if current shipment eventtype == DFLC
                                break
                            elif result[index + sub_index][3] == "ICHD":  # if current shipment eventtype == ICHD
                                if rmfc_ichd_time > 0:  # if RMFC TO ICHD Dwell time > 0
                                    rmfc_ichd_time = float(
                                        format(((sub_time.timestamp() - rmfc_ichd_time) / 60) / 60, '.2f'))
                                    result[index][21] = rmfc_ichd_time
                                    result[search_index_in_values(result, result[index][0], rmfc_time, "RMFC")][
                                        21] = rmfc_ichd_time
                                    result[index + sub_index][21] = rmfc_ichd_time
                                    result[index][18] = arival_plrm_time + plrm_rmfc_time + rmfc_ichd_time
                                    result[index + sub_index][18] = arival_plrm_time + plrm_rmfc_time + rmfc_ichd_time
                                else:
                                    result[index][18] = arival_plrm_time + plrm_rmfc_time + rmfc_ichd_time
                                    result[index + sub_index][18] = arival_plrm_time + plrm_rmfc_time + rmfc_ichd_time
                                break
                            elif result[index + sub_index][3] == "PLRM":  # if current shipment eventtype == PLRM
                                plrm_time = result[index + sub_index][2]
                                if plrm_rmfc_time == 0 and rmfc_ichd_time == 0:
                                    plrm_rmfc_time = sub_time.timestamp()
                                    arival_plrm_time = result_time
                                    result[index][19] = result_time
                                    result[index + sub_index][19] = result_time
                                else:
                                    result[index + sub_index][28] = True
                                    plrm_rmfc_time = sub_time.timestamp()
                                    arival_plrm_time = result_time
                                    result[index][19] = result_time
                                    result[index + sub_index][19] = result_time
                            elif result[index + sub_index][3] == "RMFC":  # if current shipment eventtype == RMFC
                                rmfc_time = result[index + sub_index][2]
                                if plrm_rmfc_time > 0 and rmfc_ichd_time == 0:
                                    rmfc_ichd_time = sub_time.timestamp()
                                    plrm_rmfc_time = float(
                                        format(((sub_time.timestamp() - plrm_time.timestamp()) / 60) / 60,
                                               '.2f'))
                                    result[index][20] = plrm_rmfc_time
                                    result[search_index_in_values(result, result[index][0], plrm_time, "PLRM")][
                                        20] = plrm_rmfc_time  # in the first finding previews index with function search_index_in_values and the end write PLRM To RMFC Dwell Time in this Column
                                    result[index + sub_index][20] = plrm_rmfc_time
                                else:
                                    result[index + sub_index][28] = True
                                    break
                            else:
                                result[index + sub_index][28] = True
                                break
                        elif data[3] == "ICHR":  # if arrival eventtype == ICHR
                            if result[index + sub_index][3] == "ICHD":  # if current shipment eventtype == ICHD
                                if ldfc_purm_time == 0 and purm_dflc_time == 0:
                                    result[index][22] = result_time
                                    result[index + sub_index][22] = result_time
                                    break
                                else:
                                    result[index + sub_index][28] = True
                                    break
                            elif result[index + sub_index][3] == "DFLC":  # if current shipment eventtype == DFLC
                                if purm_dflc_time > 0:
                                    purm_dflc_time = float(
                                        format(((sub_time.timestamp() - purm_dflc_time) / 60) / 60, '.2f'))
                                    result[index][26] = purm_dflc_time  # show purm_dflc_time in ICHR place
                                    result[index + sub_index][26] = purm_dflc_time  # show purm_dflc_time in DFLC place
                                    result[search_index_in_values(result, result[index][0], purm_time, "PURM")][
                                        26] = purm_dflc_time  # show purm_dflc_time in PURM place
                                    result[index][25] = ldfc_purm_time  # show ldfc_purm_time in ICHR place
                                    result[index + sub_index][25] = ldfc_purm_time  # show ldfc_purm_time in DFLC place
                                    result[index][24] = ichr_ldfc_time  # show ichr_ldfc_time in ICHR place
                                    result[index + sub_index][24] = ichr_ldfc_time  # show ichr_ldfc_time in DFLC place
                                    result[index][
                                        23] = ichr_ldfc_time + ldfc_purm_time + purm_dflc_time  # show ichr_ldfc_time in DFLC place
                                    result[index + sub_index][23] = ichr_ldfc_time + ldfc_purm_time + purm_dflc_time
                                else:
                                    if ichr_ldfc_time > 0 and ldfc_purm_time > 0 and purm_dflc_time > 0:
                                        result[index][23] = ichr_ldfc_time + ldfc_purm_time + purm_dflc_time
                                        result[index + sub_index][23] = ichr_ldfc_time + ldfc_purm_time + purm_dflc_time
                                break
                            elif result[index + sub_index][3] == "PURM":  # if current shipment eventtype == PURM
                                purm_time = result[index + sub_index][2]
                                if ldfc_purm_time > 0 and purm_dflc_time == 0:
                                    purm_dflc_time = sub_time.timestamp()
                                    ldfc_purm_time = float(format(((sub_time.timestamp() - ldfc_purm_time) / 60) / 60,
                                                                  '.2f'))
                                    result[index][24] = ldfc_purm_time
                                    result[index + sub_index][24] = ldfc_purm_time
                                    result[search_index_in_values(result, result[index][0], ldfc_time, "LDFC")][
                                        25] = ldfc_purm_time
                                else:
                                    result[index + sub_index][28] = True
                                    purm_dflc_time = sub_time.timestamp()
                                    ldfc_purm_time = float(
                                        format(((sub_time.timestamp() - ldfc_time.timestamp()) / 60) / 60,
                                               '.2f'))
                                    result[index][25] = ldfc_purm_time
                                    result[index + sub_index][25] = ldfc_purm_time
                                    result[search_index_in_values(result, result[index][0], ldfc_time, "LDFC")][
                                        25] = ldfc_purm_time
                            elif result[index + sub_index][3] == "LDFC":  # if current shipment eventtype == LDFC
                                ldfc_time = result[index + sub_index][2]
                                if ldfc_purm_time == 0 and purm_dflc_time == 0:
                                    ldfc_purm_time = sub_time.timestamp()
                                    ichr_ldfc_time = result_time
                                    result[index][24] = ichr_ldfc_time
                                    result[index + sub_index][24] = ichr_ldfc_time
                                else:
                                    result[index + sub_index][28] = True
                                    break
                            else:
                                result[index + sub_index][28] = True
                                break
                sub_index += 1
        index += 1

    index = 0
    for data in result:  # this loop for detect any rows that all column Dwell times is "-"
        result[index][27] = True if data[18] == "-" and data[19] == "-" and data[20] == "-" and data[21] == "-" and \
                                    data[22] == "-" and data[23] == "-" and data[24] == "-" and data[25] == "-" and \
                                    data[26] == "-" else False
        index += 1

    pandas.DataFrame(result, [""] * len(result), header).to_excel(export_path)  # export data in excel


def search_index_in_values(values, eq_init_nr, time, event_type):
    i = 0
    for data in values:
        if data[0] == eq_init_nr and data[2] == time and data[
            3] == event_type:  # if current row eqinitnr == eqinitnr (entries)
            break
        i += 1
    return i


def convert_str_to_time(date):  # convert str date to real date type
    start_date = date.split()
    date = start_date[0].split("/")  # split date with /
    time = start_date[1].split(":")  # split time with :

    year = int(date[2])
    month = int(date[0])
    day = int(date[1])
    hour = int(time[0])
    minute = int(time[1])
    second = int(time[2])

    result = datetime.datetime(year, month, day, hour, minute, second)  # convert str to time
    return result


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/ShipmentDWellCalculator/"
shipment_dwell_calculator(url + "input.xlsx", url + "output.xlsx")
print("finished")
