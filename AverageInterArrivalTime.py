import pandas
from fitter import Fitter


def main(input_path, export_path):
    data_frame = pandas.read_excel(input_path)  # get data from excel
    unique_data_frame = data_frame.drop_duplicates(['hour', 'unit'])
    unique_data = unique_data_frame.replace('\n', ' ', regex=True).get_values()
    data = data_frame.replace('\n', ' ', regex=True).get_values()

    result = []
    for u in unique_data:
        sum = 0
        count = 0
        ar = []
        for d in data:
            if u[0] == d[0] and u[3] == d[3]:
                sum += int(d[1])
                count += 1
                ar.append(d[1])
        avg = sum / count
        fit = Fitter(ar, min(ar), max(ar), len(ar), distributions=['gamma', 'rayleigh', 'uniform'])
        fit.fit()
        result.append([u[0], u[3], avg, str(fit.fitted_param), str(fit.get_best())])

    header = ["Hour", "Unit", "Average", "Distribution", "Best Distribution"]
    pandas.DataFrame(result, None, header).to_excel(export_path)  # export data in excel


print("start")
url = "C:/Users/Hassan/Desktop/pythonExport/AverageInterArrivalTime/"
main(url + "input.xlsx", url + "export.xlsx")
print("finished")
