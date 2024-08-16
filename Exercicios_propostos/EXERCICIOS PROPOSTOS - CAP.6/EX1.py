#Importações
import pandas as pd
import matplotlib.pyplot as plt

#dados
dfSpace = pd.read_csv('space.csv', delimiter=';')

#localizando USA e China e pegando as empresas
Empresa_eua = dfSpace[dfSpace["Location"].str.contains("USA")]["Company Name"].unique()
Empresa_china = dfSpace[dfSpace["Location"].str.contains("China")]["Company Name"].unique()

Empresas = ["EUA", "China"] #label
Empresas_data = [len(Empresa_eua), len(Empresa_china)]# dados

plt.bar(Empresas, Empresas_data, color=['blue', 'green']) #label,dados e cores das barras
plt.xlabel('País')
plt.ylabel('Número de Empresas Espaciais')
plt.title('Número de Empresas Espaciais nos EUA e na China')
plt.show()