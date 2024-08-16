
'''
nome=input('Entre com seu nome: ')

print("Nome com letras maiusculas:" ,nome.upper())
print("Nome com letras minusculas:" ,nome.lower())
print("Qauntos caracteres tem ao todo:" ,len(nome))

print("Trocar ultimo nome para do inatel: ",nome.replace('Guimarães',"do Inatel"))
'''
#2
'''
num=int(input("Entre com um numero: "))
i=0
for i in range(0,11):
  print(num*i)
  i=i+1
'''

#3
sexo_escolhido = input("Qual seu sexo?: ")

sexo_pessoa='M' or 'F'
while sexo_escolhido != sexo_pessoa:
    sexo_escolhido = input("Por favor, informe seu sexo corretamente (M/F): ")

if sexo_escolhido == 'M':
    print('Homem!')
elif sexo_escolhido == 'F':
    print('Mulher!')


  
