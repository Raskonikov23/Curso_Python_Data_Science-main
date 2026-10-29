""" 

Dados 

import pandas as pd

lista_a = [11,22,33,44,55]
lista_b = ['a','b','c','d', 'e']
series_1 = pd.Series(lista_a)
print(series_1)
print(series_1.cumsum())

import numpy as np
arr = np.arange(10)**2
print(arr)

dic = {'a':1, 'b':2, 'c':3}
print(dic)
serie_4 = pd.Series(dic)
print(serie_4)
#Criando uma Dataframe
df = pd.DataFrame({'coluna1': lista_a, 'coluna2': lista_b})
print(df)

import numpy as np
import pandas as pd 
lista_a = ['a','b','c','d','e','f','g']
print(len(lista_a))

lista_b = list(range(7))
print(lista_b)

dic = {'string': lista_a, 'numeros': lista_b}
print(dic)

df = pd.DataFrame(dic)
print(df)
df2 = pd.DataFrame({'col1':np.arange(100)**2, 'col2':np.arange(100)*5})
print(df2.head(10)) #head mostra as 10 primeiras linhas do dataframe
print(df2.tail(10)) #tail mostra as 10 últimas linhas do dataframe
print(df2.describe()) #describe mostra estatísticas do dataframe
"""
# Tratando Dados 
import pandas as pd
file = 'nba2k-full.csv'
nba = pd.read_csv(file)
#print(nba.head(10))
#print(nba.shape) #shape mostra o número de linhas e colunas do dataframe)
#print(nba.columns) #columns mostra o nome das colunas do dataframe
#print(nba['height'].mean()) #mean mostra a média das colunas numéricas do dataframe

#razao = nba['height'].mean() / nba['weight'].mean()
#print(razao)
print(nba.columns)
print(nba.sort_values(by='height')) #sort_values ordena os valores de uma coluna do dataframesudo ap
