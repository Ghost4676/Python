import csv
import pandas
# with open("Book1.csv") as data_file:
#     data = csv.reader(data_file)
#     tempeature = []
#     for row in data:
#         if row[1] !="temp":
#             tempeature.append(int(row[1]))
#     print(tempeature)

#################################################

# data = pandas.read_csv("Book1.csv")
# alpha = (data["temp"])
# #print(alpha)

# temp_list = data["temp"].to_list()
# #print(temp_list)

# add = int(sum(temp_list))
# tot = int(len(temp_list))

# #print(f"The average tempis {add/tot}")

# maxx = data["temp"].max()
# #print(maxx)

# #print(data[data.temp == int(maxx)])

# monday = data[data.day == "Monday"]
# print(f"{((monday.temp/5)*9)+32}")
# #((x/5)*9) + 32 

#####################################
# Create a CSV file with the data
#####################################
# data_dict = {
#     "students": ["A","B","C"],
#     "score": [1,6,0]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("testtt_data.csv")

########################################

data = pandas.read_csv("Central_Park.csv")
#print(data.PColor)

G = 0
C = 0
B = 0

for color in data.PColor:
    if color == "Gray":
        G += 1
    elif color == "Black":
        B += 1
    elif color == "Cinnamon":
        C += 1

print(G)
print(B)
print(C)



data_dict = {
    "Fur Colour": ["Gray","Black","Cinnamon"],
    "Count": [G,B,C]
}

data = pandas.DataFrame(data_dict)
data.to_csv("testt_data.csv")