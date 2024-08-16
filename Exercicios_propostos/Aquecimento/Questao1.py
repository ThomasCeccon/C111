import numpy as np

arr= np.loadtxt('paises.csv',delimiter=';',dtype='str',encoding='utf-8')

slicing=arr[:,0:4]

print(slicing)