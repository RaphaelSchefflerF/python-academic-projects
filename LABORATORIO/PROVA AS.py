def abrindo_arq(arq):
    arq1=open('musicas.txt','r')
    lista=arq1.read().splitlines()
    arq1.close()
    return lista
def transforma_lista(arq):
    lista= abrindo_arq(arq)
    lista2=[]
    for item in lista:
        lista2.append(item.split(';'))       
    return lista2           
def maior_tempo(arq):
    lista_tempo=transforma_lista(arq)
    lista_tempo2=[]
    for itens in lista_tempo:  
        lista_tempo2.append(int(itens[2]))
    return lista_tempo2

#1 OK
def maiorMusica(arq):
    lista= maior_tempo(arq)
    maior=0
    for item in range(len(lista)):
        if lista[item] > maior:
            maior=lista[item]
    for num in lista:
        if maior < num:
            maior=num
    return maior                
#2
def musicasDoAno(arq,ano):
    lista= transforma_lista(arq)
    musicas=[]
    for musica  in lista:
        if ano in musica:
            musicas.append(musica[0])
    return musicas
#3
def procuraMusica(arq,nome):
    lista= transforma_lista(arq)
    for item in lista:
        if nome in item:
            return ', Album:'+item[1]+', Tempo:'+item[2]+', Ano:'+item[3]
        else:
            return 'Musica Invalida!! Deseja Adiciona-la?'
#4 OK
def insereMusicaArquivo(arq, nome, album, tempo, ano):
  arq=open('musicas.txt','a')
  arq.write(nome+';'+album+';'+tempo+';'+ano)
  return arq.close()

#PRINCIPAL
arq='musicas.txt'
opcao = 0 
while opcao!=5: 
    if opcao == 1: 
        print("A maior música (em tempo) é: ", maiorMusica(arq))
    elif opcao == 2: 
        ano=input("Você deseja ver as músicas de qual ano? ") 
        print("As musicas do Ano:", ano, musicasDoAno(arq,ano))
    elif opcao == 3: 
        nome=input("Qual música você deseja ver informações? ") 
        print("As informações da Musica:", nome, procuraMusica(arq,nome))
    elif opcao == 4: 
        nome=input("Nome da musica: ") 
        album=input("Nome do álbum: ") 
        tempo=input("Tempo da música (em segundos): ") 
        ano=input("Ano da música: ") 
        insereMusicaArquivo(arq, nome, album, tempo, ano) 
        print("A musica ",nome,"foi foi inserida com sucesso!")
        
    opcao = int(input("\n Escolha a opção desejada:"\
                      "\n1. Encontrar a maior musica."\
                      "\n2. Encontrar musicas por ano"\
                      "\n3. Pesquisar música"\
                      "\n4. Inserir música no arquivo"\
                      "\n5. Sair\n"))















