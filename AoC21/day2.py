import pandas as pd

# Part 1:

df = pd.read_csv('/content/AoC_2_2021.csv')
df = df.rename(columns={df.columns[0]: 'Input'})
df = df[['Input']]
df = df['Input'].str.split(' ', expand=True)
df = df.rename(columns={df.columns[0]: 'direction', df.columns[1]: 'distance'})
df['distance'] = pd.to_numeric(df['distance'])

result = df.groupby('direction')['distance'].sum()

depth = result['down'] - result['up']
forward = result['forward']

print("Result Part 1")
print(depth * forward)

# Part 2:

horizontal = 0
aim_total = 0
aim_multiplier = 0

for index, row in df.iterrows():
    if row['direction'] == 'forward':
        aim_adder = 0
        horizontal += row['distance']
        aim_adder = aim_multiplier * row['distance']
        aim_total += aim_adder
    if row['direction'] == 'up':
        aim_multiplier -= row['distance']
    if row['direction'] == 'down':
        aim_multiplier += row['distance']

print("Result Part 2")
print(horizontal * aim_total)
