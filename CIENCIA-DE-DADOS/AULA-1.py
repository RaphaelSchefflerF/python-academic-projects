#TAREFA 2
'''
def somatoria(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * somatoria(n - 1)
    
n=3
print(somatoria(n))
'''

#TAREFA 3
'''
def somatoria_ao_quadrado(n):
    if n == 0:
        return 0
    else:
        return n**2 + somatoria_ao_quadrado(n - 1)

n = 3
print(somatoria_ao_quadrado(n))
'''

#TAREFA 4
'''
def soma_dados(conjunto):
    soma=0
    for i in range(len(conjunto)):
        soma+=conjunto[i]
    return soma

conjunto=[1,2,3]
print(soma_dados(conjunto))
'''

#TAREFA 5
'''
def soma_dados_ao_quadrado(conjunto):
    soma=0
    for i in range(len(conjunto)):
        soma+=conjunto[i]*conjunto[i]
    return soma

conjunto=[1,2,3]
print(soma_dados_ao_quadrado(conjunto))
'''

'''
def soma_dados(conjunto):
    soma=0
    for i in range(len(conjunto)):
        soma+=conjunto[i]
    return soma
        

conjunto=[1,2,3]
print(soma_dados(conjunto))
'''



