cont=0
maiorPeso=0
while cont<2:
    pesoBoi=float(input('@ do BOI:'))
    
    if pesoBoi>maiorPeso:
        maiorPeso= pesoBoi
    cont=cont+1
print('Maior Peso do Boi',maiorPeso)
