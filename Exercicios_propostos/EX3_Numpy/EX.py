#importar a biblioteca numpy
import numpy as np

'''
1) Crie um array de tamanho 21 com valores
   linearmente espaçados entre 0 e 1
'''
arr = np.linspace(0, 1, 21) #valores linearmente espaçados ente inicial e final
print('1)',arr)

print('------------------------------')

'''
2) Crie dois arrays: um de numeros pares de 0 até 51 e outro tambem de numeros pares
de 100 ate 50.Em sequida, os concatene e mostre os resultados ordenados
'''
array1=np.arange(0,51,2) #intervalo inicial e final e pulando de 2 em 2
array2=np.arange(100,50,-2)#intervalo inicial e final e pulando de 2 em 2 começando do maior para o menor
concatenacao=np.concatenate([array1,array2])
#print(concatenacao)
ordenado=np.sort(concatenacao)
print('2)',ordenado) #ordem crescente 

#print(array1)
#print(array2)
print('------------------------------')

'''
3)Ordene os resultados do array resultante da questao 2 em ordem decrescente
'''
ordenado=np.flip(np.sort(concatenacao))#ordenacao de ordem decrescente
print('3)',ordenado)

print('------------------------------')

'''
4)Crie uma matriz formada somente por uns de tamanho 3x4.Em sequida, transforme-a
  em um array 1-D
'''
matriz=np.ones([3,4]).reshape(1,12)
#print(matriz)

print('4)',matriz)

print('------------------------------')

'''
5)Crie uma matriz de tamanho qualquer.Extraia seu numero de linhas e colunas,
  multiplique-os, e diga se esta matriz poderia se tornar um vetor com numero
  par ou impar de elementos
'''
mtz=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
linhas,colunas=mtz.shape #numero de linhas e colunas
print('5)',linhas,colunas)

multiplicar_l_c=linhas*colunas

if multiplicar_l_c %2==0:
  print('Matriz com Vetor par de elementos: ',multiplicar_l_c)

else:
  print('Matriz com Vetor impar de elementos: ',multiplicar_l_c)

print('------------------------------')