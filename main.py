#THIS PROCESS WILL NEED STRIPPING AND CLEANING ETC:
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#INSTEAD, WE CAN USE THIS:
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) #comes out as a list that we can loop through **
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             new_temp = int(row[1])
#             temperature.append(new_temp)
#     print(temperature)




import pandas
#THERE ARE 2 TYPES OF OBJECT IN PANDAS: DATAFRAME and SERIES:
#Each sheet of excel or google sheets is a DATAFRAME
#Each list/column is a SERIES

data = pandas.read_csv("weather_data.csv")
print(type(data)) #we get a pandas dataframe object: <class 'pandas.core.frame.DataFrame'>
print(data) #prints out the data in a tabular form perfectly
print(type(data["temp"])) #we get a pandas series object: <class 'pandas.core.series.Series'>

data_dict = data.to_dict()
print(data_dict) #converts DATAFRAME into a dictionary

temp_list = data["temp"].tolist() #converts a SERIESs into a list
print(temp_list)

#Calculating AVERAGE TEMPERATURE:
total_temp = 0
for each_temp in temp_list:
    total_temp += int(each_temp)
avg_temp = total_temp / len(temp_list)
print(avg_temp) #prints: 17.428571428571427

#OR:
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp) #prints: 17.428571428571427

#OR:
avg_temp = data["temp"].mean()
print(avg_temp) #prints: 17.428571428571427

#Return MAX value of a series/volumn:
max_temp = data["temp"].max()
print(max_temp) #prints: 24

#Get Data in Columns:
print(data["condition"]) #prints the condition column....1
#OR:
print(data.condition) #prints the condition column.......1

#Get Data in Rows:
print(data[data["day"] == "Monday"]) #prints: 0  Monday    12     Sunny
print(data[data.day == "Monday"]) #prints: 0  Monday    12     Sunny

#Print row of data with MAX temp:
print(data[data.temp == data.temp.max()]) #prints: 6  Sunday    24     Sunny

monday = data[data.day == "Monday"] #gets hold of the monday row
print(monday.condition) #prints: 0    Sunny


#convert Mondats' temp into Fahrenheit:
