#1-Escrevendo no Arquivo.
'''
def escrever():
    arq=open('temp.txt','w')
    arq.write('Otorrinolaringologista\n')
    arq.write('Pneumoultramicroscopicossilicovulcanoconiótico\n')
    arq.write('Paralelepípedo\n')
    arq.write('Inconstitucionalissimamente\n')
    arq.close()
    
escrever()
'''

#2- Inverta a ordem da lista e grave em um segundo arquivo.
'''
def inverter():
    arq=open('temp.txt','+r')
    arq2=open('temp2.txt','w')
    conteudo=arq.readlines()

    for i in range(len(conteudo)-1,-1,-1):
        arq2.write(conteudo[i])
    
    arq.close()
    arq2.close()
    
inverter()
'''

#3- Ordene a lista da menor palavra para a maior.


    
arq2=open('temp2.txt','+r')
conteudo=arq2.read()
lista=conteudo.split('\n')
lista.remove('')
print(lista)


for palavra in lista:
    print(palavra)
    qtLetras=len(palavra)
    print(qtLetras)
    for letras in range(i+1,len(lista)):
        
        if qtLetras > len(letras):
            letras.insert(0,letras)
    print(letras)
        #if qtLetras < len(letras):
            
            
            
            
   
       
    


        
    
        

              
   































