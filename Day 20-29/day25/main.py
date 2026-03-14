# # with open("weather.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data[0])
#
# # import csv
# #
# # with open("weather.csv") as file:
# #     reader = csv.reader(file)
# #
# #     temp = []
# #     for row in reader:
# #         print(row)
# #         if row[1] != "temp":
# #             temp.append(row[1])
# #     print(temp)
#
# import pandas
# data = pandas.read_csv("weather.csv")
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
#
# # print(data["temp"].max())
# # print(data.temp)
# # print(data[data.temp == data.temp.max()])
# dd = pandas.DataFrame(data_dict)
# dd.to_csv("weather_new.csv")
# print(dd)

import pandas
data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur color" :["Gray", "Black", "Cinnamon"],
    "Count":[gray_count, black_count, cinnamon_count]

}
df = pandas.DataFrame(data_dict)
df.to_csv("colour_count.csv")
print(df)