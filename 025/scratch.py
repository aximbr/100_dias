#Day 025
# import csv
# temperature = []

# with open("weather-data.csv", "r") as fp:
#     data = csv.reader(fp)    
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
    
#     print(temperature)
import pandas

# data = pandas.read_csv("weather-data.csv")

# #print(data)
# #print(data["temp"])
# data_to_dict = data.to_dict()
# #print(data_to_dict)

# temp_list = data["temp"].to_list()

# print(temp_list)
# # average_temp = sum(temp_list)/len(temp_list)
# # average_temp = data["temp"].mean()
# # max_temp = data["temp"].max()

# average_temp = data.temp.mean()
# max_temp = data.temp.max()

# print(average_temp)
# print(max_temp)
        
# #Get data from a row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# print(monday.temp)

# temp_far = monday.temp * 9/5 +32

# print(temp_far)

#Create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)

# data.to_csv("my_data.csv")
raw_data = pandas.read_csv("2018-squirreal.csv")

colors = raw_data.groupby("Primary Fur Color")

print(colors["Primary Fur Color"].count())

new_df = colors["Primary Fur Color"].count().to_frame()

new_df.to_csv("squirrel_fur.csv")