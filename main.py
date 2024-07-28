# with open('./weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#     print(data)
#     when you print data, you get:
#     ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


##### we can use the built-in CSV module from python #####

# import csv

# with open('./weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
    

##### or we can use pandas package #####

import pandas

data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

#constructing a Pandas Data Frame
data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')