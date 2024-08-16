#Dicionario para ler o nome e a media de um aluno

sit_aluno={ 'Nome':'Ana',
             'Media': 60,
          }

# Conteudo do dicionario
print(sit_aluno)

if sit_aluno['Media']>=60:
  sit_aluno['Situacao']='Aluno(a) Ap'
  

else:
  sit_aluno['Situacao']='Aluno(a) Rep'


# Conteudo do dicionario
print(sit_aluno)
