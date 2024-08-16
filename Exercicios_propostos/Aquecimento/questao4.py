import numpy as np

arr= np.loadtxt('paises.csv',delimiter=';',dtype='str',encoding='utf-8')
paises_america_norte=arr[np.char.find(arr[:,1],'NORTHERN AMERICA')>=0]
soma=len(paises_america_norte)
print(soma)