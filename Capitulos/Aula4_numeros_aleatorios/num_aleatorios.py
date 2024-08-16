'''
NUMEROS ALEATORIOS
'''

import numpy as np

#np.random.seed(10)#calibrar p/ que maquinas distintas receba os mesmos valores aleatorios
#arr= np.random.randint(10,20,5) # var que recebe numeros aleatorios (5 numeros de 10 a 20)
#print(arr)

#elementos unicos
np.random.seed(5)# mesmos valores aleatorios
arr=np.random.randint(0,10,15)
print('x',arr)
print(np.unique(arr)) #organiza os valores aleatorios e não repete 
print(set(arr))

#OPERACAO EM MATRIZES
np.random.seed(10)
mtz=np.random.randint(1,11,9).reshape(3,3) #matriz 3x3
print(mtz)
#print(mtz.sum(axis=1)[0])    # no caso somar a linha de indice 0       axis=0 //colunas    axis=1 //linhas
#print(mtz.sum(axis=0)[1])    # no caso somar coluna de indice 1  
#print(mtz.mean(axis=0)[1])    # no caso media da coluna de indice 1  

#broadcasting: escalar x array
#print(mtz*2)

# CONDICIONAIS
#arr = mtz%2==0 # retorna a condição e não os valores
#arr1 = mtz[mtz%2==0] #mostrar numeros pares da matriz linha por linha
#cond=mtz>mtz.mean()
#print(mtz[cond])

# TRABALHANDO COM TEXTOS
arr = np.array(['Giovanni','Isaque','Luiza','Raissa'])
print(np.char.find(arr,'s'))#BUSCAR NOMES COM LETRA S (-1: nao encontrado), (1,3) posição das letras encontradas
arr2=arr[np.char.find(arr,'s')>=0]
print(arr2)






