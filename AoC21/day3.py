import csv
from copy import copy

with open ('AoC21/data/AoC_3_1_2021.csv') as file:
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

print(f'result part 1: {g*e}')

oxygen_diagnostic = copy(data_clean)

index = 0
while len(oxygen_diagnostic) > 1:
    zero = 0
    one = 0
    zero_list = []
    one_list = []
    for i in range(0, len(oxygen_diagnostic)):
        if oxygen_diagnostic[i][index] == '0':
            zero += 1
            zero_list.append(oxygen_diagnostic[i])
        else:
            one += 1
            one_list.append(oxygen_diagnostic[i])

    if one >= zero:
        oxygen_diagnostic = one_list
    else:
        oxygen_diagnostic = zero_list
    index += 1

oxygen = int(oxygen_diagnostic[0],2)

co2_diagnostic = copy(data_clean)

index = 0
while len(co2_diagnostic) > 1:
    zero = 0
    one = 0
    zero_list = []
    one_list = []
    for i in range(0, len(co2_diagnostic)):
        if co2_diagnostic[i][index] == '0':
            zero += 1
            zero_list.append(co2_diagnostic[i])
        else:
            one += 1
            one_list.append(co2_diagnostic[i])

    if one < zero:
        co2_diagnostic = one_list
    else:
        co2_diagnostic = zero_list
    index += 1

co2 = int(co2_diagnostic[0],2)

print(f'result part 2: {oxygen * co2}')
