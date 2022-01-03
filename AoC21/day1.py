import pandas as pd

# Part 1:
header_list = ['data']
df = pd.read_csv('AoC21/data/AoC_1_1_2021.csv', names= header_list)
df = df['data']
data_list = list(df)

counter = 0
for i in range(1, len(data_list)):
    if (data_list[i - 1] < data_list[i]):
        counter += 1

print(f'Result part 1: {counter}')


# Part 2:

new_list = []
for i in range(2, len(data_list)):
    item = data_list[i] + data_list[i - 1] + data_list[i - 2]
    new_list.append(item)

counter_2 = 0
for i in range(1, len(new_list)):
    if (new_list[i - 1] < new_list[i]):
        counter_2 += 1

print(f'Result part 2: {counter_2}')
