from statistics import mean, median, mode, pstdev
from scipy.stats import variation,pearsonr, linregress
import numpy as np
import matplotlib.pyplot as plt

def calcular_metricas(notas):
    # Ordena as notas para cálculos posteriores
    notas.sort()
    # Média aritmética
    media = mean(notas)
    # Moda
    try:
        moda_val = mode(notas)
    except:
        moda_val = "Sem moda única"
    # Mediana
    mediana_val = median(notas)
    # Amplitude total
    amplitude = max(notas) - min(notas)
    # Ponto médio
    ponto_medio = (max(notas) + min(notas)) / 2
    # Coeficiente de variação
    coef_var = variation(notas) * 100  # em porcentagem
    # Quartis
    n = len(notas)
    q1 = (notas[n//4 - 1] + notas[n//4]) / 2
    q2 = mediana_val
    q3 = (notas[3*n//4 - 1] + notas[3*n//4]) / 2
    return {
        "Média": media,
        "Moda": moda_val,
        "Mediana": mediana_val,
        "Amplitude Total": amplitude,
        "Ponto Médio": ponto_medio,
        "Coeficiente de Variação": coef_var,
        "Q1": q1,
        "Q2": q2,
        "Q3": q3,
        "---": "---"
    }

FBD=[6.3, 5.5, 7, 8.5, 6.8, 6.3, 7.3, 3.4, 6.4, 8, 5.5, 9, 7.5, 8.1, 7.5, 6.8, 8.4, 8, 8, 9.2]
MODELAGEM=[6, 6, 6, 6, 6.1, 6.3, 7, 7.1, 7.3, 7.3, 7.4, 7.6, 7.7, 7.7, 7.8, 8.1, 8.2, 8.8, 8.8, 9]
LPOO=[6.3, 6.1, 7.4, 6.6, 6.2, 6.4, 9.3, 3.5, 6.9, 7.3, 6.3, 9.3, 8.4, 8.4, 8, 7.6, 9.2, 10, 7.1, 10]
ED=[6.6, 7.1, 7.6, 6, 4.4, 4.6, 9.2, 4, 6.3, 6, 6.7, 9.8, 8.6, 8.1, 9.6, 7.1, 10, 8, 7.6, 9.4]
resultado_FBD = calcular_metricas(FBD)
resultado_MODELAGEM = calcular_metricas(MODELAGEM)
resultado_LPOO = calcular_metricas(LPOO)
resultado_ED = calcular_metricas(ED)

for k, v in resultado_FBD.items():
    print(f"{k}: {v}")
for k, v in resultado_MODELAGEM.items():
    print(f"{k}: {v}")
for k, v in resultado_LPOO.items():
    print(f"{k}: {v}")
for k, v in resultado_ED.items():
    print(f"{k}: {v}")

# Combinações das disciplinas
disciplinas = {"FBD": FBD, "Modelagem": MODELAGEM, "LPOO": LPOO, "ED": ED}
combinacoes = [("FBD", "Modelagem"), ("FBD", "LPOO"), ("FBD", "ED"), ("Modelagem", "LPOO"), ("Modelagem", "ED"), ("LPOO", "ED")]

for disc1, disc2 in combinacoes:
    # Cálculo do coeficiente de Pearson
    coef_pearson, _ = pearsonr(disciplinas[disc1], disciplinas[disc2])

    # Cálculo da regressão linear
    slope, intercept, _, _, _ = linregress(disciplinas[disc1], disciplinas[disc2])

    # Gráfico de dispersão
    plt.scatter(disciplinas[disc1], disciplinas[disc2], label=f'{disc1} x {disc2}')
    plt.plot(disciplinas[disc1], np.array(disciplinas[disc1]) * slope + intercept, color='red')  # reta da regressão linear

    plt.title(f'{disc1} x {disc2}')
    plt.xlabel(disc1)
    plt.ylabel(disc2)
    plt.legend()
    plt.show()

    print(f"Combinação: {disc1} e {disc2}")
    print(f"Coeficiente de Pearson: {coef_pearson}")
    print(f"Regressão Linear: y = {slope}x + {intercept}\n")
