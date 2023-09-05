#Atividade 4
'''Escreva um algoritmo que leia os valores de dois lados adjacentes
de uma figura geométrica e informe se eles representam um quadrado
perfeito ou um retângulo.
*Quadrado perfeito é aquele que possui todos os lados iguais.'''
l1=int(input('Lado 1:'))
l2=int(input('Lado 2:'))
soma1=(l1+l1)
soma2=(l2+l2)
if soma1==soma2:
   print('Quadrado Perfeito')
elif soma1!=soma2:
   print('Retangulo')
#OU
l1=int(input('Lado 1:'))
l2=int(input('Lado 2:'))
if l1==l2:
   print('Quadrado Perfeito')
else:
   print('Retangulo')
  

#Atividade 5
'''Faça um programa que leia dois números e calcule a divisão do primeiro
pelo segundo. Porém, se o usuário digitar zero para o segundo número,
não realize o cálculo e apresente uma mensagem de erro
“Não pode ser feita divisão por zero!”.'''
n1=int(input('Número 1:'))
n2=int(input('Número 2:'))
if n2<=0:
   print('Não pode ser feita divisão por zero!')
elif n2>0:
   divisao=n1/n2
   print('Divisao',divisao)
#OU
n1=int(input('Número 1:'))
n2=int(input('Número 2:'))
print('------------------------')
if n2!=0:
   divisao=n1/n2
   print('Divisao:',divisao)
else:
   print('Não pode ser feita divisão por zero!')

#Atividade 6
'''Ler três valores e um código de condição. Se o código for “c” os valores
devem ser escritos em ordem crescente.
Se o código for “d”, deve-se escrevê-los em ordem decrescente.'''

a=float(input('Escreva um número: '))
b=float(input('Escreva um número: '))
c=float(input('Escreva um número: '))
condicao=input('Crescente "cres" ou Decrescente "decres":')
#Decrescente              
if condicao=='decres':
    a>b and a>c and b>c
    print(f'A ordem decrescente é {a} , {b} e {c}')
    if a>b and a>c and c>b:
        print(f'A ordem decrescente é {a} , {c} e {b}')
    elif b>a and b>c and a>c:
        print(f'A ordem decrescente é {b} , {a} e {c}')
    elif b>a and b>c and c>a:
        print(f'A ordem decrescente é {b} , {c} e {a}')
    elif c>a and c>b and a>b:
        print(f'A ordem decrescente é {c} , {a} e {b}')
    elif c>a and c>b and b>a:
        print(f'A ordem decrescente é {c} , {b} e {a}')
#Crescente   
elif condicao=='cres':
    a<b and a<c and b<c
    print(f'A ordem crescente é {a} , {b} e {c}')
    if a<b and a<c and c<b:
        print(f'A ordem crescente é {a} , {c} e {b}')
    elif b<a and b<c and a<c:
        print(f'A ordem crescente é {b} , {a} e {c}')
    elif b<a and b<c and c<a:
        print(f'A ordem crescente é {b} , {c} e {a}')
    elif c<a and c<b and a<b:
        print(f'A ordem crescente é {c} , {a} e {b}')
    elif c<a and c<b and b<a:
        print(f'A ordem crescente é {c} , {b} e {a}')

#Atividade 1.0
a=float(input('Escreva um número: '))
b=float(input('Escreva um número: '))
c=float(input('Escreva um número: '))
if a != b and a != c and b != c:
   print('Triângulo Escaleno')
elif a==b and a==c and b==c:
   print('Triângulo Equilatero')
else:
   print('Triângulo Isóceles')
#Atividades 1.1
a=float(input('Escreva um número: '))
b=float(input('Escreva um número: '))
c=float(input('Escreva um número: '))
a<b+c and b<c+a and c<b+a
print('Pode ser lado de um Triângulo')
if a!=b and a!=c and b!=c:
   print('Triângulo Escaleno')
elif a==b and a==c and b==c:
   print('Triângulo Equilatero')
else:
   print('Triângulo Isóceles')






    
