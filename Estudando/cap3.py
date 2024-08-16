#listas
nomes=['Thomas','Zé','Ana','laura']
nomes[2]='Luiza'
print(nomes)
nomes.insert(2,'Carla')
print(nomes)

del nomes[2]
print(nomes)

nomes.pop(3)
print(nomes)

nomes.remove('Thomas')
print(nomes)

#
a={2,4,5}
b={1,5}
print(a|b,' União')
print(a-b,' diferença')
print(a&b,' intersecção')

info={'nome':'Thomas',
      'idade': 20,
      }

info['cursando']='Eng. de Computação'

print(info.values())
print('----------')
print(info.keys())
print('----------')
print(info.items())
print('----------')

for k,v in info.items():
  print(f'{k}: {v}')
