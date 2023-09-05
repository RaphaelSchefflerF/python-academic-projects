'''
#TAREFA 1

def media(valor1):
    soma=0
    for i in valor:
        soma+=i
    return soma/len(valor)
valor=[1,2,3]
print(media(valor))

#TAREFA 2

def media_harmonica(valor):
    soma=0
    for i in valor:
        soma+=1/i
    return len(valor)/soma
valor=[1,2,3]
print(media_harmonica(valor))

#TAREFA 3

def somatoria_ao_quadrado(n):
    if n == 0:
        return 0
    else:
        return n**2 
def media_quadratica(valor1):
    soma=0
    for i in valor:
        soma+=somatoria_ao_quadrado(i)
    return (soma/len(valor))**0.5 
valor=[2,1,0,1,2]
print(media_quadratica(valor))

#TAREFA 4

def somaPesos(n):
    s=0
    for i in n:
        s+=i
    return s
def media_ponderada(valor1,valor2):
    somaPesos1=somaPesos(valor2)
    somatoria=0
    for i in range(len(valor1)):
        somatoria+= valor1[i] * valor2[i]
    return somatoria/somaPesos1
valor1=[1,2,3]#VALOR
valor2=[3,2,1]#PESOS
print(media_ponderada(valor1, valor2))

#TAREFA 5

def mediana(valor):
    lista2=sorted(valor)
    resto=len(lista2)%2
    indiceImpar=int((len(lista2)/2) +0.5)
    indicePar=int(len(lista2)/2)
    if resto == 0:
        return ((lista2[indicePar-1]+lista2[indicePar])/2)
    else:
        return lista2[indiceImpar]
lista=[3,2,4,1]
print(mediana(lista))

#TAREFA 6 - FIQUEI COM PREGUIÇA DE FAZER

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
lista=[3,2,4,1,3,2]
print(moda(lista))

#TAREFA 7

def moda(lista):
    lista2=sorted(lista)
    return (lista2[-1]+lista[0])/2
lista=[3,2,4,1,3,2]
print(moda(lista))
'''
