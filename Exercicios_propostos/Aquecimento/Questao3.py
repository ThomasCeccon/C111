import numpy as np

arr= np.loadtxt('paises.csv',delimiter=';',dtype='str',encoding='utf-8',skiprows=1)

taxa_literacy=arr[:,9].astype(float)
soma_taxa=np.sum(taxa_literacy)
cont=len(taxa_literacy)

media_taxa=soma_taxa/cont

print("Media de alfabetizacao:",media_taxa,"%")