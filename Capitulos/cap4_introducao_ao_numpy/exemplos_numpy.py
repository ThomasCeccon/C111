#NumPy

#importar a biblioteca numpy
import numpy as np

# criando uma lista de numpy array
#1-dimensao
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))#saber o tipo do array

#2-dimensao matriz
mtz=np.array([[1,2],[3,4]])#linha e coluna
print(mtz)

#estruturando numpy arrays automaticamente
mtz=np.ones(9).reshape(3,3) #9 uns remodelados 3x3, quantidade de elementos deve ser proporcianal a linha e coluna pode ser 9 por 1 ou 1 por 9
print(mtz)

#zeros,ones,arange

#arange: cria elementos (alcance), setando o intervalo (inicio(inclusive),fim(exclusive),pulando de 2 em 2)
mtz=np.arange(10,20,2)
print(mtz)

#ordenar 
vetor=np.array([1,5,3,2,4])
vetor=np.sort(vetor)
print(vetor)

#operacao elemento a elemento 
arr1=np.arange(10,20,1)
arr2=np.arange(30,40,1)

print(arr1)
print(arr2)
print(arr1+arr2) #somar cada elemento coluna por coluna


print(np.concatenate([arr1,arr2]))#juntar os 2 arrays em uma colecao

# Propriedades de um numpy array
print(arr1.size)#tamanho do numpy array

#dimensao
print(arr1.ndim)

#formato
print(arr1.shape) #neste caso 10 colunas

