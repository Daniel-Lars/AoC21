import csv

with open ('/content/AoC_3_1_2021.csv') as file:
    reader = csv.reader(file)
    data = list(reader)

data_clean = [item for sublist in data for item in sublist]

gamma = ''
epsilon = ''

for item in range(0, len(data_clean[0])):
    one = 0
    zero = 0
    for i in range(len(data_clean)):
        if data_clean[i][item] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

g = int(gamma, 2)
e = int(epsilon, 2)

print(g*e)
