import numpy as np

'''1) Criar array de float com 10 elementos positivos
e negativos entre 0 e 1.Em seguida multiplicar os valores por 100 e
crie um vetor apenas com a parte inteira destes numeros (usar seed(5) antes)
'''
np.random.seed(5) #seed para numeros aleatorios
arr_float=np.random.rand(10)  #array de numeros positivos e negativos de ponto flutuante entre 0 e 1 

#multiplicar os valores por 100
print("Float: ",arr_float)

arr_inteiro=arr_float*100
arr_inteiro=arr_inteiro.astype(int) #defini o tipo do parametro
print("Inteiro:",arr_inteiro)

print("======================")

'''2)Crie uma matriz de tamanho 4x4 formado
 por numeros aleatorios inteiros entre 1 e 50 (usar seed(10) antes).
'''
np.random.seed(10)
mtz=np.random.randint(1,51,16).reshape(4,4) #matriz 4x4 com 16 valores entre 1 e 50 sendo o ultimo valor exclusive
print("Matriz 4x4: ",mtz)

print("======================")

'''3)Mostre o resultado da média de cada linha e cada coluna 
da matriz,gerada pela questao 2, em sequida apresente o maior
 valor das medias, para as linhas e colunas
'''

#resultado media linha
res_linha_0=mtz.mean(axis=1)[0] #media das linhas 0
res_linha_1=mtz.mean(axis=1)[1] #media das linhas 0
res_linha_2=mtz.mean(axis=1)[2] #media das linhas 0
res_linha_3=mtz.mean(axis=1)[3] #media das linhas 0
print(res_linha_0)
print(res_linha_1)
print(res_linha_2)
print(res_linha_3)

#Maior media entre as linhas
maior_media_linhas=max(res_linha_0,res_linha_1,res_linha_2,res_linha_3)
print('Maior média entre as linhas:',maior_media_linhas)

print("==================")

#resultaddo media coluna
res_coluna_0=mtz.mean(axis=0)[0] #media da coluna 0
res_coluna_1=mtz.mean(axis=0)[1] #media da coluna 1
res_coluna_2=mtz.mean(axis=0)[2] #media da coluna 2
res_coluna_3=mtz.mean(axis=0)[3] #media da coluna 3
print(res_coluna_0)
print(res_coluna_1)
print(res_coluna_2)
print(res_coluna_3)

#maior media entre as colunas
maior_media_colunas=max(res_coluna_0,res_coluna_1,res_coluna_2,res_coluna_3)
print("Maior média entre as colunas: ",maior_media_colunas)


print("======================")

'''
4)Baseado na matriz da questao 2, mostre 
a quantidade de aparições para cada um dos numeros.
Em sequida, mostre apenas os numeros que aparecem duas vezes
'''
#qunatidade de aparições
# Usando np.unique para obter os valores únicos e suas quantidades
val, quant = np.unique(mtz, return_counts=True)     # val -> array com os valores unicos
                                                    # quant -> quantidade de vezes que os números unicos apareceram

relacao = np.column_stack((val, quant))     # juntando os valores unicos e quantas vezes aparecerem em uma matriz
print("\n".join([f"Valor: {valor}, Quantidade: {quantidade}" for valor, quantidade in relacao]))

print(f"Números que aparecem duas vezes{relacao[relacao[:, 1] == 2][:, 0]}")


