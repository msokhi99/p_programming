# Method 1:

# with open("./weather_data.csv",mode="r") as weather_data_file:
#     contents=weather_data_file.readlines()
#     print(contents)

# Method 2:

# import csv
#
# with open("./weather_data.csv",mode="r") as weather_data_file:
#     data=csv.reader(weather_data_file)
#     temp=[]
#     for row in data:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
#     print(temp)

# Method 3: (Preferred Method)

import pandas as pd
data=pd.read_csv("./weather_data.csv")
# temp_data=data["temp"].to_list()
# total_sum=0
# for temp in temp_data:
#     total_sum+=temp
# print(f"Average temp. is: {round((total_sum/len(temp_data)),2)}")
#
# print(data["temp"].max())

# print(data[data.temp==data.temp.max()])

monday=data[data.day=="Monday"]
temp_in_celsius=monday.temp[0]
temp_in_farenheit=(temp_in_celsius * 9/5) + 32
print(f"The temp in F is: {temp_in_farenheit}")

# Squirrel dataset analysis:

sq_dataset=pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

sq_primary_fur_color=sq_dataset["Primary Fur Color"].value_counts()
sq_primary_fur_color.to_csv("fur_One.csv", index="True")
