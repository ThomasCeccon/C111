import numpy as np
import pandas as pd

'''
Pandas: Permite dados heterogeneos
'''

# Series (1D) trabalha com chave e valor (dicionario)
dic={'A':10,
     'B':20,
     'C':30 }

#criar uma series
s1=pd.Series(dic)
s2=pd.Series(data=[20,30,40],index=['A','B','D']) #indicar dados e os indices
print(s1+s2)  #c e d nao haviam nada (NaN)
print(s1.add(s2,fill_value=0))#valores vazios serao zero de nan para 0
print(s1['B'])#acessar 1 elemento 
print(s1[['B','C']])#acesso a multiplos elementos

print(s1[s1 >s1.mean()])#quais valores de s1 sao maiores que a media (condicional)



# Dataframe (2D)
np.random.seed(10)
df=pd.DataFrame(
  index=['a','b','c','d'],
  columns=['x', 'y','z'],
  data=np.random.randint(1,50,12).reshape(4,3)
)
print(df)
print(df[['x','y']])
print(df['x']['a'])

print('====================')

#slice com loc
print('loc')
print(df.loc[['b','c'],['x','y','z']],'\n') # acessar linhas B e C e as colinas X Y e Z
#print(df[['a'],['x']])

# slice com iloc
print('iloc')
print(df.iloc[1:3:]) #linhas de 1 a 3 e todas as colunas

#leitura de arquivos .csv com Pandas
df=pd.read_csv('paises.csv',delimiter=';')
print("===========")
print(df)
print("===========")
print(df.columns)# buscar colunas dos datasets
print("===========")
print(df['Country'])#buscas os paises
print("===========")
print(df.head(5)) #buscar os 5 primerios registros
print("===========")
print(df.tail(2))#buscar os 2 ultimos registros
print("===========")