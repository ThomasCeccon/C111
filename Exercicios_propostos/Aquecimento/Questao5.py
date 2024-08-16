import numpy as np

arr= np.loadtxt('paises.csv',delimiter=';',dtype='str',encoding='utf-8',skiprows=1)

#sul_caribe=arr[arr[:,1]== 'LATIN AMER. & CARIB']

#maior_renda=sul_caribe[sul_caribe[:,8].astype(float)]

#print("Maior renda: ",max(maior_renda))


#find

arr2=arr[np.char.find(arr[:,1],'LATIN AMER. & CARIB')>=0]
maxgdp=arr2[1:,8].astype(float).max()

print(maxgdp)

