import pandas as pd
import numpy as np

dfPaises=pd.read_csv('paises (1).csv',delimiter=';')


#Series em pandas
S1=pd.Series(index=['A','B','C'],data=[30,40,50])
S2=pd.Series(index=['A','B','C'],data=[1,2,3])
S3=pd.Series(index=['D','E','F'],data=[60,70,80])
print(S1+S2,'\n')
print(S1.add(S3,fill_value=0))

#Mostrar o que esta em A
print(S1['A'])

#Mostrar o que esta em A,B e C
print(S1[['A','B','C']])

#somar o que possui em A e B
print(S1['A']+S1['B'])

#DataFrame
np.random.seed(10)
df=pd.DataFrame(index=['A','B'],columns=['X','Y'],data=np.random.randint(1,50,4).reshape(2,2))
print(df,'\n')

#EX1: Fazer a soma das colunas X e Y
somaX=df['X'].sum()
print("SOMA EM X:",somaX)
somaY=df['Y'].sum()
print("SOMA EM Y:",somaY,'\n')

#EX2: Fazer a soma das linhas A e B
somaA=df['X'][0:].sum()
print("SOMA EM A:",somaA)

#ex1- mostrar os paises da oceania
paises_oceania=dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
print("Paises da oceania: ",paises_oceania)

'''
PORQUE NÃO FUNCIONA ASSIM
paises_oceania=dfPaises[dfPaises['Region']=='OCEANIA']['Country']
print("Paises da oceania: ",paises_oceania)
'''

#ex2: quantos paises sao da oceania
print(len(paises_oceania))

#ex3: mostre a media da taxa de alfabetização (usar funcao main)
media_alfabetizacao=dfPaises['Literacy (%)'].mean()
print(media_alfabetizacao)

#ex4: Encontre o nome e a regiao do pais que possui maior populacao
maior_populacao=dfPaises['Population'].idxmax()
nome_pais=dfPaises.loc[maior_populacao,'Country']
print(nome_pais)

nome_regiao=dfPaises.loc[maior_populacao,'Region']
print(nome_regiao)

#ex5 buscar nome dos paises que nao possuem costa maritima e quarde em um novo arquibo
nome_paises=df[df["Coastline (coast/area ratio)"] == 0]["Country"]
nome_paises.to_csv("noCoast.csv", sep=";", header=False, index=False)
print("Nome dos países sem costa maritima salvos em um .csv")










