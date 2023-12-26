import numpy as np
from scipy.stats import hmean, mode, tstd, tvar,percentileofscore

num1 = np.array([4,12,17,3,5,3,5,2,1,20,14,3,2,10])
print(len(num1))
num2 = np.array([5,15,20,35,10,6,11,18,5,30,32,4,10,27])
print(len(num2))
num3 = np.array([10,23,22,38,12,10,22,31,11,36,33,29,34,40])
print(len(num3))
num4 = np.array([34,32,35,40,18,17,24,42,16,38,36,36,37,46])
print(len(num4))
num5 = np.array([58,33,41,57,25,34,51,51,20,47,41,45,43,49])
print(len(num5))
num6 = np.array([59,46,42,58,33,37,53,56,56,53,52,55,50,58])
print(len(num6))

media_aritmetica1 = np.mean(num1)
media_aritmetica2 = np.mean(num2)
media_aritmetica3 = np.mean(num3)
media_aritmetica4 = np.mean(num4)
media_aritmetica5 = np.mean(num5)
media_aritmetica6 = np.mean(num6)

media_harmonica1 = hmean(num1)
media_harmonica2 = hmean(num2)
media_harmonica3 = hmean(num3)
media_harmonica4 = hmean(num4)
media_harmonica5 = hmean(num5)
media_harmonica6 = hmean(num6)

ponto_medio1 = (np.min(num1) + np.max(num1)) / 2
ponto_medio2 = (np.min(num2) + np.max(num2)) / 2
ponto_medio3 = (np.min(num3) + np.max(num3)) / 2
ponto_medio4 = (np.min(num4) + np.max(num4)) / 2
ponto_medio5 = (np.min(num5) + np.max(num5)) / 2
ponto_medio6 = (np.min(num6) + np.max(num6)) / 2
print("--------------------------")
print(f"Média aritmética 1: {media_aritmetica1}")
print(f"Média aritmética 2: {media_aritmetica2}")
print(f"Média aritmética 3: {media_aritmetica3}")
print(f"Média aritmética 4: {media_aritmetica4}")
print(f"Média aritmética 5: {media_aritmetica5}")
print(f"Média aritmética 6: {media_aritmetica6}")
print("--------------------------")
print(f"Média harmônica 1: {media_harmonica1}")
print(f"Média harmônica 2: {media_harmonica2}")
print(f"Média harmônica 3: {media_harmonica3}")
print(f"Média harmônica 4: {media_harmonica4}")
print(f"Média harmônica 5: {media_harmonica5}")
print(f"Média harmônica 6: {media_harmonica6}")
print("--------------------------")
print(f"Ponto médio 1: {ponto_medio1}")
print(f"Ponto médio 2: {ponto_medio2}")
print(f"Ponto médio 3: {ponto_medio3}")
print(f"Ponto médio 4: {ponto_medio4}")
print(f"Ponto médio 5: {ponto_medio5}")
print(f"Ponto médio 6: {ponto_medio6}")

