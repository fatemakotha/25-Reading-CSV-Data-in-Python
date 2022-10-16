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
