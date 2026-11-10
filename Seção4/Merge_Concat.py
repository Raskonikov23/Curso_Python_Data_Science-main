"""
Funcao merge e utilizada para unir duas listas ordenadas em uma unica lista ordenada.
Funcao concat tem o objetivo de juntar duas listas, mas nao necessariamente ordenadas, em uma unica lista.
import pandas as pd 
import numpy as np

dfa = pd.DataFrame(np.arange(15).reshape(5,3))

dfb = pd.DataFrame((np.arange(9)**2).reshape(3,3))

pd.concat([dfa, dfb], axis=0) # axis=0 significa que a concatenação será feita verticalmente (linhas)   

print(pd.concat([dfa, dfb]))

"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'cor': ['azul', 'vermelho', 'verde']
})

print(df1)

df2 = pd.DataFrame({
    'times': ['time1', 'time2', 'time3', 'time4'],
    'id_cor': [1, 2, 3, 4]
})

print(df2)

# Junção utilizando colunas com nomes diferentes
resultado = pd.merge(
    df1,
    df2,
    left_on='id',
    right_on='id_cor'
)

print(resultado)
