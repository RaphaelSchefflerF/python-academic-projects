a=float(input('Escreva um número: '))
b=float(input('Escreva um número: '))
c=float(input('Escreva um número: '))
condicao=input('Crescente "cres" ou Decrescente "decres":')
#Decrescente              
if condicao=='decres':
   a >= b and a >= c and b >= c
   print(f'A ordem decrescente é {a} , {b} e {c}')
   if a >= b and a >=c and c >= b:
       print(f'A ordem decrescente é {a} , {c} e {b}')
   elif b >= a and b >= c and a >= c:
      print(f'A ordem decrescente é {b} , {a} e {c}')
   elif b >= a and b >= c and c >= a:
      print(f'A ordem decrescente é {b} , {c} e {a}')
   elif c >= a and c >= b and a >=b:
      print(f'A ordem decrescente é {c} , {a} e {b}')
   elif c >= a and c >= b and b >= a:
      print(f'A ordem decrescente é {c} , {b} e {a}')
#Crescente   
elif condicao=='cres':
   a <= b and a <= c and b <= c
   print(f'A ordem crescente é {a} , {b} e {c}')
   if a <= b and a <=c and c <= b:
      print(f'A ordem crescente é {a} , {c} e {b}')
   elif b <= a and b <= c and a <= c:
      print(f'A ordem crescente é {b} , {a} e {c}')
   elif b <= a and b <= c and c <= a:
      print(f'A ordem crescente é {b} , {c} e {a}')
   elif c <= a and c <= b and a <=b:
      print(f'A ordem crescente é {c} , {a} e {b}')
   elif c <= a and c <= b and b <= a:
      print(f'A ordem crescente é {c} , {b} e {a}')



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
