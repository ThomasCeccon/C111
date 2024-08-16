import numpy as np

arr= np.loadtxt('paises.csv',delimiter=';',dtype='str',encoding='utf-8')

regioes=np.unique(arr[:,1])

print('Diferentes regioes do planeta: ',regioes)

