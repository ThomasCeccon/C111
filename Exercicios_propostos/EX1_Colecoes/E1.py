'''
1)Criar lista preenchida
'''
paises_futebol=['Brasil','França','Portugal','Argentina','Holanda']

#a) mostrar apenas os 3 primeiros colocados
print(paises_futebol[0:3])

#b) mostrar os ultimos dois colocados
print(paises_futebol[3:])

#c) Mostrar uma lista com os times em ordem alfabetica
paises_futebol.sort()
print(paises_futebol)

#d) Mostrar em qual posicao da tabela esta o Barcelona
paises_futebol.append('Barcelona')
print(paises_futebol)
print('O Barcelona está na posição', paises_futebol.index('Barcelona'), 'da tabela.')


