import pandas as pd

df = pd.read_csv('/Users/jgtrindade/Desktop/Curriculo/Python/Pandas/Theory/datacleaning/pokemon.csv')

# Drop irrelevant columns
# df = df.drop(columns=['Legendary', 'No'])


# Handle missing data
'''df = df.dropna(subset=['Type2'])
df = df.fillna({'Type2': 'None'})'''


# Fix inconsistent values
'''df['Type1'] = df['Type1'].replace({'Grass': 'GRASS',
                                   'Fire': 'FIRE',
                                   'Water': 'WATER'})'''


# Standardize text
# df['Name'] = df['Name'].str.lower()


# Fix data types
# df['Legendary'] = df['Legendary'].astype(bool)


# Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())