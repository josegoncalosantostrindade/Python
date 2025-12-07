import pandas as pd

df = pd.read_csv('/Users/jgtrindade/Desktop/Curriculo/Python/Pandas/Practice/basicanalysis/pokemon.csv')

print(df.head()) # first 5
print(df.info())
print(df.describe())

print('\n**** FILTER HEIGHT ****')
tall_pokemon = df[df['Height'] >= 2] # filtering by height
print(tall_pokemon)

print('\n**** FILTER TYPE ****')
water_pokemon = df[(df['Type1'] == 'Water') | (df['Type2'] == 'Water')] # filtering by type
print(water_pokemon)

print('\n**** SORT WEIGHT ****')
print(df.sort_values(by=['Weight']))