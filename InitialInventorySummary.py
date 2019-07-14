import pandas


def initial_inventory_summary(input_path, rmfc_export_path, ichr_export_path, first_start, first_end, second_end,
                              third_end, forth_end, fifth_end, number_of_days_for_input,
                              consider_null_weigth_as_empty):
    input_data = pandas.read_excel(input_path)  # get data from excel
    values = input_data.get_values()  # get all values from input excel

    first_result = []
    second_result = []

    count_20 = 0
    count_40 = 0
    count_45 = 0
    first_count = 0
    second_count = 0
    third_count = 0
    forth_count = 0
    fifth_count = 0
    sixth_count = 0
    seventh_count = 0
    rmfc_eqinit_list = []
    ichr_eqinit_list = []

    count = [0] * 42
    cities = ["GARDEN_CITY", "CHARLESTON", "GREER", "MEMPHIS", "CHICAGO", "JACKSONVILLE", "NEW_ORLEANS"]
    loaded = ["E", "L"]
    length_list = [20, 40, 45]

    for data in values:
        if not data[1] in rmfc_eqinit_list:
            for sub_data in values:
                if data[1] == sub_data[1]:
                    if sub_data[4] == 'RMFC':
                        rmfc_eqinit_list.append(data[1])
                        if sub_data[6] == 20:
                            count_20 += 1
                        if sub_data[6] == 40:
                            count_40 += 1
                        if sub_data[6] == 45:
                            count_45 += 1

                        if sub_data[20] <= first_start:
                            first_count += 1
                        if first_start < sub_data[20] <= first_end:
                            second_count += 1
                        if first_end < sub_data[20] <= second_end:
                            third_count += 1
                        if second_end < sub_data[20] <= third_end:
                            forth_count += 1
                        if third_end < sub_data[20] <= forth_end:
                            fifth_count += 1
                        if forth_end < sub_data[20] <= fifth_end:
                            sixth_count += 1
                        if sub_data[20] > fifth_end:
                            seventh_count += 1

        if not data[1] in ichr_eqinit_list:
            for sub_data in values:
                if data[1] == sub_data[1]:
                    if sub_data[4] == 'ICHR':
                        ichr_eqinit_list.append(data[1])
                        i = 0
                        for i1 in range(len(cities)):
                            for i2 in range(len(length_list)):
                                for i3 in range(len(loaded)):
                                    count[i] += get_count(sub_data, length_list[i2], loaded[i3], cities[i1],
                                                          consider_null_weigth_as_empty)
                                    i += 1

    result = []
    result.insert(0, count_20 / number_of_days_for_input)
    result.insert(1, count_40 / number_of_days_for_input)
    result.insert(2, count_45 / number_of_days_for_input)
    result.insert(3, first_count / number_of_days_for_input)
    result.insert(4, second_count / number_of_days_for_input)
    result.insert(5, third_count / number_of_days_for_input)
    result.insert(6, forth_count / number_of_days_for_input)
    result.insert(7, fifth_count / number_of_days_for_input)
    result.insert(8, sixth_count / number_of_days_for_input)
    result.insert(9, seventh_count / number_of_days_for_input)
    first_result.append(result)

    header = ["20", "40", "45", "0 - " + str(first_start), str(first_start) + " - " + str(first_end),
              str(first_end) + " - " + str(second_end), str(second_end) + " - " + str(third_end),
              str(third_end) + " - " + str(forth_end), str(forth_end) + " - " + str(fifth_end),
              str(fifth_end) + " - ..."]
    pandas.DataFrame(first_result, [""] * len(first_result), header).to_excel(rmfc_export_path)  # export data

    i = 0
    for i1 in range(len(cities)):
        for i2 in range(len(length_list)):
            for i3 in range(len(loaded)):
                second_result.append(
                    [str(length_list[i2]) + loaded[i3] + cities[i1], count[i] / number_of_days_for_input])
                i += 1

    header = ["category", "count"]
    pandas.DataFrame(second_result, [""] * len(second_result), header).to_excel(ichr_export_path)  # export data


def get_count(shipment, length, empty_loaded, city, consider_null_weigth_as_empty):
    count = 0
    if city == 'GARDEN_CITY':
        if shipment[6] == length and ((shipment[16] == '?' if empty_loaded == 'E' else shipment[
                                                                                           16] != '?') if consider_null_weigth_as_empty == True else
        shipment[5] == empty_loaded) and (shipment[10] == city or shipment[
            10] == 'SAVANNAH'):  # if city name is savannah add count to garden city
            count += 1
    elif city == 'CHARLESTON':
        if shipment[6] == length and ((shipment[16] == '?' if empty_loaded == 'E' else shipment[
                                                                                           16] != '?') if consider_null_weigth_as_empty == True else
        shipment[5] == empty_loaded) and (shipment[10] == city or shipment[
            10] == 'NORTH_CHARLESTON'):  # if city name is north charleston add count to charleston
            count += 1
    elif city == 'NEW_ORLEANS':
        if shipment[6] == length and ((shipment[16] == '?' if empty_loaded == 'E' else shipment[
                                                                                           16] != '?') if consider_null_weigth_as_empty == True else
        shipment[5] == empty_loaded) and (
                shipment[10] == city or shipment[10] == 'MCCALLA'):  # if city name is MCCALLA add count to NEW_ORLEANS
            count += 1
    elif city == 'CHICAGO':
        if shipment[6] == length and ((shipment[16] == '?' if empty_loaded == 'E' else shipment[
                                                                                           16] != '?') if consider_null_weigth_as_empty == True else
        shipment[5] == empty_loaded) and (
                shipment[10] == city or shipment[10] == 'COLUMBUS'):  # if city name is COLUMBUS add count to CHICAGO
            count += 1
        elif shipment[6] == length and ((shipment[16] == '?' if empty_loaded == 'E' else shipment[
                                                                                             16] != '?') if consider_null_weigth_as_empty == True else
        shipment[5] == empty_loaded) and (shipment[10] == city or shipment[
            10] == 'CINCINNATI'):  # if city name is CINCINNATI add count to CHICAGO
            count += 1
        elif shipment[6] == length and ((shipment[16] == '?' if empty_loaded == 'E' else shipment[
                                                                                             16] != '?') if consider_null_weigth_as_empty == True else
        shipment[5] == empty_loaded) and (shipment[10] == city or shipment[
            10] == 'GEORGETOWN'):  # if city name is GEORGETOWN add count to CHICAGO
            count += 1
    else:
        if shipment[6] == length and ((shipment[16] == '?' if empty_loaded == 'E' else shipment[
                                                                                           16] != '?') if consider_null_weigth_as_empty == True else
        shipment[5] == empty_loaded) and shipment[
            10] == city:  # if length and empty loaded and city is equel => count++
            count += 1
    return count


print("Start")
url = "C:/Users/Hassan/Desktop/pythonExport/InitialInventorySummary/"
initial_inventory_summary(url + 'input.xlsx', url + "RMFC_Output.xlsx", url + "ICHR_Output.xlsx", 30, 60, 70, 80, 90,
                          100, 2, True)
print("Finished")
