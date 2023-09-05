import numpy as np
from scipy.stats import hmean, mode, tstd, tvar, percentileofscore

data = np.array([7,3,6,13,10,6,8,5,3,14])
pesos = np.array([0.2,0.2,0.3,0.1,0.1,0.1,0.1,0.2,0.2,0.1])

media_aritmetica = np.mean(data)

media_harmonica = hmean(data)

media_quadratica = np.sqrt(np.mean(np.square(data)))

media_ponderada =np.average(data,weights=pesos)

mediana = np.median(data)

moda,count = mode(data)

ponto_medio = (np.min(data) + np.max(data))/2

amplitude = np.ptp(data)

desvio_medio = np.mean(np.abs(data - media_aritmetica))

desvio_padrao_pop = tstd(data,ddof=0)
desvio_padrao_amostral = tstd(data,ddof=1)

variancia_pop = tvar(data,ddof=0)
variancia_amostral = tvar(data,ddof=1)

coef_variacao=(desvio_padrao_pop/media_aritmetica)*100

print('variancia_pop=',variancia_pop)
print('variancia_amostral=',variancia_amostral)
print('coef_variacao=',coef_variacao)

print('media_aritmetica=',media_aritmetica)
print('media_harmonica=',media_harmonica)
print('media_quadratica=',media_quadratica)
print('media_ponderada=',media_ponderada)
print('mediana=',mediana)
print('moda=',moda)
print('ponto_medio=',ponto_medio)
print('amplitude_total=',amplitude)
print('desvio_medio=',desvio_medio)
print('desvio_padrao=',desvio_padrao_pop)
print('desvio_padrao=',desvio_padrao_amostral)


