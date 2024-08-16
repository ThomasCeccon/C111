import numpy as np
import matplotlib.pyplot as plt #biblioteca para visualização de dados
import pandas as pd

'''
# plot simples e composto
x = np.array([1,2,3,4])

# BroadCasting
y = x*2
y2=x**2

#legenda
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

#pontos(marcador) de indicação -> marcador,estilos de linhas e cores, aumentando linha e ponto(marcador)
#plotagem
plt.plot(x,y,'o--g',x,y2,'ob:',linewidth=3,markersize=20)
plt.show()
'''

'''
# subplots (multiplos graficos cada um em plano cartesiano diferente)
# plot simples e composto
x = np.array([1,2,3,4])

# BroadCasting
y = x*2
y2=x**2

# plot1
plt.subplot(1,3,1) #1-linha /2-colunas    /'1- grafico esta na coluna 1
plt.title('Linear')
plt.plot(x,y,'x--r')

plt.subplot(1,3,2) ##1-linha /2-colunas    /'2- grafico esta na coluna 2
plt.title('Exponencial')
plt.plot(x,y2,'o--g')

plt.subplot(1,3,3) ##1-linha /2-colunas    /'2- grafico esta na coluna 2
plt.title('seno')
plt.plot(x,y2,'o--g')

plt.show()
'''


#grafico de dispersao (scatter plot)
df=pd.read_csv('paises (1).csv',delimiter=';')

#6 maiores paises do mundo  (n maiores)  / s= size
df2 = df.nlargest(6,'Area (sq. mi.)')
plt.scatter(x=df2['Country'],y=df2['Area (sq. mi.)'],s=df2['GDP ($ per capita)']/50) #slice
plt.show()

