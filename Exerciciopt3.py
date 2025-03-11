import numpy as np 
import pandas as pd


dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
# Exercicio 1
# sucesso ta no 7
# success_count = np.sum(dataset[:, 7] == 'Success')
# total_linhas = dataset.shape[0]
# porcentagem = (success_count/(int(total_linhas)-2))*100
# print(f"Porcentagem de sucessos: {porcentagem}%")

#----------------------------------------------------------------------------
# Exercicio 2

# sdv = np.sum(dataset[1:, 6].astype(float)[dataset[1:, 6].astype(float) > 0])  # soma dos valores maiores que 0 convertidos para float

# tlez = np.count_nonzero(dataset[1:, 6].astype(float)) # total de linhas excluindo 0

# media = sdv/tlez

# print(media)

#----------------------------------------------------------------------------
# Execicio 3

# missoes = dataset[np.char.find(dataset[:, 2], 'USA') != -1]
# print(missoes)

#----------------------------------------------------------------------------
# Exercicio 4

# spacex = dataset[np.char.find(dataset[:, 1], 'SpaceX') != -1]
# caro = spacex[np.argmax(spacex[:, 6].astype(float))]
# print(f"A missão mais cara da SpaceX: {caro}")

#----------------------------------------------------------------------------
# Exercicio 5

# empresas = dataset[1:, 1]

# unique_empresas, counts = np.unique(empresas, return_counts=True)

# for empresa, count in zip(unique_empresas, counts):
    # print(f"{empresa}: {count} missões")