import pandas as pd

df = pd.read_csv('/Users/jgtrindade/Desktop/Curriculo/Python/Pandas/Theory/aggregation/pokemon.csv')

# Whole Dataframes
'''print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())'''

# Single Column
'''print(df['Height'].mean())
print(df['Height'].sum())
print(df['Height'].min())
print(df['Height'].max())
print(df['Height'].count())'''


group = df.groupby('Type1')
'''print(group['Height'].mean()) # average height for each type1
print(group['Height'].sum()) # sum of the heights for each type1
print(group['Height'].min())
print(group['Height'].max())
print(group['Height'].count())'''