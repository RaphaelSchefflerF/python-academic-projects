'''
telefone={'Maria':'844554546', 'joao':'9383748744'}
telefone['pedro']='69662256'
print(telefone)
for i in sorted(telefone):
    print(i,telefone[i])
contaLetra={}

for letra in 'Orangotango':
    contaLetra[letra]=contaLetra.get(letra,0)+1
print(contaLetra)

#ATIVIDADE 6
def frase(texto):
    dic={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','U':'u','V':'v','W':'w','X':'x','Y':'y'}
    vazia=''
    for letra in texto:
        if letra.isupper():
            vazia=vazia+dic[letra]
        else:
            vazia=vazia+letra  
    return vazia
#Principal
print(frase(input('Digite uma frase: ')))

#ATIVIDADE 7
def prefixo(palavras):
    contador=0
    for palavra in palavras: 
        if palavra.startswith("at"):
            contador=contador +1
    return contador
#principal
palavras = ["ola","atenção","pratique","programação","atingir"]
print(prefixo(palavras))


#ATIVIDADE 8
def mesclar(str1,str2):
    saida=""
    for letra in str1:
        saida =saida + letra + str2[str1.index(letra)]

    return saida

#PRINCIPAL
str1= "abc"
str2= "pqr"
print(mesclar(str1,str2))

#Web Fabio
lista_fabio=[4.0,5.0,8.0]
lista_jackson=[6.0,7.0,8.0]

def media_nota1(lista_fabio):
    soma1=0
    for i in lista_fabio:
        soma1=i+soma1
    media_fabio= soma1/3
    return media_fabio

def media_nota2(lista_jackson):
    soma2=0
    for i in lista_jackson:
        soma2=i+soma2
    media_jackson= soma2/3
    return media_jackson

def comparacao(media1,media2):

    if media1 > media2:
        return('Fabio Ganhou')
    elif media1 == media2:
        return('Deu Empate')
    else:
        return('Jackson Ganhou')


#Principal

media1=media_nota1(lista_fabio)
media2=media_nota1(lista_jackson)

print(media1)
print(media2)

print(comparacao(media1,media2))

#atividade

def data(dia,mes,ano):
    listaMes = ['janeiro', 'fevereiro',
            'março','abril','maio',
            'junho','julho', 'agosto',
            'setembro', 'outubro',
            'novembro', 'dezembro']
    return f'Você nasceu em,'

dia=int(input('Dia:'))
mes=int(input('Mês:'))
ano=int(input('Ano:'))

data(dia,mes,ano)

def principal():
	frase = “gato e cachorro”
	lista = frase.split(“ ”)
	quantidade = 0
	for item in lista:
		if verifica_minuscula(item) == True and verifica_hifen(item)
                quantidade = quantidade +1

                
def valida_frase(frase):
    frase_tolkiens=frase.split(" ")
    erros=0

    print(frase_tolkiens)
    tolkiens_validos=0

    for tolkien in frase_tolkiens:
        erros=0
        for caracter in tolkien:
            if caracter in "0123456789_" or caracter.isupper():
                erros+=1
                continue
            if caracter in".!?,":
                if caracter!=tolkien[-1]:
                    erros+=1
                    continue

        if tolkien.count("-")>1 or tolkien[0]=="-" or tolkien[-1]=="-" or erros>0:
            continue
        else:
            tolkiens_validos+=1

    return tolkiens_validos

frase = "!isto quase p0d3 -ha faca-me ha- 55 mamão! -Fim-"
print(valida_frase(frase))

def valida_frase(frase):
    frase_tolkiens=frase.split(" ")
    erros=0

    print(frase_tolkiens)
    tolkiens_validos=0

    for tolkien in frase_tolkiens:
        erros=0
        for caracter in tolkien:
            if caracter in "0123456789_" or caracter.isupper():
                erros+=1
                continue
            if caracter in".!?," and caracter!=tolkien[-1]:
                erros+=1
                continue

        if tolkien.count("-")>1 or tolkien[0]=="-" or tolkien[-1]=="-" or erros>0:
            continue
        else:
            tolkiens_validos+=1

    return tolkiens_validos



frase = "!isto quase p0d3 -ha faca-me ha- 55 mamão! -Fim-"
print(valida_frase(frase))

'''



































































