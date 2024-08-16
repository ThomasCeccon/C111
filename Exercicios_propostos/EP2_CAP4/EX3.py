import numpy as np

# Carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('..\\space.csv', delimiter=';', dtype=str, encoding='utf-8')

contagem_total = len(arr) - 1  # Quantidade total de missões (subtrai 1 para excluir o cabeçalho)

# EX1
contagem_sucesso = np.sum(np.char.find(arr[1:, 5], 'Success') >= 0)  # Quantidade de missões de sucesso
print(f"Quantidade total de missões: {contagem_total}")
print(f"Quantidade de missões com sucesso: {contagem_sucesso}")

# Mostra a porcentagem de missões que foram um sucesso
print(f"Porcentagem de sucesso: {((contagem_sucesso/contagem_total)*100):.2f}%")

# EX2
# Selecionando apenas os custos das viagens maiores que 0
arr_custos = arr[1:, 6].astype(float)
arr_custos = arr_custos[arr_custos > 0]

# Calcula a média de custos das viagens
media_custos = np.mean(arr_custos)
print(f"A média de custos das viagens é: {media_custos:.2f}")

# EX3
contagem_usa = np.sum(np.char.find(arr[1:, 2], 'USA') >= 0)  # Quantidade de missões nos USA
print(f"Quantidade de missões realizadas nos USA: {contagem_usa}")

# EX4
# Selecionando apenas as missões da SpaceX e encontrando as mais caras
spaceX_missões = arr[1:][np.char.find(arr[1:, 1], 'SpaceX') >= 0]
missão_mais_cara_spacex = spaceX_missões[np.argmax(spaceX_missões[:, 6].astype(float))]
print(f"A missão mais cara realizada pela SpaceX é: {missão_mais_cara_spacex}")

# EX5 ? (duvida)
# Contando as missões por empresa
empresas, counts = np.unique(arr[1:, 1], return_counts=True)
print("Nome das empresas e suas quantidades de missões:")
for empresa, quantidade in zip(empresas, counts):
    print(f"Empresa: {empresa}, Quantidade de Missões: {quantidade}")
