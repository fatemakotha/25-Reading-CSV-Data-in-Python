#THIS PROCESS WILL NEED STRIPPING AND CLEANING ETC:
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#INSTEAD, WE CAN USE THIS:
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file) #comes out as a list that we can loop through **
    temperature = []
    for row in data:
        new_temp = row[1]
        temperature.append(new_temp)
    print(temperature)