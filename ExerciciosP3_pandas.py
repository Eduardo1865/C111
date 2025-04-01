import numpy as np
import pandas as pd

df = pd.read_csv('paises.csv', delimiter=';')

#-------------------------------------------------------------------------------

#Questão 1

#Quais são os países da Oceania:

#oceania_paises = df[df['Region'].str.upper().str.strip() == 'OCEANIA']

#oceania_paises = oceania_paises['Country'].values

#print(oceania_paises)

#Quantos Países são da oceania

#total_de_paises = np.sum(df['Region'].str.upper().str.strip() == 'OCEANIA')

#print(total_de_paises)

#-------------------------------------------------------------------------------

#Questão 2

#largest_population = df.nlargest(1, 'Population')
#print(largest_population[['Country', 'Region']])

#-------------------------------------------------------------------------------

#Questão 3

#group_region = df.groupby('Region')
#mean_literacy = group_region['Literacy (%)'].mean()

#print(mean_literacy)

#-------------------------------------------------------------------------------

#Questão 4

#no_coast_countries = df[df['Coastline (coast/area ratio)'] == 0]

#no_coast_countries.to_csv('noCoast.csv', index=False)

#-------------------------------------------------------------------------------

#Questão 5

#def classify_help(deathrate):
#    return 'Balanced' if deathrate < 9 else 'Urgent'

#df['Humanitarian Help'] = df['Deathrate'].apply(classify_help)

#print(df)