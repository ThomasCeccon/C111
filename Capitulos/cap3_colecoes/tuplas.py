#COLEÇÕES

#Tupla: () variaveis criadas para guardar informações, guardar varios elementos
nomes= ('Goku','Vegeta','Trunks','Gohan') #é uma coleção IMUTAVEL

print(nomes) #nomes compostos na tupla

# #slicing (fatiar) de dados
# print(len(nomes)) #mostrar a quantidade de elementos
# print(nomes[0]) #mostrar no index o elemento contido
print(nomes[0:2]) #mostrar do indice 0 a 2
print(nomes[1:3]) #nomes do meio (primeiro elemento inclusivo e o segundo exclusivo)
print(nomes[-2]) #0,-1,-2 (trunks)
print(nomes[0:3:2]) # de 2 em 2

#ctrl+/ para comentar

#Listas [] coleção mutavel
nomes= ['Goku','Vegeta','Trunks','Gohan']
# print(nomes)
#
# #ADD
# nomes.append('Picolo') #adicionar elemento no final
#
# #Updata
# nomes[0]='Bulma'
#
# #Delete
# nomes.remove('Trunks') #remove por valor
# del nomes[1]  #remove por indice
#
# #select
# print(nomes)

#Conjunto  SET {}
# não guarda ordem dos elementos
#nao guarda elementos repetidos
# nao tem update

nomes= {'Goku','Vegeta','Trunks','Gohan'}

# #add
# nomes.add('Bulma')
# nomes.add('Goku')
#
# #select
# print(nomes)
#
# #remove
# nomes.remove('Trunks')


#Dicionario {}
#usa indices customizaveis Json
pessoa= {
    'nome':'Goku',
    'idade':42
}

#add
pessoa['sexo']='M'

#DELETE
del pessoa['idade']

#update
pessoa['nome']='Gohan'

pessoa2= {
    'nome':'Bulman',
    'idade':32
}

#colecao dentro de colecao
pessoas=[pessoa,pessoa2]# lista compondo os dicionarios

print(pessoas[0]['nome']) #mostrar somente o nome da primeira pessoa
print(pessoas[0]) #mostrar informações do primeiro dicionario



