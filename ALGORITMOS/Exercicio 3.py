cont=0
contF=0
contM=0
media=0
contIdade=0
while cont<3:
    idade=float(input('Idade:'))
    nacional=input('Nacionalidade:')
    sexo=input('Sexo:')
    if sexo==feminino or sexo==f:
        if idade>=18:
            contF=contF+1
    if sexo==masculino or sexo==m and nacional==br or nacional==brasileira:
        if idade>20 and idade<30:
            contM=contM+1
    
    contIdade=contIdade+idade
    cont=cont+1
print('QT de Mulheres Maiores de Idade:',contF)
