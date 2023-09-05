def amplitudeTotal(valor):
    maiorValor=0
    menorValor=0     
    return 0

def desvioMedio(lista):
    soma=0
    medi=media(lista)
    for item in lista:
        soma+=(item-medi)
    return (soma/len(lista))

def media(valor):
    soma=0
    for i in valor:
        soma+=i
    return soma/len(valor)

def desvioPadrao(lista):
    soma=0
    medi=media(lista)
    for item in lista:
        soma+=(item-medi)**2
    return (soma/len(lista))**0.5

def desvioPadraoAmostral(lista):
    soma=0
    medi=media(lista)
    for item in lista:
        soma+=(item-medi)**2
    return (soma/len(lista)-1)**0.5

def variancia(lista):
    soma=0
    medi=media(lista)
    for item in lista:
        soma+=(item-medi)**2
    return (soma/len(lista))

def coeficienteVariacao(lista):
    medi=media(lista)
    desvio=desvioPadrao(lista)
    return (100 * desvio)/medi

def mediana(valor):
    lista2=sorted(valor)
    resto=len(lista2)%2
    indiceImpar=int((len(lista2)/2) +0.5)
    indicePar=int(len(lista2)/2)
    if resto == 0:
        return ((lista2[indicePar-1]+lista2[indicePar])/2)
    else:
        return lista2[indiceImpar]
    
def moda(lista):
    frequencias = {}  #Dicionário
    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    moda = None
    max_frequencia = 0
    for num, freq in frequencias.items():
        if freq > max_frequencia:
            moda = num
            max_frequencia = freq
    return moda

def pontoMedio(lista):
    lista2=sorted(lista)
    return (lista2[-1]+lista[0])/2

valores = [158, 177, 170, 183, 172, 174, 175, 174, 185, 170, 165, 185, 187, 175, 172, 172, 170, 161, 175, 180, 184, 196, 180, 176, 170, 172]
Homens = [177, 170, 183, 172, 175, 174, 185, 170, 185, 187, 175, 172, 172, 170, 175, 180, 184, 196, 180, 176]
Mulheres=[172,161,158,165,174,170]

print("MEDIA")
print(media(valores))
print(media(Homens))
print(media(Mulheres))

print("MEDIANA")
print(mediana(valores))
print(mediana(Homens))
print(mediana(Mulheres))

print("MODA")
print(moda(valores))
print(moda(Homens))
print(moda(Mulheres))

print("PONTO MEDIO")
print(pontoMedio(valores))
print(pontoMedio(Homens))
print(pontoMedio(Mulheres))

print("AMPLITUDE TOTAL")
print(amplitudeTotal(valores))
print(amplitudeTotal(Homens))
print(amplitudeTotal(Mulheres))

print("DESVIO PADRAO")
print(desvioPadrao(valores))
print(desvioPadrao(Homens))
print(desvioPadrao(Mulheres))

print("VARIANCIA")

print(variancia(valores))
print(variancia(Homens))
print(variancia(Mulheres))

print("COEFICIENTE DE VARIANCIA")
print(coeficienteVariacao(valores))
print(coeficienteVariacao(Homens))
print(coeficienteVariacao(Mulheres))










valor=sorted(Homens)
print(valor)





