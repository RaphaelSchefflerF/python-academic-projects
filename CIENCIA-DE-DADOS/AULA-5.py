from collections import Counter
import math
import numpy as np
import matplotlib.pyplot as plt
dados1=[1,3,5,3,2,3,4,2,5,5,5,4,4,4,4,5,2,1,1,3]

dados=["maca","banana","maca","laranja","maca","banana","maca","maca","banana","laranja","uva","uva"]

frequencia_absoluta=Counter(dados1)
frequencia_absolutaQualitativa=Counter(dados)
print("Frequencia Absoluta:",frequencia_absoluta)
print("Frequencia Absoluta:",frequencia_absolutaQualitativa)

total=len(dados1)
frequencia_relativa={k:v/total for k, v in frequencia_absoluta.items()}
print('Frequencia Relativa:', frequencia_relativa)

frequencia_relativa_percentual={k:v/total *100 for k, v in frequencia_absoluta.items()}
print("Frequencia Relativa Percentual:",frequencia_relativa_percentual)
print("Quantidade de Valores na Lista:",total)
print("Dado|Frequencia Absoluta|Frequencia Relativa|Frequencia Relativa Percentual|")
print("-"*80)
for dado, frequencia_absoluta in frequencia_absoluta.items():
    frequencia_relativa = frequencia_absoluta / total
    frequencia_relativa_percentual = frequencia_relativa *100
    print(f"{dado:^4}|{frequencia_absoluta:^19}|{frequencia_relativa:^18.2f}|{frequencia_relativa_percentual:^31.2f}%")

distribuicao_de_frequencia=0

dado_temperatura=[18.9,18.7,18.4,23.2,22.3,22.0,22.4,23.0,20.9,18.3,17.5,18.0,19.1,18.9,20.0,25.1,21.5,20.8,22.4,23.7,18.3,16.1,17.2,19.8,22.6,21.2,21.2,20.1,21.4,22.2,23.2]
dado_ordenado=sorted(dado_temperatura)
print(dado_ordenado)
n=len(dado_temperatura)
k= 1+3.3* math.log10(n)
k=round(k)

h=round(((max(dado_temperatura)-(min(dado_temperatura)-1))/k),100)

print(h)

classes=[]
frequencias =Counter()

for i in range(k):
    min_val = round((min(dado_temperatura) + i * h),1)
    max_val = min(dado_temperatura) + (i+1) * h
    classes.append((min_val,max_val))

    freq = sum(1 for d in dado_temperatura if min_val <= d < max_val)
    frequencias[(min_val,max_val)] = freq


print("Intervalo de Classe\tFrequencia")
print("-"*40)
for classe, freq in frequencias.items():
    print(f"{classe[0]:^10.2f} - {classe[1]:.2f}\t{freq}")


dados2=[15,23,12,78,45,89,45,23,56,49,77,83,12,56,34,78,90,23,56,44]
bins = [0,20,40,60,80,100]
hist,edges = np.histogram(dados2,bins=bins)
print("hist:",hist)
print("edges:",edges)
print("Total de Dados na Lista:",len(dados2))
print("Lista Sortida:",sorted(dados2))
for i in range(len(bins)-1):
    print(f'{bins[i]} - {bins[i+1]} : {hist[i]}')

plt.hist(dados2, bins=bins, edgecolor='Yellow', alpha=0.7)
plt.xlabel('Intervalos')
plt.ylabel('Frequencia')
plt.title('Histograma com Intervalos')
plt.show()






