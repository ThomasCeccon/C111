#importando a biblioteca pandas
import pandas as pd 

#leitura de arquivos .csv com pandas
df=pd.read_csv('paises.csv', delimiter=';')

#print(df.head(1))

#EX1
#a) quais os paises de OCEANIA
#dados_df.loc[linhas,colunas]

#paises_oceania=df[df['Region']== 'OCEANIA'].iloc[:,0:1]
paises_oceania = df[df['Region'].str.contains('OCEANIA')]
print("Paises da Oceania: ",paises_oceania)

#b)quantos paises sao da oceania
print('Quantidade de países da Oceania: ',len(paises_oceania))

print("================================")

#EX2: MOSTRAR A MEDIA DA TAXA DE ALFABETIZAÇÃO
media=df['Literacy (%)'].mean()
print("Média de alfabetização no planete:",round(media,2),"%")

print("==============i==================")

#Ex3: ENCONTRE O NOME E A REGIAO DO PAIS QUE POSSUI A MAIOR POPULAÇAO
maior_populacao=df['Population'].idxmax()

pais_populacao=df.loc[maior_populacao,'Country']
regiao_populacao=df.loc[maior_populacao,'Region']

print("País: ",pais_populacao,"Região: ",regiao_populacao)

print("================================")

#Ex4:Buscar o nome de todos os paises que nao possuem costa maritima
nome_paises=df[df["Coastline (coast/area ratio)"] == 0]["Country"]
nome_paises.to_csv("noCoast.csv", sep=";", header=False, index=False)
print("Nome dos países sem costa maritima salvos em um .csv")
