import pandas as pd

df = pd.read_csv('/Users/jgtrindade/Desktop/Curriculo/Python/Pandas/Practice/advancedstatistics/pokemon.csv')

group = df.groupby('Type1')

'''legendary_pokemon = df[df['Legendary'] == 1]
print(legendary_pokemon)'''

print(group['Height'].mean())
print(group['Height'].sum())
print(group['Height'].median())