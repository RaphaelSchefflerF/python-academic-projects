from collections import Counter
import math
import numpy as np
from scipy.stats import hmean, mode, tstd, tvar, percentileofscore
import matplotlib.pyplot as plt
import stemgraphic

#LISTA DE DADOS
lista_dados =[70,85,68,63,73,34,64,80,55]
#LISTA DE DADOS ORDENADOS
lista_dados_ordenados = sorted(lista_dados)
#CALCULA AS FRENQUENCIAS
frequencia_absoluta=Counter(lista_dados_ordenados)
print("Frequencia Absoluta:",frequencia_absoluta)
# K CALCULA O INTERVALO DAS FREQUENCIAS
k= int(1+3.3*np.log10(len(lista_dados_ordenados)))
#HIST FREQUENCIAS ABSOLUTAS
hist,edges = np.histogram(lista_dados,bins=k)
print("hist:",hist)
print("edges:",edges)
print("Total de Dados na Lista:",len(lista_dados))
print("Lista Sortida:",lista_dados_ordenados)
#PRINTA COMO TABELA 
for i in range(k):
    print(f'{edges[i]} - {edges[i+1]} : {hist[i]}')

print("k=",k)
#PRINTA O GRAFICO DE FREQUENCIA ABSOLUTA

#OGIVAS
frequencias_acumuladas = np.cumsum(hist)
# Plotar o gráfico de ogiva

total = len(lista_dados)
frequencia_relativa = {k: v/total for k, v in frequencia_absoluta.items()}
print("Frequência Relativa:", frequencia_relativa)
# HISTOGRAMA
fig, ax = stemgraphic.stem_graphic(lista_dados, scale=10)
plt.show()




