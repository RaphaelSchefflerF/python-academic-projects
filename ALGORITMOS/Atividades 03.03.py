#Atividades
'''1-A fórmula para calcular a área de uma circunferência é: area = π * raio2.
Considerando para este problema que π = 3.14159.
Faça um programa que leia o raio e efetue o cálculo da área.'''
#Valor de Entrada
raio=float(input("Digite o raio:"))
#Processamento
area=(3.14159*raio)**2
#Saida
print("Area da Circunferencia:", area)
#OU DIRETO
raio=float(input("Digite o raio:"))
#Saida
print('Area:',3.14159*raio**2)

#OK

'''2-Em uma empresa o cálculo dos funcionários é realizado da seguinte forma:
quant. de horas trabalhadas * 4.5 * valor da hora.
Faça um programa que solicite aos usuários as informações necessárias para
mostrar o CPF, o nome e o salário de um funcionário.'''
#Valores de Entrada
nome=input('Digite o seu Nome:')
cpf=input('Digite o seu CPF (Apenas Numeros): ')
qhrs= float(input('Digite quantas Horas Trabalhadas: '))
valorHora=float(input('Valor da hora: '))
#Processamento
salario =qhrs*4.5*valorHora
#Saída Direta
print('Nome:',nome,'CPF:', cpf,'Salario:', salario)

    
'''3-Joãozinho pediu que você crie um programa para auxiliá-lo a calcular a
quantidade de litros de combustível gastos em suas viagens,
utilizando seu automóvel que faz 12 KM/L. Para isso,
ele deseja informar o tempo gasto na viagem (em horas) e a
velocidade média durante ela (em km/h).
A partir dos dados que serão informados, deve-se apresentar:
• distância percorrida
• quantos litros seriam necessários'''
#Valores de Entrada
tempo=int(input('Tempo Gasto na Viagem(horas):'))
velocidade= int(input('Velocidade media:'))
#Processamento
distancia=velocidade*tempo
#Saída Direta
print('Distancia Percorrida',distancia,'KM')
#Processamento
litros=distancia/12
#Saída Direta
print('Litros Necessarios:', litros,'L')

#OK

'''4-Leia um valor inteiro correspondente à idade de uma pessoa em dias e
informe-a em anos,meses e dias.
Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e
todo mês com 30 dias. Este é apenas um exercício com objetivo de testar
raciocínio matemático simples.'''
#Valores de Entrada
idade=int(input('Qual sua idade em dias?:'))
#Processamento
anos=int(idade/365)
#Saída
print('Anos:',anos)
#Processamento
meses1= anos*365
meses2= idade-meses1
meses=int(meses2/30)
#Saída
print('Meses:',meses)
#Processamento
dias1=anos*365
dias2=idade-dias1
dias3=int(dias2/30)
dias4=(dias2-(30*dias3))
#Saída
print('Dias:',dias4)
#OUUU DIRETO
#Valores de Entrada
idade=int(input('Qual sua idade em dias?:'))
#Processamento
anos=int(idade/365)
dias2=idade%365
meses=int(dias2/30)
dias=dias2%30
#Saída
print(anos,'Ano(s)\n',meses,'Mês(es)\n',dias,'Dia(s)\n')


#OK



#Condicional Simples
#Valores de Entrada
n1=int(input('Número 1:'))
n2=int(input('Número 2:'))
#Processamento
soma=n1+n2
#Saída
print('Soma:',soma)
#Condição se o número for simples
if soma%2==0:
       metade=soma/2
       #Saída
       print('Metade:',metade)

#Condicional 2
nota1=float(input('Nota 1:'))
nota2=float(input('Nota 2:'))
nota3=float(input('Nota 3:'))

media=(nota1+nota2+nota3)/3

if media>=7:
    print('Aprovado!!')
elif media>=4:
    print('Exame')
else: print('Reprovado')


