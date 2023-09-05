a=float(input('Escreva um número: '))
b=float(input('Escreva um número: '))
c=float(input('Escreva um número: '))
if a<b+c and b<c+a and c<b+a:
    print('Pode ser lado de um Triângulo')
    if a!=b and a!=c and b!=c:
        print('Triângulo Escaleno')
    elif a==b and a==c and b==c:
       print('Triângulo Equilatero')
    else:
       print('Triângulo Isóceles')
