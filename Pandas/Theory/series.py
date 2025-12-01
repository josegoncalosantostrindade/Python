import pandas as pd

'''data = [100, 102, 104, 200, 202] 

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# print(series.loc['c'])
# print(series.iloc[2])

print(series[series < 200])'''


calories = {'Day 1': 1750, 'Day 2': 2100, 'Day 3': 1700}

series = pd.Series(calories)

# series.loc['Day 3'] += 500
# print(series.loc['Day 3'])

print(series[series >= 2000])