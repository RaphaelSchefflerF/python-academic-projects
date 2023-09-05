print("Olá mundo!")
print("Olá Raphael Henrique Scheffler Ferreira")
#Atividade 1
print('Atividade 1!')
nota1=float(input("nota1:"))
nota2=float(input("nota2:"))
media=(nota1+nota2)/2
print("media:",media)
#Atividade 2
print('Atividade 2!')
base=float(input('base:'))
altura=float(input('altura:'))
area=(base*altura)/2
print("area:",area)
#Atividade 3
print('Atividade 3!')
val1=float(input('valor1:'))
val2=float(input('valor2:'))
soma=val1=val2
dobro=soma*2
print('soma:',soma)
print('dobro:',dobro)
#Atividade 4
print('Atividade 4!')
peso=float(input('peso:'))
taxa=float(input('taxa:'))
kilo=float(input('kilo:'))
valor=float(input(peso*kilo-taxa))
print('Valor:',valor)
#Atividade 4
peso=float(input("Peso em KG:"))
preço=peso*30
print("Valor a Pagar:", preço)
#Atividade 5
print('Atividade 5!')
salMin=float(input("Valor do Salário Mínimo:"))
qtKw=float(input("Qt.de quilowatts gasto:"))
#salmin/100-->calcula o valor do quilowatts
valorGasto=qtKw*(salMin/100)
print("Valor pago pela residência:", valorGasto)


#Atividade 9
print('Atividade 9!')
#Valores de Entrada
salario=float(input("Valor do Salário Mínimo:"))
conta1=float(input("Conta 1:"))
conta2=float(input("Conta 2:"))
#Operações
novovalor1=conta1+(conta1*2/100)
novovalor2=conta2+(conta2*2/100)
#Resultado das Operações
restou=salario-(novovalor1+novovalor2)
#Mostrar o Resultado das Operações
print("Valor Pago na Conta1:",novovalor1)
print("Valor Pago na Conta2:",novovalor2)
print("Restou do Sálario do João:", restou)
