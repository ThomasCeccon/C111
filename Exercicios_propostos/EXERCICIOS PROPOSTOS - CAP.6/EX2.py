#importações
import pandas as pd
import matplotlib.pyplot as plt

#dataset
df=pd.read_csv('Paises.csv',delimiter=';')

#buscando as regioes da america do norte
America_norte = df[df['Region'].str.contains("NORTHERN AMERICA")]
#print(America_norte)
plt.plot(America_norte["Country"], America_norte["Deathrate"], label='Taxa de Mortalidade', marker='o')
plt.plot(America_norte["Country"], America_norte["Birthrate"], label='Taxa de Natalidade', marker='o')

plt.xlabel('Países')
plt.ylabel('Taxas')
plt.title('Taxa de Mortalidade e Natalidade nos Países da América do Norte')
plt.show()