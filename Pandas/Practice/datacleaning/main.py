import pandas as pd

df = pd.read_csv('/Users/jgtrindade/Desktop/Curriculo/Python/Pandas/Practice/datacleaning/pokemon.csv')

# df = df.dropna(subset=['Type2'])
df = df.fillna({'Type2': 'None'})

df['Legendary'] = df['Legendary'].astype(bool)

df = df.drop_duplicates()
print(df.to_string())