# # with open('./weather_data.csv') as file:
# #     weather_list = [line for line in file.readlines()]

# # print(weather_list)

# # import csv


# # with open('./weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         print(row)
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #     print(temperature)

# import pandas

# data = pandas.read_csv('./weather_data.csv')

# # print(data['temp'])

# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data['temp'].to_list()
# # # print(temp_list)


# # print(f'Avg: {sum(temp_list)/len(temp_list)}')

# # print(data['temp'].mean())

# # print(data['temp'].max())

# # print(data['condition'])
# # print(data.condition)

# print(data[data.temp == data.temp.max() ] )

import pandas

squirrel_data = pandas.read_csv('squirrel_data.csv')

gray_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Color":["Grey","Cinnamon","Black"],
    "Count":[gray_squirrels,red_squirrels,black_squirrels]
}

squirrel_dataframe = pandas.DataFrame(data_dict)
print(squirrel_dataframe)
squirrel_dataframe.to_csv("squirrel_count.csv")


# print(squirrel_data.groupby(['Primary Fur Color'])['Primary Fur Color'].count())
